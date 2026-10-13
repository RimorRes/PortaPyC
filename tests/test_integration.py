import portapyc
from portapyc import Service


def test_classic_slave_service_supports_execution_and_modules(classic_server):
    host, port = classic_server
    conn = portapyc.classic.connect(host, port)
    try:
        conn.execute("answer = 40 + 2")
        assert conn.eval("answer") == 42
        assert conn.modules.sys.version_info[0] == 2
        assert conn.builtin.len([1, 2, 3]) == 3
    finally:
        conn.close()


def test_classic_connection_supports_remote_objects(classic_server):
    host, port = classic_server
    conn = portapyc.classic.connect(host, port)
    try:
        remote_values = conn.eval("[1, 2, 3]")
        assert len(remote_values) == 3
        assert remote_values[0] == 1
        assert remote_values[2] == 3
        assert conn.root.get_service_name().decode("ascii") == "SLAVE"
    finally:
        conn.close()

def test_classic_connection_supports_remote_exceptions(classic_server):
    host, port = classic_server
    conn = portapyc.classic.connect(host, port)
    try:
        try:
            conn.execute("raise ValueError('test error')")
        except ValueError as e:
            arg = e.args[0].decode("utf-8")
            assert arg == "test error"
        else:
            raise AssertionError("expected ValueError was not raised")
    finally:
        conn.close()


def test_classic_connection_supports_iterators(classic_server):
    host, port = classic_server
    conn = portapyc.classic.connect(host, port)
    try:
        remote_iter = conn.eval("iter([1, 2, 3])")
        assert next(remote_iter) == 1
        assert next(remote_iter) == 2
        assert next(remote_iter) == 3
        try:
            next(remote_iter)
        except StopIteration:
            pass
        else:
            raise AssertionError("expected StopIteration was not raised")
    finally:
        conn.close()


def test_service_exposes_methods_attributes_and_service_metadata(service_server):
    host, port = service_server
    conn = portapyc.connect(host, port)
    try:
        assert conn.root.get_answer() == 42
        assert conn.root.the_real_answer_though == 43
        assert conn.root.get_service_name().decode("ascii") == "MY"
        assert tuple(alias.decode("ascii") for alias in conn.root.get_service_aliases()) == ("MY",)
    finally:
        conn.close()


def test_service_does_not_expose_unmarked_methods(service_server):
    host, port = service_server
    conn = portapyc.connect(host, port)
    try:
        try:
            conn.root.get_question()
        except AttributeError:
            pass
        else:
            raise AssertionError("unmarked service method was exposed")
    finally:
        conn.close()


class ClientService(Service):
    def exposed_client_answer(self):
        return 7


def test_client_service_can_be_exposed_alongside_remote_service(service_server):
    host, port = service_server
    conn = portapyc.connect(host, port, service=ClientService)
    try:
        assert conn.root.get_answer() == 42
        assert conn._local_root.exposed_client_answer() == 7
    finally:
        conn.close()

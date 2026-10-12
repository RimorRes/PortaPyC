# MUST BE RUN WITH PYTHON 2.7 AND RPYC 3.3.0
import rpyc

class MyService(rpyc.Service):
    def on_connect(self):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_answer(self): # this is an exposed method
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"


if __name__ == "__main__":
    import argparse
    from rpyc.utils.server import ThreadedServer
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=18861)
    args = parser.parse_args()
    t = ThreadedServer(MyService, hostname=args.host, port=args.port, reuse_addr=True)
    t.start()
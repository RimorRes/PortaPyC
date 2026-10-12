import socket
import signal
import subprocess
import time
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SERVER_START_TIMEOUT = 10.0


def _wait_for_server(process, host, port):
    deadline = time.monotonic() + SERVER_START_TIMEOUT
    while time.monotonic() < deadline:
        if process.poll() is not None:
            output = process.stderr.read().decode("utf-8", "replace")
            raise RuntimeError(
                "server exited with code %s:\n%s" % (process.returncode, output)
            )
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.settimeout(0.2)
            try:
                probe.connect((host, port))
            except OSError:
                time.sleep(0.05)
            else:
                return
    _stop_server(process)
    raise RuntimeError("server did not start on %s:%s" % (host, port))


def _stop_server(process):
    if process.poll() is not None:
        return
    if hasattr(signal, "CTRL_BREAK_EVENT"):
        process.send_signal(signal.CTRL_BREAK_EVENT)
    else:
        process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


@pytest.fixture(scope="session")
def classic_server():
    executable = ROOT / "bin" / "rpyc_classic.exe"
    if not executable.exists():
        pytest.skip("bin/rpyc_classic.exe is required for integration tests")
    process = subprocess.Popen(
        [str(executable), "--host", "127.0.0.1", "--port", "18812", "--quiet"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0),
    )
    try:
        _wait_for_server(process, "127.0.0.1", 18812)
        yield ("127.0.0.1", 18812)
    finally:
        _stop_server(process)


@pytest.fixture(scope="session")
def service_server():
    executable = ROOT / "bin" / "test_service_server.exe"
    if not executable.exists():
        pytest.skip("bin/test_service_server.exe is required for integration tests")
    process = subprocess.Popen(
        [str(executable)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0),
    )
    try:
        _wait_for_server(process, "127.0.0.1", 18861)
        yield "127.0.0.1", 18861
    finally:
        _stop_server(process)

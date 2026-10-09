import portapyc
import struct
import time


conn = portapyc.classic.connect("localhost", 18812)
print(conn.modules.sys.version)
print(conn.modules.time.ctime())

ping_num = 0
while True:
    start = time.time()
    tx_payload = struct.pack("!I", ping_num)
    conn.builtins.print("Ping !", conn.modules.struct.unpack("!I", tx_payload)[0])

    rx_payload = conn.modules.struct.pack("!I", ping_num)
    print("Pong !", struct.unpack("!I", rx_payload)[0])
    end = time.time()


    conn.builtins.print("Waiting...")
    conn.modules.time.sleep(1)
    ping_num += 1
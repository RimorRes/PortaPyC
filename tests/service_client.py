import portapyc

conn = portapyc.connect("localhost", 18861)
print(conn.root.get_answer())

from mts import variable

server_id_instance = variable.InnodbThreadConcurrency()
server_id=server_id_instance.value
print(server_id)

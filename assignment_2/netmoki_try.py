from netmiko import ConnectHandler
import pickle

net_connect = ConnectHandler(
    device_type="linux",
    host="127.0.0.1",
    port=80,
    username="ankurkrishn",
    password="9837604991Ka15",
)

cmd_output = net_connect.send_command(
    "ls"
)

#write output to local text file named "external_file.txt"

file = open('external_file1.txt', 'wb')
pickle.dump(cmd_output, file)
file.close()

source_file = "external_file1.txt"
dest_file = "external_file2.txt"
direction = "put"
file_system = "flash:"

transfer_dict = file_transfer(
    snet_connect,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)

print(transfer_dict)
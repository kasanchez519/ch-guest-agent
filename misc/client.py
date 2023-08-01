import socket
import qmp_formatter
from client_parser import build_parser
# from qemu.qmp import Message
cmd = build_parser()
print(cmd)
PORT = 1234
# cmd = '{"execute": "create-user", "arguments": {"username": "testuser", "create-home": 1} }' # noqa E501
# cmd = '{"execute": "deploy-ssh-pubkey", "arguments": {"username": "testuser", "ssh-key": "test_ssh_key"} }' # noqa E501
# cmd = '{"execute": "get-osinfo"}'
# cmd = '{"execute": "guest-sync", "arguments": {"id": 12345} }'

# print(cmd)
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect("/tmp/ch.vsock")
s.send("CONNECT {}\n{}".format(PORT, cmd).encode('utf-8'))

buf1 = s.recv(4096)
buf2 = s.recv(4096).decode('utf-8')
print(buf2)

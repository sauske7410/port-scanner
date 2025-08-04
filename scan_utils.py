import socket

def get_banner(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024)
        return banner.decode().strip()
    except Exception:
        return ""

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except Exception:
                service = 'Unknown'
            banner = get_banner(sock)
            return (port, service, banner, True)
        else:
            return (port, '', '', False)
    except Exception:
        return (port, '', '', False)
    finally:
        sock.close()
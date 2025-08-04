import socket
import concurrent.futures
import sys
from scan_utils import scan_port
from formatter import format_port_results

def port_scan(target_host, start_port, end_port):
    target_ip = socket.gethostbyname(target_host)
    print(f"Starting scan on host: {target_ip}")
    ports = range(start_port, end_port + 1)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in ports}
        total_ports = len(ports)
        for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            port, service, banner, status = future.result()
            results.append((port, service, banner, status))
            sys.stdout.write(f"\rProgress: {i}/{total_ports} ports scanned")
            sys.stdout.flush()
    print("\n" + format_port_results(results))

if __name__ == '__main__':
    target_host = input("Enter target host/IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    port_scan(target_host, start_port, end_port)
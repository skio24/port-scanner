#!/usr/bin/env python3
"""
Basic TCP Port Scanner
Usage: python3 port_scanner.py <target> [start_port] [end_port]
Example: python3 port_scanner.py 192.168.1.1 1 1000
"""

import socket
import sys
from datetime import datetime

def scan_port(target_ip, port, timeout=1):
    """
    Attempt a TCP connection to target_ip on the given port.
    Returns True if port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <target> [start_port] [end_port]")
        print("Example: python3 port_scanner.py scanme.nmap.org 20 80")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[!] Invalid port range. Must be 1-65535 and start <= end.")
        sys.exit(1)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {target}")
        sys.exit(1)

    print("-" * 60)
    print(f"Scanning target: {target} ({target_ip})")
    print(f"Port range: {start_port} - {end_port}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port):
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit(0)

    print("-" * 60)
    if open_ports:
        print(f"Open ports found: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found in the specified range.")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
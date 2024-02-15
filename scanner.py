import argparse
import socket
import sys
import threading
import requests
from bs4 import BeautifulSoup

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} on {host} is open")
                if port == 80 or port == 443:
                    extract_vulnerabilities(host, port)
    except socket.error:
        pass

def scan_host(host, start_port, end_port):
    print(f"Scanning host {host}...")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

def extract_vulnerabilities(host, port):
    try:
        if port == 80:
            url = f"http://{host}"
        elif port == 443:
            url = f"https://{host}"
        else:
            return
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Vulnerabilities found on {url}:")
        print(soup.prettify())  
    except Exception as e:
        print(f"Failed to extract vulnerabilities from {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Network scanner with vulnerability extraction")
    parser.add_argument("host", help="Host to scan")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, nargs="?", help="End port")
    args = parser.parse_args()

    host = args.host
    start_port = args.start_port
    end_port = args.end_port if args.end_port else start_port

    num_threads = min(100, end_port - start_port + 1)
    ports_per_thread = (end_port - start_port + 1) // num_threads
    threads = []

    for i in range(num_threads):
        start = start_port + i * ports_per_thread
        end = min(start_port + (i + 1) * ports_per_thread - 1, end_port)
        thread = threading.Thread(target=scan_host, args=(host, start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

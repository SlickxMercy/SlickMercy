import os
import re
import sys
import socket
import threading
from datetime import datetime

def scan_ips(start_ip, end_ip):
    ips = []
    start_ip_split = start_ip.split('.')
    end_ip_split = end_ip.split('.')
    for i in range(int(start_ip_split[0]), int(end_ip_split[0])+1):
        for j in range(int(start_ip_split[1]), int(end_ip_split[1])+1):
            for k in range(int(start_ip_split[2]), int(end_ip_split[2])+1):
                for l in range(int(start_ip_split[3]), int(end_ip_split[3])+1):
                    ip = f"{i}.{j}.{k}.{l}"
                    ips.append(ip)
    return ips

def test_ip(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, 80))
        sock.close()
        return True
    except:
        return False

def find_cameras(start_ip, end_ip, filename):
    ips = scan_ips(start_ip, end_ip)
    
    class CameraScanner(threading.Thread):
        def __init__(self, ip_list, filename):
            threading.Thread.__init__(self)
            self.ip_list = ip_list
            self.filename = filename

        def run(self):
            for ip in self.ip_list:
                if test_ip(ip):
                    with open(self.filename, "a+") as f:
                        existing_ips = set(f.read().splitlines())
                        if ip not in existing_ips:
                            f.write(f"{ip}\n")
                            print(f"\r\033[32mAdded {ip} to {self.filename}\033[0m", end='', flush=True)

    threads = []
    num_threads = 200
    chunk_size = len(ips) // num_threads
    for i in range(num_threads):
        thread_ips = ips[i*chunk_size:(i+1)*chunk_size]
        thread = CameraScanner(thread_ips, filename)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nScan completed.")

if __name__ == '__main__':
    start_ip = input("Enter the start IP address range: ")
    end_ip = input("Enter the end IP address range: ")
    filename = input("Enter the filename to save the IP addresses: ")
    find_cameras(start_ip, end_ip, filename)

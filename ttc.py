import os, sys, re, json
from time import sleep
import random
from datetime import datetime
import requests 
dem=0
stop=1
os.system("clear")
session = requests.Session()
sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m ➺❥ \033[1;92m "
logo = """
\033[1;32m╔═════════════════════════════════════════════════════════╗
\033[1;32m \033[1;96m  \033[1;91m\033[1;95m       ➽ Facebook : La Văn Hiếu         \033[1;32m    
\033[1;32m \033[1;96m  \033[1;91m   \033[1;94m  ➽ Zalo : 0398342590            \033[1;32m      
\033[1;32m \033[1;96m\033[1;91m \033[0;33m       ➽ Momo : 0398342590         \033[1;32m       
\033[1;32m \033[1;96m\033[1;91m  \033[1;92m       ➽ Youtube :            \033[1;32m    
\033[1;32m \033[1;96m \033[1;91m\033[1;97m       ➽ decode nên ghi nguồn✨   \033[1;32m   
\033[1;32m╚═════════════════════════════════════════════════════════╝            """
print(logo)
os.system('clear')
print(logo)
t=datetime.now().strftime("%H:%M:%S")
h=open('tkttc.txt',mode='a+')
h=open('tkttc.txt',mode='r')
print('━'*60)
hung=h.read()
print(sr+'Tài Khoản  : '+hung)
h.close()
k=open('mkttc.txt',mode='a+')
k=open('mkttc.txt',mode='r')
hai=k.read()
print(sr+'Mật Khẩu : '+hai)
k.close()
print('━'*60)
hdoi=input(sr+'Bạn Muốn Đổi Tài Khoản TTC Không (y/n) : ')
if hdoi=='y' or hdoi=="Y":
 h=open('tkttc.txt',mode='w')
 os.system('clear')
 print(logo)
 tkm=input(sr+'Nhập Tài Khoản TTC Mới : ')
 h.write(tkm)
 h.close()
 k=open('mkttc.txt',mode='w')
 mkm=input(sr+'Nhập Mật Khẩu TTC Mới : ')
 k.write(mkm)
 k.close()
 tk=tkm
 mk=mkm
else:
 tk=hung
 mk=hai
nhan="ĐĂNG+NHẬP"
head_login={
 "Host":"tuongtaccheo.com",
 "content-length":"77",
 "cache-control":"max-age=0",
 "upgrade-insecure-requests":"1",
 "origin":"https://tuongtaccheo.com",
 "content-type":"application/x-www-form-urlencoded",
 "user-agent":"Mozilla/5.0 (Linux; Android 5.0; SM-N900S Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
 "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "x-requested-with":"mark.via.gp",
 "sec-fetch-site":"same-origin",
 "sec-fetch-mode":"navigate",
 "sec-fetch-user":"?1",
 "sec-fetch-dest":"document",
 "referer":"https://tuongtaccheo.com/",
 "accept-encoding":"gzip, deflate",
 "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
}
data_login={
 "username":tk,
 "password":mk,
 "submit":nhan,
}
log=session.post(f"https://tuongtaccheo.com/login.php",headers=head_login,data=data_login).text
reg = log
t = session.cookies.get_dict()
ph = t['PHPSESSID']
if int(reg.count('Sai tài khoản'))>0:
 print(sr+'Đăng nhập Thất Bại')
 exit()
else:
 print(sr+'Đăng Nhập Thành Công')
sleep(0.2)
ckttc = '_ga=GA1.2.1500701940.1621419545; _fbp=fb.1.1621419545996.7138875; __tawkuuid=e::tuongtaccheo.com::Q9Wp0PpxdaPPSauZ9+vwmtdM1UA2gWlyG0GIFEjkSr9HkXAOJNzqsTAdYqmPdrkS::2; _gid=GA1.2.239860297.1623436076; PHPSESSID=' +ph+'; _gat_gtag_UA_88794877_6=1'
cookiettc= {'cookie':ckttc}
requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc)
r2 = re.findall(r'id="soduchinh">.*<\/strong> XU', requeststtc.text)
stringx4 = ''.join(r2)
stringx4 = re.findall(r'>.*?<\/', stringx4)
stringx5 = ''.join(stringx4)
stringx5= stringx5.replace("</" , "")
soduxu = stringx5.replace(">","")
r21 = re.findall(r'Chào mừng.*?đến', requeststtc.text)
stringx4 = ''.join(r21)
stringx4 = re.findall(r'>.*?<', stringx4)
stringx5 = ''.join(stringx4)
stringx5= stringx5.replace("<" , "")
tenttc= stringx5.replace(">" , "")
os.system('clear')
print(logo)
print('━'*60)
print(sr+'Username TTC : '+tenttc)
print(sr+'Xu Hiện Tại : '+soduxu)
print('━'*60)
tkfb=input(sr+'Nhập Token Facebook : ')
check_token=json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tkfb).text)
try:
    idfb = check_token['id']
    namefb = check_token['name']
    sleep(0.1)
    print(sr+'Token Đúng !!! Chờ Chút 🤧🤧')
except:
    print(sr+'Token Die Hoặc Bị Văng Khỏi Web')
    exit()
os.system('clear')
print(logo)
print('━'*60)
print(sr+'Username TTC : '+tenttc)
print(sr+'Xu Hiện Tại : '+soduxu)
print('━'*60)
print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
print('━'*60)
print(f"{sr}\033[1;92m Nhập [1] Chạy Nhiệm Vụ Like")
print(f"{sr}\033[1;92m Nhập [2] Chạy Nhiệm Vụ Follow")
print(f"{sr}\033[1;92m Nhập [3] Chạy Random Like + Follow")
print(sr+'Tui Sẽ Cập Nhật Các Nhiệm Vụ Khác Sau')
print('━'*60)
ls=int(input(f"{sr} Nhập Số : "))
delay=int(input(f"{sr} Nhập Delay Job : "))
nvdl=int(input(f"{sr} Sau Bao Nhiêu Nhiệm Vụ Thì Tránh Block: "))
dlnv=int(input(f"{sr} Sau {nvdl} Nhiệm Vụ Nghỉ Bao Nhiêu Giây : "))
head_dat={
   "Host":"tuongtaccheo.com",
   "accept":"application/json, text/javascript, */*; q=0.01",
   "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A750GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
   "sec-fetch-site":"same-origin",
   "sec-fetch-mode":"cors",
   "sec-fetch-dest":"empty",
   "referer":"https://tuongtaccheo.com/cauhinh/",
   "accept-encoding":"gzip, deflate",
   "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
   "Cookie":ckttc,
}
data_dat={
 "iddat%5B%5D":idfb,
 "loai":"fb"
}
dat_acc=requests.post(url='https://tuongtaccheo.com/cauhinh/datnick.php', headers=head_dat, data=data_dat)
if ls==1:
 while True:
  try:
   log=session.post(f"https://tuongtaccheo.com/login.php",headers=head_login,data=data_login).text
   reg = log
   t = session.cookies.get_dict()
   ph = t['PHPSESSID']
   ckttc = '_ga=GA1.2.1500701940.1621419545; _fbp=fb.1.1621419545996.7138875; __tawkuuid=e::tuongtaccheo.com::Q9Wp0PpxdaPPSauZ9+vwmtdM1UA2gWlyG0GIFEjkSr9HkXAOJNzqsTAdYqmPdrkS::2; _gid=GA1.2.239860297.1623436076; PHPSESSID=' +ph+'; _gat_gtag_UA_88794877_6=1'
  except:
   print('lỗi')
  hea={
   "Host":"tuongtaccheo.com",
   "accept":"application/json, text/javascript, */*; q=0.01",
   "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A750GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
   "sec-fetch-site":"same-origin",
   "sec-fetch-mode":"cors",
   "sec-fetch-dest":"empty",
   "referer":"https://tuongtaccheo.com/kiemtien/",
   "accept-encoding":"gzip, deflate",
   "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
   "Cookie":ckttc,
  }
  print('━'*60)
  print ('   Bản Quyền Tool By Hấu')
  print('━'*60)
  while True:
    try:
      url_like = 'https://tuongtaccheo.com/kiemtien/getpost.php'
      referer = 'https://tuongtaccheo.com/kiemtien/'
      m = getnv(url_like,referer,ckttc)
      nvlike1 = json.loads(m)
    except:
      for a in range(5, -1, -1):
        print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
        sleep(1)
    web = requests.get(url="https://tuongtaccheo.com/kiemtien/getpost.php",headers=hea)
    log = web.json()
    
    for uid in log:
      id=uid["idpost"]
      requests.post(f"https://graph.facebook.com/{id}/likes?access_token={tkfb}").json()
      
      nhantien={
        "Host":"tuongtaccheo.com",
        "content-length":"19",
        "accept":"*/*",
        "x-requested-with":"XMLHttpRequest",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A750GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "origin":"https://tuongtaccheo.com",
        "sec-fetch-site":"same-origin",
        "sec-fetch-mode":"cors",
        "sec-fetch-dest":"empty",
        "referer":"https://tuongtaccheo.com/kiemtien/",
        "accept-encoding":"gzip, deflate",
        "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":ckttc,
       }
      da={
       "id":id,
      }
      nhanlike = requests.post(url="https://tuongtaccheo.com/kiemtien/nhantien.php",headers=nhantien,data=da).json()
      # print(nhanfl)
      requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc)
      r2 = re.findall(r'id="soduchinh">.*<\/strong> XU', requeststtc.text)
      stringx4 = ''.join(r2)
      stringx4 = re.findall(r'>.*?<\/', stringx4)
      stringx5 = ''.join(stringx4)
      stringx5= stringx5.replace("</" , "")
      soduxu = stringx5.replace(">","")
      try:
        iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
        idfb = json.loads(iid)['id']
        tenfb = json.loads(iid)['name']
        try:
         nhanlike["error"]
         t=datetime.now().strftime("%H:%M:%S")
         print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id}",end=' \r')
        except:
               nhanlike["mess"]
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{soduxu}\033[1;97m]")
               if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
               if delay==0:
                print('            ',end='\r')
               else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [\]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [|]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [/]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
      except:
       print(sr+'Token Die !!!')
       tkfb=input(sr+'Nhập Token Mới : ')
       try:
                iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
                idfb = json.loads(iid)['id']
                tenfb = json.loads(iid)['name']
                print('━'*60)
                print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
                print('━'*60)
       except:
        print(sr+'Token Die !!!')
elif ls==2:
 while True:
  head={
   "Host":"tuongtaccheo.com",
   "accept":"application/json, text/javascript, */*; q=0.01",
   "user-agent":"Mozilla/5.0 (Li=nux; Android 5.0; SM-N900S Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
   "sec-fetch-site":"same-origin",
   "sec-fetch-mode":"cors",
   "sec-fetch-dest":"empty",
   "referer":"https://tuongtaccheo.com/kiemtien/subcheo/",
   "accept-encoding":"gzip, deflate",
   "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
   "Cookie":ckttc,
  }
  print('-'*60)
  print ('   Bản Quyền Tool By Hải Magic')
  print('-'*60)
  while True:
    try:
      urlsub = 'https://tuongtaccheo.com/kiemtien/subcheo/getpost.php'
      referer = 'https://tuongtaccheo.com/kiemtien/subcheo'
      m = getnv(urlsub,referer,ckttc)
      nvsub1 = json.loads(m)
    except:
      for a in range(5, -1, -1):
        print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
        sleep(1)
    check2=requests.get(url="https://tuongtaccheo.com/kiemtien/subcheo/getpost.php",headers=head).json()
    for uid in check2:
      idfl = uid["idpost"]
      requests.post(f"https://graph.facebook.com/{idfl}/subscribers?access_token={tkfb}").json()
      nhantien={
       "Host":"tuongtaccheo.com",
       "content-length":"19",
       "accept":"*/*",
       "x-requested-with":"XMLHttpRequest",
       "user-agent":"Mozilla/5.0 (Linux; Android 5.0; SM-N900S Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36",
       "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
       "origin":"https://tuongtaccheo.com",
       "sec-fetch-site":"same-origin",
       "sec-fetch-mode":"cors",
       "sec-fetch-dest":"empty",
       "referer":"https://tuongtaccheo.com/kiemtien/subcheo/",
       "accept-encoding":"gzip, deflate",
       "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
       "Cookie":ckttc,
      }
      da={
      "id":idfl,
      }
      nhanlike = requests.post(url="https://tuongtaccheo.com/kiemtien/nhantien.php",headers=nhantien,data=da).json()
      # print(nhanfl)
      requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc)
      r2 = re.findall(r'id="soduchinh">.*<\/strong> XU', requeststtc.text)
      stringx4 = ''.join(r2)
      stringx4 = re.findall(r'>.*?<\/', stringx4)
      stringx5 = ''.join(stringx4)
      stringx5= stringx5.replace("</" , "")
      soduxu = stringx5.replace(">","")
      try:
        iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
        idfb = json.loads(iid)['id']
        tenfb = json.loads(iid)['name']
        nhanfl = requests.post(url="https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php",headers=nhantien,data=da).json()
        try:
         nhanfl["error"]
         t=datetime.now().strftime("%H:%M:%S")
         print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idfl}",end=' \r')
        except:
               nhanfl["mess"]
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idfl} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{soduxu}\033[1;97m]")
               if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
               if delay==0:
                print('            ',end='\r')
               else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [\]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [|]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [/]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
      except:
       print(sr+'Token Die !!!')
       tkfb=input(sr+'Nhập Token Mới : ')
       try:
                iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
                idfb = json.loads(iid)['id']
                tenfb = json.loads(iid)['name']
                print('━'*60)
                print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
                print('━'*60)
       except:
        print(sr+'Token Die !!!')
elif ls==3:
 while True:
  cc=random.randint(1,2)
  if cc==1:
    head={
   "Host":"tuongtaccheo.com",
   "accept":"application/json, text/javascript, */*; q=0.01",
   "user-agent":"Mozilla/5.0 (Li=nux; Android 5.0; SM-N900S Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
   "sec-fetch-site":"same-origin",
   "sec-fetch-mode":"cors",
   "sec-fetch-dest":"empty",
   "referer":"https://tuongtaccheo.com/kiemtien/subcheo/",
   "accept-encoding":"gzip, deflate",
   "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
   "Cookie":ckttc,
  }
    try:
      urlsub = 'https://tuongtaccheo.com/kiemtien/subcheo/getpost.php'
      referer = 'https://tuongtaccheo.com/kiemtien/subcheo'
      m = getnv(urlsub,referer,ckttc)
      nvsub1 = json.loads(m)
    except:
      for a in range(5, -1, -1):
        print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
        sleep(1)
    check2=requests.get(url="https://tuongtaccheo.com/kiemtien/subcheo/getpost.php",headers=head).json()
    for uid in check2:
      idfl = uid["idpost"]
      requests.post(f"https://graph.facebook.com/{idfl}/subscribers?access_token={tkfb}").json()
      nhantien={
       "Host":"tuongtaccheo.com",
       "content-length":"19",
       "accept":"*/*",
       "x-requested-with":"XMLHttpRequest",
       "user-agent":"Mozilla/5.0 (Linux; Android 5.0; SM-N900S Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36",
       "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
       "origin":"https://tuongtaccheo.com",
       "sec-fetch-site":"same-origin",
       "sec-fetch-mode":"cors",
       "sec-fetch-dest":"empty",
       "referer":"https://tuongtaccheo.com/kiemtien/subcheo/",
       "accept-encoding":"gzip, deflate",
       "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
       "Cookie":ckttc,
      }
      da={
      "id":idfl,
      }
      nhanlike = requests.post(url="https://tuongtaccheo.com/kiemtien/nhantien.php",headers=nhantien,data=da).json()
      # print(nhanfl)
      requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc)
      r2 = re.findall(r'id="soduchinh">.*<\/strong> XU', requeststtc.text)
      stringx4 = ''.join(r2)
      stringx4 = re.findall(r'>.*?<\/', stringx4)
      stringx5 = ''.join(stringx4)
      stringx5= stringx5.replace("</" , "")
      soduxu = stringx5.replace(">","")
      try:
        iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
        idfb = json.loads(iid)['id']
        tenfb = json.loads(iid)['name']
        nhanfl = requests.post(url="https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php",headers=nhantien,data=da).json()
        try:
         nhanfl["error"]
         t=datetime.now().strftime("%H:%M:%S")
         print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idfl}",end=' \r')
        except:
               nhanfl["mess"]
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idfl} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{soduxu}\033[1;97m]")
               if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
               if delay==0:
                print('            ',end='\r')
               else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [\]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [|]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [/]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
      except:
       print(sr+'Token Die !!!')
       tkfb=input(sr+'Nhập Token Mới : ')
       try:
                iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
                idfb = json.loads(iid)['id']
                tenfb = json.loads(iid)['name']
                print('━'*60)
                print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
                print('━'*60)
       except:
        print(sr+'Token Die !!!')
  if cc==2:
    hea={
   "Host":"tuongtaccheo.com",
   "accept":"application/json, text/javascript, */*; q=0.01",
   "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A750GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
   "sec-fetch-site":"same-origin",
   "sec-fetch-mode":"cors",
   "sec-fetch-dest":"empty",
   "referer":"https://tuongtaccheo.com/kiemtien/",
   "accept-encoding":"gzip, deflate",
   "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
   "Cookie":ckttc,
}
    try:
      url_like = 'https://tuongtaccheo.com/kiemtien/getpost.php'
      referer = 'https://tuongtaccheo.com/kiemtien/'
      m = getnv(url_like,referer,ckttc)
      nvlike1 = json.loads(m)
    except:
      for a in range(5, -1, -1):
        print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
        sleep(1)
    web = requests.get(url="https://tuongtaccheo.com/kiemtien/getpost.php",headers=hea)
    log = web.json()
    
    for uid in log:
      id=uid["idpost"]
      requests.post(f"https://graph.facebook.com/{id}/likes?access_token={tkfb}").json()
      
      nhantien={
        "Host":"tuongtaccheo.com",
        "content-length":"19",
        "accept":"*/*",
        "x-requested-with":"XMLHttpRequest",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A750GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "origin":"https://tuongtaccheo.com",
        "sec-fetch-site":"same-origin",
        "sec-fetch-mode":"cors",
        "sec-fetch-dest":"empty",
        "referer":"https://tuongtaccheo.com/kiemtien/",
        "accept-encoding":"gzip, deflate",
        "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":ckttc,
       }
      da={
       "id":id,
      }
      nhanlike = requests.post(url="https://tuongtaccheo.com/kiemtien/nhantien.php",headers=nhantien,data=da).json()
      # print(nhanfl)
      requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc)
      r2 = re.findall(r'id="soduchinh">.*<\/strong> XU', requeststtc.text)
      stringx4 = ''.join(r2)
      stringx4 = re.findall(r'>.*?<\/', stringx4)
      stringx5 = ''.join(stringx4)
      stringx5= stringx5.replace("</" , "")
      soduxu = stringx5.replace(">","")
      try:
        iid = requests.get(f'https://graph.facebook.com/me/?access_token={tkfb}').text
        idfb = json.loads(iid)['id']
        tenfb = json.loads(iid)['name']
      except:
       print(sr+'Token Facebook Die')
       exit()
      try:
        nhanlike["error"]
        t=datetime.now().strftime("%H:%M:%S")
        print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id}",end=' \r')
      except:
               nhanlike["mess"]
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{soduxu}\033[1;97m]")
  if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
  if delay==0:
                print('            ',end='\r')
  else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [\]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [|]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [/]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)

import requests
import os, sys, json, re
from time import sleep
session = requests.Session()
import os, sys, re, json
from time import sleep
import random
from datetime import datetime
import requests 
dem=0
stop=1
os.system("clear")
rf_acc='https://traodoisub.com/view/cauhinh'
sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m ➺❥ \033[1;92m"
logo = """
\033[1;32m╔════════════════════════════════════════════════════════════════════╗
\033[1;32m La \033[1;96m Văn \033[1;91m  Hiếu \033[1;95m  FB:La Văn Hiếu (bảnh) \033[1;32m 
\033[1;32m╚════════════════════════════════════════════════════════════════════╝            """
print(logo)
os.system("clear")
print(logo)
print(vs)
h=open('tktds.txt',mode='a+')
h=open('tktds.txt',mode='r')

hung=h.read()
print(sr+'Tài Khoản  : '+hung)
h.close()
k=open('mktds.txt',mode='a+')
k=open('mktds.txt',mode='r')
hai=k.read()
print(sr+'Mật Khẩu : '+hai)
k.close()
hdoi=input(sr+'Bạn Muốn Đổi Tài Khoản TDS Không (y/n) : ')
if hdoi=='y' or hdoi=="Y":
 h=open('tktds.txt',mode='w')
 os.system('clear')
 print(logo)
 tkm=input(sr+'Nhập Tài Khoản TDS Mới : ')
 h.write(tkm)
 h.close()
 k=open('mktds.txt',mode='w')
 mkm=input(sr+'Nhập Mật Khẩu TDS Mới : ')
 k.write(mkm)
 k.close()
 tk=tkm
 mk=mkm
else:
 tk=hung
 mk=hai
rf_login='https://traodoisub.com/home/'
head_login={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
data_login={
'username':tk,
'password':mk,
}
log=session.post(url='https://traodoisub.com/scr/login.php', headers=head_login, data=data_login).text
if "success" in log:
    print(sr+'Login Thành Công ')
else:
    print(sr+'Login Thất Bại ')
    exit()
sleep(0.2)
reg = log
m = session.cookies.get_dict()
ph = m['PHPSESSID']
cktds='PHPSESSID='+ph
os.system('clear')
print(logo)
print(vs)
head={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':rf_login,
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
}
check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
xu=check_tk.json()['xu']
print(sr+'Username : '+tk)
print(sr+'Xu Hiện Tại : '+xu)
print('-'*60)
while True:
 Token_fb=input(sr+'Nhập Token Facebook : ')
 check_token=json.loads(requests.get('https://graph.facebook.com/me/?access_token='+Token_fb).text)
 try:
    idfb = check_token['id']
    namefb = check_token['name']
    sleep(0.1)
    print(sr+'Token Đúng !!! Chờ Chút 🤧🤧')
    try:
      head_acc={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':rf_acc,
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
    }
      data_acc={
       "iddat":idfb
      }
      dat_acc=requests.post(url='https://traodoisub.com/scr/datnick.php', headers=head_acc, data=data_acc)
    except:
        idfb = check_token['id']
        print(sr+'Vui Lòng Thêm '+idfb+' Vào Traodoisub')
        exit()
    sleep(0.1)
    break
 except:
    print(sr+'Token Die Hoặc Bị Văng Khỏi Web')
os.system('clear')
print(logo)
print(vs)
print(sr+'Username : '+tk)
print(sr+'Xu Hiện Tại : '+xu)
print('-'*60)
print("\033[1;92m Chạy FB : " + str(namefb) +" | ID " + str(idfb))
print('-'*60)
print(f"{sr}\033[1;92m Nhập [1] Chạy Nhiệm Vụ Like")
print(f"{sr}\033[1;92m Nhập [2] Chạy Nhiệm Vụ Follow")
print(f"{sr}\033[1;92m Nhập [3] Chạy Nhiệm Vụ Comments ( Đang Bảo Trì )")
print(f"{sr}\033[1;92m Nhập [4] Chạy Nhiệm Vụ Share")
print(f"{sr}\033[1;92m Nhập [5] Chạy Nhiệm Vụ Like + Follow")
print(f"{sr}\033[1;92m Nhập [6] Chạy Nhiệm Vụ Like + Follow + Share")
print(f"{sr}\033[1;92m Nhập [7] Chạy Nhiệm Vụ Like + Share")
print("-"*60)
ls=int(input(f"{sr} Nhập Số : "))
delay=int(input(f"{sr} Nhập Delay Job : "))
nvdl=int(input(f"{sr} Sau Bao Nhiêu Nhiệm Vụ Thì Tránh Block: "))
dlnv=int(input(f"{sr} Sau {nvdl} Nhiệm Vụ Nghỉ Bao Nhiêu Giây : "))
if ls==1:
 while True:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    try:
             get_job=requests.get(url='https://traodoisub.com/ex/like/load.php', headers=head_job)
             id_like=get_job.json()['data'][0]['id']
             urllike='https://graph.facebook.com/'+str(id_like)+'/likes'
             datalike="access_token="+Token_fb
             lam_job_like=requests.post(urllike, data=datalike)
             nhan_like={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_like,
              "type":"like"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/like/nhantien.php', headers=nhan_like, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
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
             else:
              t=datetime.now().strftime("%H:%M:%S")
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like}",end=' \r')
              sleep(2)
    except:
            for a in range(5, -1, -1):
                print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
                sleep(1)
elif ls==2:
 while True:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/follow/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    get_job=requests.get(url='https://traodoisub.com/ex/follow/load.php', headers=head_job)
    try:
             id_follow=get_job.json()['data'][0]['id']
             urlfl='https://graph.facebook.com/'+str(id_follow)+'/subscribers'
             datalike="access_token="+Token_fb
             lam_job_fl=requests.post(urlfl, data=datalike)
             nhan_follow={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_follow,
              "type":"follow"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/follow/nhantien.php', headers=nhan_follow, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
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
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow}",end=' \r')
              sleep(2)
    except:
           for a in range(5, -1, -1):
             print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
             sleep(1)
elif ls==3:
 print('Bảo Trì ')
if ls==4:
 while True:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    get_job=requests.get(url='https://traodoisub.com/ex/share/load.php', headers=head_job)
    try:
             idshare=get_job.json()['data'][0]['id']
             datashare="access_token="+Token_fb
             message='Bản Quyền Tool By Hải Magic'
             sharee = requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message='+str(message)+'&link=https://mbasic.facebook.com/'+str(idshare)+'&access_token='+str(Token_fb)+'').json()
             nhan_share={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":idshare,
              "type":"share"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/share/nhantien.php', headers=nhan_share, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
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
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare}",end=' \r')
              sleep(2)
    except:
     for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
elif ls==5:
 while True:
  cc=random.randint(1,2)
  if cc==1:
          head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
          get_job=requests.get(url='https://traodoisub.com/ex/like/load.php', headers=head_job)
          try:
             id_like=get_job.json()['data'][0]['id']
             urllike='https://graph.facebook.com/'+str(id_like)+'/likes'
             datalike="access_token="+Token_fb
             lam_job_like=requests.post(urllike, data=datalike)
             nhan_like={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_like,
              "type":"like"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/like/nhantien.php', headers=nhan_like, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like}",end=' \r')
              sleep(2)
          except:
           for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
  elif cc==2:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/follow/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    get_job=requests.get(url='https://traodoisub.com/ex/follow/load.php', headers=head_job)
    try:
             id_follow=get_job.json()['data'][0]['id']
             urlfl='https://graph.facebook.com/'+str(id_follow)+'/subscribers'
             datalike="access_token="+Token_fb
             lam_job_fl=requests.post(urlfl, data=datalike)
             nhan_follow={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_follow,
              "type":"follow"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/follow/nhantien.php', headers=nhan_follow, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow}",end=' \r')
              sleep(2)
    except:
           for a in range(5, -1, -1):
             print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
             sleep(1)
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
elif ls==6:
 while True:
  cc=random.randint(1,3)
  if cc==1:
          head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
          get_job=requests.get(url='https://traodoisub.com/ex/like/load.php', headers=head_job)
          try:
             id_like=get_job.json()['data'][0]['id']
             urllike='https://graph.facebook.com/'+str(id_like)+'/likes'
             datalike="access_token="+Token_fb
             lam_job_like=requests.post(urllike, data=datalike)
             nhan_like={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_like,
              "type":"like"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/like/nhantien.php', headers=nhan_like, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like}",end=' \r')
              sleep(2)
          except:
           for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
  elif cc==2:
       head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/follow/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
       get_job=requests.get(url='https://traodoisub.com/ex/follow/load.php', headers=head_job)
       try:
             id_follow=get_job.json()['data'][0]['id']
             urlfl='https://graph.facebook.com/'+str(id_follow)+'/subscribers'
             datalike="access_token="+Token_fb
             lam_job_fl=requests.post(urlfl, data=datalike)
             nhan_follow={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_follow,
              "type":"follow"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/follow/nhantien.php', headers=nhan_follow, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {id_follow}",end=' \r')
              sleep(2)
       except:
           for a in range(5, -1, -1):
             print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
             sleep(1)
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
  elif cc==3:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    get_job=requests.get(url='https://traodoisub.com/ex/share/load.php', headers=head_job)
    try:
             idshare=get_job.json()['data'][0]['id']
             datashare="access_token="+Token_fb
             message='Bản Quyền Tool By Hải Magic'
             sharee = requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message='+str(message)+'&link=https://mbasic.facebook.com/'+str(idshare)+'&access_token='+str(Token_fb)+'').json()
             nhan_share={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":idshare,
              "type":"share"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/share/nhantien.php', headers=nhan_share, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
    except:
           for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
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
  elif delay==0:
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
elif ls==7:
 while True:
  cc=random.randint(1,2)
  if cc==1:
          head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
          get_job=requests.get(url='https://traodoisub.com/ex/like/load.php', headers=head_job)
          try:
             id_like=get_job.json()['data'][0]['id']
             urllike='https://graph.facebook.com/'+str(id_like)+'/likes'
             datalike="access_token="+Token_fb
             lam_job_like=requests.post(urllike, data=datalike)
             nhan_like={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_like,
              "type":"like"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/like/nhantien.php', headers=nhan_like, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
             else:
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like}",end=' \r')
              sleep(2)
          except:
           for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
  if cc==2:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    get_job=requests.get(url='https://traodoisub.com/ex/share/load.php', headers=head_job)
    try:
             idshare=get_job.json()['data'][0]['id']
             datashare="access_token="+Token_fb
             message='Bản Quyền Tool By Hải Magic'
             sharee = requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message='+str(message)+'&link=https://mbasic.facebook.com/'+str(idshare)+'&access_token='+str(Token_fb)+'').json()
             nhan_share={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/share/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":idshare,
              "type":"share"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/share/nhantien.php', headers=nhan_share, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
    except:
           for a in range(5, -1, -1):
            print(sr+'Hết nv ,Đơi ',a,end='\r')
            sleep(1)
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
  elif delay==0:
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
import os, sys, re, json
from time import sleep
import random
from datetime import datetime
import requests 
dem=0
stop=1
os.system("clear")

sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m ➺❥ \033[1;92m"
logo = """
\033[1;32m╔════════════════════════════════════════════════════════════════════╗
\033[1;32m La \033[1;96m Văn \033[1;91m  Hiếu \033[1;95m  FB:La Văn Hiếu (bảnh) \033[1;32m 
\033[1;32m╚════════════════════════════════════════════════════════════════════╝            """
print(logo)
os.system("clear")
t=datetime.now().strftime("%H:%M:%S")
h=open('tokentds.txt',mode='a+')
h=open('tokentds.txt',mode='r')
hung=h.read()
print(logo)
print(sr+'Token TDS : '+hung)
h.close()

hdoi=input(sr+'Bạn Muốn Đổi Token TDS Không (yes/no) : ')
if hdoi=='y' or hdoi=="Y":
 h=open('tokentds.txt',mode='w')
 os.system('clear')
 print(logo)
 htk=input(sr+'Nhập Token TDS Mới : ')
 h.write(htk)
 h.close()
 TDS_Token=htk
else:
 TDS_Token=hung
log=json.loads(requests.get("https://traodoisub.com/api/?fields=profile&access_token="+ TDS_Token).text)
if "success" in log:
    print(f"{sr} Đăng Nhập Thành Công")
    xu=log['data']['xu']
    user=log['data']['user']
    sleep(0.5)
    os.system("clear")
    print(logo)
    print("-"*50)
    print(f"{sr} Username TDS : {user}")
    print(f"{sr} Xu Hiện Tại : {xu}")
    print("-"*50)
    Token_fb=input(f"{sr} Nhập Token_Facebook : ")
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+Token_fb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+TDS_Token).text)
        if "success" in run:
            print("-"*50)
            print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
            sleep(0.3)
            os.system("clear")
            print(logo)
            print("-"*50)
            print(f"{sr} Username TDS : {user}")
            print(f"{sr} Xu Hiện Tại : {xu}")
            print("-"*50)
            print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
            print('-'*50)
            print(f"{sr}\033[1;92m Nhập [1] Chạy Nhiệm Vụ Like")
            print(f"{sr}\033[1;92m Nhập [2] Chạy Nhiệm Vụ Follow")
            print(f"{sr}\033[1;92m Nhập [3] Chạy Nhiệm Vụ  Like + Follow")
            print(f"{sr}\033[1;92m Nhập [4] Chạy Nhiệm Vụ Comments")
            print(f"{sr}\033[1;92m Nhập [5] Chạy Nhiệm Vụ Share")
            print(f"{sr}\033[1;92m Nhập [6] Chạy All Nhiệm Vụ")
            print("-"*50)
            ls=input(f"{sr} Nhập Số : ")
            delay=int(input(f"{sr} Nhập Delay Job (>3): "))
            nvdl=int(input(f"{sr} Sau Bao Nhiêu Nhiệm Vụ Thì Tránh Block: "))
            dlnv=int(input(f"{sr} Sau {nvdl} Nhiệm Vụ Nghỉ Bao Nhiêu Giây : "))
            hg=requests.get("https://pastebin.com/raw/F3WePrwN").text
            print("-"*50)
            print(hg)
            print("-"*50)
            while True:
                
                if ls=='1':
                  try:
                    getlike=requests.get('https://traodoisub.com/api/?fields=like&accee&access_token='+TDS_Token)
                    idlike=getlike.json()[0]['id']
                    urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
                    datalike="access_token="+Token_fb
                    try:
                     like=requests.post(urllike, data=datalike)
                    except:
                     print(sr+"Token Bị Văng Hoặc Bị Die rk")
                     Token_fb=(sr+" Nhập Token Mới : ")
                     check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+Token_fb).text)
                     if "id" in check_token:
                       idfb = check_token['id']
                       namefb = check_token['name']
                       run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+TDS_Token).text)
                       if "success" in run:
                        print("-"*50)
                        print("\033[1;92m🌍 Chạy FB : " + str(namefb) +" | ID " + str(idfb))
                    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+TDS_Token).text)
                        
                    id=idlike[0:15]
                    if "success" in nhan:
                            
                            
                        dem=dem+1
                        t=datetime.now().strftime("%H:%M:%S")
                        print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(nhan['data']['xu'])}\033[1;97m]")
                        if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        
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
                    else:
                        print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike}",end=' \r')

                  except:
                  	 for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                
                elif ls=='2':
                    try:
                     getsub=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+TDS_Token)
                     idsub=getsub.json()[0]['id']
                    except:
                      for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                    datasub = "access_token="+Token_fb
                    urlsub = 'https://graph.facebook.com/'+str(idsub)+'/subscribers'
                    try:
                     sub=requests.post(urlsub, data=datasub)
                    except:
                     print(sr+"Token Bị Văng Hoặc Bị Die rk")
                     Token_fb=input(sr+'Nhập Token Mới : ')
                    nhan = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idsub)+'&access_token='+TDS_Token).text)
                    if "success" in nhan:
                        dem=dem+1
                        t=datetime.now().strftime("%H:%M:%S")
                        print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idsub} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                        if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                        else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                            
                                print(" [\]  Đang Delay ",demtg,end='\r')
                            
                                print(" [|]  Đang Delay ",demtg,end='\r')
                            
                                print(" [/]  Đang Delay ",demtg,end='\r')
                            
                    else:
                        print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idsub}",end='\r')
                elif ls=='3':
                      try:
                        cc=random.randint(1,2)
                        if int(cc)==1:
                    
                            getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+TDS_Token)
                            idlike=getlike.json()[0]['id']
                            urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
                            datalike="access_token="+Token_fb
                            like=requests.post(urllike, data=datalike)
                            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+TDS_Token).text)
                        
                            id=idlike[0:15]
                            if "success" in nhan:
                            
                            
                                dem=dem+1
                                t=datetime.now().strftime("%H:%M:%S")
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                                if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
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
                            else:
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike}")
                    
                        
                
                        elif int(cc)==2:
                            getsub=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+TDS_Token)
                            idsub=getsub.json()[0]['id']
                            datasub = "access_token="+Token_fb
                            urlsub = 'https://graph.facebook.com/'+str(idsub)+'/subscribers'
                            sub=requests.post(urlsub, data=datasub)
                            nhan = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idsub)+'&access_token='+TDS_Token).text)
                            if "success" in nhan:
                                dem=dem+1
                                t=datetime.now().strftime("%H:%M:%S")
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idsub} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                                if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                else:
                                    for demtg in range(delay, -1, -1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                       
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        
                            else:
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idsub}",end=' \r')
                      except:
                       print(sr+' Random Lỗi Chút 👻👻')
                      
                elif ls=='4':
                    try:
                        getcmt=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+TDS_Token)
                        idcmt=getcmt.json()[0]['id']
                        datacmt = "access_token="+Token_fb
                        msgcmt=getcmt.json()[0]['msg']
                        data_cmt={
                        'access_token':Token_fb, 
                        'message':msgcmt,
                         }
                        cmtpost = requests.post(f"https://graph.facebook.com/{idcmt}/comments",data=data_cmt)
                        nhan = json.loads( requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idcmt)+'&access_token='+TDS_Token).text)
                        if "success" in nhan:
                            dem=dem+1
                            t=datetime.now().strftime("%H:%M:%S")
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mCOMMENTS\033[1;97m]\033[1;92m {idcmt} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]\n \033[1;92m➺❥ Nội Dung Comments : \033[1;97m {msgcmt}")
                            if dem==stop*nvdl:
                                stop+=1
                                for demtg in range(dlnv, -1,-1):
                                    print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [\]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [|]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [/]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
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
                        else:
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mComment\033[1;97m]\033[1;92m {idcmt}",end='\r')
                    except:
                       for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                elif ls=='5':
                    try:
                        getshare=requests.get('https://traodoisub.com/api/?fields=share&access_token='+TDS_Token)
                        idshare=getshare.json()[0]['id']
                        datashare = "access_token="+Token_fb
                        message = 'Bản Quyền Tool By Hải Magic'
                        sharee = requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message='+str(message)+'&link=https://mbasic.facebook.com/'+str(idshare)+'&access_token='+str(Token_fb)+'').json()
                        nhan = json.loads( requests.get('https://traodoisub.com/api/coin/?type=SHARE&id='+str(idshare)+'&access_token='+TDS_Token).text)
                        if "success" in nhan:
                            dem=dem+1
                            t=datetime.now().strftime("%H:%M:%S")
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idcmt} \033[1;97m[\033[1;92m+800\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                            if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
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
                        else:
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare}",end='\r')
                    except:
                        for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                elif ls=='6':
                   ss=random.randint(1,4)
                    
                   if ss==1:
                        try:
                            getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+TDS_Token)
                            idlike=getlike.json()[0]['id']
                            urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
                            datalike="access_token="+Token_fb
                            like=requests.post(urllike, data=datalike)
                            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+TDS_Token).text)
                        
                            id=idlike[0:15]
                            if "success" in nhan:
                            
                            
                                dem=dem+1
                                t=datetime.now().strftime("%H:%M:%S")
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(nhan['data']['xu'])}\033[1;97m]")
                                if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        
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
                            else:
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike}",end=' \r')
                        except:
                  	
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",end='\r')
                            sleep(0.52)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸",end='\r')
                            sleep(0.25)
                        
                
                   elif ss==2:
                        try:
                            getsub=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+TDS_Token)
                            idsub=getsub.json()[0]['id']
                            datasub = "access_token="+Token_fb
                            urlsub = 'https://graph.facebook.com/'+str(idsub)+'/subscribers'
                            sub=requests.post(urlsub, data=datasub)
                            nhan = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idsub)+'&access_token='+TDS_Token).text)
                            if "success" in nhan:
                                dem=dem+1
                                t=datetime.now().strftime("%H:%M:%S")
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idsub} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                                if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
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
                            else:
                                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idsub}",end='\r')
                        except:
                            print(" [-]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                   elif ss==3:
                    try:
                        getcmt=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+TDS_Token)
                        idcmt=getcmt.json()[0]['id']
                        datacmt = "access_token="+Token_fb
                        msgcmt=getcmt.json()[0]['msg']
                        data_cmt={
                        'access_token':Token_fb, 
                        'message':msgcmt,
      }
                        cmtpost = requests.post(f"https://graph.facebook.com/{idcmt}/comments",data=data_cmt)
                        nhan = json.loads( requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idcmt)+'&access_token='+TDS_Token).text)
                        if "success" in nhan:
                            dem=dem+1
                            t=datetime.now().strftime("%H:%M:%S")
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mCOMMENTS\033[1;97m]\033[1;92m {idcmt} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]\n \033[1;92m➺❥ Nội Dung Comments : \033[1;97m {msgcmt}")
                            if dem==stop*nvdl:
                                stop+=1
                                for demtg in range(dlnv, -1,-1):
                                    print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [\]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [|]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
                                    print(" [/]  Đang Delay ",demtg,end='\r')
                                    sleep(0.25)
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
                        else:
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mComment\033[1;97m]\033[1;92m {idcmt}",end='\r')
                    except:
                        for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ gòi Chờ Xíu Nha 🥺  ",demtg,end='\r')
                            sleep(0.25)
                   elif ss==4:
                    try:
                        getshare=requests.get('https://traodoisub.com/api/?fields=share&access_token='+TDS_Token)
                        idshare=getshare.json()[0]['id']
                        datashare = "access_token="+Token_fb
                        message = 'Bả Quyền Tool By Hải Magic'
                        sharee = requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message='+str(message)+'&link=https://mbasic.facebook.com/'+str(idshare)+'&access_token='+str(Token_fb)+'').json()
                        nhan = json.loads( requests.get('https://traodoisub.com/api/coin/?type=SHARE&id='+str(idshare)+'&access_token='+TDS_Token).text)
                        if "success" in nhan:
                            dem=dem+1
                            t=datetime.now().strftime("%H:%M:%S")
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idcmt} \033[1;97m[\033[1;92m+800\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
                            if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay ",demtg,end='\r')
                                        sleep(0.25)
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
                        else:
                            print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mSHARE\033[1;97m]\033[1;92m {idshare}",end='\r')
                    except:
                        for demtg in range(1, -1, -1):
                            print(" [-]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                            print(" [\]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [|]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸  ",demtg,end='\r')
                            sleep(0.25)
                            print(" [/]  Hết Nhiệm Vụ Rồi Chờ Tí Đi Bro 🌸 ",demtg,end='\r')
                            sleep(0.25)
                else:
                        print(sr+"Nhập Sai!!")
        else:
                exit(sr+"Cấu Hình Không Hợp Lệ")
    else:
            exit(sr+"Token Die")
    
    
else:
    print(f"{sr} Đăng Nhập Thất Bại , Vui Lòng Kiểm Tra Lại Access_Token")
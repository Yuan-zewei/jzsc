# -*- coding: utf-8 -*-
from dao import Mysql
import datetime
import uuid,re
import requests,time,json,random
from Crypto.Cipher import AES
from binascii import a2b_hex
class Base():
    def __init__(self):
        pass
    def date(self):
        date = datetime.date.today()
        return str(date)

    def uuid(self):
        uu = uuid.uuid4()
        return uu

    def ipz(self):
        # 设置代理连接
        while True:
            resp1 = requests.get('代理的连接')
            resp = resp1.text
            if str(resp1) == '<Response [200]>':
                resp1 = json.loads(resp)['data']
                http = str(resp1[0]["ip"]) + ":" + str(resp1[0]["port"])
                ip = {"http": "http://" + http, "https": "https://" + http}
                return ip
            else:
                time.sleep(random.uniform(2, 3))
    def jichutoken(self):
        try:
            while True:
                a=Mysql.jichutoken(yxq='0')
                if a:
                    return a
                else:
                    time.sleep(5)
        except Exception as e:
            print(e, '文件错误')
    def jd_nx(self,data):
        iv = b"0123456789ABCDEF"
        key = "jo8j9wGw%6HbxfFn".encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)#key,iv,AES,cbc,hex,
        plain = cipher.decrypt(a2b_hex(data))
        qw=bytes.decode(plain).rsplit('\0')
        qw1=json.loads(re.subn(r'\x02|\x0f|\x06|\x0b|\x05|\x08\x07','',str(qw[0]))[0])
        return qw1

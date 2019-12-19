# -*- coding: utf-8 -*-
from dao import Mysql
import datetime
import uuid
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
            resp1 = requests.get(
                'http://api.ip.data5u.com/dynamic/get.html?order=dac8945cfa0501d5221c5e05c4f88b9c&json=1&random=true&sep=3')
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
                    # print('暂无有效的token值程序暂停---正在获取token值')
                    time.sleep(5)
        except Exception as e:
            print(e, '文件错误')
    #破解源码加密的方法
    # def jd_nx(self,data):
    #     x = execjs.compile('''
    #     function Aes(data) {
    #         module.paths.push("\\Users\\admin\\AppData\\Roaming\\npm\\node_modules");
    #         let CryptoJS=require('crypto-js');
    #         var u= CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn"),
    #         d = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");
    #             e = CryptoJS.enc.Hex.parse(data);
    #             n = CryptoJS.enc.Base64.stringify(e);
    #           return  CryptoJS.AES.decrypt(n, u, {
    #             iv: d,
    #             mode: CryptoJS.mode.CBC,
    #             padding: CryptoJS.pad.Pkcs7
    #         }).toString(CryptoJS.enc.Utf8);
    #     }
    #            ''')
    #     return x.call('Aes', f'{data}')

    def jd_nx(self,data):
        iv = b"0123456789ABCDEF"
        key = "jo8j9wGw%6HbxfFn".encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain = cipher.decrypt(a2b_hex(data))
        return bytes.decode(plain).rsplit('\0')

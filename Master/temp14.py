# -*- coding: utf-8 -*-
import requests
import time
from biz import base
from dao import Mysql
import json
import random
from uuid import uuid4
class jzscBiz2(base.Base):
    def __init__(self):
        base.Base.__init__(self)
        self.ip=self.ipz()
        USER_AGENTS_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', ]
        self.headers = {
       'Accept':'application / json, text / plain, * / *Accept - Encoding: gzip, deflateAccept - Language: zh - CN, zh;q = 0.9',
       'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLXOudoaB0fz7nmqjLJ9wglMhpUUKvcMtoMqfGfwdLCb8g==',
       # 'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLXZe7lTc49THz4peUq97aBYhpUUKvcMtoMqfGfwdLCb8g==',
        'Connection': 'keep - alive',
        'Cookie': f'_9755xjdesxxd_ = 32;YD00341567120424 % 3AWM_TID = zLtSWcZTanBEBVUVQVIs5 % 2FT2IBc97W2s;YD00341567120424 % 3AWM_NI = mRGy3ES3CmtKX7S5tD % 2FHtXF % 2Fn0kzkFG3qQkIzSC1a5ZsZSBr % 2Ft9Hn8NHiw0HMRJnuIUAO % 2BXqcFMkgmnB1Eal0vu6lAzyZTuKaQ6VgltOJxar5s1n1hOnbm19fNRsTDmjbUk % 3D;YD00341567120424 % 3AWM_NIKE = 9ca17ae2e6ffcda170e2e6eeb5c54783b587aecf7d97ef8fb7d84a968e8babee3e918dbdb5c27c8399e1d4c12af0fea7c3b92aaf8e899ab24f91ed8d8ef7419ce99dd6f750ed98bcb9c525aef0a59bea4e85edbfb2ea43ba8d8dd2e43f9aad96b4c17aedacf7a9ed348e98a798b3448f8e868ff843979f81ccdb7ba19a838ce667ae9effa6e468f4aabbd7ef4bbaa796b5f841a38ffab7e668b8918699e47af7adff8fb4648db2ae8eb433a6929e94d750afb6aeb6ea37e2a3;Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c = 1572936867, 1573029707, 1573269205, 1573269302;gdxidpyhxdE = M5R % 5CryAVk4ztCg3Zu8oE025xHXsM4ebNykbBxJESnXac9QZain728auXCQOSJbSJ6hxME3f % 2BDJQcaIzh6njpy2bhRosEh % 5C8HZfK % 5ChdJnmarPzMT9GgMe % 2FTmfwBkadIRZT65ERa4O % 2BhMmAH6cOKAyyMIJPlfaNDeYm5DEvdjw % 2BczxgtDi % 3A1573278517540;Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c = {time.time()}',
        'Host': 'jzsc.mohurd.gov.cn',
        'Referer': 'http://jzsc.mohurd.gov.cn',
        'timeout': '30000',
            # User-Agent多。 一页换一个，就任性！
            "User-Agent": random.choice(USER_AGENTS_list)}
    # 爬取企业基础信息
    def qyjcxx(self):
        try:
            a = Mysql.qiyexx()
            if a==None:
                print('当前没有数据可以爬取')
            else:
                print(a)
                self.z = a[1] # 企业名字
                self.qyid=a[0]
                # print(self.qyid)
                url = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?complexname={self.z}&pg=0&pgsz=15&total=0'  # 链接
                print(f'正在进行========================{self.z}========================================关键字信息的爬取')
                if url == None:  # 判断这个链接正不正确
                    print('信息不正确')
                    Mysql.gxqy(cx_state='0', gsname=self.z)
                else:
                    print('--------------------------------')
                    resp = requests.get(url=url, headers=self.headers,proxies=self.ip,timeout=15)
                    # print(resp.text)
                    if str(resp) == '<Response [200]>':
                        # print(resp.text)
                        asddd = self.jd_nx(data=f'{resp.text}')
                        assss=json.loads(asddd)
                        if assss['code']==200:
                            # print(assss['data']['list'])
                            qy_list=assss['data']
                            if len(qy_list['list'])!=0:
                                Mysql.insert_qy_list(eid=self.qyid,qyname=self.z, bh='1', qy_zt='1')  # 筛选出正确的企业id
                                print('放入数据成功')
                                qy_xinxi1=qy_list['list']
                                for qy_xinxi in qy_xinxi1:
                                    print(qy_xinxi,'-=-=-=-=-=-=-----------------------')
                                    qyid=qy_xinxi['QY_ID']
                                    QY_ORG_CODE=qy_xinxi['QY_ORG_CODE']
                                    QY_NAME=qy_xinxi['QY_NAME']
                                    print(qyid,QY_ORG_CODE,QY_NAME)
                                    dwid = Mysql.qiyexx_eid(qyname=QY_NAME)
                                    print(dwid)
                                    if dwid ==None:
                                        dwid=uuid4()
                                    else:
                                        dwid=dwid[0]
                                    Mysql.gxqy_fupa_te(zt='1', gsname=a[1])
                                    a = Mysql.selecttbl_qyname(eid=self.qyid)
                                    if a == None:
                                        print('正在插入tbl_fupa_temp表')
                                        Mysql.insetqyzt(eid=dwid,type='0', cx_val=QY_NAME, cx_state='1', qiyeurl=qyid, qyzzzt='1',
                                                        ryzt='1',
                                                        ryzyzc_zt='1', bh='1',qy_jcxx_zt='1')
                                        Mysql.update_qname_list(qy_zt=1, eid=dwid[0])
                                    else:
                                        print('数据库已经存在该公司！！')
                                        Mysql.update_qname_list(qy_zt=2, eid=dwid[0])
                            else:
                                # pass
                                print(f'没有{a[1]}这个公司')
                                Mysql.gxqy_fupa_te(zt='0',gsname=a[1])
                        else:
                            print('你的ip被封')
                            self.ip = self.ipz()
                            print('ip切换成功')
                    else:
                        asddd = self.jd_nx(data=f'{resp.text}')
                        assss=json.loads(asddd)
                        print('请求失败',assss)
                        self.ip = self.ipz()
                    # break
        except Exception as e:
            print(e)
            self.ip=self.ipz()
            # return e, self.gsname


if __name__ == '__main__':
    while True:
        try:
            a = jzscBiz2()
            a.qyjcxx()
        except Exception as E:
            print(E)

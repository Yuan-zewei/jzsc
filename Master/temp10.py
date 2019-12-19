# -*- coding: utf-8 -*-
import requests
import time
from biz import base
from dao import Mysql
import json
import random
from uuid import uuid4
from qy import qyxx

class jzscBiz2(base.Base):
    def __init__(self):
        base.Base.__init__(self)
        self.jichu=self.jichutoken()[0]
        self.ip={"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
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
            'Accept': 'application / json, text / plain, * / *Accept - Encoding: gzip, deflateAccept - Language: zh - CN, zh;q = 0.9',
            'accessToken': f'{self.jichu}',
            'Connection': 'keep - alive',
            'Cookie': f'_9755xjdesxxd_ = 32;YD00341567120424 % 3AWM_TID = zLtSWcZTanBEBVUVQVIs5 % 2FT2IBc97W2s;YD00341567120424 % 3AWM_NI = mRGy3ES3CmtKX7S5tD % 2FHtXF % 2Fn0kzkFG3qQkIzSC1a5ZsZSBr % 2Ft9Hn8NHiw0HMRJnuIUAO % 2BXqcFMkgmnB1Eal0vu6lAzyZTuKaQ6VgltOJxar5s1n1hOnbm19fNRsTDmjbUk % 3D;YD00341567120424 % 3AWM_NIKE = 9ca17ae2e6ffcda170e2e6eeb5c54783b587aecf7d97ef8fb7d84a968e8babee3e918dbdb5c27c8399e1d4c12af0fea7c3b92aaf8e899ab24f91ed8d8ef7419ce99dd6f750ed98bcb9c525aef0a59bea4e85edbfb2ea43ba8d8dd2e43f9aad96b4c17aedacf7a9ed348e98a798b3448f8e868ff843979f81ccdb7ba19a838ce667ae9effa6e468f4aabbd7ef4bbaa796b5f841a38ffab7e668b8918699e47af7adff8fb4648db2ae8eb433a6929e94d750afb6aeb6ea37e2a3;Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c = 1572936867, 1573029707, 1573269205, 1573269302;gdxidpyhxdE = M5R % 5CryAVk4ztCg3Zu8oE025xHXsM4ebNykbBxJESnXac9QZain728auXCQOSJbSJ6hxME3f % 2BDJQcaIzh6njpy2bhRosEh % 5C8HZfK % 5ChdJnmarPzMT9GgMe % 2FTmfwBkadIRZT65ERa4O % 2BhMmAH6cOKAyyMIJPlfaNDeYm5DEvdjw % 2BczxgtDi % 3A1573278517540;Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c = {time.time()}',
            'Host': 'jzsc.mohurd.gov.cn',
            'Referer': 'http://jzsc.mohurd.gov.cn',
            'timeout': '30000',
            "User-Agent": random.choice(USER_AGENTS_list)}

    def qyjcxx(self):
        try:
            a = Mysql.qiyexx_url(bh='1')[0]  # 从复爬表
            if a==None:
                print('没有数据可以爬取')
                time.sleep(10)
            else:
                print(a)
                self.qyid = a[0]  # 公司eid
                self.z = a[0]  # 公司名字
                qw = self.gx_qyid()
                self.qyid1=qw
                if a[7]=='1':
                    self.jichu12()  # 基础信息的爬取
                else:
                    print('基础信息爬取完毕')
                if a[8]=='1':
                    self.qyzz()  # 基础信息的爬取
                else:
                    print('资质信息爬取完毕')
                if a[9]=='1':
                    self.qy_user()  # 基础信息的爬取
                else:
                    print('人员信息爬取完毕')
                # self.gcxmxx()
                a = Mysql.qiyexx_url(bh='1')[0]
                if a[7] == '0' and (a[8] == '0' or a[8]=='404') and (a[9] == '0' or a[9] == '404'):
                    Mysql.gxqy_fupa(cx_state='0', eid=self.qyid)
                    print('状态更新完毕')
        except Exception as e:
            print(e,'jgfufh')
            # return e, self.gsname
    def gx_qyid(self):
        try:
            print('开始更新企业id')
            qyurl=f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?complexname={self.z}&pg=0&pgsz=15&total=0'
            resp1 = requests.get(url=qyurl, headers=self.headers,proxies=self.ipz(),timeout=10)
            asddd1 = self.jd_nx(data=f'{resp1.text}')
            asddd2 = json.loads(asddd1)
            print(asddd2)
            if len(asddd2['data']['list'])==0:
                print('没有这个公司异常')
                Mysql.gxqy_fupa(cx_state='3', eid=self.qyid)
            else:
                qyid= asddd2['data']['list'][0]['QY_ID']
                Mysql.update_qyid(qyurl=qyid,eid=self.qyid)#更新企业id
                print('企业更新完毕')
                return qyid
        except Exception as e:
            qq = str(e)
            if qq.find("HTTPConnectionPool") != -1:
                print('ip失效')
                Mysql.dele_token(token=self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                print('不存在')
                print(e, '基础信息错误')
    def jichu12(self):
        # 基础信息
        try:
            qy_jichu = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/compDetail?compId={self.qyid1}'
            resp1 = requests.get(url=qy_jichu, headers=self.headers,proxies=self.ip,timeout=10)
            asddd1 = self.jd_nx(data=f'{resp1.text}')
            asddd2 = json.loads(asddd1)
            print(asddd2)
            if asddd2['code'] != 200:
                # self.hq_token(qyid=self.qyid1, name=self.z)#调用selenuim获得token值
                Mysql.dele_token(token=self.jichu)
                print(self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                if asddd2['data'] == None:
                    self.gx_qyid()
                else:
                    qyxx.qyjichu(asddd2['data']['compMap'], qyid=self.qyid)
                    Mysql.update_qyjcxx(qy_jcxx_zt='0',eid=self.qyid)
                    return '0'
        except Exception as e:
            qq=str(e)
            if qq.find("HTTPConnectionPool")!=-1:
                print('ip失效')
                Mysql.dele_token(token=self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                print('不存在')
                print(e,'基础信息错误')

    def qyzz(self):
        # 企业资质
        try:
            qy_zz = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/caDetailList?qyId={self.qyid1}&pg=0&pgsz=500'
            # qy_zz = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/caDetailList?qyId=0F0F0E060E0E0D0C0D0E0A0E0D0B09070B09&pg=0'
            resp2 = requests.post(url=qy_zz, headers=self.headers,proxies=self.ip,timeout=10)
            asddd3 = self.jd_nx(data=f'{resp2.text}')
            asddd4 = json.loads(asddd3)
            print(asddd4)
            if asddd4['code'] != 200:
                # self.hq_token(qyid=self.qyid1, name=self.z)  # 调用selenuim获得token值
                Mysql.dele_token(token=self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                print(asddd4)
                if asddd4['data'] == None:
                    self.gx_qyid()
                else:
                    print(asddd4)
                    a123 = asddd4['data']['pageList']['list']
                    if len(a123) != 0:
                        p1 = 0
                        for resp in a123:
                            p1 += 1
                            print(f'一共{len(a123)}个企业资质现在是第{p1}个企业资质')
                            qyxx.qyzz(resp=resp, qyid=self.qyid)
                        if p1 == len(a123):
                            Mysql.updatet_qyzzzt(qyzzzt='0',eid=self.qyid)
                            return '0'
                    else:
                        print('没有企业资质')
                        Mysql.updatet_qyzzzt(qyzzzt='404', eid=self.qyid)
                        return '404'
        except Exception as e:
            qq = str(e)
            if qq.find("HTTPConnectionPool") != -1:
                print('ip失效')
                Mysql.dele_token(token=self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                print('不存在')
                print(e, '资质信息错误')

    def qy_user(self):
        # 企业人员信息的爬取
        try:
            ry_url = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/regStaffList?qyId={self.qyid1}&pg=0&pgsz=5000'
            # print(ry_url)
            resp2 = requests.get(url=ry_url, headers=self.headers,proxies=self.ip,timeout=10)
            asd3 = self.jd_nx(data=f'{resp2.text}')
            asd4 = json.loads(asd3)
            print('人员')
            if asd4['data'] == None:
                self.gx_qyid()
            else:
                ry_urlte = asd4['data']['pageList']['list']
                if len(ry_urlte) == 0:
                    print('该公司没有人员信息')
                    Mysql.updateryzt(ryzt='404', eid=self.qyid)
                    return '404'
                else:
                    # asd=Mysql.selecttbl_qyname(eid=self.qyid)
                    # Mysql.delete_tbl_user(qyid=self.qyid)  # 删除人员的基础信息
                    # Mysql.deletetbl_user_zcxx1(qyid=self.z)
                    a1 = Mysql.selectryurl_ys1(eid=self.qyid)
                    print(a1,'-=-----------------------------------------')
                    if a1[0]==None:
                        a2=0
                        po = 1
                        Mysql.delete_tbl_user(qyid=self.qyid)
                        Mysql.deletetbl_user_zcxx1(qyid=self.qyid)
                        print('删除成功')
                    else:
                        a2=int(a1[0])-1
                        po =int(a1[0])
                    # print(ry_urlte[int(a2)-1:])
                    for res in ry_urlte[a2:]:
                        print(res)
                        print(f'--------------------------一共{len(ry_urlte)}个人++++第{po}个人--------------------------------')
                        userid = uuid4()
                        user = res['RY_ID']
                        username = res['RY_NAME']
                        ry_xinxi = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/staff/staffDetail?staffId={user}'
                        resp3 = requests.get(url=ry_xinxi, headers=self.headers,proxies=self.ip,timeout=10)
                        asd5 = self.jd_nx(data=f'{resp3.text}')
                        asd6 = json.loads(asd5)
                        print(asd6)
                        if asd6['code'] != 200:
                            print(asd6)
                            # self.hq_token(qyid=self.qyid1, name=self.z)#调用selenuim获得token值
                            print(self.jichu)
                            Mysql.dele_token(token=self.jichu)
                            print('token删除成功')
                            Mysql.token(token=self.jichu)
                            self.jichu = self.jichutoken()[0]
                            self.ip = {"http": "http://" + self.jichutoken()[1],
                                       "https": "https://" + self.jichutoken()[1]}
                            print(self.jichu)
                            break
                        else:
                            qyxx.ryxx(resp=asd6['data']['staffMap'], qyid=self.qyid, user=userid)
                            asd7 = asd6['data']['regCertList']
                            print('人员注册信息',asd7)
                            x=1
                            for res in asd7:
                                print(f'{username}一共有{len(asd7)}个注册信息正在爬取第{x}个注册信息')
                                qyxx.ryxx_xinxi(resp=res,user=userid, zc_dwid=self.qyid)
                                x+=1
                            print('sddd',len(asd7),x-1)
                            if len(asd7)==x-1:
                                Mysql.updatery_page_zd(ry_page_zd=po, eid=self.qyid)  # 实时更新爬取的页数
                                po += 1
                            else:
                                pass
                            if po-1 == len(ry_urlte):
                                Mysql.updateryzt(ryzt='0', eid=self.qyid)#更新爬取状态
                                return '0'
                            else:
                                pass
        except Exception as e:
            qq = str(e)
            if qq.find("HTTPConnectionPool") != -1:
                print('ip失效')
                Mysql.dele_token(token=self.jichu)
                print('token删除成功')
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
                self.ip = {"http": "http://" + self.jichutoken()[1], "https": "https://" + self.jichutoken()[1]}
            else:
                print('不存在')
                print(e, '人员信息错误')
    def gcxmxx(self):
        try:
            qy_gcxm_list = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/compPerformanceListSys?qy_id={self.qyid1}&pg=0&pgsz=15'
            resp2 = requests.post(url=qy_gcxm_list, headers=self.headers)
            asddd3 = self.jd_nx(data=f'{resp2.text}')
            print(asddd3)
            asddd4 = json.loads(asddd3)
            if asddd4['code'] != 200:
                # self.hq_token(qyid=self.qyid1, name=self.z)  # 调用selenuim获得token值
                Mysql.token(token=self.jichu)
                self.jichu = self.jichutoken()[0]
            # print('----工程项目列表！！!\n', asddd4)
            gcxm_datas = asddd4['data']['list']
            if len(gcxm_datas) == 0:
                print('该公司没有工程项目信息')
                return '404'
            else:
                self.a = 0
                for res1 in gcxm_datas:
                    self.a += 1
                    print(f'----------------------------一共{len(gcxm_datas)}个工程项目现在是第{self.a}个工程项目-------------------------')
                    gcxm_url_ID = res1['ID']  # 工程项目的详情页连接
                    qy_gcxm = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/project/projectDetail?id={gcxm_url_ID}'
                    resp3 = requests.post(url=qy_gcxm, headers=self.headers)
                    asddd5 = self.jd_nx(data=f'{resp3.text}')
                    asddd6 = json.loads(asddd5)
                    if asddd6['code'] != 200:
                        # self.hq_token(qyid=self.qyid1, name=self.z)  # 调用selenuim获得token值
                        Mysql.token(token=self.jichu)
                        self.jichu = self.jichutoken()[0]
                    gcxm_data = asddd6['data']
                    if len(gcxm_data) > 0:
                        print(f'第{self.a}个项目{gcxm_data["PRJNAME"]}的相关信息！！！！！')
                        print(gcxm_data)
                        qyxx.gcxm(resp=gcxm_data, qyid=self.qyid, i=self.a)  # 工程项目的部分信息
                        qyxx.gcxm_jcxx(resp=gcxm_data, qyid=self.qyid)                       # 工程项目的基础信息
                        qyxx.gcxm_weizhi(resp=gcxm_data, qyid=self.qyid)                     # 工程项目的未知信息
                if self.a==len(gcxm_datas):
                    return '0'
        except Exception as e:
            print(e)
            self.gcxmxx()

if __name__ == '__main__':
    while True:
        a = jzscBiz2()
        a.qyjcxx()

import json,time,re,pyautogui
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dao import Mysql
from selenium.webdriver import ActionChains
from PIL import Image
from token.chaojiying import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.command import Command
from Crypto.Cipher import AES
from binascii import a2b_hex
from selenium.webdriver.support.wait import WebDriverWait
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
import random,requests
headers = {
    'Accept': 'application / json, text / plain, * / *Accept - Encoding: gzip, deflateAccept - Language: zh - CN, zh;q = 0.9',
    'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLWV76R7mVXvG+ABPQw7ggYRhpUUKvcMtoMqfGfwdLCb8g==',
    'Connection': 'keep - alive',
    'Cookie': f'_9755xjdesxxd_ = 32;YD00341567120424 % 3AWM_TID = zLtSWcZTanBEBVUVQVIs5 % 2FT2IBc97W2s;YD00341567120424 % 3AWM_NI = mRGy3ES3CmtKX7S5tD % 2FHtXF % 2Fn0kzkFG3qQkIzSC1a5ZsZSBr % 2Ft9Hn8NHiw0HMRJnuIUAO % 2BXqcFMkgmnB1Eal0vu6lAzyZTuKaQ6VgltOJxar5s1n1hOnbm19fNRsTDmjbUk % 3D;YD00341567120424 % 3AWM_NIKE = 9ca17ae2e6ffcda170e2e6eeb5c54783b587aecf7d97ef8fb7d84a968e8babee3e918dbdb5c27c8399e1d4c12af0fea7c3b92aaf8e899ab24f91ed8d8ef7419ce99dd6f750ed98bcb9c525aef0a59bea4e85edbfb2ea43ba8d8dd2e43f9aad96b4c17aedacf7a9ed348e98a798b3448f8e868ff843979f81ccdb7ba19a838ce667ae9effa6e468f4aabbd7ef4bbaa796b5f841a38ffab7e668b8918699e47af7adff8fb4648db2ae8eb433a6929e94d750afb6aeb6ea37e2a3;Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c = 1572936867, 1573029707, 1573269205, 1573269302;gdxidpyhxdE = M5R % 5CryAVk4ztCg3Zu8oE025xHXsM4ebNykbBxJESnXac9QZain728auXCQOSJbSJ6hxME3f % 2BDJQcaIzh6njpy2bhRosEh % 5C8HZfK % 5ChdJnmarPzMT9GgMe % 2FTmfwBkadIRZT65ERa4O % 2BhMmAH6cOKAyyMIJPlfaNDeYm5DEvdjw % 2BczxgtDi % 3A1573278517540;Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c = {time.time()}',
    'Host': 'jzsc.mohurd.gov.cn',
    'Referer': 'http://jzsc.mohurd.gov.cn',
    'timeout': '30000',
    "User-Agent": random.choice(USER_AGENTS_list)}
# 破解源码加密的方法
def jd_nx(data):
    iv = b"0123456789ABCDEF"
    key = "jo8j9wGw%6HbxfFn".encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = cipher.decrypt(a2b_hex(data))
    qw = bytes.decode(plain).rsplit('\0')
    qw1 = json.loads(re.subn(r'\x02|\x0f|\x06|\x0b|\x05|\x08\x07', '', str(qw[0]))[0])
    return qw1
#更新企业qyid
def gx_qyid(z,eid):
    print('开始更新企业id')
    qyurl = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?complexname={z}&pg=0&pgsz=15&total=0'
    resp1 = requests.get(url=qyurl, headers=headers)
    asddd2 = jd_nx(data=f'{resp1.text}')
    if len(asddd2['data']['list']) == 0:
        print('没有这个公司异常')
        Mysql.gxqy_fupa(cx_state='3', eid=eid)
    else:
        qyid = asddd2['data']['list'][0]['QY_ID']
        Mysql.update_qyid(qyurl=qyid, eid=eid)  # 更新企业id
        return qyid
#selenuim
def selenu(url,qyname,ip):
    print(f'开始尝试')
    caps = DesiredCapabilities.CHROME
    caps['loggingPrefs'] = {'performance': 'ALL'}
    caps = {
        'browserName': 'chrome',
        'loggingPrefs': {
            'browser': 'ALL',
            'driver': 'ALL',
            'performance': 'ALL',
        },
        'goog:chromeOptions': {
            'perfLoggingPrefs': {
                'enableNetwork': True,
            },
            'w3c': False,
        },
    }
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('w3c', False)
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])#开始实验性功能非常牛叉的参数,防止网页发现你是selenuim
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument(f'--proxy-server=http://{ip}')#隐藏浏览器
    driver = webdriver.Chrome(options=chromeOptions,desired_capabilities=caps)
    driver.maximize_window()
    driver.set_page_load_timeout(40)#超过这个时间直接报错
    driver.get(f'http://jzsc.mohurd.gov.cn/data/company/detail?id={url}')
    a=1
    while True:
        try:
            time.sleep(3)
            he1 = driver.page_source
            time.sleep(1)
            if he1.find('重新验证')!=-1 and he1.find(f'{qyname}')==-1:
                # driver.switch_to.window(driver.window_handles[0])#切换窗口发现没啥用
                time.sleep(3)
                tijiao = driver.find_element_by_xpath('//*[@id="app"]/div/header/div[5]/div/div[3]/div/button[1]/span')
                driver.execute_script("arguments[0].click();", tijiao)
                time.sleep(1)
                # driver.switch_to.window(driver.window_handles[0])#切换窗口
                hem = driver.page_source
                time.sleep(1)
                for ui in range(0,6):
                    if hem.find('请完成安全验证')!=-1 or hem.find(f'{qyname}')==-1:
                        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
                        current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
                        time.sleep(0.5)
                        imgelement = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]')
                        locations = imgelement.location
                        sizes = imgelement.size
                        rangle = (
                            int(locations['x'] + 20), int(locations['y'] + 20),
                            int(locations['x'] + sizes['width'] - 20),
                            int(locations['y'] + sizes['height'] - 20))
                        pfilename = '.\\image'#路径错的话使用绝对路径
                        save_path = pfilename + '\\' + current_time1 + '_' + current_time + '.png'
                        time.sleep(1.5)
                        driver.save_screenshot(save_path)
                        img = Image.open(save_path)
                        jpg = img.convert('RGB')
                        jpg = img.crop(rangle)
                        path = pfilename + '\\' + current_time1 + '_' + current_time + '.png'
                        time.sleep(1)
                        jpg.save(path)
                        print("图片截取成功!")
                        chaojiying = Chaojiying_Client('账号', '密码','软件id')  # 用户中心>>软件ID
                        im = open(path,'rb').read()
                        zuo=chaojiying.PostPic(im, 9103)
                        groups = zuo.get('pic_str').split('|')
                        locations_chaojiying = [[int(number) for number in group.split(',')] for group in groups]
                        if len(locations_chaojiying) > 0:
                            element = WebDriverWait(driver, 5, 0.5).until(
                                EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
                            ActionChains(driver).move_to_element(element)
                            time.sleep(0.5)
                            location_x = 0
                            location_y = 0
                            pyautogui.moveTo(locations['x'] + 25, int(locations['y'] + 96), duration=0.3)#驱动鼠标操作，可以使用，只是看看
                            for location in locations_chaojiying:
                                pyautogui.moveRel(location[0] - location_x, location[1] - location_y,
                                                  duration=0.6)
                                driver.execute(Command.MOVE_TO, {'xoffset': location[0], 'yoffset': location[1]})
                                print(" 点击坐标 " + str(location[0]), str(location[1]))
                                ActionChains(driver).move_to_element_with_offset(element, location[0],
                                                                                 location[
                                                                                     1] + 2).click().perform()
                                time.sleep(random.randint(1,3)+random.random())
                                location_x = location[0]
                                location_y = location[1]
                        time.sleep(10)#防止网页加载速度过慢拿不到公司名字
                        print('移动成功')
                        hem12=driver.page_source
                        if hem12.find(f'{qyname}')!=-1:
                            print('跳过验证码')
                            logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
                            token=re.findall("accessToken': '(.*?)==', 'timeout': '30000'",str(logs))[-1]+'=='
                            a21=Mysql.seletoken(token=token)
                            if a21:
                                print('token已存在跳过')
                            else:
                                Mysql.insert_token(token=token,ip=ip)
                                a=0
                            while True:
                                a12=Mysql.jichutoken(yxq='0')
                                if a12:
                                    print('token获得成功暂停5秒钟',token)
                                    time.sleep(5)
                                else:
                                    driver.refresh()
                                    break
                        else:
                            print('验证失败或者没有这个公司重新尝试')
                            time.sleep(3)
                            break
                            # driver.refresh()
            elif he1.find(f'{qyname}') != -1:
                logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
                token = re.findall("accessToken': '(.*?)==', 'timeout': '30000'", str(logs))[-1] + '=='
                a21 = Mysql.seletoken(token=token)
                if a21:
                    print('token已存在跳过')
                else:
                    Mysql.insert_token(token=token,ip=ip)
                    a = 0
                while True:
                    time.sleep(2)
                    a12 = Mysql.jichutoken(yxq='0')
                    if a12:
                        print('token获得成功暂停5秒钟', token)
                        time.sleep(5)
                    else:
                        driver.refresh()
                        break
            elif he1.find(f'{qyname}')==-1:
                print(f'2第{a}次刷新')
                driver.refresh()
                break
            else:
                time.sleep(1.5)
                driver.refresh()
                break
        except Exception as e:
            print(e)
            driver.quit()
            break
def ipz():
    # 设置代理连接
    while True:
        resp = requests.get('代理连接').text
        if resp.find('data') != -1:
            resp1 = json.loads(resp)['data']
            http = str(resp1[0]["ip"]) + ":" + str(resp1[0]["port"])
            return http
        else:
            time.sleep(5)
while True:
    a = Mysql.qiyexx_url(bh='1')
    for x in a:
        try:
            qyid = x[0]  # 公司eid
            z = x[2]  # 公司名字
            qyid1 = x[3]#qyid
            qw=gx_qyid(z=z,eid=qyid)#这个东西可以优化，在失败或者加载不出东西可以尝试更新，不用每次加载
            selenu(qw,z,ipz())
        except Exception as E:
            print(E)
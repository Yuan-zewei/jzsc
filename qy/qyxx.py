# -*- coding: utf-8 -*-
from utils import util
from dao import Mysql
import time
from uuid import uuid4
#时间戳转换
def time_s(tim):
    ti=tim/1000
    timeArray = time.localtime(ti)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime
#企业基础信息
def qyjichu(resp,qyid):
    print(resp)
    #企业名字
    gsname =resp['QY_NAME']
    # 统一社会信用代码
    xydm =resp['QY_ORG_CODE']
    # 企业法定代表人
    qyfr =resp['QY_FR_NAME']
    # 企业登记注册类型
    qytype =resp['QY_GSZCLX_NAME']
    # 企业注册属地
    qysd =resp['QY_REGION_NAME']
    # 企业经营地址
    qyAdr =resp['QY_ADDR']
    qy = Mysql.selecttbl_qy(qyid=qyid)
    # # 查询复爬表中有无资质人员工程等url
    print(qy)
    if qy == None:
        print(f'-------------------------------{gsname}的基础信息正在插入--------------------------------')
        Mysql.inserttbl_qy(qyid=qyid, xydm=xydm, zjjgid="", qyname=gsname, frdb=qyfr, qyzcsd="",
                           zclx=qytype, zcsd=qysd, jydz=qyAdr)

    else:
        print(f'-------------------------------{gsname}的基础信息正在更新--------------------------------')
        Mysql.updatetbl_qy(qyid=qyid, xydm=xydm, zjjgid="", frdb=qyfr, qyzcsd="",
                           zclx=qytype, zcsd=qysd, jydz=qyAdr, qyname=gsname)

# 企业资质
def qyzz(resp,qyid):
    # print(resp)
    try:
        zzlb = resp['APT_TYPE_NAME']
        zzzsh = resp['APT_CERTNO']
        zzmc = resp['APT_NAME']
        a1 = resp['APT_GET_DATE']
        a2 = resp['APT_EDATE']
        fzrq = time_s(a1)
        zsyxq = time_s(a2)
        fzjg = resp['APT_GRANT_UNIT']
        zc_fw=resp['APT_NAME']
        cx = Mysql.selecttbl_qy_zz(qyid=qyid, zsh=zzzsh, zzmc=zzmc)
        if cx==None:
            Mysql.inserttbl_qy_zz(zzlx=zzlb, zsh=zzzsh, zzmc=zzmc, fzrq=fzrq, zsyxq=zsyxq, fzjg=fzjg, qyid=qyid,
                                  zzfw=zc_fw)
        else:
            Mysql.updatetbl_qy_zz(zzlx=zzlb, zsh=zzzsh, zzmc=zzmc, fzrq=fzrq, zsyxq=zsyxq, fzjg=fzjg, qyid=qyid,zc_fw=zc_fw)
    except Exception as e:
        util.logger.error(e)



# 企业注册人员基础信息提取
def ryxx(resp,qyid,user):
    try:
        name = resp['RY_NAME']
        zjhm = resp['IDCARD']
        zczy = resp['RY_CARDTYPE_NAME']
        sex=resp['RY_SEX_NAME']
        ues=Mysql.selecttbl_qiye_user_qyid(username=name, sex=sex, zjlx=zczy, zjhm=zjhm, qyid=qyid)
        print(ues)
        if ues!=None:
            Mysql.delete_tbl_user_user(userid=ues[0])
            Mysql.deletetbl_user_zcxx1_user(userid=ues[0])
            print('这个人员已存在，删除人员的基础注册信息')
            Mysql.inserttbl_user(username=name, sex=sex, zjlx=zczy, zjhm=zjhm, qyid=qyid, userid=user)
            print(f'{name}{user}基础信息插入完成')
        else:
            Mysql.inserttbl_user(username=name, sex=sex, zjlx=zczy, zjhm=zjhm, qyid=qyid, userid=user)
            print(f'{name}{user}基础信息插入完成')
    except Exception as e:
        util.logger.error(e)
def ryxx_xinxi(resp,user,zc_dwid):
    try:
        name = resp['RY_NAME']
        zclb=resp['REG_TYPE_NAME']
        zsbh=resp['REG_CERTNO']
        if zsbh==None:
            zsbh=''
        zyyzh=resp['REG_SEAL_CODE']
        a21 = resp['REG_EDATE']
        yxq = time_s(a21)
        zc_dw=resp['QY_NAME']
        zc_zy=resp['REG_PROF_NAME']
        drjs=''
        Mysql.inserttbl_user_zcxx_log1(userid=user, zclb=zclb, zsbh=zsbh, zyyzh=zyyzh, yxq=yxq,
                                       zc_dwid=zc_dwid,
                                       zc_dw=zc_dw, zc_zy=zc_zy, drjs=drjs)
        print(f'{name}{user}注册信息插入完成')
    except Exception as e:
        print('注册信息报错',e)
#————————————————————————————————————————————————————————————————————————————————————————————————————————
def gcxm(resp,qyid,i):
    print('--该工程项目的部分信息--')
    try:
        xmid = resp['PRJNUM']             #项目编号
        if xmid==None:
            xmid=''
        sjxmbh=resp['PROVINCEPRJNUM']     #省级项目编号
        if sjxmbh==None:
            sjxmbh=''

        xmmc=resp['PRJNAME']              #项目名称
        if xmmc==None:
            xmmc=''

        if resp['PROVINCE']==None:
            resp['PROVINCE']=''
        else:
            if resp['CITY']==None:
                resp['CITY']=''
                gsd=resp['PROVINCE']
            else:
                if resp['COUNTY']==None:
                    gsd=resp['PROVINCE']+'-'+resp['CITY']
                else:
                    gsd =resp['PROVINCE']+'-' + resp['COUNTY']+'-'+resp['CITY']


        xmlb=resp['PRJTYPENUM']           #项目类别
        if xmlb==None:
            xmlb=''
        jsdw_bh=''                        #建设单位编号
        if jsdw_bh==None:
            jsdw_bh=''
        jsdw = resp['BUILDCORPNAME']      #建设单位
        if jsdw==None:
            jsdw=''
        jsdw_xydm=resp['BUILDCORPCODE']   # 建设单位信用代码
        if jsdw_xydm==None:
            jsdw_xydm=''

        szqh=gsd             # 所在区划
        jsxz=resp['PRJPROPERTYNUM']       #建设性质
        if jsxz==None:
            jsxz=''
        gzyt=resp['PRJFUNCTIONNUM']       #工程用途
        if gzyt==None:
            gzyt=''

        ztz = resp['ALLINVEST']
        if ztz == None:
            ztz = ''
        else:
            ztz = str(ztz) +'（万元）'   #总投资
        zmj = resp['ALLAREA']
        if zmj==None:
            zmj=''
        else:
            zmj=str(zmj) +'（平方米）'  #总面积

        lxjb=resp['PRJAPPROVALLEVELNUM']  # 立项级别
        if lxjb==None:
            lxjb=''
        lxwh=resp['PRJAPPROVALNUM']       # 立项文号
        if lxwh==None:
            lxwh=''

        if Mysql.selecttbl_qy_xm(qyid=qyid, xmid=xmid):
            Mysql.updatetbl_qy_xm(qyid=qyid, xmid=xmid, sjxmbh=sjxmbh, xmmc=xmmc, gsd=gsd,
                                       xmlb=xmlb,
                                       jsdw_bh=jsdw_bh,
                                       jsdw=jsdw, jsdw_xydm=jsdw_xydm, szqh=szqh, jsxz=jsxz, gzyt=gzyt, ztz=ztz,
                                       zmj=zmj,
                                       lxjb=lxjb, lxwh=lxwh)

        else:
            Mysql.inserttbl_qy_xm(qyid=qyid, xmid=xmid, sjxmbh=sjxmbh, xmmc=xmmc, gsd=gsd,
                                       xmlb=xmlb,
                                       jsdw_bh=jsdw_bh,
                                       jsdw=jsdw, jsdw_xydm=jsdw_xydm, szqh=szqh, jsxz=jsxz, gzyt=gzyt, ztz=ztz,
                                       zmj=zmj,
                                       lxjb=lxjb, lxwh=lxwh)
        print(f'         第{i}个项目{xmmc}的部分信息插入完成')
        # else:
        #     Mysql.updatetbl_user_zcxx(userid=user, zclb=zclb, zsbh=zsbh, zyyzh=zyyzh, yxq=yxq,
        #                               zc_dwid=zc_dwid, zc_dw=zc_dw, zc_zy=zc_zy, drjs=drjs)
            # print(f'{name}{user}注册信息更新完成')
    except Exception as e:
        print(e)
def gcxm_jcxx(resp,qyid):
    print('--该工程项目的基础信息--')
    try:
        xmid = resp['PRJNUM']

        addr=resp['ADDRESS']             #具体地点
        print(addr)
        if addr==None:
            address=''
        else:
            address = resp['ADDRESS']

        zjb=resp['NATIONALPERCENTTAGE']    #国有资金出资比例
        if zjb==None:
            zjbl=''
        else:
            zjbl = resp['NATIONALPERCENTTAGE']

        zj=resp['FUNDSOURCE']             # 资金来源
        if zj==None:
            zjly=''
        else:
            zjly = resp['FUNDSOURCE']

        jsyd=resp['BUILDPLANNUM']           #建设用地规划许可证编号
        if jsyd==None:
            jsydxkzbh=''
        else:
            jsydxkzbh = resp['BUILDPLANNUM']

        jscg = resp['PROJECTPLANNUM']      #建设工程规划许可证编号
        if jscg==None:
            jscgghxkzbh=''
        else:
            jscgghxkzbh = resp['PROJECTPLANNUM']

        jhk=resp['BEGINDATE']        # 计划开工
        if jhk==None:
            jhkg=''
        else:
            jhkg = time_s(resp['BEGINDATE'])
        jh=resp['ENDDATE']            # 计划竣工
        if jh==None:
            jhjg=''
        else:
            jhjg = time_s(resp['ENDDATE'])
        j=resp['PRJSIZE']                #建设规模
        if j==None:
            jsgm=''
        else:
            jsgm=resp['PRJSIZE']

        if resp['DATASOURCE']==None:
            sjly=''
        else:
            sjly = resp['DATASOURCE']  # 数据来源

        if resp['DATALEVEL']==None:
            sjdj=''
        else:
            sjdj = resp['DATALEVEL']  # 数据等级

                                  #重点项目
        if resp['IS_FAKE'] == None:
            zdxm = ''
        elif resp['IS_FAKE']==0:
            zdxm='否'
        else:
            zdxm='是'

        if resp['PRJAPPROVALDATE']==None:
            lxpfsj=''
        else:
            lxpfsj = resp['PRJAPPROVALDATE']  # 立项批复时间

        if resp['PRJAPPROVALDEPART']==None:   # 立项批复机关
            lxpfjg=''
        else:
            lxpfjg = resp['PRJAPPROVALDEPART']


        print('\t具体地点:',address,'\t国有资金出资比例:',zjbl,'\t资金来源:',zjly,'\t建设用地规划许可证编号:',jsydxkzbh,'\t建设工程规划许可证编号:',jscgghxkzbh,'\t计划开工:',jhkg,'\t计划开工:',jhjg,'\t计划竣工:',jsgm,'\t建设规模:',sjly,'\t数据来源:',sjly,'\t数据等级:',sjdj,'\t重点项目:',zdxm,'\t立项批复时间:',lxpfsj,'\t立项批复机关:',lxpfjg)
        if Mysql.selecttbl_qy_xm_jcxx(qyid=qyid, xmid=xmid):
            Mysql.updatetbl_qy_xm_jcxx(qyid=qyid, xmid=xmid, address=address, zjbl=zjbl, zjly=zjly,jsydxkzbh=jsydxkzbh,jscgghxkzbh=jscgghxkzbh,jhkg=jhkg, jhjg=jhjg, jsgm=jsgm, sjly=sjly, sjdj=sjdj, zdxm=zdxm,lxpfsj=lxpfsj,lxpfjg=lxpfjg)

        else:
            Mysql.inserttbl_qy_xm_jcxx(qyid=qyid, xmid=xmid, address=address, zjbl=zjbl, zjly=zjly,jsydxkzbh=jsydxkzbh,jscgghxkzbh=jscgghxkzbh,jhkg=jhkg, jhjg=jhjg, jsgm=jsgm, sjly=sjly, sjdj=sjdj, zdxm=zdxm,lxpfsj=lxpfsj,lxpfjg=lxpfjg)
        print(f'         该项目基础信息插入完成')
    except Exception as e:
        print(e)


def gcxm_weizhi(resp,qyid):
    ID=resp['ID']
    url='http://jzsc.mohurd.gov.cn/data/project/detail?id='+ID
    print(f'--工程项目基础信息中未知的字段--\n其相关链接:{url}')
    try:
        xmid = resp['PRJNUM']
        yy = resp['PRJCODE']
        if yy==None:
            y=''
        else:
            y=resp['PRJCODE']
        aa = resp['LOCATIONX']
        if aa==None:
            a=''
        else:
            a=resp['LOCATIONX']
        bb=resp['LOCATIONY']
        if bb==None:
            b=''
        else:
            b = resp['LOCATIONY']
        cc=resp['ALLLENGTH']
        if cc==None:
            c=''
        else:
            c=resp['ALLLENGTH']
        dd=resp['ISMAJOR']
        if dd==None:
            d=''
        else:
            d=resp['ISMAJOR']
        ee=resp['JZJNINFO']
        if ee==None:
            e=''
        else:
            e=resp['JZJNINFO']
        ff = resp['INVPROPERTYNUM']
        if ff==None:
            f=''
        else:
            f=resp['INVPROPERTYNUM']
        gg=resp['INVPROPERTY']
        if gg==None:
            g=''
        else:
            g=time_s(resp['INVPROPERTY'])
        hh=resp['WANDAOLEE_ROWGUID']
        if hh==None:
            h=''
        else:
            h=time_s(resp['WANDAOLEE_ROWGUID'])
        ii=resp['SORTNUM']
        if ii == None:
            i = ''
        else:
            i=resp['SORTNUM']
        jj=resp['PREFIX']
        if jj==None:
            j=''
        else:
            j=resp['PREFIX']
        kk=resp['JSBJGSIGN']
        if kk==None:
            k=''
        else:
            k=resp['JSBJGSIGN']
        ll=resp['PKID']
        if ll==None:
            l=''
        else:
            l=resp['PKID']
        mm=resp['CXXMINFO']
        if mm==None:
            m=''
        else:
            m=resp['CXXMINFO']
        nn=resp['CHECKDEPARTNAME']
        if nn==None:
            n=''
        else:
            n=resp['CHECKDEPARTNAME']
        oo=resp['PRJTWODIMCODE']
        if oo==None:
            o=''
        else:
            o=resp['PRJTWODIMCODE']
        pp=resp['PRJAPPROVALDEPART']
        if pp==None:
            p=''
        else:
            p=resp['PRJAPPROVALDEPART']
        qq=resp['CHECKDEPARTNAME']
        if qq==None:
            q=''
        else:
            q=resp['CHECKDEPARTNAME']
        ss=resp['PRJAPPROVALDATE']
        if ss==None:
            s=''
        else:
            s=resp['PRJAPPROVALDATE']
        tt=resp['MARK']
        if tt==None:
            t=''
        else:
            t=resp['MARK']
        uu=resp['FAKE_CORP_NAME']
        if uu==None:
            u=''
        else:
            u=resp['FAKE_CORP_NAME']
        vv=resp['FAKE_CORP_ID']
        if vv==None:
            v=''
        else:
            v=resp['FAKE_CORP_ID']

        print(f'LOCATIONX:{a},LOCATIONY:{b},ALLLENGTH:{c},ISMAJOR:{d},JZJNINFO:{e},INVPROPERTYNUM:{f},INVPROPERTY:{g},WANDAOLEE_ROWGUID:{h},SORTNUM:{i},PREFIX:{j},JSBJGSIGN:{k},PKID:{l},CXXMINFO:{m},CHECKDEPARTNAME:{n},PRJTWODIMCODE:{o},PRJAPPROVALDEPART:{p},CHECKDEPARTNAME:{q},PRJAPPROVALDATE:{s},MARK:{t},FAKE_CORP_NAME:{u},prjcode:{v}')
        if Mysql.selecttbl_qy_xm_weizhi(qyid=qyid, xmid=xmid):
            Mysql.updatetbl_qy_xm_weizhi(qyid=qyid, xmid=xmid, locationx=a, locationy=b, alllength=c,ismajor=d,jzjninfo=e,invpropertynum=f, invproperty=g, wandaolee_roeguid=h, sortnum=i, prefix=j, jsbjgsign=k,pkid=l,cxxninfo=m,checkdepariname=n,prjtwodimcode=o,prjapprovaldepart=p,checkdepartname=q,prjapprovaldate=s,mark=t,fake_corp_name=u,fake_corp_id=v,prjcode=y)

        else:
            Mysql.inserttbl_qy_xm_weizhi(qyid=qyid, xmid=xmid, locationx=a, locationy=b, alllength=c,ismajor=d,jzjninfo=e,invpropertynum=f, invproperty=g, wandaolee_roeguid=h, sortnum=i, prefix=j, jsbjgsign=k,pkid=l,cxxninfo=m,checkdepariname=n,prjtwodimcode=o,prjapprovaldepart=p,checkdepartname=q,prjapprovaldate=s,mark=t,fake_corp_name=u,fake_corp_id=v,prjcode=y)
        print(f'         该项目未知信息插入完成')

    except Exception as e:
        print(e)
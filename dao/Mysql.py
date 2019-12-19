# -*- coding: utf-8 -*-
from utils import util, dbmysql
import time
def qiyexx_list(**kwargs):
    rs = None
    try:
        # sql="select * from q_psname where zt <> 0 order by id limit 5,10;"
        sql="select * from q_name_list where bh='%s' and qy_zt='1' order by inserttime desc limit 1;"%(kwargs['bh'])
        rs = dbmysql.fetchall(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 更新企业状态爬取的状态下关键字
def gxqy(**kwargs):
    rs = None
    try:
        sql = "UPDATE tbl_query_temp SET cx_state ='%s' WHERE cx_val='%s';" % (kwargs['cx_state'], kwargs['gsname'])
        # cx_state标记
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新企业状态爬取的状态下
def gxqy_fupa_te(**kwargs):
    rs = None
    try:
        sql = "UPDATE q_psname SET zt ='%s' WHERE qyname='%s';" % \
              (kwargs['zt'],kwargs['gsname'])
        # cx_state标记
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 从数据库当中提取数据关键字
def qiyexx(**kwargs):
    rs = None
    try:
        sql="select * from q_psname where zt is null ORDER BY eid DESC LIMIT 1;"
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 从数据库当中提取数据关键字
def qiyexx_eid(**kwargs):
    rs = None
    try:
        sql="select * from q_psname where qyname='%s';"%(kwargs['qyname'])
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#插入企业存在的公司名字
def insert_qy_list(**kwargs):
    rs=None
    try:
        inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql="insert into q_name_list (eid,qyname,bh,qy_zt,inserttime) value ('%s','%s','%s','%s','%s');"%(kwargs['eid'],kwargs['qyname'],kwargs['bh'],kwargs['qy_zt'],inserttime)
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs=dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# # 查询有没有qyid
def selecttbl_qy(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_qy where qyid ='%s';" % kwargs["qyid"]
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
# # 插入企业信息表
def inserttbl_qy(**kwargs):
    rs = None
    try:
        sql = "insert into tbl_qy (qyid,qyname,xydm,frdb,zclx,zcsd,jydz) value ('%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"], kwargs["qyname"], kwargs["xydm"], kwargs["frdb"],
            kwargs["zclx"], kwargs["zcsd"], kwargs["jydz"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新企业基础信息的爬取状态
def update_qyjcxx(**kwargs):
    rs = None
    try:
        # inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql = "update tbl_fupa_temp set qy_jcxx_zt='%s'where eid='%s';" % (
            kwargs["qy_jcxx_zt"],kwargs["eid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
        return rs
# 更新企业的qyid
def update_qyid(**kwargs):
    rs = None
    try:
        # inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql = "update tbl_fupa_temp set qiyeurl='%s'where eid='%s';" % (
            kwargs["qyurl"],kwargs["eid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
        return rs
# 更新企业资质爬取状态
def updatet_qyzzzt(**kwargs):
    rs = None
    try:
        sql = "update tbl_fupa_temp set qyzzzt='%s' where eid='%s';" % (
            kwargs["qyzzzt"], kwargs["eid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新注册人员基础信息爬取状态
def updateryzt(**kwargs):
    rs = None
    try:
        sql = "update tbl_fupa_temp set ryzt ='%s'where eid='%s';" % (kwargs["ryzt"], kwargs["eid"])
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# # 更新企业信息表
def updatetbl_qy(**kwargs):
    rs = None
    try:
        sql = "update tbl_qy set xydm='%s',frdb='%s',zclx='%s',zcsd='%s',jydz='%s' where qyid='%s';" % (
            kwargs["xydm"], kwargs["frdb"], kwargs["zclx"], kwargs["zcsd"], kwargs["jydz"], kwargs["qyid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#查询企业资质是否存在
def selecttbl_qy_zz(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_qy_zz where qyid ='%s' and zsh='%s' and zzmc='%s';" % (
            kwargs["qyid"], kwargs["zsh"], kwargs["zzmc"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
# 插入企业资质表
def inserttbl_qy_zz(**kwargs):
    rs = None
    try:
        sql = "insert into tbl_qy_zz(qyid,zzlx,zsh,zzmc,fzrq,zsyxq,fzjg,zzfw) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"], kwargs["zzlx"], kwargs["zsh"], kwargs["zzmc"], kwargs["fzrq"], kwargs["zsyxq"],
            kwargs["fzjg"], kwargs["zzfw"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)

    except Exception as e:
        util.logger.error(e)
    return rs
# 更新企业资质表
def updatetbl_qy_zz(**kwargs):
    rs = None
    try:
        sql = "update tbl_qy_zz set zzlx='%s',fzrq='%s',zsyxq='%s',fzjg='%s' where qyid='%s' and(zsh='%s' or zzmc='%s');" % (
            kwargs["zzlx"], kwargs["fzrq"], kwargs["zsyxq"], kwargs["fzjg"],kwargs["qyid"] , kwargs["zsh"], kwargs["zzmc"]
            )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        # print('更新资质信息的sql语句',sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 查询公司注册人员中企业id
def selecttbl_qiye_user_qyid(**kwargs):
    rs = None
    try:
        sql = "select userid from tbl_user where qyid='%s' and username='%s' and sex='%s' and zjlx='%s' and zjhm='%s';" % (kwargs["qyid"],kwargs["username"],kwargs["sex"],
                                                                                                                           kwargs["zjlx"],kwargs["zjhm"],)
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 个人详情 名字 性别 证件类型 身份证号
def inserttbl_user(**kwargs):
    rs = None
    try:
        sql = "insert into tbl_user(qyid,userid,username,sex,zjlx,zjhm) VALUES ('%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"],kwargs["userid"], kwargs["username"], kwargs["sex"], kwargs["zjlx"], kwargs["zjhm"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新人员表
def updatetbl_user(**kwargs):
    rs = None
    try:

        sql = "update tbl_user set username='%s',sex='%s',zjlx='%s',zjhm='%s' where qyid='%s' and userid='%s';" % (
            kwargs["username"], kwargs["sex"], kwargs["zjlx"], kwargs["zjhm"],kwargs["qyid"],kwargs["userid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 查询有没有id
def selecttbl_user_zcxx(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_user_zcxx where zc_dwid ='%s' and userid ='%s' and zclb='%s' and zyyzh='%s' and zc_zy='%s';" % (
            kwargs["zc_dwid"],kwargs["userid"], kwargs["zclb"], kwargs["zyyzh"], kwargs["zc_zy"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
        # print(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# # 插入人员注册信息表
def inserttbl_user_zcxx_log1(**kwargs):
    rs = None
    try:
        sql = "insert into tbl_user_zcxx(userid,zclb,zsbh,zyyzh,yxq,zc_dwid,zc_dw,zc_zy,drjs) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["userid"], kwargs["zclb"], kwargs["zsbh"], kwargs["zyyzh"], kwargs["yxq"], kwargs["zc_dwid"],kwargs["zc_dw"], kwargs["zc_zy"], kwargs["drjs"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# # 更新人员注册信息表
def updatetbl_user_zcxx(**kwargs):
    rs = None
    try:
        sql = "update tbl_user_zcxx set zsbh='%s',yxq='%s',zc_dw='%s',drjs='%s' where zc_dwid='%s'and userid='%s' and( zclb='%s' or zyyzh='%s' or zc_zy='%s') ;" % (
            kwargs["zsbh"], kwargs["yxq"], kwargs["zc_dw"], kwargs["drjs"], kwargs["zc_dwid"], kwargs["userid"],
            kwargs["zclb"], kwargs["zyyzh"], kwargs["zc_zy"])
        # sql = "update tbl_user_zcxx_log set zsbh='%s',yxq='%s',zc_dwid='%s',zc_dw='%s',drjs='%s' where zc_dwid='%s'and (userid='%s'or zclb='%s' or zyyzh='%s' or zc_zy='%s') ;" % (kwargs["zsbh"], kwargs["yxq"], kwargs["zc_dwid"], kwargs["zc_dw"], kwargs["drjs"],kwargs["qyid"], kwargs["userid"],kwargs["zclb"],kwargs["zyyzh"],  kwargs["zc_zy"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
        # print(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#删除企业人员的基础信息
def delete_tbl_user(**kwargs):
    rs = None
    try:
        sql = "delete from tbl_user where qyid ='%s';" % (kwargs["qyid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#删除人员的注册信息
def deletetbl_user_zcxx1(**kwargs):
    rs = None
    try:
        sql = "DELETE FROM tbl_user_zcxx WHERE zc_dwid='%s';" % (kwargs["qyid"])
        rs = dbmysql.query(sql)
        print(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#删除企业人员的基础信息
def delete_tbl_user_user(**kwargs):
    rs = None
    try:
        sql = "delete from tbl_user where userid ='%s';" % (kwargs["userid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#删除人员的注册信息
def deletetbl_user_zcxx1_user(**kwargs):
    rs = None
    try:
        sql = "DELETE FROM tbl_user_zcxx WHERE userid='%s';" % (kwargs["userid"])
        rs = dbmysql.query(sql)
        print(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#查询复爬是否存在企业
# # 查询有没有企业id
def selecttbl_qyname(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_fupa_temp where eid ='%s';" % kwargs["eid"]
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
# # 查询有没有企业名字
def selecttbl_qyname_user(**kwargs):
    rs = None
    try:
        sql = "select ry_num_zd from tbl_fupa_temp where eid ='%s';" % kwargs["eid"]
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
#复爬插入企业信息
def insetqyzt(**kwargs):
    rs = None
    try:
        inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql = "INSERT INTO tbl_fupa_temp(eid,type,cx_val,cx_state,qiyeurl,qyzzzt,ryzt,ryzyzc_zt,inserttime,bh,qy_jcxx_zt) value ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["eid"],kwargs["type"], kwargs["cx_val"], kwargs["cx_state"], kwargs["qiyeurl"], kwargs["qyzzzt"], kwargs["ryzt"],kwargs["ryzyzc_zt"],inserttime,kwargs["bh"],kwargs["bh"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#更新企业表的状态
def update_qname_list(**kwargs):
    rs = None
    try:
        # inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql = "update q_name_list set qy_zt='%s'where eid='%s';" % (
            kwargs["qy_zt"],kwargs["eid"])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        # print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
        return rs
# 更新企业状态爬取的状态及插入时间
def gxqy_fupa(**kwargs):
    rs = None
    try:
        inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql = "UPDATE tbl_fupa_temp SET inserttime ='%s',cx_state ='%s' WHERE eid='%s';" % (inserttime,kwargs['cx_state'], kwargs['eid'])
        # cx_state标记
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 从数据库当中提取公司存在的qyid-------------------------------暂定------------------------------------
def qiyexx_url(**kwargs):
    rs = None
    try:
        # sql="SELECT * FROM tbl_query_temp WHERE cx_state='1' LIMIT 1;"
        sql = "select * from tbl_fupa_temp where cx_state='1' and type='0' and bh='%s' order by inserttime desc LIMIT 1;"%(kwargs['bh'])
        # print(sql)
        rs = dbmysql.fetchall(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新人员中断页数
def updatery_page_zd(**kwargs):
    rs = None
    try:
        sql = "update tbl_fupa_temp set ry_num_zd ='%s'where eid='%s';" % (kwargs["ry_page_zd"], kwargs["eid"])
        print(sql)
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 查询人员-从断点继续爬取
def selectryurl_ys1(**kwargs):
    rs = None
    try:
        sql = "select ry_num_zd from tbl_fupa_temp where eid='%s';" % kwargs['eid']
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
    # # 插入项目表详细信息  首页>项目数据>项目信息

#插入企业项目
def inserttbl_qy_xm(**kwargs):
    rs = None
    try:
        sql = "insert into tbl_qy_xm(qyid,xmid,sjxmbh,xmmc,gsd,xmlb,jsdw_bh,jsdw,jsdw_xydm,szqh,jsxz,gzyt,ztz,zmj,lxjb,lxwh) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"], kwargs["xmid"], kwargs["sjxmbh"], kwargs["xmmc"], kwargs["gsd"], kwargs["xmlb"],
            kwargs["jsdw_bh"], kwargs["jsdw"], kwargs["jsdw_xydm"], kwargs["szqh"], kwargs["jsxz"], kwargs["gzyt"],
            kwargs["ztz"], kwargs["zmj"], kwargs["lxjb"], kwargs["lxwh"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
    # # 查询项目表详细信息  首页>项目数据>项目信息

#查询企业项目
def selecttbl_qy_xm(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_qy_xm where xmid='%s' and qyid = '%s';" % (kwargs["xmid"], kwargs['qyid'])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#更新企业项目
def updatetbl_qy_xm(**kwargs):
    rs = None
    try:
        sql = "update tbl_qy_xm set sjxmbh='%s',xmmc='%s',gsd='%s',xmlb='%s',jsdw_bh='%s',jsdw='%s',jsdw_xydm='%s',szqh='%s',jsxz='%s',gzyt='%s',ztz='%s',zmj='%s',lxjb='%s',lxwh='%s' where xmid='%s' and qyid='%s';" % (
            kwargs["sjxmbh"], kwargs["xmmc"], kwargs["gsd"], kwargs["xmlb"],
            kwargs["jsdw_bh"], kwargs["jsdw"], kwargs["jsdw_xydm"], kwargs["szqh"], kwargs["jsxz"], kwargs["gzyt"],
            kwargs["ztz"], kwargs["zmj"], kwargs["lxjb"], kwargs["lxwh"], kwargs["xmid"], kwargs["qyid"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 更新基础项目表信息
def inserttbl_qy_xm_jcxx(**kwargs):
    rs = None
    try:

        sql = "insert into tbl_qy_xm_jcxx(qyid,xmid,address,zjbl,zjly,jsydxkzbh,jscgghxkzbh,jhkg,jhjg,jsgm,sjly,sjdj,zdxm,lxpfsj,lxpfjg) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"], kwargs["xmid"], kwargs["address"], kwargs["zjbl"], kwargs["zjly"], kwargs["jsydxkzbh"],
            kwargs["jscgghxkzbh"], kwargs["jhkg"], kwargs["jhjg"], kwargs["jsgm"], kwargs["sjly"], kwargs["sjdj"],
            kwargs["zdxm"], kwargs["lxpfsj"], kwargs["lxpfjg"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 查询基础项目表信息
def selecttbl_qy_xm_jcxx(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_qy_xm_jcxx where xmid='%s' and qyid = '%s';" % (kwargs["xmid"], kwargs['qyid'])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 更新基础项目表信息
def updatetbl_qy_xm_jcxx(**kwargs):
    rs = None
    try:
        sql = "update tbl_qy_xm_jcxx set address='%s',zjbl='%s',zjly='%s',jsydxkzbh='%s',jscgghxkzbh='%s',jhkg='%s',jhjg='%s',jsgm='%s',sjly='%s',sjdj='%s',zdxm='%s',lxpfsj='%s',lxpfjg='%s' where xmid='%s' and qyid='%s';" % (
            kwargs["address"], kwargs["zjbl"], kwargs["zjly"], kwargs["jsydxkzbh"],
            kwargs["jscgghxkzbh"], kwargs["jhkg"], kwargs["jhjg"], kwargs["jsgm"],  kwargs["sjly"],
            kwargs["sjdj"], kwargs["zdxm"], kwargs["lxpfsj"], kwargs["lxpfjg"], kwargs["xmid"], kwargs["qyid"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新工程项目未知信息表的信息
def inserttbl_qy_xm_weizhi(**kwargs):
    rs = None
    try:
        'qyid=qyid, xmid=xmid, locationx=a, locationy=b, alllength=c,ismajor=d,jzjninfo=e,invpropertynum=f, invproperty=g, wandaolee_roeguid=h, sortnum=i, prefix=j, jsbjgsign=k,pkid=l,cxxninfo=m,checkdepariname=n,prjtwodimcode=o,prjapprovaldepart=p,checkdepartname=q,prjapprovaldate=s,mark=t,fake_corp_name=u,fake_corp_id=v,lxpfjg=y'
        sql = "insert into tbl_qy_xm_weizhi(qyid,xmid,locationx,locationy,alllength,ismajor,jzjninfo,invpropertynum,invproperty,wandaolee_roeguid,sortnum,prefix,jsbjgsign,pkid,cxxninfo,checkdepariname,prjtwodimcode,prjapprovaldepart,checkdepartname,prjapprovaldate,mark,fake_corp_name,fake_corp_id,prjcode) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
            kwargs["qyid"], kwargs["xmid"], kwargs["locationx"], kwargs["locationy"], kwargs["alllength"], kwargs["ismajor"],
            kwargs["jzjninfo"], kwargs["invpropertynum"], kwargs["invproperty"], kwargs["wandaolee_roeguid"], kwargs["sortnum"], kwargs["prefix"],
            kwargs["jsbjgsign"], kwargs["pkid"], kwargs["cxxninfo"], kwargs["checkdepariname"], kwargs["prjtwodimcode"], kwargs["prjapprovaldepart"], kwargs["checkdepartname"], kwargs["prjapprovaldate"], kwargs["mark"], kwargs["fake_corp_name"], kwargs["fake_corp_id"], kwargs["prjcode"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 查询工程项目未知信息表的信息
def selecttbl_qy_xm_weizhi(**kwargs):
    rs = None
    try:
        sql = "select * from tbl_qy_xm_weizhi where xmid='%s' and qyid = '%s';" % (kwargs["xmid"], kwargs['qyid'])
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.first(sql)
    except Exception as e:
        util.logger.error(e)
    return rs

# 更新工程项目未知信息表的信息
def updatetbl_qy_xm_weizhi(**kwargs):
    rs = None
    try:
        sql = "update tbl_qy_xm_weizhi set locationx='%s',locationy='%s',alllength='%s',ismajor='%s',jzjninfo='%s',invpropertynum='%s',invproperty='%s',wandaolee_roeguid='%s',sortnum='%s',prefix='%s',jsbjgsign='%s',pkid='%s',cxxninfo='%s',checkdepariname='%s',prjtwodimcode='%s',prjapprovaldepart='%s',checkdepartname='%s',prjapprovaldate='%s',mark='%s',fake_corp_name='%s',fake_corp_id='%s',prjcode='%s' where xmid='%s' and qyid='%s';" % (
            kwargs["locationx"], kwargs["locationy"], kwargs["alllength"], kwargs["ismajor"],
            kwargs["jzjninfo"], kwargs["invpropertynum"], kwargs["invproperty"], kwargs["wandaolee_roeguid"],
            kwargs["sortnum"], kwargs["prefix"],
            kwargs["jsbjgsign"], kwargs["pkid"], kwargs["cxxninfo"], kwargs["checkdepariname"], kwargs["prjtwodimcode"],
            kwargs["prjapprovaldepart"], kwargs["checkdepartname"], kwargs["prjapprovaldate"], kwargs["mark"],
            kwargs["fake_corp_name"], kwargs["fake_corp_id"], kwargs["prjcode"], kwargs["xmid"], kwargs["qyid"]
        )
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#--------------------------------------------------token和ip测试专用---------------------------------------------
#查询企业的token值
def jichutoken(**kwargs):
    rs=None
    try:
        sql = "select * from token_ceshi where yxq ='%s';" % kwargs["yxq"]
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
#查询企业的token值
def seletoken(**kwargs):
    rs=None
    try:
        sql = "select token from token_ceshi where token ='%s';" % kwargs["token"]
        rs = dbmysql.first(sql)
        return rs
    except Exception as e:
        util.logger.error(e)
        return rs
#插入token值和ip
def insert_token(**kwargs):
    rs=None
    try:
        inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sql="insert into token_ceshi (token,yxq,inserttime,ip) value ('%s','%s','%s','%s');"%(kwargs['token'],'0',inserttime,kwargs['ip'])
        print(sql)
        sql = sql.replace('\\', '-').replace('\n', '').replace('\r', '').replace('\t', '')
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新token值的状态
def token(**kwargs):
    rs = None
    try:
        sql="update token_ceshi set yxq='1' where token='%s';"%(kwargs['token'])
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
# 更新token值的状态
def dele_token(**kwargs):
    rs = None
    try:
        sql="DELETE from token_ceshi  where token='%s';"%(kwargs['token'])
        rs = dbmysql.query(sql)
    except Exception as e:
        util.logger.error(e)
    return rs
#======================================================================================================
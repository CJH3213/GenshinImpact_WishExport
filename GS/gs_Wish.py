import copy
import json
import time
import requests
from urllib.parse import urlparse
from enum import Enum


# 祈愿类型：新手、常驻、角色Up、武器Up
class GachaType(Enum):
    Novice = 100
    Permanent = 200
    CharacterEvent = 301
    Weapon = 302
    CharacterEvent2 = 400


class GS_Wish:
    m_baseUrl = 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?'

    m_queryDict = {
        'win_mode': 'fullscreen',
        'authkey_ver': 1,
        'sign_type': 2,
        'auth_appid': 'webview_gacha',
        'init_type': 301,
        'gacha_id': '',     # 这个值会从url解析出来
        'timestamp': '1692144064',      # 时间戳也可以使用实时的
        'lang': 'zh-cn',
        'device_type': 'pc',
        'game_version': 'CNRELWin4.0.1_R17742988_S17600751_D17940433',
        'region': 'cn_gf01',
        'authkey': 'abcdKey',   # 这个值才是重点，每个人每隔几天就会变换
        'game_biz': 'hk4e_cn',
        'gacha_type': 301,
        'page': 1,
        'size': 5,
        'end_id': 0
    }

    def __init__(self, orgUrl):
        # 从抓取的url中分离参数，并转为字典储存
        self.getQueryDictByUrl(orgUrl)

    # 将两字典共有key的值更新到成员m_queryDict字典
    def updateQueryDict(self, otherDict):
        for (k, v) in otherDict.items():
            if k in self.m_queryDict:
                self.m_queryDict[k] = v

    # 从url获取参数部分，转为字典存储
    def getQueryDictByUrl(self, orgUrl):
        # 解析url，分离出参数部分
        parsedUrl = urlparse(orgUrl)
        print(parsedUrl)
        queryUrl = parsedUrl.query
        # 分割参数存为字典
        queryDict = dict((q.split('=')[0], q.split('=')[1]) for q in queryUrl.split('&'))
        # 将两字典共有key的值更新到成员m_queryDict字典
        for (k, v) in queryDict.items():
            if k in self.m_queryDict:
                self.m_queryDict[k] = v
        # return query_dict

    # 根据参数成新的url，不影响原始参数
    def getNewUrl(self, **kwargs):
        # 修改关键参数
        new_queryDict = copy.deepcopy(self.m_queryDict)
        for (k, v) in kwargs.items():
            if k in new_queryDict:
                new_queryDict[k] = v
        # 字典还原成参数字符串
        new_query = '&'.join(['{}={}'.format(key, value) for (key, value) in new_queryDict.items()])
        # 构造新的URL
        new_url = '{}{}'.format(self.m_baseUrl, new_query)
        return new_url

    # 输入url，获取指定池子记录
    def getGaCha(self, gacha_type):
        total_gacha = []
        last_page = 1
        last_id = '0'  # 第一页时end_id先设为0，第二页时end_id为第一页最后一个记录的id
        while True:
            # 生成对应页码的url
            new_url = self.getNewUrl(gacha_type=gacha_type.value, page=last_page, end_id=last_id)
            # 向官方发送请求，保存收到的祈愿记录
            req = requests.get(new_url)
            jsObj = json.loads(req.text)
            gacha_list = jsObj['data']['list']
            total_gacha += gacha_list
            # 输出结果
            print(new_url)
            print(req.text)
            for item in gacha_list:
                print(item)
            # 若没有结果了，退出查询
            if len(gacha_list) == 0:
                break
            # 准备下一页的url参数
            last_page += 1
            last_id = gacha_list[len(gacha_list) - 1]['id']
            # 每页之间冷却2s，防止被禁
            time.sleep(1)

        return total_gacha

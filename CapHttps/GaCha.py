import csv

from gs_Wish import GS_Wish
from gs_Wish import GachaType


# 输出祈愿记录列表到控制台
def outPutOnCMD(pool_name, gacha_list):
    print(f"\r\n {pool_name}")
    for item in gacha_list:
        gacha_type_str = GachaType(int(item['gacha_type'])).name
        print("类型：{}, 名称：{}, 星级：{}, 祈愿类型：{}, 祈愿时间：{}".
              format(item['item_type'], item['name'], item['rank_type'], gacha_type_str, item['time']))


# 输出祈愿记录列表到文件
def outPutOnFile(file_path, gacha_list):
    with open(file_path, 'w', newline='', encoding="utf_8_sig") as f:
        writer = csv.writer(f)
        writer.writerow(['类型', '名称', '星级', '祈愿类型', '祈愿时间'])
        for item in gacha_list:
            row_list = [
                item['item_type'],
                item['name'],
                item['rank_type'],
                GachaType(int(item['gacha_type'])).name,
                item['time']
            ]
            writer.writerow(row_list)


# 抓包获取到打开祈愿历史时的请求网址
# 其中的重点是gacha_id和authkey等值
# PC端output_log文件能找齐这些重要参数也可以不用完整的url
m_cap_url = ''  # 抓取到的url粘贴到此处

gs_wish = GS_Wish(m_cap_url)

m_gacha_list1 = gs_wish.getGaCha(GachaType.Weapon)
pool_name1 = '武器池'
outPutOnFile(pool_name1 + '.csv', m_gacha_list1)
outPutOnCMD(pool_name1, m_gacha_list1)

m_gacha_list2 = gs_wish.getGaCha(GachaType.CharacterEvent)
pool_name2 = '角色池'
outPutOnFile(pool_name2+'.csv', m_gacha_list2)
outPutOnCMD(pool_name2, m_gacha_list2)

m_gacha_list3 = gs_wish.getGaCha(GachaType.Permanent)
pool_name3 = '常驻池'
outPutOnFile(pool_name3+'.csv', m_gacha_list3)
outPutOnCMD(pool_name3, m_gacha_list3)

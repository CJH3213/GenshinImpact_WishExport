import csv
import os
import time

from gs_Wish import GS_Wish, GachaType
from switchMitmdump import SwitchMitmdump


class Task:
    m_task_manager = []

    def __init__(self, tasks):
        self.m_task_manager = tasks

    def on_running(self):
        print('baseTask')

    def back_task(self):
        self.m_task_manager.pop(len(self.m_task_manager)-1)

    def add_task(self, new_task):
        self.m_task_manager.append(new_task)


class Main_Task(Task):
    def on_running(self):

        print('''请输入标号以执行任务：
        1. 安装CA证书
        2. 启动抓包
        3. 导出数据''')

        input_str = input('')

        if input_str is None or input_str == '':
            return

        if input_str == '1':
            print('开始安装CA证书，需要您的操作')
            self.add_task(Install_CA_Task(self.m_task_manager))
        elif input_str == '2':
            print('启动抓包工具，请检查是否启动成功')
            self.add_task(Start_Capture_Task(self.m_task_manager))
        elif input_str == '3':
            print('正在导出数据，请耐心等候')
            self.add_task(Export_Data_Task(self.m_task_manager))
        else:
            print('未定义操作，请重新选择')


class Install_CA_Task(Task):
    def on_running(self):
        ca_file = 'C:/Users/CJH01200203/.mitmproxy/mitmproxy-ca.p12'
        is_exist = os.path.exists(ca_file)

        if not is_exist:
            print('mitmproxy未在用户文件夹下生成CA证书')
            print('可尝试运行mitmproxy.exe以生成证书后，再次安装证书')
            self.back_task()
            return

        print('''证书已存在，请根据以下提示选择安装选项：
        本地计算机
        默认路径
        不要设密码
        将所有的证书都放入下列存储 - 浏览 - 受信任的根证书颁发机构
        下一页 - 完成 - 导入成功''')
        os.system(ca_file)
        self.back_task()
        return


class Start_Capture_Task(Task):
    def on_running(self):
        sw_mitm = SwitchMitmdump(8888, 'Addons/addons.py')
        sw_mitm.start_listen()

        time.sleep(5.0)

        print('代理端口：8888，已经打开mitmdump')
        print('抓取到祈愿url后会停止抓包，url保存在当前目录txt文件')
        print('请打开祈愿界面，点击历史记录，以获得最新url')

        input('是否已经获取到最新url？ 任意输入停止抓包')
        sw_mitm.close_listen()

        self.back_task()


class Export_Data_Task(Task):
    def on_running(self):
        ca_file = '~url_cap.txt'
        is_exist = os.path.exists(ca_file)
        if is_exist is False:
            print('没有找到存放url的文件，请重新抓包')
            self.back_task()
            return

        cap_url = ''  # 抓取到的url粘贴到此处
        with open(ca_file, 'r') as url_txt:
            cap_url = url_txt.read()

        gs_wish = GS_Wish(cap_url)
        if gs_wish.isEffective():
            print('url无效，请重新抓包')
            self.back_task()
            return

        export_dir = './ExportResults'
        os.mkdir(export_dir)

        m_gacha_list1 = gs_wish.getGaCha(GachaType.Weapon)
        pool_name1 = '/武器池'
        outPutOnFile(export_dir + pool_name1 + '.csv', m_gacha_list1)

        m_gacha_list2 = gs_wish.getGaCha(GachaType.CharacterEvent)
        pool_name2 = '/角色池'
        outPutOnFile(export_dir + pool_name2 + '.csv', m_gacha_list2)

        m_gacha_list3 = gs_wish.getGaCha(GachaType.Permanent)
        pool_name3 = '/常驻池'
        outPutOnFile(export_dir + pool_name3 + '.csv', m_gacha_list3)

        print(f'导出完成，请查看 {export_dir} 文件夹下的csv文件')
        self.back_task()
        return


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

if __name__ == '__main__':
    task_manager = []

    main_task = Main_Task(task_manager)
    task_manager.append(main_task)

    while True:
        last_task = task_manager[-1]
        last_task.on_running()
        print('---                                        ---')


    # sw_mitm = SwitchMitmdump(8888, 'Addons/addons.py')

    # try:
    #     # sw_mitm.start_listen()
    #     print('''执行：
    #         1. 安装CA证书
    #         2. 启动抓包
    #         3. 导出数据
    #     ''')
    #     input('')
    #     print('已启动代理，端口8888，请检查是否可以抓取网络……')
    #
    #     # 抓取到的url储存到当前路径下txt文本里
    #     # time.sleep(5.0)
    #
    # finally:  # 无论如何最终都要关闭代理，否则会影响到网络正常使用
    #     pass
    #     # sw_mitm.close_listen()

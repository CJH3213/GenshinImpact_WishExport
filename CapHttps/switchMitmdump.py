import os
import time
from subprocess import Popen


class SwitchMitmdump:
    # m_mitmdump_pid = 0
    m_port = 8888
    m_script_dir = ''
    m_mitmdump_popen: Popen = None

    def __init__(self, port: int, script_dir: str):
        self.m_port = port
        self.m_script_dir = script_dir

    # 启动抓包工具
    def start_listen(self):
        # 先设置win网络代理服务器端口
        Popen(f'winproxy set --all 127.0.0.1:{self.m_port}').communicate()  # communicate()是等待winproxy执行完毕，命令行空闲
        time.sleep(0.2)
        # 开启win网络代理
        Popen('winproxy on').communicate()
        time.sleep(0.2)
        # 运行抓包工具
        self.m_mitmdump_popen = Popen(f'mitmdump -p {self.m_port} -s {self.m_script_dir}')
        print('mitmdump进程PID：', self.m_mitmdump_popen.pid)

    # 关闭抓包工具
    def close_listen(self):
        # 关闭win网络代理
        Popen('winproxy off').communicate()

        if self.m_mitmdump_popen is None:
            # 获取正在监听8080端口的进程PID，此处获取到的PID是启动mitmdump的py管道进程
            # 终止该py管道进程，也会终止由它启用的子进程mitmdump
            with os.popen(f'netstat -ano | findstr {self.m_port} | findstr LISTENING') as result:
                result_str = result.read()
                print('正在监听端口的进程PID：', result_str)
                mitmdump_pid = result_str.split('      ')[-1]
                if mitmdump_pid:
                    Popen(f'taskkill /f -t /pid {mitmdump_pid}')    # /f强制终止 /t终止该pid进程和它启动的子进程
        else:
            self.m_mitmdump_popen.kill()


if __name__ == '__main__':
    sw = SwitchMitmdump(8888, 'Addons/addons.py')
    sw.start_listen()
    time.sleep(5.0)
    sw.close_listen()
    time.sleep(5.0)

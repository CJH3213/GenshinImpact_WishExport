import sys
import winreg
import ctypes

# 如果从来没有开过代理 有可能key不存在 会报错
# INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
#                                    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
#                                    0, winreg.KEY_ALL_ACCESS)

INTERNET_SETTINGS_SUB_KEY = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

# 设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW


# 修改键值
def set_key(reg_key, name, reg_type, value):
    # _, reg_type = winreg.QueryValueEx(reg_key, name)  # 如果reg_key下没有name这个值，会抛出异常
    winreg.SetValueEx(reg_key, name, 0, reg_type, value)


# 启用代理
def enable_proxy(port: int):
    with (winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, INTERNET_SETTINGS_SUB_KEY, 0, winreg.KEY_ALL_ACCESS)
          as internet_settings):
        set_key(internet_settings, 'ProxyEnable', winreg.REG_DWORD, 1)  # 启用
        set_key(internet_settings, 'ProxyOverride1', winreg.REG_SZ, u'*.local;<local>')  # 绕过本地
        server_value = u'http=127.0.0.1:{};https=127.0.0.1:{}'.format(port, port)
        set_key(internet_settings, 'ProxyServer', winreg.REG_SZ, server_value)  # 代理IP及端口
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)


# 停用代理
def disable_proxy():
    with (winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, INTERNET_SETTINGS_SUB_KEY, 0, winreg.KEY_ALL_ACCESS)
          as internet_settings):
        set_key(internet_settings, 'ProxyEnable', winreg.REG_DWORD, 0)  # 停用
    internet_settings.Close()
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1]:
            enable_proxy(8888)
        else:
            disable_proxy()

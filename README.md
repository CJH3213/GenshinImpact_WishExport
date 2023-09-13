# GenshinImpact_WishExport
原神祈愿记录导出，python练手，需要抓包祈愿查询url

打开抓包工具（比如Charles），然后打开原神祈愿历史页面，
回到抓包工具，复制“https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog……”
一大串网址到GaCha.py的m_cap_url变量
然后关闭抓包工具（抓包工具会影响到py的网络请求），运行GaCha.py，结果会保存同级路径下的三个cvs文件

# GenshinImpact_WishExport
原神祈愿记录导出，python练手，需要抓包祈愿查询url   
    
打开抓包工具（比如Charles），然后打开原神祈愿历史页面，   
回到抓包工具，复制“https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog……”   
一大串网址到GaCha.py的m_cap_url变量，   
然后关闭抓包工具（抓包工具会影响到py的网络请求），运行GaCha.py，结果会保存在同级路径下的三个cvs文件。   
    
23-9-20：
现在已经将mitmproxy抓包工具集成到项目内；
可以通过命令行的简单菜单直接选择要执行的操作啦。   
    
![image](https://github.com/CJH3213/Images-blog/blob/main/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E5%9B%BE%E7%89%87/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E7%A4%BA%E4%BE%8B%E5%9B%BE1.png?raw=true)
    
![image](https://github.com/CJH3213/Images-blog/blob/main/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E5%9B%BE%E7%89%87/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E7%A4%BA%E4%BE%8B%E5%9B%BE2.png?raw=true)
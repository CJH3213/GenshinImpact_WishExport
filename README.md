# GenshinImpact_WishExport
原神祈愿记录导出，python练手小项目     
依赖库：mitmproxy、winproxy     

23-0-14：     
打开抓包工具（比如Charles），然后打开原神祈愿历史页面，   
回到抓包工具，复制“https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog……”    
一大串网址到GaCha.py的m_cap_url变量，   
然后关闭抓包工具（抓包工具会影响到py的网络请求），运行GaCha.py，结果会保存在同级路径下的三个cvs文件。   
    
23-9-20：    
现在已经将mitmproxy抓包工具集成到项目内；    
可以通过命令行的简单菜单直接选择要执行的操作啦。     

通过CMD或python开发环境执行main.py文件    
显示：    
        请输入标号以执行任务：     
                1. 安装CA证书      
                2. 启动抓包     
                3. 导出数据    
       
首先手动运行mitmproxy.exe软件一会儿后关闭，使其在用户文件夹.mitmproxy下生成.p12文件   
这是CA证书，安装了它才能抓取未加密的https内容     
双击mitmproxy-ca.p12的运行证书安装向导，或者在菜单下输入1回车    
    
证书安装完毕后可以输入2回车，打开任意网页测试抓包工具是否准备就绪    
正常抓包情况下，网页可以正常访问，控制台会随着访问网页出现大量日志     
如果出现断网等情况，请检查CA证书的安装、全局代理设置是否正确等    
    
确保抓包正常后，打开原神祈愿界面，点击历史记录     
抓包工具会将抓取到的url储存在~url_cap.txt下，抓包工具自动退出，可能会出现短暂断网，刷新一下就好了     
菜单输入任意字符并回车，关闭抓包（包含关闭抓包工具进程，停用全局代理）    
    
菜单输入3回车，导出祈愿记录     
一次性导出角色池、武器池、常驻池的祈愿记录为csv文件，储存在ExportResults文件夹下     
     


![image](https://github.com/CJH3213/Images-blog/blob/main/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E5%9B%BE%E7%89%87/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E7%A4%BA%E4%BE%8B%E5%9B%BE1.png?raw=true)
    
    
![image](https://github.com/CJH3213/Images-blog/blob/main/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E5%9B%BE%E7%89%87/%E5%8E%9F%E7%A5%9E%E7%A5%88%E6%84%BF%E5%AF%BC%E5%87%BA%E5%B0%8F%E5%B7%A5%E5%85%B7_%E7%A4%BA%E4%BE%8B%E5%9B%BE2.png?raw=true)
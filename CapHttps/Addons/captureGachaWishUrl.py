import logging

import mitmproxy.http
from mitmproxy import ctx, http

file_path = '~url_cap.txt'
url_check = 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?'

class CaptureGachaWishUrl:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        logging.info("!!!host:: %s" % flow.request.host)

        if flow.request.host != 'hk4e-api.mihoyo.com':
            return

        full_url = flow.request.pretty_url

        if url_check in full_url:
            logging.info("!!!host:: %s" % full_url)
            # 抓取到匹配的祈愿url，储存在路径下的txt文本里
            with open(file_path, 'w', newline='', encoding="utf_8") as f:
                f.write(flow.request.pretty_url)

            # 捕获到了就关闭抓包工具，上级程序才能继续执行
            ctx.master.shutdown()


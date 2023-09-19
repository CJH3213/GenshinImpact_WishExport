from mitmproxy.tools.main import mitmdump
import counter
import captureGachaWishUrl

addons = [
    # counter.Counter(),
    captureGachaWishUrl.CaptureGachaWishUrl(),
]

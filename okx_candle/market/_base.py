from okx_api.market import Market
from okx_api.public import Public


class MarketBase():
    def __init__(
            self,
            instType: str,
            key: str = '',
            secret: str = '',
            passphrase: str = '',
            timezone='Asia/Shanghai'
    ):
        self.instType = instType.upper()

        FLAG = '0'  # 实盘
        self.marketAPI = Market(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG
        )
        self.publicAPI = Public(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG
        )
        self.timezone = timezone

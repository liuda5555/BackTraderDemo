import backtrader as bt


class TestStrategy(bt.Strategy):

    def __init__(self) -> None:
        # 保存收盘价的引用
        self.dataclose = self.datas[0].close

    def next(self):
        # 记录收盘价
        self.log('Close, %.2f' % self.dataclose[0])

    def log(self, txt, dt=None):
        # 记录策略的执行日志
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

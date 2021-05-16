from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from strategies import MyStrategy
from datafeeds.baostockdata import BaoStockTest

if __name__ == '__main__':


    cerebro = bt.Cerebro()

    cerebro.addstrategy(MyStrategy)
    # 每次买100股
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)

    # 加载数据到模型中
    data = bt.feeds.GenericCSVData(
        dataname='600519.csv',
        fromdate=datetime.datetime(2010, 1, 1),
        todate=datetime.datetime(2020, 4, 12),
        dtformat='%Y%m%d',
        datetime=2,
        open=3,
        high=4,
        low=5,
        close=6,
        volume=10
    )
    cerebro.adddata(data)

    # 设定初始资金和佣金
    cerebro.broker.setcash(1000000.0)
    cerebro.broker.setcommission(0.005)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

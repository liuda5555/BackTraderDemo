from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from strategies.TestStrategy import TestStrategy
from datafeeds.MyData import *
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(TestStrategy)
    # 每次买100股
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)

    # path = "f://all_trading_data/stock data/sh600000.csv"
    myData = Mydata();

    # 加载数据到模型中
    data = bt.feeds.PandasDirectData(
        dataname=myData.getData(),
        fromdate=datetime.datetime(2013, 1, 1),
        todate=datetime.datetime(2013, 1, 31),
        dtformat='%Y-%m-%d',
        datetime=2,
        open=3,
        high=4,
        low=5,
        close=6,
        volume=8
    )
    cerebro.adddata(data, name='sh600000')

    # 设定初始资金和佣金
    cerebro.broker.setcash(1000000.0)
    cerebro.broker.setcommission(0.005)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    b = Bokeh(style='bar', plot_mode='single', scheme=Tradimo())
    cerebro.plot(b)

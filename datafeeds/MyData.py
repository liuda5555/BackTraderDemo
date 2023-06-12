import sys

import pandas as pd
import numpy as np
import datetime


class Mydata():

    def getData(self):
        # print(sys.path)
        # path = "/resources/sh600000.csv"
        path = "C:/Users/Administrator/PycharmProjects/BackTraderDemo/resources/sh600000.csv"

        df = pd.read_csv(path)
        # df['date'] =datetime.datetime.strptime(df['date'],'%Y-%m-%d')
        # df['date'] = df['date'].astype('datetime64[ns]')
        # df['date'] = df['date'].astype(pd.to_datetime())
        df['date'] = pd.to_datetime(df['date'])

        # return df.iloc[::-1]
        return df.reindex(index=df.index[::-1])

# mydata = Mydata()
# test = mydata.getData()
#
# print(type(test))
# print(test)
# print(type(test['date'][1]))
# print(test['code'])
# print(test.loc[:,'code'])

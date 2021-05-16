import baostock as bs
import pandas as ps

lg = bs.login();

class BaoStockData():

    islogin = False

    #自动登录系统
    def __init__(self):
        if not self.islogin:
            lg = bs.login()
            if not lg.error_code == '0':
                print('登录失败！，%s' % lg.error_msg)
                raise Exception('登录失败！' + lg.error_msg)
            else:
                self.islogin = True

    def do_data_by_dataFrame(self,stock_code=None,start_date=None,end_date=None):

        rs = bs.query_history_k_data_plus("sh.600198",
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                          start_date='2017-07-01', end_date='2017-07-30',
                                          frequency="d", adjustflag="3")
        if not rs.error_code == '0':
            raise Exception('数据获取失败！' + rs.error_msg)

        dt = rs.get_data()

        print(type(dt))
        print(dt)

print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

data_list = []

# while(rs.error_code == '0') & (rs.next()):
#     data_list.append(rs.get_row_data())
# df = ps.DataFrame(data_list,columns=rs.fields)
# print(df);

bs.logout();
import pandas as pd

import datetime


def read(y):
    df1=pd.read_csv(y)
    # print(df1)
    #print(df1.DATE[0])
    date_format= '%d-%m-%Y'
    try:
        date_obj = datetime.datetime.strptime(df1.DATE[0], date_format)


        # df1.reset_index('index')


    except:
        j = 0
        for i in df1.DATE:
            df1.at[j, 'DATE'] = datetime.datetime.strptime(i, "%d-%b-%Y")
            j = j + 1

        k = 0
        for i in df1.DATE:
            year = df1.DATE[k].strftime("%Y")
            month = df1.DATE[k].strftime("%m")
            day = df1.DATE[k].strftime("%d")
            df1.at[k, 'DATE'] = day + "-" + month + "-" + year
            k = k + 1

    return df1[['DATE','TIME','HIGH','LOW','OPEN','CLOSE','QUANTITY','AVERAGE']]
# df1=read('csv_file\AXISBANK.csv')
# print(df1)
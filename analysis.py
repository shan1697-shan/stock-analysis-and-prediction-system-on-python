import pandas as pd


import datetime




# if con:
#     print('Connected successfully')
# df1=pd.read_csv("csv_file/AXISBANK.csv")
# #print(df1.DATE[0])
# j=0
# for i in df1.DATE:
#     df1.at[j,'DATE']=datetime.datetime.strptime(i, "%d-%b-%Y")
#     j=j+1
#
# k=0
# for i in df1.DATE:
#     year=df1.DATE[k].strftime("%Y")
#     month=df1.DATE[k].strftime("%m")
#     day=df1.DATE[k].strftime("%d")
#     df1.at[k, 'DATE'] = day+"-"+month+"-"+year
#     k=k+1

def report(df1):
    print('analysis has been started')
    nw=1
    con=0
    #x=df1.AVERAGE.idxmax()
    # print(x)
    # columnsData = df1.loc[ x , : ]
    #print(columnsData)
    df=pd.DataFrame()
    df2=pd.DataFrame()
    # df=df.append([df1.loc[2,:],df1.loc[1,:],df1.loc[x,:]])
    # print(df)
    no_row=df1.DATE.count()
    #print(no_row)

    for i in range((no_row-1)):
        if df1.DATE[i]==df1.DATE[nw]:
            # print(df1.DATE[i])
            df=df.append(df1.loc[i,:])

        else:
            #print(df)
            x = df.CLOSE.idxmax()
            # print(type(x))
            #print(x)
            # print(df.loc[x,:])
            rcountdf=df.DATE.count()
            con=con+rcountdf
            #print(rcountdf)
            # print(df)
            df2 = df2.append([df1.loc[(con-rcountdf), :],df1.loc[x, :],df1.loc[(con-1), :]])
            df = df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7]], axis=1, inplace=True)
            df=pd.DataFrame()

        if nw<(no_row-1):
            nw = nw + 1
        else:
            continue

    # df2=df2.drop(df.columns[[0]],axis=1,inplace=True)
    # df2=df2.reset_index(level="DATE")


    # print(df2[['DATE','TIME','HIGH','LOW','OPEN','CLOSE','QUANTITY','AVERAGE']])

    return df2[['DATE','TIME','HIGH','LOW','OPEN','CLOSE','QUANTITY','AVERAGE']]


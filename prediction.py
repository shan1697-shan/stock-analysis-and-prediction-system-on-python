import sklearn.model_selection as ms
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import read_file as rf
import math
import datetime
import frameGUI as fg


def predict(impframe):
    df = rf.read('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\ADANIPORTS.csv' )
    df1 = rf.read('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\ASIANPAINT.csv' )
    df2 = rf.read('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\AXISBANK.csv')
    df3 = [df, df1, df2]
    result = pd.concat(df3)
    # print(result)
    # result.reset_index(inplace=True, drop=True)
    nwlst=[result,impframe]
    dframe= pd.concat(nwlst)
    dframe.reset_index(inplace=True,drop=True)
    # print(dframe)
    des=dframe.describe()
    # print(des)
    x = dframe[['HIGH', 'LOW', 'QUANTITY']].values
    y = dframe['CLOSE']
    xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, test_size=0.2, random_state=0)
    regression=LinearRegression()
    regression=regression.fit(xtrain, ytrain)
    # check=regression
    # print(check)
    # print(regression.coef_)
    # print(regression.intercept_)
    predicted=regression.predict(xtest)
    # print(predicted)
    ytest = np.array(list(ytest))
    predicted = np.array(predicted)
    nxtdate=[]
    date=dframe.DATE[0]
    # print(date)

    for itr in predicted:
        date=datetime.datetime.strptime(date, "%d-%m-%Y")

        year = date.strftime("%Y")
        year = int(year)
        month = date.strftime("%m")
        month = int(month)


        day = date.strftime("%d")
        day = int(day)


        if (year % 400 == 0):
            leap_year = True
        elif (year % 100 == 0):
            leap_year = False
        elif (year % 4 == 0):
            leap_year = True
        else:
            leap_year = False

        if month in (1, 3, 5, 7, 8, 10, 12):
            month_length = 31
        elif month == 2:
            if leap_year:
                month_length = 29
            else:
                month_length = 28
        else:
            month_length = 30

        if day < month_length:
            day += 1
        else:
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

        date = str(day) + "-" + str(month) + "-" + str(year)
        # print(date)
        nxtdate.append(date)



    nxtdate=np.array(nxtdate)

    pframe=pd.DataFrame({"DATE":nxtdate.flatten(), "Predicted Closing Price":predicted.flatten()})
    dframe1=pd.DataFrame({'actual':ytest.flatten(), 'predicted':predicted.flatten()})
    # print(dframe1.head(25))

    print("Predictions:")
    print(pframe.head(10))
    fg.funtable(pframe.head(10))
    # print("Do you want to save prediction in csv file:")
    # x=input()
    # if x.capitalize()=='YES':
    #     loc=input("enter Loction:")
    #     nme=input("enter name:")
    #     lon=loc+nme
    #     file=pframe.head(10).to_csv(lon)

    # print('mean absolute error', metrics.mean_absolute_error(ytest, predicted))
    # print('mean squared error', metrics.mean_squared_error(ytest, predicted))
    # print('root mean squared error', math.sqrt(metrics.mean_squared_error(ytest, predicted)))

    graph=dframe1.head(25)
    graph.plot(kind='bar')

    plt.show()
    # if check == True:
    #     print("model trained successfully")
    #
    # else:
    #     print("model trainning was unsuccessful")



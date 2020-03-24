print("hello")
import pandas as pd
import datetime

a=pd.read_csv("C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\axis.csv")

# # print(a)
# # a.reset_index()
# # a=a.drop(['index'],axis=1)
# # print(a)
# # print(type(a))
#
# fdate=a.DATE[0]
# print(fdate)
# fdate = datetime.datetime.strptime(fdate, "%d-%m-%Y")
# year = fdate.strftime("%Y")
# year=int(year)
# print(year)
# month = fdate.strftime("%m")
# month=int(month)
# print(month)
# day = fdate.strftime("%d")
# day=int(day)
# print(day)
#
# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False
#
# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30
#
# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is %d-%d-%d." % (day, month, year))
#
# date=str(day)+"-"+str(month)+"-"+str(year)
# print(date)
# print(type(date))
df=pd.read_csv('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\ADANIPORTS.csv',)
df1=pd.read_csv('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\ASIANPAINT.csv',)
df2=pd.read_csv('C:\\Users\\91727\\PycharmProjects\\majorproj\\csv_file\\AXISBANK.csv',)
df3= [df,df1,df2]
result=pd.concat(df3)
result.reset_index(inplace=True,drop=True)

print(result)
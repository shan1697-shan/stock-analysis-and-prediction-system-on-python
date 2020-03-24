import read_file
import pandas as pd
import analysis as an
import prediction as pre
import graph_report as gr
import pymysql as pym
import datetime


# con=pym.connect(host='localhost',user='root',password='',db='stockprediction')

def main():
    data=pd.DataFrame
    if data.empty:
        pass
        # print(data)
    else:
        data=data.drop(data.columns[[0, 1, 2, 3, 4, 5, 6, 7]], axis=1, inplace=True)
    print("Enter the path of the csv file:")
    x = input()
    data=read_file.read(x)
    # print(read_file.df1)
    print(data)
    while True:
        choice=int(input("Press 1 for report\n Press 2 for graphical report\n Press 3 to predict\n Press 4 to Quit:"))
        if choice==1:
            dataf=an.report(data)
            dataf=dataf.reset_index()
            dataf=dataf.drop(['index'],axis=1)
            print(dataf)
            path=input("enter the path to save the analysed report:")
            name=input("Enter the name of the file:")
            string=path+name+'.csv'
            print(string)
            file=dataf.to_csv(string)
            # today=str(datetime.date.today())
            # db=(name,x,today)
            # curs = con.cursor()
            # sql = "INSERT INTO stock('name','df','date') VALUES (%s,%s,%s)"
            # curs.execute(sql,db)
            # con.commit()

        elif choice==2:
            gr.greport(data)

        elif choice==3:
            pre.predict(data)


        elif choice==4:
            exit()

        else:
            print("Wrong Choice")


if __name__ == '__main__':
    main()

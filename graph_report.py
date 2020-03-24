import pandas as pd
import matplotlib.pyplot as plt
import analysis as an

def greport(dataframe):
    rep=dataframe
    rep=rep.iloc[::-1]
    # graph=plt.plot(dataframe.DATE,dataframe.CLOSE,"go")
    # graph=plt.title("REPORT")
    # graph=plt.xlabel("DATE")
    # graph=plt.ylabel("PRICE")
    # graph=plt.show()
    ax = plt.gca()

    rep.plot(kind='line', x='DATE', y='OPEN', ax=ax)
    rep.plot(kind='line', x='DATE', y='CLOSE', color='red', ax=ax)

    plt.show()
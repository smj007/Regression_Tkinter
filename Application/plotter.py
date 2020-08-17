import pandas as pd
from  matplotlib import pyplot as plt
import matplotlib
import seaborn as sns

def plot(filename, xlabel, ylabel):
    df = pd.read_csv(filename)
    sns.set(rc={'figure.figsize':(12,6)})
    sns.regplot(x=xlabel, y=ylabel, data=df)
    # regression line shows a possible positive correlation - as temp increases so does rainfall.
    plt.show() 
    
    return

if __name__ == '__main__':
    plot('tempRainYearly.csv','Temp', 'Rain' )
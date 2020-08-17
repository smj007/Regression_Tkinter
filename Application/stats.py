import pandas as pd

def stats_data(filename, xlabel, ylabel):
    df = pd.read_csv(filename)

    xdata = df[xlabel]
    ydata = df[ylabel]

    stats_X = xdata.describe()
    stats_Y = ydata.describe()
    
    return stats_X, stats_Y

if __name__ == '__main__':
    print (stats_data('tempRainYearly.csv','Temp', 'Rain' ))
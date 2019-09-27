import pandas as pd

def data_mpg():
    df = pd.read_csv('clean.csv')

    return df

def data_hp():
    df = pd.read_csv('clean.csv')

    usaRank = list(df[df['origin']=='usa'].sort_values(by='horsepower',ascending=False)['name'].values[:3])
    japanRank = list(df[df['origin']=='japan'].sort_values(by='horsepower',ascending=False)['name'].values[:3])
    europeRank = list(df[df['origin']=='europe'].sort_values(by='horsepower',ascending=False)['name'].values[:3])

    newdict3 = {
        'usa': usaRank,
        'japan': japanRank,
        'europe': europeRank
    }
    df1 = pd.DataFrame(newdict3, index=['Rank 1','Rank 2','Rank 3'])
    return df1


def data_irit():
    df = pd.read_csv('clean.csv')

    usaRank = list(df[df['origin']=='usa'].sort_values(by='mpg',ascending=False)['name'].values[:3])
    japanRank = list(df[df['origin']=='japan'].sort_values(by='mpg',ascending=False)['name'].values[:3])
    europeRank = list(df[df['origin']=='europe'].sort_values(by='mpg',ascending=False)['name'].values[:3])

    newdict3 = {
        'usa': usaRank,
        'japan': japanRank,
        'europe': europeRank
    }
    df2 = pd.DataFrame(newdict3, index=['Rank 1','Rank 2','Rank 3'])
    return df2

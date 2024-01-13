import pandas as pd

data = pd.read_csv('../NaiveBayesianLab6/data.csv')

te = len(data)
np = len(data.loc[data[data.columns[-1]]=='Yes'])
nn = te-np

training = data.sample(frac=0.75, replace=False)
test = pd.concat([data, training, training]).drop_duplicates(keep=False)

prob={}
for col in training[:-1]:
    prob[col]={}
    vals=set(data[col])
    for val in vals:
        temp = training.loc[training[col]==val]
        pe=len(temp.loc[temp[temp.columns[-1]]=='Yes'])
        ne=len(temp)-pe
        prob[col][val]=[pe/np, ne/nn]

pred = []
count=0
for i in range(len(test)):
    row=test.iloc[i, :]
    fpp=np/te
    fnn=nn/te

    for col in test.columns[:-1]:
            fpp*=prob[col][row[col]][0]
            fnn*=prob[col][row[col]][1]
    if fpp>fnn:
        pred.append('Yes')
    else: pred.append('No')
    if pred[-1] == row[-1]:
        count += 1

print('Actual values: ', list(test[test.columns[-1]]))
print('Predicted values: ', pred)
print('Accuracy: ', count/len(test))

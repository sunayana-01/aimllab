import csv

with open('../CandidateEliminationLab3/trainingexamples.csv') as f:
    csv_read = csv.reader(f)
    data = list(csv_read)

    specific = data[1][:-1]
    general = [['?' for _ in range(len(specific))] for _ in range(len(specific))]
    count=1

    for i in data:
        if i[-1]=='Yes':
            for j in range(len(specific)):
                if i[j]!=specific[j]:
                    specific[j]='?'
                    general[j][j]='?'
        else:
            for j in range(len(specific)):
                if i[j]!=specific[j]:
                    general[j][j]=specific[j]
                else:
                    general[j][j]='?'

        print('Step: ', count)
        print('Specific hypothesis: ', specific)
        print('General hypothesis: ', general)
        count+=1

    gh=[]
    for i in general:
        for j in i:
            if j!='?':
                gh.append(i)
                break
    
    print('Final specific hypothesis: ', specific)
    print('Final general hypothesis: ', gh)
import csv
ll=[["Звездные войны", "Терминатор", "Искусственный интеллект"],
    ["Дурак", "Матильда","Левиафан"],
    ["Люди в черном","Я - робот","Эволюция"]]
with open('st.csv', 'w') as f:
    w = csv.writer(f, delimiter = ',')

    for l in ll:
        w.writerow(l)

with open('st.csv', 'r') as f:
    r=csv.reader(f,delimiter=',')
    for row in r:
        print(','.join(row))

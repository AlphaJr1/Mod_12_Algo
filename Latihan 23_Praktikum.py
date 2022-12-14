import csv
with open ('Negara.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    for row in csv_reader:
        print(row)

import pandas as pd
#nama = pd.read_csv('C:/Users/user/Documents/Abang Adri/Tugas Kampus/Prak-Algoritma/Negara.csv')
#print(nama)
df = pd.DataFrame(row)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(df)
print(mean)
print(std)
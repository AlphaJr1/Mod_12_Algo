
import pandas as pd
Negara = pd.read_csv('C:/Users/user/Documents/Abang Adri/Tugas Kampus/Prak-Algoritma/Negara.csv')


df = pd.DataFrame(Negara)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya : ")
print(df)
print("\nBerikut Data Mean : ")
print(mean)
print("\nBerikut Data Standard Deviation : ")
print(std)

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print("Data Berhasil Dibuat")
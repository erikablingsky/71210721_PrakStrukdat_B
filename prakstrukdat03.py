rangeData =int(input("Masukkan range Data :"))

dik = {}
for i in range(rangeData):
    if i%2 ==0:
        if i != 0:
            faktorial = 1
            for e in range(2,i+1):
                faktorial = faktorial * e 
            dik[i] = faktorial
        else:
            dik[i]=1

print (dik)
data = int(input("data yang ditampilkan :"))
if data not in dik:
    print("Data tidak ditemukan ")
else:
    print(dik[data])
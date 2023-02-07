import math
import numpy as np

def simpangan_baku(data):
    n = len(data)
    rata_rata = sum(data)/n
    total = 0
    for i in range(n):
        total += (data[i] - rata_rata)**2
    return math.sqrt(total/(n-1))

def mean(data):
    return sum(data)/len(data)  

def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n//2]
    else:
        return (data[n//2 - 1] + data[n//2]) / 2

def modus(data):
    data.sort()
    n = len(data)
    frekuensi = []
    for i in range(n):
        frekuensi.append(data.count(data[i]))
    if max(frekuensi) == 1:
        return "Tidak ada modus"
    else:
        sama_banyak = []
        for i in range(n):
            if frekuensi[i] == max(frekuensi):
                sama_banyak.append(data[i])
        return list(dict.fromkeys(sama_banyak))
    
def variansi(data):
    n = len(data)
    rata_rata = sum(data)/n
    total = 0
    for i in range(n):
        total += (data[i] - rata_rata)**2
    return total/(n-1)

def kuartil_bawah(data):
    data.sort()
    n = len(data)
    index = (n + 1) * 25 / 100
    if index.is_integer():
        return data[int(index) - 1]
    else:
        floor = int(index) - 1
        ceil = floor + 1
        return (data[floor] + data[ceil]) / 2
    
def kuartil_atas(data):
    data.sort()
    n = len(data)
    index = (n + 1) * 75 / 100
    if index.is_integer():
        return data[int(index) - 1]
    else:
        floor = int(index) - 1
        ceil = floor + 1
        return (data[floor] + data[ceil]) / 2
    
def percentil_ke_n(data, n):
    return np.percentile(data, n)

def desil_ke_n(data, n):
    return np.percentile(data, n*10)

if __name__ == "__main__":
    # Example
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Data: ", data)
    print("Mean: ", mean(data))
    print("Median: ", median(data))
    print("Modus: ", modus(data))
    print("Simpangan Baku: ", simpangan_baku(data))
    print("Variansi: ", variansi(data))
    print("Kuartil Bawah: ", kuartil_bawah(data))
    print("Kuartil Atas: ", kuartil_atas(data))
    print("Percentil ke-50: ", percentil_ke_n(data, 50))
    print("Desil ke-5: ", desil_ke_n(data, 5))
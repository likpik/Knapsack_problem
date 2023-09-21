import time

def ad(l, n, b):
    t1 = time.time()
    m = [[0] * (b+1) for i in range(n+1)]
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if l[i-1][1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-l[i-1][1]]+l[i-1][2])
    fmax = m[n][b]
    wmax = 0
    s = []
    while m[i][j] != 0:
        while m[i][j] <= m[i-1][j]:
            i -= 1
        s.append(i)
        i -= 1
        j -= l[i][1]
    for i in s:
        wmax += l[i-1][1]
    t2 = time.time()
    t = t2 - t1
    return s, wmax, fmax, t

def az(l, b):
    for i in range(len(l)):
        a = l[i][2] / l[i][1]
        l[i].append(a)
    s = []; r = 0; w = 0
    t1 = time.time()
    l.sort(reverse=True, key=lambda x: x[3])
    for i in range(len(l)):
        if l[i][1] <= b:
            s.append(l[i][0])
            r += l[i][1]
            w += l[i][2]
            b -= l[i][1]
    t2 = time.time()
    t = t2 - t1
    return s, r, w, t

def ab(l, n, b):
    l.sort(reverse=True)
    s = []; fmax = 0; wmax = 0
    t1 = time.time()
    for X in range(1, 2**n):
        x = list(bin(X)[2:])
        x = ['0'] * (n - len(x)) + x
        w = 0; f = 0
        for i in range(len(x)):
            if x[i] == '1':
                w += l[i][1]
        if w <= b:
            for i in range(len(x)):
                if x[i] == '1':
                    f += l[i][2]
                if f > fmax:
                    fmax = f
                    wmax = w
                    res = x
    t2 = time.time()
    t = t2-t1
    for i in range(n):
        if res[i] == '1':
            s.append(l[i][0])
    return s, wmax, fmax, t

l = []
f = open("plik.txt")
f1 = f.readline()
n, b = [int(x) for x in f1.split()]
for i in range(n):
    f2 = f.readline()
    r, w = [int(x) for x in f2.split()]
    l.append([i+1,r,w])
f.close()

print()
print("pojemność plecaka: ", b)
print("przedmioty wejściowe: ", l)
print()

ad = ad(l,n,b)
print("-------------ALGORYTM DYNAMICZNY-------------")
print()
print("przedmioty włożone do plecaka: ", ad[0])
print("łączna waga przedmiotów: ", ad[1])
print("łączna wartość przedmiotów: ", ad[2])
print("czas szukania rozwiązania: ", ad[3])
print()

az = az(l,b)
print("-------------ALGORYTM ZACHŁANNY-------------")
print()
print("przedmioty włożone do plecaka: ", az[0])
print("łączna waga przedmiotów: ", az[1])
print("łączna wartość przedmiotów: ", az[2])
print("czas szukania rozwiązania: ", az[3])
print()

ab = ab(l,n, b)
print("-------------ALGORYTM SIŁOWY-------------")
print()
print("przedmioty włożone do plecaka: ", ab[0])
print("łączna waga przedmiotów: ", ab[1])
print("łączna wartość przedmiotów: ", ab[2])
print("czas szukania rozwiązania: ", ab[3])

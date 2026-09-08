import math
import random

N = 1000


def hafman(frekvencije: dict):
    ukupno = sum(frekvencije.values())
    nodes = []

    for simbol, freq in frekvencije.items():
        nodes.append([freq / ukupno, {simbol: ""}])

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        levo = nodes.pop(0) # najmanji
        desno = nodes.pop(0) # drugi najmanji
        novi_kodovi = {}
        for sim, kod in levo[1].items():
            novi_kodovi[sim] = "0" + kod
        for sim, kod in desno[1].items():
            novi_kodovi[sim] = "1" + kod
        nodes.append([levo[0] + desno[0], novi_kodovi]) # novi cvor sa zbirnom frekvencijom i kodovima

    return nodes[0][1] # vraca koren stabla sa recnikom simbol:kod


def main():

    # Uslovne verovatnoce
    p00 = float(input("Unesite verovatnocu da se posle 0 javi 0: "))
    p10 = 1 - p00 #verovatnoca da se posle 0 javi 1
    q11 = float(input("Unesite verovatnocu da se posle 1 javi 1: "))
    q01 = 1 - q11
    
    # Stacionarne verovatnoce
    p0 = q01 / (1 - p00 + q01)
    p1 = 1 - p0

    print(f"\nGenerisana sekvenca (N = {N}):")

    sekvenca = []

    for i in range(N):
        if i == 0:
            if random.random() < p0:
                sekvenca.append(0)
            else:
                sekvenca.append(1)
        else:
            if sekvenca[i-1] == 0:
                if random.random() < p00:
                    sekvenca.append(0)
                else:
                    sekvenca.append(1)
            else:
                if random.random() < q11:
                    sekvenca.append(1)
                else:
                    sekvenca.append(0)
        print(sekvenca[i], end="")

    
    #Entropija
    #zdruzene verovatnoce
    z00 = p0 * p00
    z01 = p0 * p10
    z10 = p1 * q01
    z11 = p1 * q11

    H = -(z00 * math.log2(p00) + z01 * math.log2(p10) + z10 * math.log2(q01) + z11 * math.log2(q11))
    print(f"\nEntropija: {H:.4f} [Sh/simb]")
    
    # Hafmanov kod
    print("\n======= Hafmanov kod =======")


    # Prvi red
    c0 = sekvenca.count(0)
    c1 = sekvenca.count(1)

    if c0 >= c1:
        code0 = "0"
        code1 = "1"
    else:
        code0 = "1"
        code1 = "0"

    L1 = (c0*len(code0) + c1*len(code1))
    print("L1:", L1)


    # Drugi red
    blokovi2 = []

    for i in range(0, len(sekvenca) - 1, 2):
        blokovi2.append((sekvenca[i], sekvenca[i+1]))

    c00 = blokovi2.count((0, 0))
    c01 = blokovi2.count((0, 1))
    c10 = blokovi2.count((1, 0))
    c11 = blokovi2.count((1, 1))

    p00_2 = c00 / len(blokovi2)
    p01_2 = c01 / len(blokovi2)
    p10_2 = c10 / len(blokovi2)
    p11_2 = c11 / len(blokovi2)

    H2 = 0
    if p00_2 > 0: H2 -= p00_2 * math.log2(p00_2)
    if p01_2 > 0: H2 -= p01_2 * math.log2(p01_2)
    if p10_2 > 0: H2 -= p10_2 * math.log2(p10_2)
    if p11_2 > 0: H2 -= p11_2 * math.log2(p11_2)
    H2 /= 2 
    print(f"\nH2: {H2:.4f} [Sh/simb]")

    freq2 = {(0,0): c00, (0,1): c01, (1,0): c10, (1,1): c11}
    kod2 = hafman(freq2)

    compressed2 = (
    c00 * len(kod2[(0,0)]) +
    c01 * len(kod2[(0,1)]) +
    c10 * len(kod2[(1,0)]) +
    c11 * len(kod2[(1,1)])
    )

    print("L2:", compressed2)

    # Treci red
    blokovi3 = []
    for i in range(0, len(sekvenca) - 2, 3):
        blokovi3.append((sekvenca[i], sekvenca[i+1], sekvenca[i+2]))

    c000 = blokovi3.count((0, 0, 0))
    c001 = blokovi3.count((0, 0, 1))
    c010 = blokovi3.count((0, 1, 0))
    c011 = blokovi3.count((0, 1, 1))
    c100 = blokovi3.count((1, 0, 0))
    c101 = blokovi3.count((1, 0, 1))
    c110 = blokovi3.count((1, 1, 0))
    c111 = blokovi3.count((1, 1, 1))

    p000_3 = c000 / len(blokovi3)
    p001_3 = c001 / len(blokovi3)
    p010_3 = c010 / len(blokovi3)
    p011_3 = c011 / len(blokovi3)
    p100_3 = c100 / len(blokovi3)
    p101_3 = c101 / len(blokovi3)
    p110_3 = c110 / len(blokovi3)
    p111_3 = c111 / len(blokovi3)

    H3 = 0
    if p000_3 > 0: H3 -= p000_3 * math.log2(p000_3)
    if p001_3 > 0: H3 -= p001_3 * math.log2(p001_3)
    if p010_3 > 0: H3 -= p010_3 * math.log2(p010_3)
    if p011_3 > 0: H3 -= p011_3 * math.log2(p011_3)
    if p100_3 > 0: H3 -= p100_3 * math.log2(p100_3)
    if p101_3 > 0: H3 -= p101_3 * math.log2(p101_3)
    if p110_3 > 0: H3 -= p110_3 * math.log2(p110_3)
    if p111_3 > 0: H3 -= p111_3 * math.log2(p111_3)
    H3 /= 3
    print(f"\nH3: {H3:.4f} [Sh/simb]")

    freq3 = {
        (0,0,0): c000, (0,0,1): c001, (0,1,0): c010, (0,1,1): c011,
        (1,0,0): c100, (1,0,1): c101, (1,1,0): c110, (1,1,1): c111,
    }
    kod3 = hafman(freq3)

    compressed3 = (
    c000 * len(kod3[(0,0,0)]) +
    c001 * len(kod3[(0,0,1)]) +
    c010 * len(kod3[(0,1,0)]) +
    c011 * len(kod3[(0,1,1)]) +
    c100 * len(kod3[(1,0,0)]) +
    c101 * len(kod3[(1,0,1)]) +
    c110 * len(kod3[(1,1,0)]) +
    c111 * len(kod3[(1,1,1)])
    )

    print("L3:", compressed3)

if __name__ == "__main__":
    main()
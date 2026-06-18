billetes = [200, 100, 50, 20, 10]
montos = [380, 670, 920]

for m in montos:
    print("Monto:", m)
    total = 0
    for b in billetes:
        c = m // b
        if c > 0:
            print(f"{c} billetes de {b}")
            total += c
            m = m % b
    print("Total billetes:", total)
    print()

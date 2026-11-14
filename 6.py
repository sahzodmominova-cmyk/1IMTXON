import csv

yonalishlar = {}

with open("qatnov.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        yonalish = qator["yonalish"]
        yolovchi = int(qator["yolovchi"])

        if yonalish in yonalishlar:
            yonalishlar[yonalish] += yolovchi
        else:
            yonalishlar[yonalish] = yolovchi

for yonalish, jami in yonalishlar.items():
    print(f"{yonalish}-yo'nalish: {jami} nafar")
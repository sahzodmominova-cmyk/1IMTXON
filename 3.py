kodlar = [" UZ-2026-AB1234 ", "UZ-26-AB1234", "UZ-2026-aB1234"]

def tekshirish(kod):
    kod = kod.strip()
    qismlar = kod.split("-")

    if len(qismlar) == 3:
        yil = qismlar[1]
        seriya = qismlar[2]

        if (qismlar[0] == "UZ" and len(yil) == 4
            and yil.isdigit() and len(seriya) == 6
            and seriya[:2].isupper() and seriya[2:].isdigit()):

            print(f"{kod}: yaroqli | yil: {yil} | seriya: {seriya}")
        else:
            print(f"{kod}: yaroqsiz")
    else:
        print(f"{kod}: yaroqsiz")


for kod in kodlar:
    tekshirish(kod)
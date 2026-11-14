xizmatlar = {
    "diagnostika": 50000,
    "tozalash": 80000,
    "sozlash": 40000,
    "almashtirish": 120000
}

def hisobla(*args, **kwargs):
    jami = 0

    for xizmat in args:
        if xizmat in xizmatlar:
            jami += xizmatlar[xizmat]
        else:
            print(f"Ogohlantirish: {xizmat} xizmati topilmadi!")

    chegirma = jami * kwargs["chegirma"] / 100
    tolov = jami - chegirma

    print(f"Mijoz: {kwargs['mijoz']}")
    print(f"Xizmatlar jami: {jami} so'm")
    print(f"Chegirma: {chegirma:.0f} so'm")
    print(f"To'lov: {tolov:.0f} so'm")


hisobla("diagnostika","tozalash","sozlash",mijoz="Nodira",chegirma=10)
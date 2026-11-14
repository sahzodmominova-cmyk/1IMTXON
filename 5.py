import json


def kutubxona_inventari():
    try:
        with open("inventar.json", "r", encoding="utf-8") as fayl:
            kitoblar = json.load(fayl)

        mavjud_kitoblar = []

        for kitob in kitoblar:
            nom = kitob.get("nom", "Noma'lum")
            jami = kitob.get("jami", 0)
            band = kitob.get("band", 0)
            mavjud = jami - band

            print(f"{nom}: {mavjud} ta mavjud")

            mavjud_kitoblar.append({
                "nom": nom,
                "mavjud": mavjud
            })

        with open("mavjud_kitoblar.json", "w", encoding="utf-8") as f:
            json.dump(mavjud_kitoblar, f, indent=4)

        print(f"{len(mavjud_kitoblar)} ta yozuv saqlandi.")

    except FileNotFoundError:
        print("Xatolik: 'inventar.json' fayli topilmadi!")
    except Exception as e:
        print(f"Kutilmagan xatolik yuz berdi: {e}")


kutubxona_inventari()

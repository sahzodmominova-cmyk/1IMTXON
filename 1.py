log = " hall-a, HALL-B, hall-a, , hall-c, HALL-B, hall-a "

natija = [x.strip().upper() for x in log.split(',') if x.strip()]
print(f"Tozalangan: {natija}")

noyoblar = len(set(natija))
print(f"Noyob bo'limlar: {noyoblar}")

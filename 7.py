import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

ortacha = sum(sarf) / len(sarf)

yuqori_kunlar = []
yuqori_sarf = []

for i in range(len(sarf)):
    if sarf[i] > ortacha:
        yuqori_kunlar.append(kunlar[i])
        yuqori_sarf.append(sarf[i])

print(f"O'rtacha sarf: {ortacha:.2f} kWh")
print(f"O'rtachadan yuqori kunlar: {', '.join(yuqori_kunlar)}")

plt.plot(kunlar, sarf, marker="o", label="Elektr sarfi")
plt.axhline(ortacha, linestyle="--", label="O'rtacha sarf")
plt.scatter(yuqori_kunlar, yuqori_sarf, label="Yuqori sarf")

plt.title("7 kunlik energiya sarfi")
plt.xlabel("Hafta kunlari")
plt.ylabel("Elektr sarfi (kWh)")
plt.legend()
plt.grid()

plt.savefig("energiya_tahlili.png")
plt.show()
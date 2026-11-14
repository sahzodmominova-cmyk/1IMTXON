haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

hafli=0
for c in haroratlar:
    if c <= -18:
        hafli+=1
ortacha=sum(haroratlar)/len(haroratlar)
print(f"Xavfli olchovlar: {hafli}\n Ortacha harorat:{ortacha:.2f}")

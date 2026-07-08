ad=input("Zehmet olmasa adinizi qeyd edin")
yas=int(input("Zehmet olmasa yasinizi qeyd edin"))
gelir=int(input("Zehmet olmasa ayliq gelirinizi qeyd edin"))
dogum_ili=2026-yas
vergi=gelir* 20/100
xalis_gelir=gelir-vergi

print(f"Doğum ili {dogum_ili}")
print(f"Ayliq vergi {vergi}")
print(f"Xalis gelir {xalis_gelir}")


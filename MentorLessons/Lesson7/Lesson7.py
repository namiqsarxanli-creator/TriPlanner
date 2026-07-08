# telebeler=["Anar", "Leyla","Aygun","Anar"]
# print(telebeler)
# telebler=set(telebeler)
# print(telebler)
#
# telebeler={"Anar", "Leyla","Aygun","Anar"}
# print(telebeler)


# sinif_A = {"Anar", "Günel", "Nicat"}
# sinif_B = {"Günel", "Fidan", "Ramin"}
#
# umumi= sinif_A | sinif_B
#
# ortaq= sinif_A & sinif_B
#
# ferq=sinif_A - sinif_B




#Tasks

# rengler = ["qırmızı", "yaşıl", "mavi", "qırmızı", "sarı", "yaşıl"]
#
# rengler=set(rengler)
# print(rengler)



# icazeli_kodlar = {101, 202, 303, 404, 505}
#
# i=int(input("Zehmet olmasa kod daxil edin"))
#
# if i in icazeli_kodlar:
#     print("Kod var")
# else:
#     print("Kod yoxdur")



# dost1 = {"Inception", "Interstellar", "The Dark Knight", "Tenet"}
# dost2 = {"Interstellar", "Avatar", "Tenet", "The Prestige"}
#
# ortaq=dost1 & dost2
# print(ortaq)
#
# ferq=dost1-dost2
# print(ferq)


# mehsullar = {
#     "alma": 2,
#     "banan": 4,
#     "portağal": 3
# }
#
# mehsullar.update({"albali": 5})
# print(mehsullar)
#
# qiymet=mehsullar.get("armud", "mehsul tapilmadi")
# print(qiymet)



# mehsullar = {
#     "alma": 2,
#     "banan": 4,
#     "portağal": 3,
#     "albalı": 5
# }
#
# cem=0
#
# for i in mehsullar.values():
#     cem+=i
#     print(cem)


#
# orxan_dostlar = {"Eldar", "Aysel", "Rauf", "Kənan"}
# leyla_dostlar = {"Aysel", "Məmməd", "Kənan", "Nigar"}
#
# ortaq= orxan_dostlar & leyla_dostlar
# print(ortaq)
#
# ferq=orxan_dostlar - leyla_dostlar
# print(ferq)



# orxan_dostlar = {"Eldar", "Aysel", "Rauf", "Kənan"}
# leyla_dostlar = {"Aysel", "Məmməd", "Kənan", "Nigar"}
#
# umumi=orxan_dostlar | leyla_dostlar
# print(umumi)
# print(len(umumi))



# imtahan_ballari = {"Murad": 85, "Zəhra": 92, "Emin": 74}
#
# for acar, deyer in imtahan_ballari.items():
#     print(f"telebe:", acar,"bal:" ,deyer)



# oxunmali_kitablar = {"1984", "Səfillər", "Xəmsə"}
#
# oxunmali_kitablar.add("Heyvanıstan")
#
# oxunmali_kitablar.remove("Səfillər")
#
# print(oxunmali_kitablar)



# menyu = {
#     "Plov": 12,
#     "Pitsa": 15,
#     "Şorba": 5,
#     "Kabab": 18
# }
#
#
# budce=float(input("zehmet olmasa maximum budcenizi daxil edin"))
#
# for yemek, qiymet in menyu.items():
#     if qiymet <= budce:
#         print(f"{yemek}: {qiymet} AZN")



# bloklanmis_ipler = {"192.168.1.5", "10.0.0.23", "172.16.0.45"}
# unvan=input("zehmet olmasa ip unvan qeyd edin")
#
# if unvan in bloklanmis_ipler:
#     print("Giriş qadağandır! (Bloklanıb)")
# else:
#     print("Giriş uğurludur.")


# metn = "python oyrənmək maraqlıdır və python həm də çox populyardır"
# sozler=metn.split()
# dic={
#
# }
#
# for soz in sozler:
#     if soz not in dic:
#         dic[soz]=1
#     else:
#         dic[soz]+=1
#     print(dic)


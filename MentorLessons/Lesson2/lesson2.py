#if, elif, else- serti operatorlari

a=3
b=5

# if a>b:
#     print("A B-den boyukdur")
#
# if b>a:
#     print("B A-dan boyukdur")

# else:
#     print("B A-dan boyukdur")


# tempratur=30
#
# if tempratur>25:
#     print("Hava istidir")
#
# else:
#     print("Hava soyuqdur")


# imtahan_bali=81
#
# if imtahan_bali>90:
#     print("Siz elacasiniz")
#
# elif imtahan_bali>80:
#     print("siz zerbecisiniz")
# else:
#     print("siz kesilmisiniz")


# avtomobilin_sureti=int(input("Zehmet olmasa avtomobilin suretini qeyd edin"))
# if avtomobilin_sureti>110:
#     print("Siz suret heddini asdiniz, cerime tetbiq oluna biler")
# elif 60<avtomobilin_sureti<110:
#     print("Normal sürətlə hərəkət edirsiniz")
# else:
#     print("Çox yavaş gedirsiniz, sağ zolağa keçin")

# mehsulun_qiymeti=int(input("Mehsulun qiymetini daxil edin"))
# mehsulun_qiymeti-=mehsulun_qiymeti*15/100
# print(f"Endirimli qiymet{mehsulun_qiymeti}")

# tam_eded=int(input("Tam eded daxil edin"))
# if tam_eded>0:
#     print("Ədəd müsbətdir")
# elif tam_eded<0:
#     print("Ədəd mənfidir")
# else:
#     print("Daxil edilən ədəd sıfırdır")


# istifadecinin_yasi=int(input("Zehmet olmasa yasinizi qeyd edin"))
# if istifadecinin_yasi<12 or istifadecinin_yasi>65:
#     print("Pulsuz")
# else:
#     print("10Azn")

# sayi=int(input("Eded daxil edin"))
#
# if sayi%2==0:
#     print("Cutdur")
# else:
#     print("Tekdir")

# a=int(input("a"))
# b=int(input("b"))
# c=int(input("c"))
# if a>b and a>c:
#     print("En boyuk",a)
# elif b>c:
#     print("En boyuk", b)
# else:
#     print("En boyuk",c)

# bal=int(input("Balinizi daxil edin"))
# if bal>90:
#     print("Qiymet,A")
# elif bal>=75:
#     print("Qiymet, B")
# elif bal>=60:
#     print("Qiymet, C")
# else:
#     print("Kesildiniz")


# a=float(input("Birinci eded:"))
# b=float(input("Ikinci eded:"))
# op=input("Emeliyyat (+, -, *, /)")
#
# if op=="+":
#     print(a+b)
# elif op=="-":
#     print(a-b)
# elif op=="*":
#     print(a*b)
# elif op=="/" and b!=0:
#     print(a/b)
# else:
#     print("Xeta, sifira bolme")


#EV TAPSIRIGI

# istifadeci=int(input("Zehmet olmasa her gun nece stekan su icdiyinizi qeyd edin"))
#
# if 0<istifadeci<3:
#     print("Çox az su içirsiniz, sağlığınız üçün zərərlidir!")
# elif 4<istifadeci<7:
#     print("Yaxşıdır, amma bir az da artıra bilərsiniz.")
# else:
#     print("Əla! Gündəlik normadan artıq su içirsiniz")


# mebleg=float(input("Zehmet olmasa alis-veris mebleginizi qeyd edin"))
#
# if mebleg<100:
#     print("endirim yoxdur, tam məbləği çap edin")
# elif mebleg<300:
#     mebleg-=mebleg*0.1
#     print("Odenis: ",mebleg, "AZN")
# else:
#     mebleg-=mebleg*0.2
#     print("Odenis: ",mebleg, "AZN")



# gunun_nomresi=int(input("Zehmet olmasa gunun nomresini qeyd edin. (1-7): "))
#
# if gunun_nomresi==6 or gunun_nomresi==7:
#     print("Bu gün həftəsonudur, istirahət edin!")
# else:
#     print("İş günüdür, uğurlar!")


# sifaris_meblegi=float(input("Zehmet olmasa sifaris meblegini qeyd edin "))
#
# if sifaris_meblegi>50:
#     print("Catdirilma pulsuzdur. Yekun mebleg:",sifaris_meblegi, "AZN")
# else:
#     sifaris_meblegi+=3
#     print("Catdirilma 3 AZN. Yekun mebleg:",sifaris_meblegi, "AZN")


# saat=int(input("Zehmet olmasa saati qeyd edibn,(0-23): "))
#
# if saat<0 or saat>23:
#     print("Saat duzgun qeyd olunmayib")
# elif 7<saat<22:
#     print("Gunduz rejimi aktiv")
# else:
#     print("Gece rejimi aktiv")


# sefer_sayi=int(input("Zehmet olmasa metrodan ay erzinde metrodan nece defe istifade edeceyinizi qeyd edin "))
#
# ferdi_bilet=sefer_sayi*0.30
# abonelik=10
#
# if ferdi_bilet<abonelik:
#     ferq=abonelik-ferdi_bilet
#     print("Fərdi bilet sərfəlidir. Qənaət:", round(ferq, 2), "AZN")
# else:
#     ferq=ferdi_bilet-abonelik
#     print("Abonelik sərfəlidir. Qənaət:", round(ferq, 2), "AZN")


# imtahan_bali=int(input("Zehmet olmasa imtahan balinizi qeyd edin: "))
# devamiyyet_faizi=float(input("Zehmet olmasa devamiyyet faizinizi qeyd edin: "))
#
# if imtahan_bali>=60 and devamiyyet_faizi>80:
#     print("Sertifikat almağa haqq qazandınız!")
# elif imtahan_bali<60 and devamiyyet_faizi<=80:
#     print("Həm bal, həm davamiyyət şərti ödənilmədi.")
# elif imtahan_bali<60:
#     print("İmtahan balınız kifayət deyil.")
# else:
#     print("Davamiyyətiniz kifayət deyil.")




























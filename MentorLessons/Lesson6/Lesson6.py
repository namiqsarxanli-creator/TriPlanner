# meyve="alma"
#
# if meyve=="alma":
#     print("True")

# meyveler=["alma","banan","armud","gilas"]
#
# if "alma" in meyveler:
#     print("Var")

# sinif_otaqi = [
#     ["Əli",    "Vəli",   "Ayşə"],   # Sətir 0
#     ["Leyla",  "Murad",  "Kənan"],  # Sətir 1
#     ["Nigar",  "Elvin",  "Səid"]    # Sətir 2
# ]
#
# # print(sinif_otaqi[1])
#
# cumle = "salam necesiniz?"
# print(cumle.capitalize()) # "Salam necesiniz?"
#
# # 4. title() — HƏR SÖZÜN ilk hərfi böyüdür
# ad_soyad = "orxan veliyev"
# print(ad_soyad.title())   # "Orxan Veliyev"

# seher = input("Şəhər adı yazın: ") # İstifadəçi "BaKu" yazdı fərz edək
#
# if seher.lower() == "baku":
#     print("Paytaxta xoş gəlmisiniz!")


#Tasks

# sifarisler=["Kofe", "Pizza", "Su"]
# sifarisler.insert(0,"Cay")
# sifarisler.append("Sirniyyat")
# sifarisler.remove("Su")
# print(sifarisler)
# print(len(sifarisler))


# masin_melumati=("Toyota", 2022, "Gümüşü")
# print(masin_melumati[1])
# for x in masin_melumati:
#     print(x)


# pleylist = ["Mahnı A", "Mahnı B", "Mahnı C", "Mahnı D", "Mahnı E", "Mahnı F"]
# print(pleylist[:2])
# print(pleylist[-2:])
# print(pleylist[2:4])

# idmanlar = ("Futbol", "Basketbol", "Tennis")
#
# idmanlar=list(idmanlar)
# idmanlar.append("Voleybol")
# idmanlar.insert(0,"Üzgüçülük")
# idmanlar.sort()
# idmanlar=tuple(idmanlar)
# print(idmanlar)


# hefte_1 = [15, 45, 8]
# hefte_2 = [60, 12, 35, 90]
#
# butun_xercler=hefte_1+hefte_2
# butun_xercler.sort()
# print(butun_xercler)
# butun_xercler.sort(reverse=True)
# print(butun_xercler)
# xercler=[x for x in butun_xercler if x>30]
# print(xercler)



# istifadeciler = ["admin", "user01", "shadow", "guest"]
# ad=input("zehmet olmasa bir ad qeyd edibn: ").lower()
# if ad in istifadeciler:
#     print("Giriş uğurludur!")
# else:
#     print("İstifadəçi tapılmadı!")


# teatr = [
#     ["Boş", "Dolu", "Boş"],  # 1-ci sıra (Sıra 0)
#     ["Dolu", "Dolu", "Boş"], # 2-ci sıra (Sıra 1)
#     ["Boş", "Boş", "Dolu"]   # 3-cü sıra (Sıra 2)
# ]
#
# print(teatr[1][0])
# print(teatr[2][2])
#
# for sira in teatr:
#     for nomre in sira:
#         print(nomre, end=" ")
#     print()


# numuneler = [12, 7, 19, 24, 5, 10, 33, 50]
#
# x=[i for i in numuneler if i%2==0]
# x.sort()
# print(x)



# sahmat = [
#     ["A1", "B1"],
#     ["A2", "B2"]
# ]
#
# sahmat[1][1]="Sah"
# for row in sahmat:
#     print(row, end="")


# cumle = "python proqramlaşdırma dillərin ən populyarı hesab olunur"
# sozler=cumle.split()
# qisa_sozler=[]
# for x in sozler:
#     uzunluq= len(x)
#     print(f"{x}-{uzunluq}")
#
#     if uzunluq<3:
#         qisa_sozler.append(x)
# print(qisa_sozler)


# inventar = ["qılınc", "qalxan", "iksir"]
#
#
# while True:
#    soz = input("Zehmet olmasa qeyd yazin: bax/at/gotur/cix ")
#
#
#    if soz=="cix":
#        print("🎒 Macəra bitdi! Çantanız qorunub saxlanıldı.")
#        break
#    elif soz=="bax":
#        print(f"💼 Çantanızdakı əşyalar: {inventar}")
#        print(f"📊 Toplam əşya sayı: {len(inventar)}")
#
#    elif soz=="gotur":
#        yeni_esya=input("Yerden ne goturdun:").lower()
#        inventar.append(yeni_esya)
#        print(f"{yeni_esya}, elave olundu")
#    elif soz=="at":
#        silinen_esya=input("Zehmet olmasa atmaq istediyini yazin").lower()
#
#        if silinen_esya in inventar:
#            inventar.remove(silinen_esya)
#            print(f"🗑️ '{silinen_esya}' çantadan atıldı.")
#        else:
#            print(f"❌ Xəta: Çantanızda '{silinen_esya}' adında bir əşya yoxdur!")
#    else:
#        print("⚠️ Yanlış əmr! Zəhmət olmasa 'bax', 'at', 'götür' və ya 'çıx' yazın.")


# ballar = [45, 89, 100, 75, 100, 92, 89]
# unikal=set(ballar)
# unikal=list(ballar)
# unikal.sort()
# unikal.pop()
# print(unikal[-2])


#Ev tapsirigi

# qonaqlar = ["Aysel", "Məmməd", "Aysel", "Leyla", "Məmməd", "Kənan"]
# temiz_siyahi=[]
#
# for ad in qonaqlar:
#     print(ad)
#
#     if ad not in temiz_siyahi:
#         temiz_siyahi.append(ad)
#
#     else:
#         print(f"{ad} ad artiq siyahida var")



# xercler = [12, 15, 8, 20, 25, 30, 35]
# xercler2=xercler[-3:]
# orta_xerc=sum(xercler2)/len(xercler2)
# print(orta_xerc)
#
# if orta_xerc>25:
#     print("xeberdarliq")
# else:
#     print("normal")




# sebet = [15, 25, 40, 20]
# aktiv_kuponlar = ("YAY2026", "GƏNCƏ10", "XÜSUSİ")
# toplam=(sum(sebet))
# kupon_kodu=input("Zehmet olmasa kupin kodunu daxil edin")
#
# if kupon_kodu in aktiv_kuponlar:
#     faiz=toplam*0.1
#     toplam-=faiz
#     print("Endirimden sonraki qiymet", toplam)
#
# else:
#     print(toplam)


# filmler = ["Inception", "Avatar", "Amelie", "Gladiator", "Coco"]
# yeni_filmler=[]
#
# for film in filmler:
#
#     if len(film)<=5:
#         boyuk=film.upper()
#         yeni_filmler.append(boyuk)
#
# print("Orijinal siyahı:", filmler)
# print("Seçilmiş və böyüdülmüş filmlər:", yeni_filmler)



# ziyaretciler=[]
#
#
# while len(ziyaretciler)<3:
#     ad= input("Zehmet olmasa adi qeyd edin: ")
#     ziyaretciler.append(ad)
#     print(ziyaretciler)
#
# print("Qeydiyyat bitdi!")




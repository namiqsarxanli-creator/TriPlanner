from encodings import iso8859_3

# for i in range(10):
#     print(i)

#list

# meyve="alma"
# meyve2="nar"
# meyveler=["alma","nar","armud"]
#
# for meyve in meyveler:
#     print(meyve)

# reqemler=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for reqem in reqemler:
 # if reqem%2==0:
 #    print(reqem,"cutdur")
 # else:
 #    print(reqem,"tekdir")

# reqemler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# for reqem in reqemler:
#  if reqem==5:
#      break
#  print(reqem)

# meyveler=["alma","nar","armud"]
#
# for nomresi,meyve in enumerate (meyveler, start=1):
#     print(nomresi,meyve)

# a=2

# while a<5:
#     print(a)
#     a+=1

#task

# for i in range(1,11):
#     print(i)


# reqemler=[1,2,3,4,5,6,7,8,9,10]
#
# for i in reqemler:
#     if i%2!=0:
#         print(i)
#

# for i in range(1,6):
#     print(i*i)


# meyveler=["alma","armud","nar"]
#
# for i,meyve in enumerate(meyveler, start=1):
#     print(i,meyve)


# ededler=[4,7,2,-3,5,-1]
#
# for i in ededler:
#     if i<0:
#        print("Tapildi", i)
#        break

# ededler = [3, 0, 7, 0, 2, 0, 9]
#
# for i in ededler:
#     if i==0:
#         continue
#     print(i)

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)

# eded=int(input("Zehmet olmasa eded qeyd edin"))
#
# for i in range (1,eded):
#     if i%5==0:
#      print(i)


# qiymetler = [2, 5, 3]
# cemi_mebleg = 0
#
# for i in qiymetler:
#     cemi_mebleg+=i
# print("Toplam ödəniləcək məbləğ:", cemi_mebleg)


# eded=int(input("Zehmet olmasa eded qeyd edin"))
# cem=0
#
# for i in range(1,eded+1):
#   if i%2==0:
#     cem+=i
# print(f"Cem {cem}")


# rengler = ["Qırmızı", "Yaşıl", "Mavi"]
#
# for reng in rengler:
#     print(reng)

# reqemler = [12, 45, 7, 23, 9, 88, 31]
#
# for i in reqemler:
#     if i%2==1 and i>20:
#         break
# print("Sansli reqem tapildi", i)


# balanslar = [100, -20, 50, -5, 200, 0]
#
# for i in balanslar:
#     if i<0:
#         continue
#     print(i)

# eded=int(input("Zehmet olmasa bir eded qeyd edin"))
#
# for i in range(1,eded):
#     print(f"{i}-nin kubu {i**3}")

# qiymetler = [10, 20, 30, 40, 50]
#
# for i,qiymet in enumerate(qiymetler):
#    if i%2==0:
#        qiymet-=2
#    print("Mehsul",i,"yeni qiymet",qiymet)

# eded=1
# cem=0
#
# while eded<=10:
#     cem+=eded
#     eded+=1
# print("1-dən 10-a qədər ədədlərin cəmi:",cem)

#
# meyveler = ["Alma", "Banan", "Alça", "Portağal"]
#
# for meyve in meyveler:
#     print(meyve)
#     if meyve=="Alça":
#        print("Alca tapildi")


# for i in range(1,51):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     else:
#         print(i)


# cem=0
#
# for i in range(1,21):
#     if i%2==0:
#         cem=cem+i
# print(f"Cem, {cem}")

# balans=800
#
# while True:
#     giris=input("meblegi daxil edin (ve ya cix): ")
#     if giris== "cix":
#          print("ATM-den cixildi, sag olun")
#          break
#
#     mebleg=int(giris)
#
#     if mebleg>balans:
#         print("Balans kifayet etmir")
#     elif mebleg<=0:
#         print("Duzgun mebleg daxil edin")
#     else:
#         balans=balans-mebleg
#         print(f"Uğurlu! Yeni balansınız: {balans} AZN")


# balans=100
# ay=0
#
# while balans<=500:
#     ay+=1
#     faiz=balans*0.1
#     balans+=faiz
#     print(balans)
#
# print(f"Yekun nəticə: Pulun 500 AZN-i keçməsi üçün {ay} ay lazım oldu.")


# while True:
#
#     sifre=input("Girisde sifre teyin edin: ")
#
#     if len(sifre)<8:
#         print("Şifrə çox qısadır! Ən azı 8 simvol olmalıdır.")
#     elif "123" in sifre:
#         print("Şifrə çox sadədir! İçində '123' kombinasiyası ola bilməz.")
#     else:
#         print("Şifrə uğurla qeydə alındı!")
#         break


# sifre="secret123"
# kod=""
#
# while kod!=sifre:
#     kod = input("Sifrenizi teyin edin")
#
#     if kod!=sifre:
#         print("Yenidən cəhd edin")
#     else:
#         print("Giriş uğurludur")



# import random
#
# gizli_reqem=random.randint(1,25)
# cehd=3
#
# while cehd>0:
#     texmin=int(input("zehmet olmasa texmininizi yazin: "))
#
#     if texmin==gizli_reqem:
#         print("Duzgun tapdiniz")
#         break
#
#     elif texmin<gizli_reqem:
#         print("Daha boyuk")
#
#     else:
#         print("Daha boyuk")
#
#     cehd-=1
# print("Cehd sayiniz bitti")
#
# if cehd==0 and gizli_reqem!=texmin:
#     print(f"Cehd sayiniz bitti, gizli reqem {gizli_reqem} idi")




# reqem=[1,2,3,4]
# ikiq=[r*2 for r in reqem]
# print(ikiq)

# qiymet=[1,2,3],[4,5,6,],[7,8,9]
#
# print(qiymet[1][2])


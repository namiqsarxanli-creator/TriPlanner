# def salamlama(ad):
#     print("Salam",ad)
#
# salamlama("Eli")
# salamlama("Aynur")



# def salamlama():
#     return "Salam",ad
#
# salamlama()
# print(salamlama())



# def topla(a,b):
#     return a+b
# print(topla(3,4))



# def sahe(en,uzunluq):
#     sahe=en*uzunluq
#     return sahe
#
# print(sahe(5,5))




# def tek_cut(reqem):
#     if reqem%2==0:
#         return 'Cut'
#     else:
#         return "Tek"
#
# print(tek_cut(7))




# def max_eded(a,b,c,d):
#     return max(a,b,c,d)
# print(max_eded(1,2,3,4))


# def ad_soyad(ad,soyad):
#     return f"{ad} {soyad}"
# print(ad_soyad("ad","soyad"))



# def parol_yoxlama(parol):
#     if len(parol) >7:
#         return "Guclu parol"
#     else:
#         return "Zeif parol"
#
# print(parol_yoxlama("123"))






# from openai import OpenAI
#
#
# musteri=OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
#
# def sual_ver(sual):
#
#     cavab=musteri.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#                 "role":"user",
#                 "content":sual
#             }
#         ]
#     )
#     return cavab.choices[0].message.content
#
# cavab=sual_ver("Python nedir")
# print(cavab)




#Tasks

# def celsius_to_fahrenheit(c):
#         return c* 1.8 + 32
# print(celsius_to_fahrenheit(20))



# def suret_hesabla(km,saat):
#     return km/saat
#
# print(suret_hesabla(150,3))




# def kvadrat_hesabla(teref):
#     perimetr=4*teref
#     sahe=teref*teref
#     return perimetr,sahe
#
# print(kvadrat_hesabla(5))




# def yas_hesabla(doguldugu_il):
#     yas=2026-doguldugu_il
#     return yas
#
# print(yas_hesabla(1999))



# def usd_to_azn(mebleg):
#     mezenne=mebleg*1.7
#     return mezenne
#
# print(usd_to_azn(100))



# def hava_durumu(seher,temp):
#     return f"{seher} seherinde hazirda {temp} derece isti var"
#
# print(hava_durumu("baki",20))


# def email_yarat(ad,soyad):
#     return f"{ad}.{soyad}@company.com"
#
#
# print(email_yarat("namiq","sarxanli"))



# def faiz_tap(eded,faiz):
#     faiz=eded*faiz/100
#     return faiz
#
# print(faiz_tap(100,35))



# def yer_melumati(seher,olke):
#     return seher,olke
#
# print(yer_melumati("Paris","Fransa"))



# def eded_yoxla(eded):
#
#   if eded<0:
#       return "menfi"
#   elif eded>0:
#       return "musbet"
#   else:
#       return "sifir"
#
#
# print(eded_yoxla(5))




# def ortalam_tap(list):
#     cem=sum(list)
#     say=len(list)
#     return cem/say
# print(ortalam_tap([1,2,3,4,5]))



#
# def kecenleri_tap(bal):
#     kecenler=[]
#     for i in bal:
#         if i>51:
#             kecenler.append(i)
#     return kecenler
#
# print(kecenleri_tap([45, 60, 85, 30, 92]))




# def uzunluqlari_olc(siyahi):
#     uzunluqlar=[]
#     for soz in siyahi:
#         uzunluqlar.append(len(soz))
#     return uzunluqlar
#
# print(uzunluqlari_olc(["Python", "AI", "Code"]))




# def teqaud_hesabla(telebeler):
#     neticeler = {}
#     for ad, bal in telebeler.items():
#         if bal > 90:
#             status = "ÆlaÃ§Ä± TÉ™qaÃ¼dÃ¼"
#         elif bal >= 70:
#             status = "YarÄ±mÃ§Ä±q TÉ™qaÃ¼d"
#         else:
#             status = "TÉ™qaÃ¼d DÃ¼ÅŸmÃ¼r"
#         neticeler[ad] = status
#     return neticeler
#
# telebeler = {"Æli": 95, "Leyla": 82, "Murad": 60}
# print(teqaud_hesabla(telebeler))




#EvTapsirigi


#Task1


# def endirimi_hesabla(qiymet,faiz):
#     endirim=qiymet*faiz/100
#     yekun_qiymet=qiymet-endirim
#     return yekun_qiymet
#
# print(endirimi_hesabla(100,35))


#Task2

# def kubun_hecmi(teref):
#     hecm=teref*teref*teref
#     netice=f"3 olculu kubun hecmi: {hecm}"
#     return netice
#
# print(kubun_hecmi(5))


#Task3

# def soz_say(cumle):
#     soz=cumle.split()
#     return len(soz)
#
# print(soz_say("salam necesen"))


#Task4

# def bas_herfle_yaz(cumle):
#     sozler=[]
#     for soz in cumle:
#        sozler.append(soz.capitalize())
#     return sozler
#
# print(bas_herfle_yaz(["python", "sÃ¼ni", "intellekt"]))


#Task5

# def yasa_gore_salam(ad,soyad,yas):
#     if yas<18:
#         return f"Salam {ad} {soyad}, hÉ™lÉ™ yetkinlik yaÅŸÄ±na Ã§atmamÄ±san!"
#     elif yas>=65:
#         return f"Salam {ad} {soyad}, xoÅŸ gÉ™ldin"
#     else:
#         return f"HÃ¶rmÉ™tli {ad} {soyad}, xoÅŸ gÉ™ldiniz!"
#
# print(yasa_gore_salam("Murad", "Æliyev", 17))


# Task6

# def kalulyator(a,b,isare):
#     if isare=="+":
#         return a+b
#     elif isare=="-":
#         return a-b
#     elif isare=="*":
#         return a*b
#     elif isare=="/":
#         if b == 0:
#             return "XÉ™ta: SÄ±fÄ±ra bÃ¶lmÉ™k olmaz"
#         else:
#             return a / b
#     else:
#         return "Xeta"
#
#
#
# print(kalulyator(6,7,"*"))
# print(kalulyator(6,0,"/"))
# print(kalulyator(6,0,"a"))



#Task7

# def en_boyuk_element(ededler):
#     en_boyuk = max(ededler)
#     return f"SiyahÄ±dakÄ± É™n bÃ¶yÃ¼k É™dÉ™d: {en_boyuk}"
#
# print(en_boyuk_element([4, 17, 9, 3]))


#Task8

# def menfileri_tap(ededler):
#     menfiler=[]
#     for i in ededler:
#         if i <0:
#             menfiler.append(i)
#     return menfiler
#
# print(menfileri_tap([5,6,-2]))







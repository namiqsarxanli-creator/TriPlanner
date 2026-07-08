# mesaj=input("Sualinizi qeyd edin; ")
#
# while(True):
#
#  if "salam" in mesaj:
#     print("Salam, Restoranımıza xoş gəldiniz!")
#  elif "menyu" in mesaj:
#     print("Bu gün: plov, kabab, şorba")
#  elif "qiymet" in mesaj:
#     print("Orta çek 15 AZN-dir")
#  elif "sifaris" in mesaj:
#     print("Sifarişiniz qəbul edildi")
#     break
#  else:
#     print("Başa düşmədim, zəhmət olmasa yenidən yazın")
#     mesaj = input("Sualinizi qeyd edin; ")


# for sira_nomresi in range (11):
#     print(sira_nomresi)

# meyveler= ["alma","heyva","nar"]
#
# for meyve in meyveler:
#     print(meyve)


# import random
#
# zer1 = random.randint(1, 6)
# while (zer1 != 6):
#     print('Zer 1 :', zer1)
#     zer1 = random.randint(1, 6)
#
# print('Zer 1 :', zer1)
# print('Shesh Qosha')


# meyveler = ['alma','nar', 'gilas','alma','tut', 'gilas','feyxoa','nar', 'gilas']
#
# for sira_nomresi, meyve in enumerate(meyveler):
#     if meyve == 'feyxoa':
#         break
#     if meyve == 'tut':
#         continue
#     print(f' {meyve} {sira_nomresi + 1}')

#EvTapsirigi

# adlar  = ["Anar", "Leyla", "Rauf", "Günel", "Tural"]
# ballar = [72, 45, 88, 51, 38]
#
# for x,i in zip(adlar, ballar):
#     if i<50:
#         status = "Zəif ❌"
#         color="\033[91m"
#     else:
#         status = "Keçdi ✅"
#         color="\033[92m"
#
#     reset = "\033[0m"
#     print(f"{color}  {x:<8} {i:<5} → {status}  {reset}")
        
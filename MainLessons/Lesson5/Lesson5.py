#Ev tapsirigi

melumat={
    "Hava": "Hava durumunu deyir",
    "Tercume" : "Mətni tərcümə edir"
}

for acar,deyer in melumat.items():
    print(acar,"/ Is:",deyer)

print(melumat.get("musiqi","Bu alət yoxdur"))

melumat["axtaris"] = "İnternetdə axtarış edir"
print(melumat)


siyahi=["hava", "tercume", "hava", "axtaris"]
tekrarsiz=list(set(siyahi))
print(tekrarsiz)

# ------------------------------------------------

melumat={
    "hava": "Hava durumunu deyir",
    "tercume" : "Mətni tərcümə edir"
}

sual=input("Ne isteyirsen? ").lower()


tapildi=False

for acar,deyer in melumat.items():
    if acar in sual :
        print("Tapılan alət:", acar, "/ Is:",deyer)
        tapildi=True
if not tapildi:
        print("Uygun alet tapilmadi")
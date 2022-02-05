zırhlar = {"demir": 10,"çelik": 20}


karakterler = {
    "karakter1" : {"silah": "kılıç",
                   "güç": 30,
                   "sağlık": 100,
                   "zırh" :zırhlar["demir"]},

   "karakter2" : {"silah": "kılıç",
                   "güç": 30,
                   "sağlık": 100,
                   "zırh" :zırhlar["çelik"]}
}

def vur(saldiran,saldirilan):
    guc = saldiran["güç"]
    saglik = saldirilan["sağlık"]
    zırh = saldirilan["zırh"]
    damage = guc-zırh
    saglik -= damage
    saldirilan["sağlık"]= saglik

print(karakterler["karakter2"]["sağlık"])


vur(karakterler["karakter1"],karakterler["karakter2"])
print(karakterler["karakter2"]["sağlık"])




#Dictionary-Sözlük
#kapsayıcıdır, sırasız ve değiştirilebilirdir
#indexleme yok
#bir key bunun value değeri anahtar sözcük ve ona karşılık değer

#d={key : value
#   key2 : value2
#   key3 : value3}
d={"orange":"portakal","apple" : "elma"}
#4 eleman değil 2 eleman var
print(d)
print(len(d))

d2={"iclal": ["student",20],"hilal":["student",14]}
print(d["orange"]) #karşılığı olan portakalı bastırır
print(d2["iclal"])
print(d2["iclal"]+d2["hilal"])
#iki açıklamayı tek listede yazdım

#eleman ekleme :
d["pink"]="pembe"
print(d)
#değiştirmek için :
d["pink"]="pemberenk" #pink e baştan değer atıyor pembe yerine pemberenk
print(d)
d[2]="pemberenk"
print(d)

#string ve sayı sabit veri yapısı key olarak atanır ve değişmez aynı
#list i atayamam sabit değil list i key olarak yapamam
#tuple sabit olduğu için key yaparım
#sabitten anlattığım -> değiştirilemez

t="*"
d[t]="yıldız"
print(d)



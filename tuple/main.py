#tuple

t=("iclal","a",4,7,3)
t2="iclal","b",6,2
t3=("limon",) #tek elemanlı tuple da , eklenebilir
print(type(t))
print(t2)
#tuple değiştirilemez
#kapsayıcıdır farklı türde veri içerebilir
#sıralıdır(yani 0.index 1.index gibi)

print(t[0]) # -> 1. index
print(t[0:2])# 0.index ten 2.index e kadar olan

# değiştiremem tekrar 0.index i değiştirmeyi farklı değer atamayı denedim olmadı
#t[0]=7
#print(t)
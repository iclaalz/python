# listeler değiştirilebilir
# kapsayıcıdır yani farklı tipte verileri tutabilir
# listeler sıralıdır
# List deneme method 

numbers= [5,3,6,7,2]
print(numbers)
print(type(numbers))

list=['a',4,8,5.4]
print(list)

print(len(list))
print(type(list[3]))


list2=[numbers,list]
print(list2)

print(list2[1:2])

list3=['a',20,[34,76,32]]
print(list3)
print(list3[2][1])

list3[0]=10 #listenin 0.indexini degistirdim
print(list3)

list3[0:1]=5,7
print(list3)

list3[0:1]="b","c"  #degistirdi
print(list3)

list3=list3+[8] #8 i ekledi
print(list3)

del list3[4] #silme
print(list3)

print(dir(list3)) # liste metodlarını sıralar

#append metodu listeye eleman eklemek için kullanılır
list3.append("iclal")
print(list3)

#remove -> listeden eleman silmek için kullanılır
list3.remove("iclal")
print(list3)

#insert -> index e eleman ekliyor
#insert(eklenen index, eleman)
list3.insert(1,11)
print(list3)

print(len(list3))
list3.insert(7,3)
print(list3)

#listeden index ile eleman silmek için -> pop
list3.pop(1)
print(list3)

#count -> sayma metodu kaç tane oldugunu söyler
print(list3.count(5))
print(list3.count(3))

#copy metodu : listeyi kopyalamak ilk halini saklamak için falan
list3yedek=list.copy()
print(list3yedek)

#extend -> iki listeyi birleştirmek için
list3.extend(list3yedek) #list3 e list3yedek i ekledi
print(list3)

#bir eleman hangi indexte -> index
print(list3.index(4))

#reverse -> elemanı tersten yazar 0.index sonda gibi
list3.reverse()
print(list3)

#sort -> sıralama için
liste=[2,5,1,6,8]
print(liste)
liste.sort()
print(liste)

#clear -> listenin içindeki elemanların hepsini siler


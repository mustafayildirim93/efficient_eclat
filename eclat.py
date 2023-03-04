# # transaction database verilir
# transactions = {
#     1: ["item1", "item2"],
#     2: ["item2", "item3"],
#     3: ["item1", "item3"],
#     4: ["item1", "item2", "item3"],
#     5: ["item1", "item2"],
# }

file = open("itemset.txt", "r")
lines = file.readlines()
file.close()
transactions = {}
for row in lines: 
    row = row.replace("\n", "").replace(",", "")
    row_list = row.split()
    transactions[row_list[0]] = row_list[1:]


    


# destek değeri sorgulanmak istenen nesne kümesi verilir
query_input = input("support değerini sorgulamak istediğiniz itemseti giriniz\n")
query_set = query_input.split()


# transaction databasedeki her item için TidList oluşturulur
tid_list = {}
item_list = []

# transaction databasedeki her itemi tekrar etmeyen bir listeye atıyoruz. bunun yerine set de kullanılabilir
for items in transactions.values():
    for item in items:
        if item not in item_list:
            item_list.append(item)

# her item için görüldüğü Tid değerleri kaydedilir. döngü içerisinde list comprehension kullanılır 
for item in item_list:
    tid_list[item] = [tid for tid, items in transactions.items() if item in items]


#tid_listin son hali yazdırılır
print(tid_list)

# En az supporta sahip iki nesnenin TidListleri kullanılarak kesişimlerinden oluşan yeni bir TidList oluşturulur. intersection methodu set veri yapısı için kesişim 
# işlemi yapar
result_tid_list = set(tid_list[query_set[0]]).intersection(tid_list[query_set[1]])

# Bu işlem, sırasıyla daha sonraki en az desteğe sahip  itemsetin TidListi karşılaştırarak yeni bir TidList oluşturularak devam ettirilir
for item in query_set[2:]:
    result_tid_list = result_tid_list.intersection(tid_list[item])

# Son oluşan TidListin içindeki item sayısı ilgili itemsetin support değerini verecektir
support = len(result_tid_list)
# support değeri yazdırılır
print(support/len(transactions))
#birlikte görüldükleri kümeler yazdırılır
print(result_tid_list)

# f = open("test.txt","r",encoding="utf-8")
# line = f.readlines()
# aList = []
# for i in line:
#     newName = i.replace("rf","python")
#     aList.append(newName)
# f = open("test.txt","w",encoding="utf-8")
# for i in aList:
#     f.write(i)


def test(*itid,number=1):
    if number ==1:
        print("itid值是："+str(itid[0]))
    if number >1:
        list_list = []
        dict_list = {}
        for i in itid:
            dict_list["name"]=i
            list_list.append(dict_list.copy())

        print(list_list)








if __name__ == "__main__":
    test(12,56,number=2)
    pass



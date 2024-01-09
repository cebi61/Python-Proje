list_methods = []
for metod in dir(list):
    if metod.startswith("__"):
        continue
    list_methods.append(metod)




set_methods = []
for metod in dir(set):
    if metod.startswith("__"):
        continue
    set_methods.append(metod)



string_methods = []
for metod in dir(str):
    if metod.startswith("__"):
        continue
    string_methods.append(metod)




tuple_methods = []
for metod in dir(tuple):
    if metod.startswith("__"):
        continue
    tuple_methods.append(metod)



dict_methods = []
for metod in dir(dict):
    if metod.startswith("__"):
        continue
    dict_methods.append(metod)


basliklar = ["List Methods","Set Methods","String Methods","Tuple Methods","Dict Methods"]
classes = [list_methods,set_methods,string_methods,tuple_methods,dict_methods]

max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)

with open("Methods.txt","w") as f:
    for baslik in basliklar:
        print(baslik,end="")
        print(" "*(30-len(baslik)),end="") 
        f.write(baslik)
        f.write(" "* (30 - len(baslik)))
    for i in range(max_len):
        print()
        f.write("\n")
        for class_ in classes:
            if i >= len(class_):
                print("-------",end="")
                print(" " * 23,end="")
                f.write("-------")
                f.write(" " * 23)
            else:
                print(class_[i],end="")
                print("-------" * (30 - len(class_[i])),end="")
                f.write(class_[i])
                f.write(" " * (30 - len(class_[i])))
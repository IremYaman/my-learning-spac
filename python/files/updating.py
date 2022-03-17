# with open("newfile3.txt","r+",encoding="utf-8") as file:  #r+ hem okuma hem yazma modu
#     print(file.read())

# with open("newfile3.txt","r+",encoding="utf-8") as file:
#     file.seek(12)
#     print(file.write("güncelle"))

# with open("newfile3.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("newfile3.txt","a",encoding="utf-8") as file:
#     file.write("\nÜniversite")

# with open("newfile3.txt","r",encoding="utf-8") as file:
    # print(file.read())

# with open("newfile3.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Bilgisayar\n" + content
#     file.seek(0)
#     file.write(content)
    
# with open("newfile3.txt","r",encoding="utf-8") as file:
#     print(file.read())

with open("newfile3.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"İspanyolca\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)

with open("newfile3.txt","r",encoding="utf-8") as file:
    print(file.read())

with open("newfile.txt","r",encoding= "utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)              #seek ile kürsörün konumunu değiştiririz
    print(file.tell())        #tell kürsörün konumunu söyler
    content2 = file.read()    #bu şekilde dosyanın baştan okunmasını sağlayabiliriz
    print(content2)


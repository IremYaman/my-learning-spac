# "w": Write yazma modu
#       **dosyayı konumda oluşturur
#       **dosya içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w", encoding="utf-8")
# file.write("İrem Yaman")
# file.close()

# "a" Append ekleme modu
#       **dosya konumda yoksa oluşturur

# file = open("newfile.txt","a", encoding="utf-8")
# file.write("Mert Kuzu\n")
# file.close()

# "x" create oluşturma
#       **dosya zaten varsa hata verir

file = open("newfile2.txt","x", encoding="utf-8")
file.close()
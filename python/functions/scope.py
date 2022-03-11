x = "global x"
#glocal scope
def function():                        #fonksiyon içerisindeki değişimler aksi belirtilmediği takdirde fonksiyon içine özeldir.
    #local scope
    x = "local x"


function()
print(x)

##############

name = "Çınar"
def namechange(new_name):
    name = new_name
    print(name)

namechange("Ada")

##############

name = "unknown"
def greeting():
    name = "Mert"


    def hello():
        name = "İrem"                        #Sonuç İrem ile gelir 
        print(f"Hello, {name}")

    hello()

greeting()

##############

x = 50
def test():
    global x                                #global yazarak fonksiyon içerisindeki değişimlerin globolde değişmesini sağladık
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")


test()
print(x)

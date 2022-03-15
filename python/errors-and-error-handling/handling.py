while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as e:                                     #bu şekilde tüm hataları kabul ederiz ve hata türünü de tespit edebiliriz
        print("you entered something wrong: ", e)
    # except:                                                  #bu şekilde tüm hataları kabul ederiz ama hata türünü tespit edemeyiz
    #     print("you entered something wrong")
    # except (ZeroDivisionError,ValueError) as e:              #bu şekilde de yazılabilir
    #     print("you entered something wrong")                 #as ...  hangi değerde hata olduğunu tespit etmemizi sağlar
    #     print(e)
    # except ZeroDivisionError:
    #     print("y can't be 0")
    # except ValueError:
    #     print("you have to enter numbers")
    else:
        break
    finally:
        print("try except ended")
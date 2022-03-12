class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    #SPECIAL METHOD 
    def __str__(self):              
        return f"Name of the movie: {self.title}, movie's director: {self.director}, duration: {self.duration}"

    def __len__(self):
        return self.duration

    
    def __del__(self):
        print("This movie has been deleted. ")


m = Movie("Dune", "Denis Villeneuve", 155)

print(str(m))
print(len(m)) #it has to be integer and it is not enough to only use the special method and return the value. You have to print it with a len command.
del m #even if you dont delete m like this, it will be deleted automaticly and __del__ method will print whatever you've wrote inside of it to terminal.
print(m) 






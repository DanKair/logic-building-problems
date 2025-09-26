"""class Book:
    def __init__(self, title, author, pages, read_pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read_pages = read_pages

    def read(self, pages: int):
        self.read_pages += pages
        if self.read_pages > self.pages:
            self.read_pages = self.pages  # prevent over-reading

    def progress(self):
        return round((self.read_pages / self.pages) * 100, 2)
    
    def restart(self):
        self.read_pages = 0
        return f"Your progress is now: {self.read_pages} read pages"

    def __str__(self):
        return f"{self.title} by {self.author} ({self.read_pages}/{self.pages} read)"              

obj1 = Book("Harry Poter", "J.K Rowling", 300, 120) 
print(obj1)
print(obj1.progress())
print(obj1.restart())  
print(obj1) 
"""

"""class Movie:
    def __init__(self, title, director, duration_minutes, watched_minutes):
        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes
        self.watched_minutes = watched_minutes

    def watch(self, minutes: int):
        self.watched_minutes += minutes
        if self.duration_minutes < self.watched_minutes:
            self.watched_minutes = self.duration_minutes
            return "You've reached the end of the movie."

    def progress(self):
        return round((self.watched_minutes / self.duration_minutes) * 100, 2)             

    def __str__(self):
        return f"{self.title} by {self.director} ({self.watched_minutes}/{self.duration_minutes} minutes watched) " 

obj1 = Movie("Interstellar", "Christopher Nolan", 180, 110)  
print(obj1)  
print(obj1.watch(80)) 
print(obj1)  """  

"""class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def info(self):
        return f"Brand: {self.brand}\nMax Speed: {self.max_speed} km/h"        

    def __str__(self):
        return f"Vehicle from brand: {self.brand} with max speed: {self.max_speed} km/h" 

class Car(Vehicle):
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
    
    def info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nMax Speed: {self.max_speed} km/h"

class Bike(Vehicle):
    def __init__(self, brand, engine_ecc, max_speed):
        self.brand = brand
        self.engine = engine_ecc
        self.max_speed = max_speed
    
    def info(self):
        return f"Brand: {self.brand}\nEngine: {self.engine}\nMax Speed: {self.max_speed} km/h"    """               



class Person:
    number_of_people = 0

    def __init__(self, name, age, skills: list):
        self.name = name
        self.age = age
        self.skills = skills
        Person.person_created()
        # alternative for person_created() method
        # Person.number_of_people += 1
    
    def show_skills(self):
        return self.skills
    
    def add_skills(self, skill: str):
        self.skills.append(skill)

    @classmethod
    def person_created(cls):
        cls.number_of_people += 1

p1 = Person("John", 36, ["driving","cooking","marketing"])

print(p1.name)
print(p1.age)
print(p1.skills)
print(p1.add_skills("coding"))
print(p1.show_skills())
print(p1.number_of_people)
p1.person_created()
print(p1.number_of_people)

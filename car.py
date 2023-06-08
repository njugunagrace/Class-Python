class Car:
    wheels=4
    def __init__(self,make,model,color,year,speed):
        self.make=make
        self.model=model
        self.color=color
        self.year=year
        self.speed=speed
        
   
    def age_of_car(self):
        age= 2023-self.year 
        return f"The car is {age} years old" 
    def distance_covered(self,time):
        distance=self.speed*time
        return f"the car covered a distance of {distance} km" 
    def description_of_car(self):
        return f"This is a {self.make} {self.model} and it's a {self.color} in color"
    
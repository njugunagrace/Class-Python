#The ever changing ankara: you are a fashion designer known for your unique and vibrant ankara designs. recently you've discovered that some of your fabric patterns change their designs based on the temperature and mood of the wearer. 
# you want to create a software application that can predict the changes in the fabric design given the mood and temperature data. think about the classes you will need to model the changing ankara and how to predict the changes

class Ankara:
    def __init__(self,pattern,color):
        self.pattern=pattern
        self.color=color
    def update_design(self,mood): 
        if mood>=5:
            return f"${self.color} is the new update"
        else:
            return f"${self.color} is the new update"

class Temperature:
    def __init__(self,value,unit):  
        self.value=value
        self.unit=unit
    def predict_temperature(self):
        if self.value>25:
            return f"${self.value} is too hot for heavy clothes"
        elif self.value==25:
            return f"${self.value} is optimal for non-heavy and too light clothes"
        else:
            return f"${self.value} is the too  cold for light clothes"\
                

#the Great migration forecast: Every year millions of wildbeaast, zebras and other animals participate in the great migration across the serengeti-mara ecosystem. as a conservationist, you want to develop a software system 
# that models this migration, predicting the movement of the herds based on weather patterns, river levels and the animals, the environment and the various factors that influence the migration       

class Migration:
    def __init__(self,species,age,speed,currentLocation):
        self.species=species
        self.age=age
        self.speed=speed
        self.currentLocation=currentLocation
    def move(self):
        if self.speed>=70:
            return f"It will take less time for ${self.species} to migrate"
    
        else:
            return f"It will take more time for ${self.species} to migrate"

     
    def makeDecision(self):
        if self.currentLocation=="cold" and "hot"
            return f"${self.species} are likely to migrate"
        else:
            return f"${self.species} are unlikely to migrate"
   
    def interactWithEnvironment(self,env):
        if env=="dangerous" and "scarcity of food":
            return f"${self.species} are likely to migrate"
    
        else:
            return f"${self.species} are unlikely to migrate"

class River:
    def __init__(self,waterLevel,flowRate){
        self.waterLevel=waterLevel
        self.flowRate=flowRate
    }
    def riverChanges(self):
        if self.waterLevel>=50 and self.flowRate=="rushy":
            return f"${self.species} are unlikely to migrate"

        
        else:
            return f"${self.species} are likely to migrate"

    

#Nollywood movie planner:As a producer in the booming nollywood movie industry, you are in charge of multiple film projects at once.each movie has different cast members, shooting schedules and budgets.
#you want to write a program to help manage your film projects efficiently. the software should be able to handle the complexities of scheduling, budgeting and coordinating between different movie projects.


        

    

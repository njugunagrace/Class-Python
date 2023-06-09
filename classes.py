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
        if self.currentLocation=="cold" and self.currentLocation=="hot":
            return f"${self.species} are likely to migrate"
        else:
            return f"${self.species} are unlikely to migrate"
   
    def interactWithEnvironment(self,env):
        if env=="dangerous" and "scarcity of food":
            return f"${self.species} are likely to migrate"
    
        else:
            return f"${self.species} are unlikely to migrate"

class River:
    def __init__(self,waterLevel,flowRate):
        self.waterLevel=waterLevel
        self.flowRate=flowRate
    
    def riverChanges(self):
        if self.waterLevel>=50 and self.flowRate=="rushy":
            return f"${self.species} are unlikely to migrate"

        
        else:
            return f"${self.species} are likely to migrate"

    

#Nollywood movie planner:As a producer in the booming nollywood movie industry, you are in charge of multiple film projects at once.each movie has different cast members, shooting schedules and budgets.
#you want to write a program to help manage your film projects efficiently. the software should be able to handle the complexities of scheduling, budgeting and coordinating between different movie projects.

class Nollywood:
    def __init__(self,title,cast_members,shooting_schedule,budget):
        self.title=title
        self.cast_memebers=cast_members
        self.shooting_schedule=shooting_schedule
        self.budget=budget
        
    def update_shooting_schedule(self,schedule): 
        self.shooting_schedule=schedule  
        
    def update_budget(self,budget):
        self.budget=budget
        
class Film_Project_Manager:
    def __init__(self): 
        self.projects=[]   
    
    def add_project(self,project):
        self.projects.append(project)
    
    def remove_project(self,project):
        self.projects.remove(project)   
   
    def get_project(self): 
        return self.projects
    
project_manager = Film_Project_Manager()

project1 = Nollywood("Movie 1", ["Actor 1", "Actor 2"], "Schedule 1", 120000)
project2 = Nollywood("Movie 2", ["Actor 3", "Actor 4"], "Schedule 2", 250000)

project_manager.add_project(project1)
project_manager.add_project(project2)

print(project_manager.get_project())  


#the magical baobab: in a small village , there is a baobab tree believed to have magical properties . every season , it bears different types of fruits , each with its own unique power. 
#you've decided to create a software system that tracks the changes in the tree and predicts what type of fruit will bear next season and what powers it will possess. the system should also record the effect of each fruit when consumed.
    
class Fruit:
    def __init__(self, type, power, effect):
        self.type = type
        self.power = power
        self.effect = effect

fruit1 = Fruit("Fruit 1", "Power 1", "Effect 1")
fruit2 = Fruit("Fruit 2", "Power 2", "Effect 2")

data_base=[]
data_base.append(fruit1)
data_base.append(fruit2)

class BaobabTree:
    def __init__(self):
        self.fruits = []
    
    def add_fruit(self, fruit):
        self.fruits.append(fruit)
    
    def predict_next_fruit(self):
        
      
        return predicted_fruit

baobab_tree = BaobabTree()


baobab_tree.add_fruit(fruit1)
baobab_tree.add_fruit(fruit2)

predicted_fruit = baobab_tree.predict_next_fruit()
print(predicted_fruit)
    
  
 #The legendary african drum circles: you're a part of a community that hosts one of the largest drum circles , each with its unique sound and rhythm. the Djembe, talking drum and bougarabou are among the popular ones. 
 # these drums have common properties such as the material they're made from and their sizes , but they also have distinct characteristics. for instance, the talking drum can mimic the lines of human speech, 
 # the djembe is known for its wide range of tones, and the bougarabou is noted for its deep rich bass tones. you want to create a sofware application model of the drum circle that encapsulates these different types of drums.
 # you wish to include methods for each drum that represent the sound it makes, and also group similar drums together. think about creating a base drum class that contains properties and methods common to all drums and then
 # create subclasses for each specific type of drum (like Djembe,talkingDrum and baogarabou). the subclasses should inherit from the base drum class and also implement their unique characteristics. this software model would help newcomers understand the characteristics of each drum and how they conribute to the overall rhythm of the drum cicle             
 
 
class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size

    def make_sound(self,tone):
        return f"The drum produces ${tone}"
        

class Djembe(Drum):
    # def __init__(self, material, size):
    #     super().__init__(material, size)

    def make_sound(self,tone):
        return f"The drum produces ${tone}"

class TalkingDrum(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)

    def make_sound(self,tone):
        return f"The drum produces ${tone}"

class Bougarabou(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)

    def make_sound(self,tone):
        return f"The drum produces ${tone}"

djembe = Djembe("Wood", "Medium")
talking_drum= TalkingDrum("Leather", "Large")
bougarabou = Bougarabou("Wood", "Large")

djembe.make_sound()
talking_drum.make_sound()
bougarabou.make_sound()
   

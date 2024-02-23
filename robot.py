class Robot:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print("Initialization {0}".format(self.name))
        Robot.population += 1
    
    def __del__(self):
        print(f"{self.name} destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was last")
        else:
            print("Still {0} robots".format(Robot.population))
    
    def say_hi(self):
        print("Hello! My name is {0}".format(self.name))
    
    def how_many():
        print("This planet has {0} robots.".format(Robot.population))
droid = Robot( "R2D2" )
Robot.how_many()
droid2 = Robot ("C3PO")
Robot.how_many()
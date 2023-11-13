# *** WRITE THIS CODE IN NOTEPAD ***
#  This package should have individual classes for Rectangle, Square, Circle, Cylinder, Sphere
#  These classes should use inheritance to properly manage the code!
#  Include methods like volume, surface area and getters/setters for dimensions

class Baseclass:
    def volume(self):
        pass

    def surface_area(self):
        pass

class Derived1(Baseclass):
    pass


class Derived2(Baseclass):
    pass


class Derived3(Derived1, Derived2):
    pass


from shutil import copyfile

copyfile("C:/Users/Dynamo/Desktop/form/new.txt", "C:/Users/Dynamo/Desktop/form/old.txt")

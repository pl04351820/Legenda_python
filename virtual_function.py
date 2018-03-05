from abc import ABCMeta, abstractmethod  
  
  
class Base():  
    # __metaclass__ = ABCMeta  
  
    def __init__(self):  
        pass  
 
    @abstractmethod  
    def get(self):  
        print ("Base.get()")  
        pass  
  
  
class Derive1(Base):  
    def get(self):  
        print ("Derive1.get()")
  
  
class Derive2(Base):  
    def get(self):  
        print ("Derive2.get()")
  
  
if __name__ == '__main__':  
    b = Derive1()
    b.get()

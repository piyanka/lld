from abc import ABC, abstractmethod

class Chair(ABC):

    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):

    @abstractmethod
    def lie_on(self):
        pass


class ModernChair(Chair):

    def sit_on(self):
        return "Sitting on Modern Chair"
    
class ModernSofa(Sofa):

    def lie_on(self):
        return "Lieing  on Modern Sofa"
    


class VictoriaChair(Chair):

    def sit_on(self):
        return "Sitting on Victoria Chair"
    
class victoriaSofa(Sofa):

    def lie_on(self):
        return "Sitting on Victoria sofa"
        


class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass



class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()


    def create_sofa(self):
        return ModernSofa()
    


class VictoriaFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return VictoriaChair()


    def create_sofa(self):
        return victoriaSofa()  



def get_furniture(factory: FurnitureFactory):
    chair = factory.create_chair() 
    sofa = factory.create_sofa()


    print(chair.sit_on())
    print(sofa.lie_on())


print("Modern Furniture")
get_furniture(ModernFurnitureFactory())

print("Victoria Furniture")
get_furniture(VictoriaFurnitureFactory())
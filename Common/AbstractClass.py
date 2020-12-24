from abc import ABCMeta,abstractclassmethod


class AbstractWindowComponents(metaclass=ABCMeta):
    @abstractclassmethod
    def draw(cls,*args):
        pass

    @abstractclassmethod
    def set_location(cls,location):
        pass


class InterfaceState(metaclass=ABCMeta):
    name = 'state'

    @abstractclassmethod
    def show(cls,*args):
        pass

    def __str__(self):
        return self.name


class Server(metaclass=ABCMeta):
    @abstractclassmethod
    def receive(cls,request):
        pass


from abc import ABCMeta,abstractclassmethod


class AbstractWindowComponents(metaclass=ABCMeta):
    @abstractclassmethod
    def draw(cls, screen):
        pass

    @abstractclassmethod
    def set_location(cls,location):
        pass


# Frame 必须继承自AbstractFrame 且必须实现show方法，传入参数必须是window_size
class AbstractFrame(metaclass=ABCMeta):

    @abstractclassmethod
    def show(cls,screen,clock):
        pass


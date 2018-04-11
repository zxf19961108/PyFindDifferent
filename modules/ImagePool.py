import pygame
class ImagePool:
    __instance=None
    def __new__(cls, *args, **kwargs):
        #单例模式
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        #初始化图片池
        self.uiPool=[]
        self.bg=None

        t1 = pygame.image.load("res/btn0.png").convert_alpha()  #按钮
        t2 = pygame.image.load("res/btn1.png").convert_alpha()  #按钮
        t3=pygame.image.load("res/bg.jpg")
        self.uiPool.append(t1)
        self.uiPool.append(t2)
        self.bg=t3

    def drawBg(self,destSuf):
        destSuf.blit(self.bg, [0,0])
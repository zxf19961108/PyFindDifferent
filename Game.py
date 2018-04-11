import pygame,sys
from modules.ImagePool import *
from modules.Button import *

class Game:
    def __init__(self):
        #引擎初始化
        pygame.init()
        #设置窗口大小以及标题
        self.screen = pygame.display.set_caption('找不同')
        self.screen = pygame.display.set_mode([1024, 768])
        #初始化图片池
        self.imgPool=ImagePool()
        #创建一个按钮
        self.btn=Button(100,100,200,200,"",0,1,1,None)
        #游戏主循环
        self.mainLoop()
        #游戏结束清理资源
        pass

    def mainLoop(self):
        # 游戏循环
        while True:
            # FPS=60
            pygame.time.delay(16)
            #事件处理
            self.inputLogic()
            # 逻辑更新
            self.logicUpdate()
            # 显示更新
            self.viewUpdate()
            # 清理游戏资源
            pass

    def viewUpdate(self):
        self.imgPool.drawBg(self.screen)
        self.btn.draw(self.screen)
        pygame.display.flip()
        pass

    def logicUpdate(self):
        pass

    def inputLogic(self):
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEMOTION:
                self.btn.colli(*pygame.mouse.get_pos())
        pass

if __name__ == '__main__':
    Game()
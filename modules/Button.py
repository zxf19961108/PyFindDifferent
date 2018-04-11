from modules.ImagePool import ImagePool

class Button:
    NORMAL=0
    MOVE=1
    DOWN=2
    def __init__(self,x,y,w,h,text,imgNormalId,imgMoveId,imgDownId,callBackFunc):
        #引用图片池（单例）
        self.imgPool=ImagePool()
        #初始化按钮相关属性
        self.imgsId=[]
        self.imgsId.append(imgNormalId)     #普通状态显示的图片
        self.imgsId.append(imgMoveId)       #被选中时显示的图片
        self.imgsId.append(imgDownId)       #被按下时的图片
        self.callBackFunc=callBackFunc      #触发事件
        self.status=Button.NORMAL       #按钮当前状态
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def draw(self,destSuf):
        destSuf.blit(self.imgPool.uiPool[self.imgsId[self.status]], [self.x, self.y])

    def colli(self,x,y):
        #碰撞检测
        if self.x<x<self.x+self.w and self.y<y<self.y+self.h:
            self.status=Button.MOVE
        else:
            self.status = Button.NORMAL
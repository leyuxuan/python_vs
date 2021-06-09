from tkinter import *
from PIL import Image,ImageTk,ImageSequence
from tkinter import ttk
from tool import merge_face
import random
import threading
import time

pool = [
    "./image/惊悚.png",
    "./image/难过.png",
    "./image/无表情.png",
    "./image/呆.png",
    "./image/高兴.png",
    "./image/气愤.png",
    "./image/悲伤.png",
    "./image/生气.png",
]

class Ui():

    def __init__(self,path1,path2):
        """
        初始化函数
        - 图片文件
        - 主窗口
        - 窗口运行状态
        """
        self.__path_1 = path1
        self.__path_2 = path2
        self.__main_window = None
        self.__top_window = None
        self.__image_area = None
        self.__button_status = False
        self.result_path = None
        # 展示窗体的高度与宽度
        self.window_size = [300,400]
        # 请求是否返回成功
        self.__showFlag = False

    def __create_window(self):
        """
        创建主窗口及设置相关默认参数
        - 主窗口
        - 窗口标题
        - 窗口尺寸及位置
        - 窗口是否可以自由变化
        """
        self.__window = Tk()
        self.__window.title("人脸融合")                # 窗口标题
        self.__window.geometry('800x600+200+100')   # 窗口大小
        self.__window.configure(bg="lightblue")   # 窗口背景颜色
        self.__window.resizable(0,0)              # 防止用户修改窗口尺寸
        self.__window.attributes('-alpha', 1.0)


    def background(self):
        """
        绘制背景图片
        """
        self.bg = self.get_image("image/bg.png")
        # label文件绘制
        self.__main_window = Canvas(self.__window,width=800, height=600)
        self.__main_window.create_image(0, 0, image=self.bg, anchor='nw')
        self.__main_window.pack(fill="both",expand=True)

    def deafault_decoration(self):
        """
        界面默认装饰
        """
        # 读取图片问价
        self.part = self.get_image("./image/无表情.png")
        self.__main_window.create_image(97, 52, image=self.part, anchor='center')

    def decoration(self):
        """
        图案随机改变
        - TODO: 随机切换图案|容器切换
        """
        # 读取图片
        path = random.choice(pool)
        self.part = self.get_image(path)
        self.__main_window.create_image(97, 52, image=self.part, anchor='center')

    def get_image(self,path):
        """
        读取图片并转化为TK可以使用的对象(工具函数)
        - 或进行基础的图片转换
        """
        # 读取图片(图片路径)
        im =  Image.open(path)
        image  = ImageTk.PhotoImage(im)
        return image

    def get_icons(self):
        """
        读取装饰素材文件
        """
        self.pool = list()


    def read_image(self,path):
        """
        读取图片并转化为TK可以使用的对象
        - 或进行基础的图片转换
        """
        # 读取图片(图片路径)
        im =  Image.open(path)
        # 获取图片的尺寸
        width, height = im.width , im.height
        # 计算图片的窗框比()
        rate = width/height
        if rate > 1:
            im_resized = im.resize((self.window_size[0], int(self.window_size[0]/rate)))
        elif rate < 1:
            im_resized = im.resize((int(self.window_size[1]*rate),self.window_size[1]))
        else:
            im_resized = im.resize((self.window_size[0],self.window_size[0]))
        # 转换图像类型
        image  = ImageTk.PhotoImage(im_resized)

        return image

    def __create_image_area(self):
        """
        # 照片显示区【左右两张图片】+ 中间的图标
        - 图片显示区域
        - 控件: frame + label
        """
        # 加载图片
        self.image_1 = self.read_image(self.__path_1)
        self.image_2 = self.read_image(self.__path_2)
        # 创建显示区域
        self.__image_area = LabelFrame(self.__main_window,bg="lightblue",borderwidth=0)

        # 尺寸由图片尺寸决定
        image_one = Label(self.__image_area,bg="lightyellow",image=self.image_1,width=self.window_size[0],height=self.window_size[1],borderwidth=4.5)
        image_two = Label(self.__image_area,bg="lightyellow",image=self.image_2,width=self.window_size[0],height=self.window_size[1],borderwidth=4.5)

        image_one.pack(side="left",padx=30,fill="both",expand=True)
        image_two.pack(side="left",padx=30,fill="both",expand=True)

        # 填充父容器及与父容器之间的间距
        self.__image_area.place(x=28,y=105)

    def __button(self):
        """
        # 点击按钮【点击融合】
        - 点击融合按钮
        - 控件: button
        """
        self.image  = self.get_image("./image/btn.png")
        self.btn = Button(self.__main_window,
                            image=self.image,
                            command=self.show_result,
                            relief="groove",
                            #  relief="flat",bd = 0
                            )

        self.btn.place(x=300,y=525)

    def close(self):
        # 设置显示标识为不显示
        self.__showFlag = False

    def request(self):
        """
        发送网络请求
        """
        print("融合中")
        # # 人脸融合
        data = merge_face(self.__path_1, self.__path_2)
        # - TODO: 文件名称修改
        with open('image/med.png','wb') as file:
            file.write(data)
        # 请求完成
        self.close()
        # 状态控制
        self.__showFlag = True
        print("融合完成")


    def create_topwindow(self,width,height,title):
        """
        创建顶部显示窗口
        - 点击就是刷新
        """
        # 绘制图案
        self.decoration()

        # 点击销毁窗口后，再新生成窗口
        if self.__top_window:
            self.__top_window.destroy()

        # 创建窗口
        self.__top_window = Toplevel()

        # 设置位置及尺寸
        self.__top_window.geometry('{}x{}+1000+100'.format(width,height))
        # 窗口名称
        self.__top_window.title(title)
        # 窗口是否可以伸缩变换
        self.__top_window.resizable(0,0)

    def show_result(self):
        """
        等待窗口及最终窗口
        """
        if self.__top_window is None:
            # 开启新线程保持滚动条显示
            t = threading.Thread(target=self.request)
            t.setDaemon(True)
            t.start()

        # 点击销毁窗口后，再新生成窗口
        if self.__top_window:
            self.__top_window.destroy()

        # 循环等待
        while not self.__showFlag:
            """ 动图循环等待 """
            for path in pool:
                # 配置图片
                self.part = self.get_image(path)
                self.__main_window.create_image(97, 52, image=self.part, anchor='center')
                time.sleep(0.2)
                self.__main_window.update_idletasks()  #刷新
                self.__main_window.update()
                if self.__showFlag:
                    break

        if self.__showFlag:
            if self.result_path:
                self.eye = self.read_image(self.result_path)
                width = self.eye.width()
                height = self.eye.height()
                # 直接创建窗口及画布
                self.create_topwindow(width,height,"融合结果")
                self.picture = Canvas(self.__top_window,bg='white',width=width,height=height)
                self.picture.place(x=0,y=0)
                self.picture.create_image((3,3),anchor="nw",image=self.eye)

    def set_result_path(self,path):
        """
        设置返回结果 path
        - TODO: 程序内部固定
        """
        self.result_path =  path

    def __quit(self):
        """status"""
        sys.exit()

    def show(self):
        """
        显示所有控件
        - 层层初始化并执行
        """
        # 创建窗口
        self.__create_window()
        # 添加背景图片
        self.background()
        # 创建图形显示区域
        self.__create_image_area()
        # 创建按钮
        self.__button()
        # 默认图案
        self.deafault_decoration()
        # 循环显示
        self.__window.protocol("WM_DELETE_WINDOW",self.__quit)
        self.__window.mainloop()

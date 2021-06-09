import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import warnings
import requests as r
import os
print('正在准备中...')
ss = '''海拔,温度
697,15.3
3103,0.8
1597,9.9
777,14.8
2261,5.9
840,14.4
2921,1.9
577,16.0
2741,3.0
3094,0.9
2973,1.6
713,15.2
1115,12.8
1241,12.0
519,16.3
3200,0.2
2192,6.3
3040,1.2
2939,1.8
2559,4.1
1385,11.1
616,15.7
1307,11.6
3089,0.9
2569,4.0
2048,7.2
1710,9.2
3429,-1.1
2781,2.8
609,15.8
2052,7.1
692,15.3
2211,6.2
3171,0.4
2801,2.6
1404,11.0
1436,10.8
1748,9.0
2470,4.6
1360,11.3
3160,0.5
3414,-1.0
1896,8.1
2617,3.7
767,14.8
3291,-0.3
1791,8.7
1694,9.3
2849,2.3
2037,7.2
1294,11.7
2375,5.2
1497,10.5
2696,3.3
3131,0.7
1829,8.5
500,16.4
598,15.9
3032,1.2
2523,4.3
2261,5.9
936,13.8
1575,10.0
2483,4.5
2372,5.2
604,15.8
2335,5.4
1056,13.1
3363,-0.7
2961,1.7
1584,9.9
710,15.2
1451,10.7
2767,2.8
2287,5.7
2743,3.0
2251,5.9
3194,0.3
2535,4.2
3336,-0.6
2206,6.2
2994,1.5
1000,13.4
2146,6.6
1923,7.9
3217,0.1
1947,7.8
1192,12.3
2241,6.0
881,14.2
1114,12.8
810,14.6
1020,13.3
1402,11.0
619,15.7
3457,-1.3
637,15.6
2727,3.1
2458,4.7
3392,-0.9
'''

def get_file():
    os.makedirs('image',exist_ok = True)
    x = 'https://my.xiguacity.cn/18240783/5efeeb89f19b2f6e0cae48a1/'
    for s in range(2):
        img1 = r.get(x + '1.gif')
        img2 = r.get(x + '2.gif')
        img3 = r.get(x + '3.gif')
        img4 = r.get(x + '4.gif')
        img5 = r.get(x + '5.gif')
        img6 = r.get(x + 'bg_.png')
    with open("image/1.gif",'wb') as f:
        f.write(img1.content)
    with open("image/2.gif",'wb') as f:
        f.write(img2.content)
    with open("image/3.gif",'wb') as f:
        f.write(img3.content)
    with open("image/4.gif",'wb') as f:
        f.write(img4.content)
    with open("image/5.gif",'wb') as f:
        f.write(img5.content)
    with open("image/bg_.png",'wb') as f:
        f.write(img6.content)
    with open('海拔温度数据.csv', 'w') as file_object:
        file_object.write(ss)
get_file()


warnings.filterwarnings("ignore")
platform = sys.platform
if "darwin" in platform:
    plt.rcParams['font.family'] = ['Hiragino Sans GB']
else:
    plt.rcParams['font.family'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
# 绘制图形
def draw_line(trainer):
    # 模拟数据
    x = np.random.randint(500,9000,100,int)
    y = trainer.coef_[0][0] * x + trainer.intercept_[0]
    # 预测连线
    plt.plot(x, y, label='真实值', color='r')
    # # 添加附属信息
    plt.xlabel('海拔(m)')
    plt.ylabel('温度(℃)')
    plt.title("温度预测")
    # plt.grid()
    # plt.show()
    plt.savefig('预测.png')


from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

# 判断图片路径
image_pool = [
    "image/1.gif",
    "image/2.gif",
    "image/3.gif",
    "image/4.gif",
    "image/5.gif",
]

class Ui():

    def __init__(self,model):
        """
        初始化函数
        - 图片文件
        - 主窗口
        - 窗口运行状态
        """
        self.__main_window = None
        self.__top_window = None
        self.__image_area = None
        # 获取模型核心信息
        self.model_intercept_ = model.intercept_[0]
        self.model_coef_ = model.coef_[0][0]
        self.image_path = image_pool[0]
        self.status = True

    def __create_window(self):
        """
        创建主窗口及设置相关默认参数
        - 主窗口
        - 窗口标题
        - 窗口尺寸及位置
        - 窗口是否可以自由变化
        """
        self.__main_window = Tk()
        self.__main_window.title("登山小助手")               # 窗口标题
        self.__main_window.geometry('411x731+300+50')   # 窗口大小
        self.__main_window.configure(bg="lightblue")   # 窗口背景颜色
        self.__main_window.resizable(0,0)            # 防止用户修改窗口尺寸
        self.input_ = StringVar()
        # 计算结果
        self.__result =  StringVar()
        self.__result.set("提示:输入海拔数据")

    def background(self):
        """
        绘制背景图片
        """
        self.bg = self.read_image("image/bg_.png")
        self.__panel = Label(self.__main_window, image=self.bg)
        self.__panel.pack(side='top', fill='both', expand='yes')

    def change_picture(self,path):
        """
        改变背景图片
        - 默认原始图片大小
        """
        self.img = self.read_image(path)
        self.image_path = path
        # self.img = path
        # TODO:改变对应的变量
        # self.picture.config(image=self.img)

    def read_image(self,path):
        """
        读取图片并转化为TK可以使用的对象(工具函数)
        - 或进行基础的图片转换
        """
        # 读取图片(图片路径)
        im =  Image.open(path)
        image  = ImageTk.PhotoImage(im)
        return image

    def handler(self):
        """
        判断输入数据是否合理
        - 判断数据
        """
        # 判断输入是否为数值类型（删除空格及数值类型转换）
        # 数据判断及结果返回
        # print(self.input_.get())
        try:
            if float(self.input_.get()) < 0:
                self.__result.set("请输入大于0的数字")
            elif float(self.input_.get()) < 9000:
                # 计算结果
                res = self.model_intercept_ + float(self.input_.get()) * self.model_coef_
                fal_res = "海拔: {}米\n温度约为: {}℃".format(self.input_.get(),round(res,2))
                # 输出数据（展示数据）
                self.__result.set(fal_res)
                # 切换
                if float(self.input_.get()) < 1000:
                    self.change_picture(image_pool[1])
                elif float(self.input_.get()) < 2000:
                    self.change_picture(image_pool[2])
                elif float(self.input_.get()) < 3500:
                    self.change_picture(image_pool[3])
                else:
                    self.change_picture(image_pool[4])

            elif float(self.input_.get()) > 9000:
                self.__result.set("输入的值需小于9000哦")

        except:
            self.__result.set("警告:数据输入错误")

    def __input(self):
        """
        数据输入海拔数据
        - 数据输入
        """
        self.altitude = Entry(self.__panel,
                                font=("Calibri",20),
                                fg = "DarkOrange",
                                textvariable=self.input_,
                                width=14,
                                justify="center",
                                relief="solid")

        self.altitude.place(x=22,y=44)

    def __button(self):
        """
        # 点击按钮
        - 点击融合按钮
        - 控件: button
        """
        self.btn = Button(self.__panel,font=("Calibri",16),text="预测",fg = "DarkOrange",command=self.handler,padx=2,pady=2)
        self.btn.place(x=283,y=39)


    def __show(self):
        """
        显示预测结果
        """
        self.show_area = Label(self.__panel,
                                font=("Calibri",18),
                                textvariable = self.__result,
                                fg = "DeepSkyBlue",
                                bg = "white",
                                height=3,
                                width=25,
                                justify="left",
                                wraplength=200,
                                )
        # 单独显示图片
        # self.img = self.read_image("image/zf.png")
        # self.picture = Label(self.__panel, image=self.img)
        self.picture = Canvas(self.__panel,bg='white',width=372,height=449)
        # 显示判断结果
        self.show_area.place(x=30,y=610)
        self.picture.place(x=18,y=125)

    def change_status(self):
        """status"""
        self.status = False
        sys.exit()

    #分解gif并逐帧显示
    def pick(self,event):
        while self.status:
            im = Image.open(self.image_path)
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            #frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                pic = ImageTk.PhotoImage(frame)
                # 配置图片
                self.picture.create_image((3,3),anchor="nw",image=pic)
                time.sleep(0.2)
                self.__panel.update_idletasks()  #刷新
                self.__panel.update()

    def show(self):
        """
        显示所有控件
        - 层层初始化并执行
        """
        # 创建窗口
        self.__create_window()
        # 背景图片
        self.background()
        # 输入框
        self.__input()
        # 点击按钮
        self.__button()
        self.__show()
        self.picture.bind("<Enter>",self.pick)
        # 循环显示
        self.__main_window.protocol("WM_DELETE_WINDOW",self.change_status)
        self.__main_window.mainloop()


# 启动函数
def predict_tool(data):
    ui = Ui(data)
    ui.show()





# 读取数据
data = pd.read_csv('海拔温度数据.csv')
x = data[['海拔']]
y = data[['温度']]

# 训练模型
t = LinearRegression()
t.fit(x,y)

# 启动预测工具
predict_tool(t)

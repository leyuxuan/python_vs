from PIL import ImageDraw
from ui import *
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
# 人脸图片
image1 = filedialog.askopenfilename()
print('图片一:',image1)
root.destroy()
root = tk.Tk()
root.withdraw()
image2 = filedialog.askopenfilename()
print('图片二:',image2)
root.destroy()

# 界面展示
ui = Ui(image1,image2)
ui.set_result_path('image/med.png')
ui.show()

# -*- coding: utf-8 -*-
 
import base64
import tkinter as tk
from tkinter import filedialog
def write_file(x):
    f = open('bse64.txt',mode='w') 
    f.write(x)   # write 写入
    f.close()   #关闭文件

root = tk.Tk()
root.withdraw()
 
with open(filedialog.askopenfilename(),"rb") as f:
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())
    # base64.b64decode(base64data)
    write_file(str(base64_data))

import requests
import json
import base64
import os
from PIL import Image

def get_size(filePath):
    """
    判断文件大小
    """
    if os.path.isfile(filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize/float(1024 * 1024)
        return round(fsize, 2)
    else:
        print("检查一下文件是否存在")
        return 0

def re_size(filePath):
    """
    修改文件大小
    """
    # 获取文件大小
    size = get_size(filePath)
    # 计算文件缩放比例
    if size != 0:
        rate = round(2/size, 2)
    # 图片缩放
    if size > 1.9:
        img = Image.open(filePath)
        width = int(img.size[0]*rate)
        height = int(img.size[1]*rate)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(filePath)

# 返回人脸矩形框
def find_face(imgpath):
    """
    寻找人脸位置

    """
    user_id = get_UserID()
    request_url = "https://study-web.xiguacity.cn/external/face/detect"
    # 参数信息
    headers = {
        'Content-Type': 'application/json',
        }
    re_size(imgpath)
    # base64 加密图片
    with open(imgpath, 'rb') as file:
        ff1 = base64.b64encode(file.read())
        ff1_ = str(ff1,'utf-8')
    params = {
        "image":ff1_,
        "studentNumber":user_id,
        }
    params = json.dumps(params)
    #  真实请求
    response = requests.post(request_url, data=params, headers=headers).json()

    # print(params)
    if not response["body"]:
        print('no human face in pic')
        return
    else:
        print("find face in {face}".format(face=imgpath))
    rectangle = response["body"]["location"]
    return [(rectangle['left'],rectangle['top']),(rectangle['left']+rectangle['width'],rectangle['top']+rectangle['height'])]

# 返回人脸融合图片
def merge_face(template_image, target_image, template_face_rectangle=0, target__face_rectangle=0):
    """
    人脸融合
    """
    user_id = "18240783"
    request_url = "https://study-web.xiguacity.cn/external/face/merge"
    headers = {'content-type': 'application/json'}

    # - TODO: 判断图片大小（自动压缩）
    re_size(template_image)
    re_size(target_image)

    # base64加密
    with open(template_image, 'rb') as file:
        ff1 = base64.b64encode(file.read())
        ff1_ = str(ff1,'utf-8')

    with open(target_image, 'rb') as f2:
        ff2 = base64.b64encode(f2.read())
        ff2_ = str(ff2,'utf-8')

    params = {
        "templateImage":ff1_,
        "targetImage":ff2_,
        "studentNumber":user_id,
        }
    params = json.dumps(params)
    #print(params)
    response = requests.post(request_url, data=params, headers=headers).json()
    if response["code"] != "200":
        print("人脸融合失败")
        return
    result = response["body"]["mergedImage"]
    # 返回人脸融合
    imgdata = base64.b64decode(result)
    return imgdata

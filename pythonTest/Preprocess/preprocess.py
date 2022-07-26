"""
  预处理图像的模块-包括灰度转换，模糊，阈值，canny边缘检测，膨胀和侵蚀
"""

import cv2
import numpy as np
def process(image):
    """
 函数预处理图像参数

     """

    
    #将图像转换为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    #模糊图像有助于进一步处理
    kernel = np.ones((5,5),np.float32)/25
    gray = cv2.filter2D(gray,-1,kernel)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    
    #阈值化或二值化在这里完成
    ret,threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    
    #利用Canny边缘检测对二值化图像进行边缘检测
    edged = cv2.Canny(gray, 0.5*ret, ret)

    
    #图像中的边缘被放大和侵蚀，这样边缘就
 
    for i in range(5):
        edged = cv2.dilate(edged, kernel, iterations=1)#膨胀
        edged = cv2.erode(edged, kernel, iterations=1)#腐蚀

    
    return edged

def init(image):
    """
        方法初始化路径参数

    """

    edged = process(image)
    return edged
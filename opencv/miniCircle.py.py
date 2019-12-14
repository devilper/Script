import cv2 as cv # 导入python 第三方库 opencv-python
import numpy as np # 导入python 第三方库 numpy 


def main():
	img = np.zeros((520, 520, 3), np.uint8) #生成一张520像素*520像素 大小的图片

	# 生成图片和读取图片选其一就好

	#img =cv.imread('/home/devilper/Desktop/2.jpg')  # 读取一张已有的图片 

	# 坐标点的样式
	point_size = 1 # 坐标点的大小(必须为整数)
	point_color = (0,0,255) # 坐标点的颜色
	thickness = 2  # 线条粗细

	# 坐标点()
	points_list = [(260, 260), (436, 160), (500, 200), (200, 180), (320, 250), (445, 380)] # 想要画的坐标点

	# 遍历坐标点画出每一个坐标点
	for point in points_list:
		cv.circle(img, point, point_size, point_color, thickness) # 画坐标点


	# 画最小包络圆
	cnt = np.array(points_list) # 坐标点形式转换

	(x,y), radius = cv.minEnclosingCircle(cnt) # 计算出最小包络圆的圆心、半径

	center = (int(x), int(y)) # 圆心坐标
	radius = int(radius)  # 最小包络圆半径

	cv.circle(img, center,radius,point_color,0) # 画圆

	# 图片上添加文字
	text = "Center :{center}".format(center=center) # 一行文字内容 (不能添加中文)
	text1 = "Diameter: {radius}".format(radius = radius * 2)

	size = img.shape[1:2][0] # 图片y轴大小

	# 文字显示在图片上
	# 参数分别为 图片 文字内容 文字坐标       字体              字体大小 字体颜色  字体粗细
	cv.putText(img, text,  (0,size-50),cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)
	cv.putText(img, text1,  (0,size-20),cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)

	cv.namedWindow("image")
	cv.imshow('image', img)  #显示图片
	cv.waitKey (10000) # 显示 10s 即 10s 后消失
	cv.destroyAllWindows() # 关闭显示窗口

if __name__ == '__main__':
	
	main() # 执行方法
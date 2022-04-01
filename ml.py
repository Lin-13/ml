from calendar import c
import numpy as np
import cv2 as cv
a=np.eye(3)
print(a)
src=cv.imread("D:/Document/test.jpg")
cv.imshow("src",src)
cv.waitKey(0)
b=np.array([[1.2,2,3],[4,5,6],[7,8,9]],dtype=np.complex_,ndmin=2)
print(b)
dt=np.dtype([('age',np.int8)],align=False,copy=True)

c=np.array([(12),(34)],dtype=dt)
print(c)
student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
l=np.array([('abc',20,20),('xyz',12,12)],dtype=student)
print(l)
print(l.flags)
print(l.itemsize)

l.reshape(1,2)
print(l)
e=np.empty([3,2],dtype=int)
print(e)
e=2*e
print(e)
#从已有数组创建数组
x=[1,2,3]
x1=np.asarray(x,dtype=np.float32)
print(x1)
#迭代器
it=iter(x)
x2=np.fromiter(it,dtype=float)
print(x2)
print(next(it))
#流
s=b'helloworld'
np_s=np.frombuffer(s,dtype='S1')
print(np_s)
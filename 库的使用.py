import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus'] = False#横纵坐标负数就可以显示了
import numpy as np
t=np.linspace(-np.pi,np.pi,1000)
x=1*(2*np.cos(t)-np.cos(2*t))
y=1*(2*np.sin(t)-np.sin(2*t))
plt.title('heart by dikaer')
plt.axis([-3.5,3.5,-3.5,3.5])#xmin,xmax,ymin,ymax  plt.xlim(xmin,xmax)也阔以
plt.autoscale()#自动售房轴视图的数据
plt.grid(True) #开启网格
'''
for a,b in zip(x,y):
    plt.text(a,b+0.1,'%.0f'%b,ha = 'center',va = 'center',fontsize=7)
    #在a，b+0.1 的每个位置 写上高度 居中
'''
plt.plot(x,y,color='r',linewidth='3',linestyle='-')
plt.show()



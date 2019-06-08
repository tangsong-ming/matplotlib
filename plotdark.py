import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']='SimHei'
x=np.linspace(0,10,1000)
y=np.cos(2*np.pi*x)*np.exp(-x)+0.8
plt.plot(x,y,'k',color='r',label='$exp-decay$',linewidth=3)
plt.legend()
plt.axis([0,6,0,1.8])
ix=(x>0.8)&(x<6)
plt.fill_between(x,y,0,where=ix,facecolor='blue',alpha=0.25)#alpha=0.25  变了颜色
#两条曲线围城的多边形
plt.text(1.9,0.2,r'$\int_a^b f(x)\mathrm{d}x$',horizontalalignment='center')
plt.show()


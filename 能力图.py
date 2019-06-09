import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']='SimHei'
labels=np.array(['综合','KDA','发育','推进','生存','输出'])
nAttr=6
data=np.array([7,5,6,8,9,7])#数据值  同心圆上画六边形
angles=np.linspace(0,2*np.pi,nAttr,endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure(facecolor='white')
plt.subplot(polar=True)
plt.plot(angles,data,'o-',color='g',linewidth=2)#o  把点描出来
plt.fill(angles,data,facecolor='g',alpha=0.25)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.52,0.97,'王者能力值雷达图',ha='center')
plt.grid(True)
plt.savefig('wangzhe.jpg')
plt.show()

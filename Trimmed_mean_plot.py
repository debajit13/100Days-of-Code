import matplotlib.pyplot as plt
import statistics 
list=[100,900,200,400,600,500,300,800,1000,700,55,87,90,537,679,37,857,789,87,876,765,123,321,23]
list.sort()
tv=int((0.1*len(list)))
list=list[tv:]
list=list[:len(list)-tv]
m=statistics.mean(list)
me=statistics.median(list)
y=[]
for i in range (len(list)):
    y.append(5)
plt.plot(list,y,"r--")
plt.plot(m,[5],"bs")
plt.plot(me,[5],"g^")
plt.plot([500],[5],"ro")

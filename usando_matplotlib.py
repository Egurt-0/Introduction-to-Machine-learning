import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__path__)

x = [1,2,5,7,8,10]
y = [20,40,30,50,70,90]
plt.scatter(x,y,alpha=0.8, edgecolors="w", s=1000)
plt.title("teste")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")


z = np.polyfit(x,y, 1)
p = np.poly1d(z)
plt.plot(x, p(y),  "r--")
plt.grid()
plt.show()
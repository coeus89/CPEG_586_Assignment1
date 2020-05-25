import sys
import numpy as np
from numpy.linalg import inv
import math
import matplotlib.pyplot as plt



def main():
    x = [1, 2, 3, 4, 5, 6]
    y = [3.2, 6.4, 10.5, 17.7, 28.1, 38.5]

    A1 = 0
    A2 = 0
    A3 = 0
    B1 = 0
    B2 = 0
    B3 = 0
    C1 = 0
    C2 = 0
    C3 = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0

    le = 0
    while le < len(x):
        A1 += 2*x[le]**4
        B1 += 2*x[le]**3
        C1 += 2*x[le]**2
        A2 += 2*x[le]**3
        B2 += 2*x[le]**2
        C2 += 2*x[le]**1
        A3 += 2*x[le]**2
        B3 += 2*x[le]**1
        C3 += 2*x[le]**0

        Y1 += (2*x[le]**2)*y[le]
        Y2 += (2*x[le]**1)*y[le]
        Y3 += (2*x[le]**0)*y[le]

        le = le + 1
    
    lse = np.matrix( [[A1,B1,C1],
                    [A2,B2,C2],
                    [A3,B3,C3]])

    rse = np.matrix( [[Y1],
                    [Y2],
                    [Y3]])
    
    lseInverse = inv(lse)
    ABC = lseInverse.dot(rse)
    #print(ABC)
    A = ABC[0,0]
    B = ABC[1,0]
    C = ABC[2,0]
    print("A: " + str(A))
    print("B: " + str(B))
    print("C: " + str(C))

    # area = 10
    # colors = ['black']
    # plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    # plt.title('Linear Least Squares Regression')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # #plot the fitted line
    # yfitted = A*x**2 + B*x + C
    # line,=plt.contour(x, yfitted, '--', linewidth=2) #line plot
    # line.set_color('red')
    # plt.show()





if __name__ == "__main__":
    sys.exit(int(main() or 0))

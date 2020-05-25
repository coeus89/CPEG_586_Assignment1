import sys
import numpy as np
from numpy.linalg import inv
import math
import matplotlib.pyplot as plt



def main():
    x = np.ndarray((6,1))
    y = np.ndarray((6,1))
    
    x[0,0] = 1
    x[1,0] = 2
    x[2,0] = 3
    x[3,0] = 4
    x[4,0] = 5
    x[5,0] = 6
    y[0,0] = 3.2
    y[1,0] = 6.4
    y[2,0] = 10.5
    y[3,0] = 17.7
    y[4,0] = 28.1
    y[5,0] = 38.5
    # x = [1, 2, 3, 4, 5, 6]
    # y = [3.2, 6.4, 10.5, 17.7, 28.1, 38.5]

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
    while le < x.size:
        A1 += 2*x[le,0]**4
        B1 += 2*x[le,0]**3
        C1 += 2*x[le,0]**2
        A2 += 2*x[le,0]**3
        B2 += 2*x[le,0]**2
        C2 += 2*x[le,0]**1
        A3 += 2*x[le,0]**2
        B3 += 2*x[le,0]**1
        C3 += 2*x[le,0]**0

        Y1 += (2*x[le,0]**2)*y[le,0]
        Y2 += (2*x[le,0]**1)*y[le,0]
        Y3 += (2*x[le,0]**0)*y[le,0]

        le = le + 1
    lse = np.ndarray((3,3))
    lse[0,0] = A1
    lse[0,1] = B1
    lse[0,2] = C1
    lse[1,0] = A2
    lse[1,1] = B2
    lse[1,2] = C2
    lse[2,0] = A3
    lse[2,1] = B3
    lse[2,2] = C3
    # lse = np.matrix( [[A1,B1,C1],
    #                 [A2,B2,C2],
    #                 [A3,B3,C3]])
    rse = np.ndarray((3,1))
    rse[0,0] = Y1
    rse[1,0] = Y2
    rse[2,0] = Y3
    # rse = np.matrix( [[Y1],
    #                 [Y2],
    #                 [Y3]])
    
    lseInverse = inv(lse)
    ABC = lseInverse.dot(rse)
    print(ABC)
    A = ABC[0,0]
    B = ABC[1,0]
    C = ABC[2,0]
    # print("A: " + str(A))
    # print("B: " + str(B))
    # print("C: " + str(C))

    area = 10
    colors = ['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    #plot the fitted line
    yfitted = A*x**2 + B*x + C
    line,=plt.contour(x, yfitted, '--', linewidth=2) #line plot
    line.set_color('red')
    plt.show()





if __name__ == "__main__":
    sys.exit(int(main() or 0))

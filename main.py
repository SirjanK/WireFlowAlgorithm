import numpy as np
from scipy import optimize

def main():
    c = np.array([0,0,0,1])
    Aub = np.array([[-2,5,-4,-1], [-1,-5,8,-1], [3, -1, -3,-1]])
    bub = np.array([0, 0, 0])
    Aeq = np.array([[1,1,1,0]])
    beq = np.array([1])
    result = optimize.linprog(c, Aub, bub, A_eq=Aeq, b_eq=beq)
    print(result)

if __name__ == '__main__':
    main()

import numpy as np

class mn():
    def __init__(self):
        self.T = np.array([[0, 0.2, -0.5, 0.4],
             [-0.2, 0.5, 1.25, 2.5],
             [0.3, -0.5, 0.4, -0.8]])
        self.bx = 0
        self.cx = 0



    def calc(self):

        if(self.T[0][0] == 0):
            self.T[[0, 1]] = self.T[[1, 0]]
        if (self.T[0][0] == 0):
            self.T[[0, 2]] = self.T[[2, 0]]
        self.bx = self.T[1][0] / self.T[0][0]
        self.cx = self.T[2][0] / self.T[0][0]

        i = 0
        for i in range(4):
            self.T[1][i] = self.T[1][i] - self.bx * self.T[0][i]
            self.T[2][i] = self.T[2][i] - self.cx * self.T[0][i]

        if (self.T[1][1] == 0):
            self.T[[2, 1]] = self.T[[1, 2]]
        self.cx = self.T[2][1] / self.T[1][1]

        i = 0


        for i in range(4):
            self.T[2][i] = self.T[2][i] - self.cx * self.T[1][i]

        if (self.T[2][2] == 0):
            self.T[[2, 1]] = self.T[[1, 2]]

        z = self.T[2][3]/self.T[2][2]
        y = (self.T[1][3] - self.T[1][2] * z) / self.T[1][1]
        x = (self.T[0][3] - self.T[0][2] * z - self.T[0][1] * y) / self.T[0][0]

        print("z = " + str(z))
        print("y = " + str(y))
        print("x = " + str(x))
        print(self.T)



if __name__ == '__main__':
    obj = mn()
    obj.calc()


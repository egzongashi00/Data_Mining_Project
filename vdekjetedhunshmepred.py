import sys

import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import numpy as np

x = []
y = []
z = []
a = []
h = []

with open('C:/Users/DELL/Downloads/vdekjetedhunshme.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append((row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))
        a.append(int(row[3]))
        h.append(int(row[0]))

p = int(sys.argv[1])
q = int(p) - 2019

regression_model = LinearRegression()
regression_model2 = LinearRegression()
regression_model3 = LinearRegression()

xarray = np.array(h).reshape(-1, 1)
yarray = np.array(y)
zarray = np.array(z)
aarray = np.array(a)

i = 1

for c in range(q):
    regression_model.fit(xarray, yarray)
    regression_model.predict([[2019 + i]])
    regression_model2.fit(xarray, zarray)
    regression_model2.predict([[2019 + i]])
    regression_model3.fit(xarray, aarray)
    regression_model3.predict([[2019 + i]])

    y.append(int(regression_model.predict([[2019 + i]])))
    z.append(int(regression_model2.predict([[2019 + i]])))
    a.append(int(regression_model3.predict([[2019 + i]])))
    x.append(str(2019 + i))
    i = i + 1

plt.plot(x, y, label='Fatekeqsite', color="BLUE")
plt.plot(z, label='Vetevrasje', color="BLACK")
plt.plot(a, label='Vrasje', color="RED")
plt.ylim(bottom=0)

plt.xlabel('Viti')
plt.ylabel('Numri i vdekjeve')
plt.title('Vdekjet e dhunshme')
plt.legend()
plt.show()

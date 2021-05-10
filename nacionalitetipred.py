import sys

import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import numpy as np

x = []
y = []
z = []
a = []
b = []
f = []
d = []
h = []

with open('C:/Users/DELL/Downloads/nacionaliteti.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))
        a.append(int(row[3]))
        b.append(int(row[4]))
        f.append(int(row[5]))
        d.append(int(row[6]))
        h.append(int(row[0]))

p = int(sys.argv[1])
q = int(p) - 2019

regression_model = LinearRegression()
regression_model2 = LinearRegression()
regression_model3 = LinearRegression()
regression_model4 = LinearRegression()
regression_model5 = LinearRegression()
regression_model6 = LinearRegression()

xarray = np.array(h).reshape(-1, 1)
yarray = np.array(y)
zarray = np.array(z)
aarray = np.array(a)
barray = np.array(b)
farray = np.array(f)
darray = np.array(d)

i = 1

for c in range(q):
    regression_model.fit(xarray, yarray)
    regression_model.predict([[2019 + i]])
    regression_model2.fit(xarray, zarray)
    regression_model2.predict([[2019 + i]])
    regression_model3.fit(xarray, aarray)
    regression_model3.predict([[2019 + i]])
    regression_model4.fit(xarray, barray)
    regression_model4.predict([[2019 + i]])
    regression_model5.fit(xarray, farray)
    regression_model5.predict([[2019 + i]])
    regression_model6.fit(xarray, darray)
    regression_model6.predict([[2019 + i]])

    y.append(int(regression_model.predict([[2019 + i]])))
    z.append(int(regression_model2.predict([[2019 + i]])))
    a.append(int(regression_model3.predict([[2019 + i]])))
    b.append(int(regression_model4.predict([[2019 + i]])))
    f.append(int(regression_model5.predict([[2019 + i]])))
    d.append(int(regression_model6.predict([[2019 + i]])))
    x.append(str(2019 + i))
    i = i + 1


plt.plot(x, y, label='Shqiptar', color="BLUE")
plt.plot(z, label="Serb", color="BLACK")
plt.plot(a, label="RAE", color="PINK")
plt.plot(b, label="Boshnjak", color="GREEN")
plt.plot(f, label="Turk", color="RED")
plt.plot(d, label="Tjeter", color="PURPLE")

plt.xlabel('Viti')
plt.ylabel('Numri i vdekjeve')
plt.title('Numri i vdekjeve sipas nacionalitetit')
plt.legend()
plt.show()

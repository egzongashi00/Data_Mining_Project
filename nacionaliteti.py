import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
a = []
b = []
c = []
d = []

with open('C:/Users/DELL/Downloads/nacionaliteti.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))
        a.append(int(row[3]))
        b.append(int(row[4]))
        c.append(int(row[5]))
        d.append(int(row[6]))

plt.plot(x, y, label='Shqiptar', color="BLUE")
plt.plot(z, label="Serb", color="BLACK")
plt.plot(a, label="RAE", color="PINK")
plt.plot(b, label="Boshnjak", color="GREEN")
plt.plot(c, label="Turk", color="RED")
plt.plot(d, label="Tjeter", color="PURPLE")

plt.xlabel('Viti')
plt.ylabel('Numri i vdekjeve')
plt.title('Numri i vdekjeve sipas nacionalitetit')
plt.legend()
plt.show()

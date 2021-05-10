import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
a = []

with open('C:/Users/DELL/Downloads/vdekjetedhunshme.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append((row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))
        a.append(int(row[3]))

plt.plot(x, y, label='Fatekeqsite', color="BLUE")
plt.plot(z, label='Vetevrasje', color="BLACK")
plt.plot(a, label='Vrasje', color="RED")
plt.ylim(bottom=0)
plt.xlabel('Viti')
plt.ylabel('Numri i vdekjeve')
plt.title('Vdekjet e dhunshme')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []

with open('C:/Users/DELL/Downloads/gjinia.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append((row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))

plt.plot(x,y, label='Meshkuj', color="BLUE")
plt.plot(z, label="Femra", color="RED")
plt.ylim(bottom=0)
plt.xlabel('Viti')
plt.ylabel('Numri i vdekjeve')
plt.title('Numri i vdekjeve sipas gjinise')
plt.legend()
plt.show()

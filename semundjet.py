import matplotlib.pyplot as plt
import numpy as np

y = np.array([54, 920, 112, 72, 2027, 313, 111, 92])
mylabels = ["Sëmundjet infektive dhe parazitare", "Tumoret",
            "Sëmundjet endokrine", "Sëmundjet e sistemit nervor",
            "Sëmundjet e sistemit të qarkullimit të gjakut", "Sëmundjet e sistemit të frymëmarrjes", "Sëmundjet e sistemit urogjenital",
            "Sëmundjet e sistemit të tretjes"]

plt.pie(y, labels=mylabels, startangle=200)
plt.title("Vdekjet sipas grupeve te sëmundjeve")
plt.show()

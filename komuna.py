import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({
    "Prishtine": [727, 825, 901, 833, 773, 893, 928, 817, 921, 1075],
    "Mitrovice": [361, 330, 544, 321, 415, 366, 365, 444, 430, 396],
    "Peje": [381, 420, 392, 425, 430, 461, 496, 541, 575, 549],
    "Prizren": [740, 764, 707, 751, 761, 859, 842, 944, 911, 881],
    "Ferizaj": [465, 499, 424, 401, 502, 452, 520, 429, 478, 538],
    "Gjilan": [488, 501, 417, 397, 453, 498, 470, 512, 545, 580],
    "Gjakova": [443, 469, 398, 394, 483, 505, 542, 579, 542, 588]
},
    index=["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]
)
plotdata.plot(kind="bar")
plt.title("Numri i vdekjeve sipas komunave")
plt.xlabel("Viti")
plt.ylabel("Numri i te vdekureve")

plt.show()

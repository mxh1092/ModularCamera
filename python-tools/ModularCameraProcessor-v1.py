import numpy as np
import pandas as pd
import pept
from pept.visualisation import PlotlyGrapher

data = np.loadtxt('data/Test_Singles.dat', usecols=(0, 2, 7, 8, 9, 10, 12))


ID = data[:, 0]
head = data[:, 1]
t = data[:, 2]
x = data[:, 3]
y = data[:, 4]
z = data[:, 5]
comptons = data[:, 6]


window = 10*10e-9
deadtime1 = 3*10e-6

mask = np.zeros(len(data))
i = 0

while i < len(data)-1:


    if t[i+1]-t[i] <= window:

        if head[i+1] == 0 and head[i] == 1:

            mask[i] = 1

            i += 2

        if head[i] == 0 and head[i+1] == 1:

            mask[i] = 1

            i += 2

        else:

            i += 1

            continue

    i += 1


def makeLORs(data, mask, filename):


    ID = data[:, 0]
    head = data[:, 1]
    t = data[:, 2]
    x = data[:, 3]
    y = data[:, 4]
    z = data[:, 5]
    comptons = data[:, 6]

    open(filename,'w')

    for i in range(len(data)-1):

        with open(filename,'a') as f:

            if mask[i] == 1:

                lor = [t[i], x[i], y[i], z[i], t[i+1], x[i+1], y[i+1], z[i+1]]

                for item in lor:

                    f.write("%s\t" % str(item))
                f.write('\n')

            else:

                continue
    f.close()

filename = 'data/lors.txt'

makeLORs(data, mask, filename)

lors = np.loadtxt(filename, usecols=(0, 1, 2, 3, 5, 6, 7))

lors = pept.LineData(lors)

# Create a PlotlyGrapher instance, then have it create a Plotly figure.
grapher = PlotlyGrapher()

# Add a Plotly trace from the LoRs
grapher.add_lines(lors)
grapher.show()

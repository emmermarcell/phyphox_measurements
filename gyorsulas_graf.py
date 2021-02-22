import numpy as np
import matplotlib.pyplot as plt

# adatok betoltese
data = np.loadtxt('meresek\\2_3sarok3.csv', delimiter='\t', skiprows=1)

# tengelyek definialasa
Time = data[:,0]-0.5# az eleje nem kell
Acc = np.zeros((3, Time.size))
Acc[0] = data[:,1]
Acc[1] = data[:,2]
Acc[2] = data[:,3] * -1 # fordítva tartottam a telefonom

# meresi pontok abrazolasa
fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('Telefon gyorsulás')
axs[0].plot(Time, Acc[0], 'C0.')
axs[1].plot(Time, Acc[1], 'g.')
axs[2].plot(Time, Acc[2], 'r.')
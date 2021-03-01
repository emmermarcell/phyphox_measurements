import numpy as np
import matplotlib.pyplot as plt

# adatok beolvasasa
data = np.loadtxt('meresek\\3_2hutomagnes.csv', delimiter='\t', skiprows=1)

# 10x6 meresi pontom van, ezekre atlagolom a meresi ertekeket
Bx = data[:,1]
Bx_split = np.array_split(Bx, 10*6)
Bx_avg = np.array([np.mean(arr) for arr in Bx_split]).reshape(6,10)

By = data[:,2]
By_split = np.array_split(By, 10*6)
By_avg = np.array([np.mean(arr) for arr in By_split]).reshape(6, 10)

Bz = data[:,3]
Bz_split = np.array_split(Bz, 10*6)
Bz_avg = np.array([np.mean(arr) for arr in Bz_split]).reshape(6, 10)

# kígyózva vettem fel az adatokat, itt ezt sorba teszem
for i in range(6)[::2]:
    Bx_avg[i] = np.flip(Bx_avg[i])
    By_avg[i] = np.flip(By_avg[i])
    Bz_avg[i] = np.flip(Bz_avg[i])

X = np.arange(0, 5, 0.5)
Y = np.arange(0, 3, 0.5)

x, y = np.meshgrid(np.arange(0, 5, 0.5),
                 np.arange(0, 3, 0.5)  
    )

print(X.size, Bx_avg.size)
print(Y.size, By_avg.size)

# betutipus beallitasa
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax = plt.subplots()
Q = ax.quiver(X, Y, Bx_avg, By_avg, Bz_avg, units='inches', pivot='tail', width=0.04)
ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \mu T$', labelpos='E',
                    coordinates='figure')
ax.scatter(x[::, ::], y[::, ::], color='0.7', s=3)

ax.set_xlabel('$x$ (cm)')
ax.set_ylabel('$y$ (cm)')
ax.set_title("Fóliamágnes mágneses térprofilja")

plt.savefig('foliamagnes_terkep', dpi=300)
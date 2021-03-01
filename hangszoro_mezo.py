import numpy as np
import matplotlib.pyplot as plt

# adatok beolvasasa
data = np.loadtxt('meresek\\3_2hangszoro2.csv', delimiter='\t', skiprows=1)

# 7x8 meresi pontom van, ezekre atlagolom a meresi ertekeket
Bx = data[:,2]
Bx_split = np.array_split(Bx, 41)
Bx_avg = np.array([np.mean(arr) for arr in Bx_split])
for k in range(5):
    Bx_avg = np.insert(Bx_avg, 11 + 8*k, [0,0,0])
    Bx_avg[14+ 8*k:16+ 8*k] *= -1
Bx_avg = Bx_avg.reshape(7,8)

By = data[:,1] * -1
By_split = np.array_split(By, 41)
By_avg = np.array([np.mean(arr) for arr in By_split])
for k in range(5):
    By_avg = np.insert(By_avg, 11 + 8*k, [0,0,0])
    By_avg[14+ 8*k:16+ 8*k] *= -1
By_avg = By_avg.reshape(7,8)

Bz = data[:,3]
Bz_split = np.array_split(Bz, 41)
Bz_avg = np.array([np.mean(arr) for arr in Bz_split])
for k in range(5):
    Bz_avg = np.insert(Bz_avg, 11 + 8*k, [0,0,0])
Bz_avg = Bz_avg.reshape(7,8)

# terbeli pontok meghatározása
X = np.arange(-20, 15+1, 5)
Y = np.arange(-15, 15+1, 5)

x, y = np.meshgrid(np.arange(-20, 15+1, 5),
                   np.arange(-15, 15+1, 5)
                   )

print(X.size,Y.size)

# betutipus beallitasa
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax = plt.subplots()
Q = ax.quiver(X, Y, Bx_avg, By_avg, Bz_avg, units='inches', pivot='tail')
ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \mu T$', labelpos='E',
                    coordinates='figure')

ax.scatter(x[::, ::], y[::, ::], color='0.7', s=3)

ax.set_xlabel('$x$ (cm)')
ax.set_ylabel('$y$ (cm)')
ax.set_title("Hangszóró mágneses térprofilja")
# ax.grid()

plt.savefig('hangszoromagnes_terkep2', dpi=300)
import numpy as np
from scipy.integrate import trapz
import matplotlib.pyplot as plt

# adatok betoltese
data = np.loadtxt('meresek\\2_1szabadeses150cm2.csv', delimiter='\t', skiprows=1)

# tengelyek definialasa
Time = data[:,0] -2 # az eleje nem kell
Acc = np.zeros((3, Time.size))
Acc[0] = data[:,1]* -1
Acc[1] = data[:,2]* -1
Acc[2] = data[:,3]* -1# fordítva tartottam a telefonom

# A sebesség numerikus integrálása a gyorsulasbol trapezszaballyal
Vel = np.zeros((3, Time.size))
for j in range(3):
    for i, val in enumerate(Acc[j]):
        Vel[j][i] = trapz(Acc[j][:i], Time[:i])
    
# Az elmozdulas numerikus integrálása a sebessegbol trapezszaballyal
Pos = np.zeros((3, Time.size))
for j in range(3):
    for i, val in enumerate(Vel[j]):
        Pos[j][i] = trapz(Vel[j][:i], Time[:i])

# betutipus beallitasa
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# meresi pontok abrazolasa
fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('Telefon második szabadesésének elmozdulásvektora')
axs[0].plot(Time, Pos[0], 'C0.', label = "Az x irányú elmozdulás: $\Delta x = ($" + str( round(Pos[0][-1] - Pos[0][0], 3) ) + "$\pm$" + str( round((Pos[0][-1] - Pos[0][0])/100, 3) ) + ") m,") 
axs[1].plot(Time, Pos[1], 'g.', label = "Az y irányú elmozdulás: $\Delta y = ($" + str( round(Pos[1][-1] - Pos[1][0], 3) ) + "$\pm$" + str( round((Pos[1][-1] - Pos[1][0])/100, 3) ) + ") m,")
axs[2].plot(Time, Pos[2], 'r.', label = "A z irányú elmozdulás: $\Delta z = ($" +  str( round(Pos[2][-1] - Pos[2][0], 3) ) + "$\pm$" + str( round((Pos[2][-1] - Pos[2][0])/100, 3) ) + ") m,")

# tengely hibajanak definialasa es abrazolasa errorbarokkal
yerror = 0.1 *Acc
axs[0].errorbar(Time, Pos[0], yerr=yerror[0], fmt=' ', color='lightskyblue')
axs[1].errorbar(Time, Pos[1], yerr=yerror[1], fmt=' ', color='springgreen')
axs[2].errorbar(Time, Pos[2], yerr=yerror[2], fmt=' ', color='#FE6F5E')

# tengelyek elnevezese, cim, stb.
axs[0].set_ylabel('$x$ (m)')
axs[1].set_ylabel('$y$ (m)')
axs[2].set_ylabel('$z$ (m)')
for ax in axs:
    ax.set_xlabel('$t$ (s)')
    ax.label_outer()
    ax.legend()
    ax.grid()
    
# grafikon mentese
plt.savefig('szabadeses_grafikon_2', dpi=300)
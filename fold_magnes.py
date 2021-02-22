import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * x + b

# adatok betoltese
data = np.loadtxt('meresek\\3_1fold2konyha.csv', delimiter='\t', skiprows=1)

# tengelyek es hibainak definialasa
Time = data[:,0]# az eleje nem kell
Ind = np.zeros((3, Time.size))
Ind[0] = data[:,1]
Ind[1] = data[:,2]
Ind[2] = data[:,3]* -1# fordítva tartottam a telefono

# betutipus beallitasa
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# meresi pontok abrazolasa
fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('A Föld mágneses terének harmadik mérése (Konyha)')
axs[0].plot(Time, Ind[0], 'C0.', label = 'x irányú mágneses indukcióvektor')
axs[1].plot(Time, Ind[1], 'g.', label = 'y irányú mágneses indukcióvektor')
axs[2].plot(Time, Ind[2], 'r.', label = 'z irányú mágneses indukcióvektor')

# tengely hibajanak definialasa es abrazolasa errorbarokkal
yerror = 0.1 *Ind + 0.0001
axs[0].errorbar(Time, Ind[0], yerr=yerror[0], fmt=' ', color='lightskyblue')
axs[1].errorbar(Time, Ind[1], yerr=yerror[1], fmt=' ', color='springgreen')
axs[2].errorbar(Time, Ind[2], yerr=yerror[2], fmt=' ', color='#FE6F5E')

# gorbeillesztes
popt1, pcov1 = curve_fit(lambda x, b: func(x, 0, b), Time, Ind[0], sigma = yerror[0], absolute_sigma=True)
popt2, pcov2 = curve_fit(lambda x, b: func(x, 0, b), Time, Ind[1], sigma = yerror[1], absolute_sigma=True)
popt3, pcov3 = curve_fit(lambda x, b: func(x, 0, b), Time, Ind[2], sigma = yerror[2], absolute_sigma=True)

print(popt1)
print(np.sqrt(np.diag(pcov1)))
print(popt2)
print(np.sqrt(np.diag(pcov2)))
print(popt3)
print(np.sqrt(np.diag(pcov3)))

axs[0].plot(Time, func(Time, 0, *popt1), 'r-', label = 'Illesztés: $B_{x} = (-1.6245 \pm 0.6322) \cdot 10^{-5}~\mu$T')
axs[1].plot(Time, func(Time, 0, *popt2), 'y-', label = 'Illesztés: $B_{y} = (35.7475 \pm 0.0470)~\mu$T')
axs[2].plot(Time, func(Time, 0, *popt3), 'C0-', label = 'Illesztés: $B_{z} = (31.4063 \pm 0.0413)~\mu$T')

# tengelyek elnevezese, cim, stb.
for ax in axs:
    ax.set_xlabel('$t$ (s)')
    ax.set_ylabel('$B$ ($\mu$T)')
    ax.label_outer()
    ax.legend()
    ax.grid()
    
plt.savefig('foldmagnes3', dpi=300)
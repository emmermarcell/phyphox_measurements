import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import sqrt

def func(x, a, b):
    return a * x + b

# adatok betoltese
data1 = np.loadtxt('meresek\\1_1szabadeses_foldon.csv', delimiter='\t', skiprows=1)
data2 = np.loadtxt('meresek\\1_2szabadeses_pulton_90cm.csv', delimiter='\t', skiprows=1)
data3 = np.loadtxt('meresek\\1_3szabadeses_polcon_210cm.csv', delimiter='\t', skiprows=1)

# tengelyek es hibainak definialasa
Time1 = data1[:,0]
Grav1 = data1[:,4]
Time2 = data2[:,0]
Grav2 = data2[:,4]
Time3 = data3[:,0]
Grav3 = data3[:,4]

# betutipus beallitasa
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# meresi pontok abrazolasa
fig, axs = plt.subplots(3, sharex=True, sharey=True)
# fig.suptitle('A gravitációs gyorsulás mérése')
fig.tight_layout()
axs[0].plot(Time1, Grav1, 'C0.')
axs[1].plot(Time2, Grav2, 'g.')
axs[2].plot(Time3, Grav3, 'r.')

# tengely hibajanak definialasa es abrazolasa errorbarokkal
yerror1 = 0.01 * Grav1
yerror2 = 0.01 * Grav2
yerror3 = 0.01 * Grav3
axs[0].errorbar(Time1, Grav1, yerr=yerror1, fmt=' ', color='lightskyblue')
axs[1].errorbar(Time2, Grav2, yerr=yerror2, fmt=' ', color='springgreen')
axs[2].errorbar(Time3, Grav3, yerr=yerror3, fmt=' ', color='#FE6F5E')

# gorbeillesztes
popt1, pcov1 = curve_fit(lambda x, b: func(x, 0, b), Time1, Grav1, sigma = yerror1, absolute_sigma=True)
popt2, pcov2 = curve_fit(lambda x, b: func(x, 0, b), Time2, Grav2, sigma = yerror2, absolute_sigma=True)
popt3, pcov3 = curve_fit(lambda x, b: func(x, 0, b), Time3, Grav3, sigma = yerror3, absolute_sigma=True)

print(popt1)
print(np.sqrt(np.diag(pcov1)))
print(popt2)
print(np.sqrt(np.diag(pcov2)))
print(popt3)
print(np.sqrt(np.diag(pcov3)))

axs[0].plot(Time1, func(Time1, 0, *popt1), 'r-', label = 'Illesztés: $g = (9.8469 \pm 0.0006)$ m/s$^{2}$')
axs[1].plot(Time2, func(Time2, 0, *popt2), 'y-', label = 'Illesztés: $g = (9.8408 \pm 0.0006) $ m/s$^{2}$')
axs[2].plot(Time3, func(Time3, 0, *popt3), 'C0-', label = 'Illesztés: $g = (9.8387 \pm 0.0006)$ m/s$^{2}$')

# tengelyek elnevezese, cim, stb.
fig.subplots_adjust(left=None, bottom=None, right=None, top=1.2, wspace=None, hspace=None)
axs[0].set_title('Első mérés: $h = 0$ cm')
axs[1].set_title('Második mérés: $h = 90$ cm')
axs[2].set_title('Harmadik mérés: $h = 210$ cm')
for ax in axs:
    ax.set_xlabel('$t$ (s)')
    ax.set_ylabel('$g$ (m/s$^{2}$)')
    ax.label_outer()
    ax.legend()
    ax.grid()
    
plt.savefig('gravitacio', dpi=300, bbox_inches='tight')
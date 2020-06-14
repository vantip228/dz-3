import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def plots(axs):
  x1 = np.random.rand(100)
  y1 = np.random.rand(100)
  x2 = x1 # + np.random.rand(100)/100
  y2 = y1 # + np.random.rand(100)/100
  x3 = x1 # + np.random.rand(100)/100
  y3 = y1 # + np.random.rand(100)/100
  x4 = np.random.rand(100)
  y4 = np.random.rand(100)
  x5 = x1 + np.random.rand(100)/100
  y5 = y1 + np.random.rand(100)/100

  (ax1, ax2, ax3, ax4) = axs
  for ax in axs:
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

  ax1.plot(x1, y1, 'o', color='#ff0000', markersize=1)
  ax2.plot(x2, y2, 'o', color='#00ff00', markersize=1)
  ax3.plot(x3, y3, 'o', color='#ffff00', markersize=1)

  # ax4.plot(x1, y1, 'o', color='#ff0000', markersize=1)
  # ax4.plot(x2, y2, 'o', color='#00ff00', markersize=1)
  ax4.plot(x3, y3, 'o', color='#ffff00', markersize=1)
  ax4.plot(x4, y4, 'o', color='#0000ff', markersize=1)
  ax4.plot(x5, y5, 'o', color='#0000ff', markersize=1)

plt.style.use('dark_background')
fig, axs = plt.subplots(4,2)

arr = list(zip(*axs))
plots(arr[0])
plots(arr[1])
# fig.tight_layout()

strs = ["PRB","PRA","PRA+\nPRB","PRA,\nPRB +\n DAPI"]
for ax, l in zip(arr[0], strs):
  ax.set_ylabel(l, rotation=0, labelpad=20)

plt.show()

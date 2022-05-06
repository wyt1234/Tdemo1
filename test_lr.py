from matplotlib import pyplot as plt
import numpy as np

warmup_step = 4000.0
init_lr = 0.01
lr_scheduler = lambda step: init_lr * warmup_step ** 0.5 * \
                            np.minimum((step + 1) * warmup_step ** -1.5, (step + 1) ** -0.5)

for i in range(1, 300):
    x = i * 1000
    y = lr_scheduler(x)
    print(y)

# xdata1 = [i for i in range(1, 300)]
# ydata1 = [lr_scheduler(i) for i in range(1, 300)]
# fig, ax = plt.subplots(1, 1, figsize=(9, 3))
# ax.plot(xdata1, ydata1)
# fig.suptitle('Categorical Plotting')
# plt.show()

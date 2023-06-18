import matplotlib.pyplot as plt
import numpy as np

def createHistGraph(probalities, categories_map):

    fig, axs = plt.subplots(probalities.shape[1])

    for category in range(probalities.shape[1]):
        col = (np.random.random(), np.random.random(), np.random.random())
        axs[category].hist(probalities[:, category], color=col, range=(1/probalities.shape[1], 1.01), label=list(categories_map.keys())[category])
        axs[category].legend()
from glob import glob

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

import rasterio as rio
from rasterio.plot import plotting_extent
from rasterio.plot import show
from rasterio.plot import reshape_as_raster, reshape_as_image

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from scipy.io import loadmat
from sklearn.metrics import classification_report, accuracy_score

import plotly.graph_objects as go

np.seterr(divide='ignore', invalid='ignore')

def getCategory(path):
    url = path.split("/")
    category = url[4]
    return category


def getParentImageNumber(path):
    url = path.split("/")
    category = url[5]
    return category


def getImagePartNumber(path):
    url = path.split("/")
    category = url[6]
    return category

def toGrouped(array):
    np_array = np.asarray(array)
    print(f"Shape of array is {np_array.shape}")
    grouped_items = []
    for i in np_array:
        tpl = (i, getCategory(i), getParentImageNumber(i), getImagePartNumber(i))
        grouped_items.append(tpl)

    return np.asarray(grouped_items)

def load_dataset5():
    from glob import glob

    S_sentinel_bands = glob("/tmp/shared/dataset_5/**/*B?*.tiff", recursive=True)
    S_sentinel_bands.sort()
    S_sentinel_bands

    grouped_items = toGrouped(S_sentinel_bands)

    return grouped_items


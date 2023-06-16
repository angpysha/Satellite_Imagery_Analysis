import btree
import numpy as np
## Input data should be like this [water, [forest, [field, city]]]

def create_tree(array):
    tree = btree.BTree(left=array[0])
    if isinstance(array[1], np.ndarray):
        tree.right = create_tree(array[1])
    else:
        tree.right = array[1]
    return tree
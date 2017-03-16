import glob
import numpy as np
import os

recover_numpy_path ="/home/chenyiru/FluxPreservation/experiments/1000_200_basic/result/*.npy"
files = glob.iglob(recover_numpy_path)
revert_save_dir = "/home/chenyiru/FluxPreservation/experiments/1000_200_basic/revertrecover/"

for i in files:
    print i
    filename = os.path.basename(i)
    MAX = 4
    MIN = - 0.1

    #used to revert the recovered the numpy array

    recover_numpy = np.load(i)
    revert_numpy = MIN + 1.0/10.0*(MAX-MIN)* np.sinh(3*recover_numpy)

    revert_save_path = revert_save_dir + filename

    np.save(revert_save_path, revert_numpy)





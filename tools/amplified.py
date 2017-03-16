import cv2
import numpy as np
import os
import glob

save_dir = "/Users/ruru/Dropbox/amplified/"
numpy_dir = "/Users/ruru/Dropbox/Flux/Tentuple/"

npy_path = "%s/*.npy"%(numpy_dir + "fits_threhold")
files =  glob.iglob(npy_path)

for i in files:

    filename = os.path.basename(i)[:-4]

    fits_threhold = np.load(i)
    fits_threhold = fits_threhold[:,:,1]
    jpg_fitsthrehold  = cv2.imread(numpy_dir + "fits_threhold/" + filename + ".jpg")
    jpg_fitsthrehold = jpg_fitsthrehold[0:424,0:424, ]

    revertrecover = np.load(numpy_dir + "revertrecover/" + filename +".npy")
    revertrecover = revertrecover[0:424,0:424,1]
    jpg_revertrecover = cv2.imread(numpy_dir + "revertrecover/" + filename +".jpg")
    jpg_revertrecover = jpg_revertrecover[0:424,0:424,]

    #keep the amplied
    jpg_revertrecover[fits_threhold < revertrecover] = 0
    jpg_fitsthrehold[fits_threhold < revertrecover] = 0

    jpg_revertrecover[fits_threhold > revertrecover] = 255
    jpg_fitsthrehold[fits_threhold > revertrecover] = 255

    save_path = save_dir + filename + "recover(diminished set to white & amplified set to black)" +".jpg"
    cv2.imwrite(save_path, jpg_revertrecover)

    save_path = save_dir + filename + "original(diminished set to white & amplified set to black))" + ".jpg"
    cv2.imwrite(save_path, jpg_fitsthrehold)






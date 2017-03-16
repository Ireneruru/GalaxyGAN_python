import numpy as np
import os
import pyfits
import glob

fits_dir = "/mnt/ds3lab/chenyiru/FluxPreservation/fits200"
fits_thresold_dir = "/home/chenyiru/FluxPreservation/experiments/1000_200_basic/fits_thresold/"
fits = '%s/*/*-g.fits'%(fits_dir)
files = glob.iglob(fits)

for i in files:
    print i
    file_name = os.path.basename(i)

    filename = file_name.replace("-g.fits", '')
    filename_g = '%s/%s/%s-g.fits'%(fits_dir,filename,filename)
    filename_r = '%s/%s/%s-r.fits'%(fits_dir,filename,filename)
    filename_i = '%s/%s/%s-i.fits'%(fits_dir,filename,filename)

    gfits = pyfits.open(filename_g)
    rfits = pyfits.open(filename_r)
    ifits = pyfits.open(filename_i)
    data_g = gfits[0].data
    data_r = rfits[0].data
    data_i = ifits[0].data

    figure_original = np.ones((data_g.shape[0],data_g.shape[1],3))
    figure_original[:,:,0] = data_g
    figure_original[:,:,1] = data_r
    figure_original[:,:,2] = data_i

    # thresold
    MAX = 4
    MIN = -0.1

    figure_original[figure_original<MIN]=MIN
    figure_original[figure_original>MAX]=MAX

    fits_thresold_path = fits_thresold_dir+ "fitsthresold"+filename

    np.save(fits_thresold_path,figure_original)
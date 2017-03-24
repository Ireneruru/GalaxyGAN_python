import numpy as np
import cv2
import os
import glob
import pyfits
import sys

original_fits_path = sys.argv[1]
recover_path = sys.argv[2]
analysis_save_dir = sys.argv[3]

if not os.path.exists(analysis_save_dir):
    os.makedirs(analysis_save_dir)

save_fits = 1
fits_threshold = 1
save_recover = 1
recover_recover = 1


#save original fits
if save_fits:
    if not os.path.exists(analysis_save_dir + "/original_fits"):
        os.system("mkdir %s" % analysis_save_dir + "/original_fits")
    os.system("cp -r %s %s" % (original_fits_path + "/*", analysis_save_dir +
              "/original_fits"))
    print "cp -r %s %s" % (original_fits_path + "/*", analysis_save_dir +
              "/original_fits")

#fits threshold
if fits_threshold:
    fits_dir = analysis_save_dir + "/original_fits"
    fits_thresold_dir = analysis_save_dir + "/fits_threshold"
    if not os.path.exists(fits_thresold_dir):
        os.system("mkdir %s" % fits_thresold_dir)
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

        fits_thresold_path = fits_thresold_dir+ "/" + filename +"_threshold"
        np.save(fits_thresold_path,figure_original)
        print fits_thresold_path

#save recover output
if save_recover:
    if not os.path.exists(analysis_save_dir + "/recover"):
        os.system("mkdir %s" % analysis_save_dir + "/recover" )
    os.system("cp -r %s %s" % (recover_path + "/*" , analysis_save_dir+"/recover"))

#recover original scale
if recover_recover:
    recover_numpy_path = recover_path + "/*.npy"
    files = glob.iglob(recover_numpy_path)
    revert_save_dir = analysis_save_dir + "/recover_originalscale"
    if not os.path.exists(revert_save_dir):
        os.system("mkdir %s" % revert_save_dir)

    for i in files:
        filename = os.path.basename(i)
        filename = filename[:-4]
        MAX = 4
        MIN = - 0.1

        #used to revert the recovered the numpy array
        recover_numpy = np.load(i)
        revert_numpy = MIN + 1.0/10.0*(MAX-MIN)* np.sinh(3*recover_numpy)

        revert_save_path = revert_save_dir + "/" + filename + "_recover_originalscale"
        print revert_save_path
        np.save(revert_save_path, revert_numpy)

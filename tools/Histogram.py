# Python program to load a FITS image and display it

# import needed extensions
from numpy import *
import matplotlib.pyplot as plt # plotting package
import matplotlib.cm as cm # colormaps
import pyfits
import glob
import os
import sys
import scipy.misc


# read in the file
# change input.fits to the name of your file
f = open("/home/chenyiru/FluxPreservation/tools/a", "w")
for npy in glob.glob("/home/chenyiru/FluxPreservation/experiments/1000_200_basic/revertrecover/*.npy"):
    img = load(npy)
    name = os.path.basename(npy)[:-4]
    fits_thresold_path = '/home/chenyiru/FluxPreservation/experiments/1000_200_basic/fits_thresold/fitsthresold%s.npy' % (name)
    h = load(fits_thresold_path)

    # copy the image data into a numpy (numerical python) array
    img_fits = h[0:424,0:424,1]
    img = img[0:424,0:424,1]
    '''
    plt.ion() # do plots in interactive mode
    colmap = plt.get_cmap('gray') # load gray colormap

    # plot the image on the screen
    plt.figure(1)
    plt.imshow(img, cmap=colmap) # plot image using gray colorbar
    '''
    # img is a 2-d array, need to change to 1-d to make a histogram
    #imgh = 1.0*img # make a copy
    nx, ny = img.shape # find the size of the array
    imgh = reshape(img, nx*ny) # change the shape to be 1d
    imgf = reshape(img_fits, nx*ny)


    # print some statistics about the image
    print name

    print 'Original Image minimum = ', min(imgf), 'Recoverd Image minimun = ', min(imgh)
    print 'Original Image maximum = ', max(imgf), 'Recoverd Image maximum = ', max(imgh)
    print 'Original Image mean = ', mean(imgf), 'Recoverd Image mean = ', mean(imgh)
    print 'Original standard deviation', std(imgf), 'Recoverd standard deviation = ', std(imgh)

    f.write(name +"\tomin\t" + str(std(imgh)) +"\trmin\t"+ str(min(imgh)) + "\tomax\t"+ str(max(imgf))+"\trmax\t" + str(max(imgh))+ "\tomean\t"+str(mean(imgf))+"\trmean\t" \
            + str(mean(imgh)) + "\todev\t" + str(std(imgf))+ "\trdev\t" + str(std(imgh)) +"\n")

    # now plot a histogram of the image values
    '''
    plt.figure(2)
    plt.xlabel('Pixel Values')
    plt.ylabel('Distribution')
    plt.yscale('log')
    plt.title( "y-axis log")
    plt.hist(imgh, bins=64, range=(-0.2,4.5), alpha=0.5, histtype='stepfilled', color="blue",label="recovered(original scale)")
    plt.hist(imgf, bins=64, range=(-0.2, 4.5),  alpha=0.5 ,histtype='stepfilled', color="red", label="original")
    plt.legend(loc='upper right')

    plt.savefig("/Users/ruru/Dropbox/histogram/%s_original&recover(original scale)_log.png" % name)

    plt.close()
    '''

    #plow = -0.1
    #phi = 4
    #q = where((imgh >= plow) & (imgh <= phi))
    #imghcut = imgh[q]

    #print 'Image minimum = ', min(imghcut)
    #print 'Image maximum = ', max(imghcut)
    #print 'Image mean = ', mean(imghcut)
    #print 'Image standard deviation = ', std(imghcut)


f.close()
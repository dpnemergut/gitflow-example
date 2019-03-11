import numpy as np
from astropy.io import fits

def mean_fits(iFitsFileList):
    for fitsFile in iFitsFileList:
        hdulist = fits.open(fitsFile)
        try:
            data = data + hdulist[0].data
        except NameError:
            data = hdulist[0].data

    return data/len(iFitsFileList)

if __name__ == '__main__':
    # Test your function with examples from the question
    data = mean_fits(['images/image0.fits', 'images/image1.fits', 'images/image2.fits'])
    print(data[100, 100])

    # You can also plot the result:
    import matplotlib.pyplot as plt
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()

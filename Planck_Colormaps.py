"""Create planck color maps for use with matplotlib.
Derived from the HEALPix IDL code. See
src/idl/visu/planck_colors.pro
in the HEALPix source for details."""

import numpy as np
import matplotlib.colors as colors

def _create_cmap(name, Itab, Rtab, Gtab, Btab) :
    """Helper function to create a color map from tabulated values copied
    from the HEALPix IDL code."""
    red = np.array([ Itab/255., Rtab/255., Rtab/255. ])
    blue = np.array([ Itab/255., Btab/255., Btab/255. ])
    green = np.array([ Itab/255., Gtab/255., Gtab/255. ])

    cdict = { 'red' : red.T, 'blue' : blue.T, 'green' : green.T }
    cmap = colors.LinearSegmentedColormap(name, cdict)
    cmap.set_bad('gray') # Arbitrary choice.
    cmap.set_under('white') # For use with healpy.mollview().
    return cmap


def create_cmap_planck_T () :
    """Planck temperature color map created by S. Colombi."""
    Itab = np.array([   0,  42,  85, 127, 170, 212, 255])
    Rtab = np.array([   0,   0,   0, 255, 255, 255, 100])
    Gtab = np.array([   0, 112, 221, 237, 180,  75,   0])
    Btab = np.array([ 255, 255, 255, 217,   0,   0,   0])
    return _create_cmap('PlanckT', Itab, Rtab, Gtab, Btab)

def create_cmap_planck_foreground () :
    """Planck foreground color map created by K. Gorski."""
    Itab = np.array([   0,  13,  26,  39,  52,  65,  76,  77,  88, 
                        101, 114, 127,   140, 153, 166, 179,   192, 
                        205, 218, 231, 255] )
    Rtab = np.array([   0,  10,  30,  80, 191, 228, 241, 241, 245, 
                        248, 249.9, 242.25,204, 165, 114, 127.5, 178.5, 
                        204, 229.5, 242.25, 252.45] )
    Gtab = np.array([   0,  20, 184, 235, 239, 240, 241, 241, 240, 
                        235, 204,   153,  76.5,  32,   0, 127.5, 178.5, 
                        204, 229.5, 242.25, 252.45] )
    Btab = np.array([ 255, 255, 255, 255, 250, 245, 212, 212, 175, 
                      130, 38.25, 12.75,  0,   32,  32, 153,   204, 
                      229.5, 242.25, 249.9, 255] )
    return _create_cmap('Planckfg', Itab, Rtab, Gtab, Btab)

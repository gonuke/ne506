import numpy as np

import direct_sampling as ds

def _randomDomain(num_bins, x_min, x_max):
    """
    Generate a set of randomly spaced bins within
    a specific domain
    
    inputs
    -------
    num_bins : Integer
        Number of histogram bins
    x_min : Real
        Minimum of the domain to be sampled
    x_max : Real
        Maximum of the domain to be sampled
        
    Returns
    --------
    bin_bounds : numpy array of Real
        bin boundaries
    """

    # some values to get moderate bin spacing
    max_bin_width = 0.75
    min_bin_width = 0.25
    
    bin_widths = ds.sampleUniform(min_bin_width, max_bin_width, 
                                  np.random.rand(num_bins))

    # insert the left edge of the first bin
    bin_bounds = np.insert(np.cumsum(bin_widths),0,0)
    # scale bins to fit desired domain
    bin_bounds = (x_max - x_min) * bin_bounds / bin_bounds[-1] + x_min
    
    return bin_bounds

def randomHistogram(num_bins=6, x_min=0, x_max=10):
    """
    Generate a random unnormalized histogram distribution 
    with a fixed number of random bin widths and random bin heights
    
    inputs
    -------
    num_bins : Integer
        Number of histogram bins
    x_min : Real
        Minimum of the domain to be sampled
    x_max : Real
        Maximum of the domain to be sampled
        
    Returns
    --------
    bin_bounds : list(Real)
        n_bins + 1 bin boundaries
    bin_heights : list(Real)
        bin heights
    """
    
    bin_bounds = _randomDomain(num_bins, x_min, x_max)    
    bin_heights = np.random.rand(num_bins)
    return bin_bounds, bin_heights

def randomLine(scale = 5):
    """
    Generate a random arbitrary linear distribution by defining
    two points (x1, p1) and (x2, p2)
    
    Paramters
    ---------
    scale : Real
        A scale length for the space between the x values
        
    Returns
    --------
    x : numpy array of 2 Real values
    p : numpy array of 2 Real values
   
    """
    
    # create a pair of x-values and ensure they are increasing by
    # forming the cumulative sum
    x = np.cumsum(np.random.rand(2))
    p = np.random.rand(2) 
    
    return x * scale, p

def randomPiecewiseLinear(num_bins=6, x_min=0, x_max=10):
    """
    Generate a random piecewise lienar distribution with 
    random bin widths and random bin heights
    
    inputs
    -------
    num_bins : Integer
        Number of histogram bins
    x_min : Real
        Minimum of the domain to be sampled
    x_max : Real
        Maximum of the domain to be sampled
        
    Returns
    --------
    bin_bounds : list(Real)
        n_bins + 1 bin boundaries
    bin_heights : list(Real)
        bin heights
    """

    bin_bounds = _randomDomain(num_bins, x_min, x_max)    
    bin_heights = np.random.rand(num_bins + 1)
    return bin_bounds, bin_heights
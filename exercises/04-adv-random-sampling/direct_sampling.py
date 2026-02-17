import numpy as np

# discrete distribution
def sampleDiscrete(x, p, prn):
    """
    Function to sample from a discrete distribution.
    
    Parameters
    ----------
    x : numpy array of Real
        possible values to be sampled
    p : numpy array of Real
        density function to be sampled
    prn : Real
        a pseudo-random number
        
    Returns
    --------
    Real value sampled from choices in x
    """
    if len(x) != len(p):
        raise ValueError(f'Number of choices ({len(x)}) must match number of probabilities ({len(p)}).')
    
    if np.any(p < 0):
        raise ValueError(f'All probabilities must be non-negative, but a negative probability was provided.')
    
    cdf = np.cumsum(p)
    cdf /= cdf[-1]
    
    bin = 0
    while prn > cdf[bin]:
        bin += 1
    
    return x[bin]
    
# uniform distribution
def sampleUniform(t_min, t_max, prn):
    """
    Function to sample a value from a PDF with 
    uniform probability in an arbitrary domain.
    
    Parameters
    ----------
    t_min : Real
        lower bound of the domain
    t_max : Real
        upper bound of the domain
    prn : Real
        a pseudo-random number
        
    Returns
    -------
    Real : a value on the domain between t_min and t_max        
    """
    return (t_max - t_min) * prn + t_min


# rising linear distribution
def sampleRisingLinear(t_min, t_max, prn):
    """
    Function to sample a value from a PDF with 
    a linear probability with a positive slope
    in an arbitrary domain.
   
    
    Parameters
    ----------
    t_min : Real
        Lower bound of the domain
    t_max : Real
        Upper bound of the domain
    prn : Real
        A pseudo-random number
        
    Returns
    -------
    Real : a value on the domain between t_min and t_max
    """
    return t_min + np.sqrt(prn) * (t_max - t_min)


# falling linear distribution
def sampleFallingLinear(t_min, t_max, prn):
    """
    Function to sample a value from a PDF with 
    a linear probability with a negative slope
    in an arbitrary domain.
    
    Parameters
    ----------
    t_min : Real
        Lower bound of the domain
    t_max : Real
        Upper bound of the domain
    prn : Real
        A pseudo-random number
        
    Returns
    -------
    Real : a value on the domain between t_min and t_max
    """
    return t_max - np.sqrt(prn) * (t_max - t_min)
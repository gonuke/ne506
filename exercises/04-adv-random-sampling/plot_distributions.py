import numpy as np
import matplotlib.pyplot as plt

def plotHistogram(x, p, samples=None, hist_bins=50):
    """
    Plot a defined histogram distribution and opptionally a histogram
    of a set of sampled values.
    
    Parameters
    -----------
    x : numpy array of Real
        bin boundaries for histogram
    p : numy array of Real
        bin heights for histogram
    samples : numpy array of Real
        sampled values to be plotted as a histogram
    hist_bins : Int
        number of bins for histogram
    """
    
    if len(p)+1 != len(x):
        raise ValueError(f'There must be one more bin boundary ({len(x)}) than probability ({len(p)}) ')
    
    plt.stairs(p,x, label="original distribution")
    
    if samples is not None:
        histogram_area = np.sum((x[1:] - x[:-1]) * p)
        hist, bin_edges = np.histogram(samples, hist_bins, density=True)
        plt.stairs(hist * histogram_area, bin_edges, label="sampled histogram")
    
    plt.ylim(0,1.1)
    plt.legend()
    plt.show()
    
def plotLine(x, p, samples=None, hist_bins=50):
    """
    Plot a line distribution and optionally a histogram
    of a set of sampled values.
    
    Parameters
    -----------
    x : numpy array of Real
        two values for the independent variable
    p : numy array of Real
        two values for the probability
    samples : numpy array of Real
        sampled values to be plotted as a histogram
    hist_bins : Int
        number of bins for histogram
    """
    
    if len(x) != 2 or len(p) != 2:
        ValueError(f'This plotting function expects a linear distribution with two '
                   f'({len(x)}) x-values and two ({len(p)}) probabilities.')
    
    plt.plot(x, p, label="original distribution")
        
    if samples is not None:
        linear_area = (x[1] - x[0]) * 0.5 * (p[1] + p[0])
        hist, bins = np.histogram(samples, 100, density=True)
        plt.stairs(hist * linear_area, bins, label="sampled distribution")
    
    plt.legend()
    plt.ylim(0,1.1)
    plt.show()
    
def plotPiecewiseLinear(x, p, samples=None, hist_bins=50):
    """
    Plot a piecewise linear distribution and optionally a histogram
    of a set of sampled values.
    
    Parameters
    -----------
    x : numpy array of Real
        the independent variable
    p : numy array of Real
        the corresponding probabilities
    samples : numpy array of Real
        sampled values to be plotted as a histogram
    hist_bins : Int
        number of bins for histogram
    """
    
    # some value checking
    if len(x) < 2:
        raise ValueError('There must be at least 3 points in the domain')
    if len(x) != len(p):
        raise ValueError(f'The number of domain points ({len(x)}) and PDF points ({len(p)}) must be the same')
    
    
    plt.plot(x,p, label="original distribution")
    
    if samples is not None:
        piecewise_area = np.sum( (x[1:] - x[:-1]) * 0.5 * (p[1:] + p[:-1]))
        hist, bins = np.histogram(samples, 100, density=True)
        plt.stairs(hist * piecewise_area , bins, label="sampled distribution")
    
    plt.ylim(0,1.1)
    plt.legend()
    plt.show()
    
def plotContinuous(x_min, x_max, pdf_fcn, bounding_fcn=None, samples=None, hist_bins=50):
    
    
    x = np.linspace(x_min, x_max, 1000, endpoint=True)
    pdf = pdf_fcn(x)
    plt.plot(x, pdf, label="original distribution")
    
    if bounding_fcn is not None:
        plt.plot(x, bounding_fcn(x), label="bounding function")
        
    if samples is not None:
        area_estimate = np.sum( (x[1:] - x[:-1]) * 0.5 * (pdf[1:] + pdf[:-1]))
        hist, bins = np.histogram(samples, 100, density=True)
        plt.stairs(hist * area_estimate, bins, label="sampled distribution")
    
    plt.legend()
    plt.show()
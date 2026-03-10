import numpy as np

from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d


def detect_peaks_glb(x : np.ndarray, Fs : int = 100, pk_height : float = 0.01):
    r"""
    Detect peaks with global threshold.
    
    Restructured from Sunny's code at https://github.com/SunnyCYC/CrossModalBeat/blob/main/genEST-LOC-ABT.py
    
    Args:
        x (np.ndarray): The novelty function to be detected, in the shape of a 1D array.
        Fs (int): Sampling frequency of the novelty function. E.g., 100.
        pk_height (float): Threshold height for peak detection (after gussian filter and normalization). Between 0 and 1. E.g., 0.01.
        
    Returns:
        est (np.ndarray): Estimated peak in seconds.
    """
    
    pk_prominence = 0.01  # Prominence threshold for peak detection. E.g., 0.01.
    pk_distance = 7       # Minimum distance between peaks in samples
    
    # Apply Gaussian filter to the novelty function
    x = gaussian_filter1d(x, sigma=3)
    x = x / x.max()

    # Find indices of peaks in the novelty function
    peaks_idx, _ = find_peaks(x, height = pk_height, 
                    distance = pk_distance, 
                    prominence = pk_prominence)
    
    # Convert indices of peaks to time in seconds
    est = peaks_idx / Fs
    
    return est
    
    

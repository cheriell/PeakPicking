import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d


def compute_local_average(x, M):
    r"""Compute local average of signal

    Notebook: C6/C6S1_NoveltySpectral.ipynb

    Args:
        x (np.ndarray): Signal
        M (int): Determines size (2M+1) in samples of centric window  used for local average

    Returns:
        local_average (np.ndarray): Local average signal
    """
    L = len(x)
    local_average = np.zeros(L)
    
    for m in range(L):
        a = max(m - M, 0)
        b = min(m + M + 1, L)
        local_average[m] = (1 / (2 * M + 1)) * np.sum(x[a:b])
        
    return local_average


def detect_peaks_loc(x : np.ndarray, Fs : int = 100, win_sec : float = 10.0):
    r"""
    Detect peaks with local threshold.
    
    Restructured from Sunny's code at https://github.com/SunnyCYC/CrossModalBeat/blob/main/genEST-LOC-ABT.py
    
    Args:
        x (np.ndarray): The novelty function to be detected, in the shape of a 1D array.
        Fs (int): Sampling frequency of the novelty function. E.g., 100.
        win_sec (float): Window size for local average in seconds. E.g., 5, 10, 20.
    
    Returns:
        est (np.ndarray): Estimated peak in seconds.
    """
    
    global_height = 0.01  # Global minimum height of the novelty function
    pk_distance = 7       # Minimum distance between peaks in samples
        
    # Apply Gaussian filter and normalize the novelty function
    x = gaussian_filter1d(x, sigma=3)
    x = x / x.max()
    
    # Compute local average of the novelty function
    M = int(np.ceil(win_sec * Fs))
    locav = compute_local_average(x, M)
    
    # Clip the local average with global min height
    locav = np.clip(locav, global_height, 1)
    
    # Find indices of peaks in the novelty function
    peaks_idx, _ = find_peaks(x, height = locav, distance = pk_distance)
    
    # Convert indices of peaks to time in seconds
    est = peaks_idx / Fs
    
    return est
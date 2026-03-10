# PeakPicking

This repository provides implementation for the peak picking algorithm with a local threshold set up in our paper [Cross-Modal Approaches to Beat Tracking: A Case Study on Chopin Mazurkas](https://transactions.ismir.net/articles/10.5334/tismir.238).

## Running instructions

### Peak picking with global threshold

    from peak_picking.glb import detect_peaks_glb
    est = detect_peaks_glb(x, Fs, pk_height)

where:

    Args:
        x (np.ndarray): The novelty function to be detected, in the shape of a 1D array.
        Fs (int): Sampling frequency of the novelty function. E.g., 100.
        pk_height (float): Threshold height for peak detection (after gussian filter and normalization). E.g., 0.01.
        
    Returns:
        est (np.ndarray): Estimated peak in seconds.

Please refer to [`./docs/example_usage_glb.ipynb`](./docs/example_usage_glb.ipynb) for example usage.

### Peak picking with local threshold

    from peak_picking.loc import detect_peaks_loc
    est = detect_peaks_loc(x, Fs, win_sec)
    
where:

    Args:
        x (np.ndarray): The novelty function to be detected, in the shape of a 1D array.
        Fs (int): Sampling frequency of the novelty function. E.g., 100.
        win_sec (float): Window size for local average in seconds. E.g., 5, 10, 20.

    Returns:
        est (np.ndarray): Estimated peak in seconds.

Please refer to [`./docs/example_usage_loc.ipynb`](./docs/example_usage_loc.ipynb) for example usage.
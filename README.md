# PeakPicking

This repository provides implementation for the peak picking algorithm with a local threshold set up in our paper [Cross-Modal Approaches to Beat Tracking: A Case Study on Chopin Mazurkas](https://transactions.ismir.net/articles/10.5334/tismir.238).

## Running instructions

    est = detect_peaks_loc(x, Fs, win_sec)
    
where:
- x: the novelty function, in the shape of a 1D array.
- Fs: the sampling frequency, in Hz.
- win_sec: the window size in seconds.

Returns:
- est: the estimated peak in seconds.

Please refer to `./docs/example_usage.ipynb` for example usage.
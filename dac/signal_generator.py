import numpy as np
import time

def get_sin_wave_amplitude(freq, current_time):
    value = np.sin(2 * np.pi * freq * current_time)
    normalized_value = (value + 1) / 2
    return normalized_value

def wait_for_sampling_period(sampling_frequency, last_sample_time):
    period = 1.0 / sampling_frequency
    next_sample_time = last_sample_time + period
    current_time = time.time()
    
    if next_sample_time > current_time:
        time.sleep(next_sample_time - current_time)
    
    return next_sample_time
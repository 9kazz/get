import numpy as np
import time

def get_sin_wave_amplitude(freq, current_time):
    value = np.sin(2 * np.pi * freq * current_time)
    normalized_value = (value + 1) / 2
    return normalized_value

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
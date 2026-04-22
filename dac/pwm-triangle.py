import pwm_dac as pwm
import signal_generator as sg
import time

def get_triangle_wave_amplitude(freq, current_time):
    period = 1.0 / freq
    time_in_period = current_time % period
    normalized_value = (time_in_period / period) * 2
    
    if normalized_value > 1:
        normalized_value = 2 - normalized_value
    
    return normalized_value

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, amplitude, False)
    
    start_time = time.time()
    next_sample_time = start_time
    
    while True:
        current_time = time.time() - start_time
        
        normalized_value = get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_value * amplitude
        
        dac.set_voltage(voltage)
        
        next_sample_time = sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
        
        if self.verbose:
            print(f"Инициализирован PWM ЦАП на пине {self.gpio_pin} с частотой {self.pwm_frequency} Гц")
    
    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
        
        if self.verbose:
            print("ШИМ остановлен, GPIO сброшены и очищены")
    
    def set_voltage(self, voltage):
        if voltage < 0 or voltage > self.dynamic_range:
            raise ValueError(f"Напряжение должно быть в диапазоне от 0 до {self.dynamic_range} В")
        
        duty_cycle = voltage / self.dynamic_range * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        
        if self.verbose:
            print(f"Установлено напряжение {voltage:.3f} В (duty cycle: {duty_cycle:.1f}%)")


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError as e:
                if "could not convert string to float" in str(e) or "invalid literal" in str(e):
                    print("Вы ввели не число. Попробуйте ещё раз\n")
                else:
                    print(f"{e}\n")
    
    finally:
        dac.deinit()
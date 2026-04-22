import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
        
        if self.verbose:
            print(f"Инициализирован R2R ЦАП на пинах {self.gpio_bits}")
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        
        if self.verbose:
            print("GPIO сброшены и очищены")
    
    def set_number(self, number):
        if number < 0 or number > 255:
            raise ValueError("Число должно быть в диапазоне от 0 до 255")
        
        binary = [int(bit) for bit in bin(number)[2:].zfill(8)]
        binary.reverse()
        
        GPIO.output(self.gpio_bits, binary)
        
        if self.verbose:
            print(f"Установлено число {number} (0b{bin(number)[2:].zfill(8)})")
    
    def set_voltage(self, voltage):
        if voltage < 0 or voltage > self.dynamic_range:
            raise ValueError(f"Напряжение должно быть в диапазоне от 0 до {self.dynamic_range} В")
        
        number = int(round(voltage / self.dynamic_range * 255))
        self.set_number(number)
        
        if self.verbose:
            actual_voltage = number / 255 * self.dynamic_range
            print(f"Установлено напряжение {actual_voltage:.3f} В")


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
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
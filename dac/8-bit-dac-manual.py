import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dynamic_range = 3.3
dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
gpio.setup(dac_bits, gpio.OUT)
gpio.output(dac_bits, 0)

def voltage2number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print("Напряжение выходит за динамический диапазон ЦАП (0 - {dynamic_range:.2f}) В")
        print("Устанавливаем 0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number2dac(number):
    bin_sig = [int(element) for element in bin(number)[2:].zfill(8)]
    gpio.output(dac_bits, bin_sig)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage2number(voltage)
            number2dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз:")

finally:
    gpio.output(dac_bits, 0)
    gpio.cleanup()
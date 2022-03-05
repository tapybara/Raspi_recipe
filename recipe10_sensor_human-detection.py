from shutil import register_unpack_format
from gpiozero import InputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

PIN_SR501 = 4

"取得間隔"
SAMPLING_TIME = 1.0

def main():
    factory = PiGPIOFactory()
    sr501 = InputDevice(PIN_SR501, pull_up=False, pin_factory=factory)

    try:
        while True:
            if sr501.is_active:
                print("Motion detected.")
            else:
                print("no movement.")
            sleep(SAMPLING_TIME)
    except KeyboardInterrupt:
        print("stop")

    return

if __name__ == "__main__":
    main()
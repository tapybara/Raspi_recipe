from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


#SWピンの設定
PIN_BTN1 = 5

def main():
    # SWピンを入力に設定（プルアップ設定）
    factory = PiGPIOFactory()
    btn = Button(PIN_BTN1, pull_up=True, pin_factory=factory)

    # スイッチを押している
    try:
        while True:
            if btn.is_pressed:
                print("ON")
            else:
                pass
            sleep(0.10)
    except KeyboardInterrupt:
        print("STOP")

    return

if __name__ == "__main__":
            main()
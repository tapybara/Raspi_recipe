from sys import displayhook
from gpiozero import LEDCharDisplay
from time import sleep

def main():
    # GPIOのBCM番号を7segLEDのa,b,c,d,e,f,dpの順でLEDCharDhisplayに格納）
    display = LEDCharDisplay(21, 20, 16, 22, 23, 24, 12, dp = 25)

    for char in '321G0':
        display.value = char
        sleep (1)

        display.off()

if __name__ == "__main__":
            main()
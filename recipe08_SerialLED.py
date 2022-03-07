import time
import board
import neopixel

# PIN, LED数
PIN_PIXEL = board.D18
NUM_PIXELS = 8 

def main():
    ORDER = neopixel.GRB
    pixels = neopixel.NeoPixel(PIN_PIXEL, NUM_PIXELS, brightness=0.010, auto_write=False, pixel_order=ORDER)

    # 0番目をRED指定
    pixels[0] = (255, 0, 0)
    # 1番目をGREEN指定
    pixels[1] = (0, 255, 0)
    # 2番目をBLUE指定
    pixels[2] = (0, 0, 255)
    # 3番目をWHITE指定
    pixels[3] = (255, 255, 255)

    # LEDの状態を更新(ここで点灯)
    pixels.show()
    time.sleep(5)

    # 消灯
    pixels.fill((0, 0, 0))
    pixels.show()


if __name__ == "__main__":
    main()
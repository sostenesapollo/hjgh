from pynput.keyboard import Key, Controller
import time

k = Controller()

#k.press(Key.cmd)

#keyboard.type("texto")
#keyboard.press(key.tab)

with k.pressed(Key.cmd):
    k.press('1')
    k.release('1')

time.sleep(2)

k.type('Sóstenes Apollo')
k.press(Key.tab)
k.press(Key.tab)
k.type('99988284904')
k.press(Key.tab)
k.type('Rua do mangueirão, 354, Vila Alecrim')
k.press(Key.tab)
k.press(Key.tab)
k.type("m")

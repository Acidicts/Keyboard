import board
import busio

from kmk.kmkkeyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes

NUM_LEDS = 84

COL_PINS = {
    0:  "GP11",
    1:  "GP12",
    2:  "GP13",
    3:  "GP14",
    4:  "GP15",
    5:  "GP16",
    6:  "GP17",
    7:  "GP18",
    8:  "GP19",
    9:  "GP20",
    10: "GP21",
    11: "GP22",
    12: "GP23",
    13: "GP24",
    14: "GP25",
}

ROW_PINS = {
    0: "GP5",
    1: "GP6",
    2: "GP7",
    3: "GP8",
    4: "GP9",
    5: "GP10",
}

missing = [f"col {k}" for k, v in COL_PINS.items() if not v] + \
          [f"row {k}" for k, v in ROW_PINS.items() if not v]
if missing:
    raise ValueError("Fill in these pins in code.py: " + ", ".join(missing))

keyboard = KMKKeyboard()

keyboard.col_pins = tuple(getattr(board, COL_PINS[i]) for i in range(len(COL_PINS)))
keyboard.row_pins = tuple(getattr(board, ROW_PINS[i]) for i in range(len(ROW_PINS)))

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP3, board.GP4, None, False),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, None),),
    ((KC.BRID, KC.BRIU, None),),
]

i2c_bus = busio.I2C(board.GP1, board.GP0)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    display=driver,
    width=128,
    height=32,
    flip=False,
    brightness=0.8,
    dim_time=20,
    dim_target=0.1,
    off_time=60,
)
display.entries = [
    TextEntry(text='Layer:', x=0, y=0),
    TextEntry(text='BASE', x=48, y=0, layer=0),
    TextEntry(text='FN', x=48, y=0, layer=1),
]
keyboard.extensions.append(display)

rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=NUM_LEDS,
    rgb_order=(1, 0, 2),
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=60,
    animation_mode=AnimationModes.RAINBOW,
    animation_speed=1,
)
keyboard.extensions.append(rgb)

XXXXXXX = KC.NO
_______ = KC.TRNS

keyboard.keymap = [
    [
        [KC.ESC,  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.DEL,  KC.MUTE],
        [KC.GRV,  KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,KC.EQL, KC.BSPC, KC.PGUP],
        [KC.TAB,  KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,KC.RBRC,KC.BSLS, KC.PGDN],
        [KC.CAPS, KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,KC.ENT, XXXXXXX, KC.HOME],
        [KC.LSFT, KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.RSFT,KC.UP,  XXXXXXX, KC.END],
        [KC.LCTL, KC.LALT,KC.LGUI,KC.SPC, XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,KC.RGUI,KC.MO(1),KC.RCTL,KC.LEFT,KC.DOWN, KC.RIGHT],
    ],
    [[_______ for _ in range(15)] for _ in range(6)],
]

if __name__ == '__main__':
    keyboard.go()
import time
import usb_hid
import digitalio
import board
import neopixel
import microcontroller
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Configure "fuse" button on pin 29
fuse_button = digitalio.DigitalInOut(board.GP29)
fuse_button.direction = digitalio.Direction.INPUT
fuse_button.pull = digitalio.Pull.UP

# Configure NeoPixel LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

def toggle_mount():
    """Toggles the mount state by modifying the non-volatile memory and resetting the microcontroller."""
    microcontroller.nvm[0] = int(not microcontroller.nvm[0])
    microcontroller.reset()

# Change evil mode to read/write 
if not microcontroller.nvm[0]:
    if not fuse_button.value:
        # Blink green LED twice
        for _ in range(2):
            pixel[0] = (0, 255, 0)
            time.sleep(0.3)
            pixel[0] = (0, 0, 0)
            time.sleep(0.3)
        toggle_mount()

# Change read/write to evil mode
if microcontroller.nvm[0]:
    pixel[0] = (0, 255, 0)
    time.sleep(0.5)
    pixel[0] = (0, 0, 0)
    time.sleep(0.5)
    while fuse_button.value:
        pass
    
    # Blink red LED four times
    for _ in range(4):
        pixel[0] = (255, 0, 0)
        time.sleep(0.3)
        pixel[0] = (0, 0, 0)
        time.sleep(0.3)
    
    toggle_mount()

# Blink blue LED two times, rubber ducky is ready
for _ in range(2):
    pixel[0] = (0, 0, 255)
    time.sleep(0.5)
    pixel[0] = (0, 0, 0)
    time.sleep(0.5)

# Mapping of special keys
SPECIAL_KEYS = {
    "ENTER": Keycode.ENTER,
    "RETURN": Keycode.RETURN,
    "WIN": Keycode.WINDOWS,
    "R": Keycode.R,
    "TAB": Keycode.TAB,
    "CTRL": Keycode.CONTROL,
    "ALT": Keycode.ALT,
    "DELETE": Keycode.DELETE,
    "SPACE": Keycode.SPACE,
    "ESC": Keycode.ESCAPE,
    "BACKSPACE": Keycode.BACKSPACE,
    "LCTRL": Keycode.LEFT_CONTROL,
    "RCTRL": Keycode.RIGHT_CONTROL,
    "LSHIFT": Keycode.LEFT_SHIFT,
    "RSHIFT": Keycode.RIGHT_SHIFT,
    "LALT": Keycode.LEFT_ALT,
    "RALT": Keycode.RIGHT_ALT,
    "A": Keycode.A,
    "B": Keycode.B,
    "C": Keycode.C,
    "D": Keycode.D,
    "E": Keycode.E,
    "F": Keycode.F,
    "G": Keycode.G,
    "H": Keycode.H,
    "I": Keycode.I,
    "J": Keycode.J,
    "K": Keycode.K,
    "L": Keycode.L,
    "M": Keycode.M,
    "N": Keycode.N,
    "O": Keycode.O,
    "P": Keycode.P,
    "Q": Keycode.Q,
    "S": Keycode.S,
    "T": Keycode.T,
    "U": Keycode.U,
    "V": Keycode.V,
    "W": Keycode.W,
    "X": Keycode.X,
    "Y": Keycode.Y,
    "Z": Keycode.Z,
    "ONE": Keycode.ONE,
    "TWO": Keycode.TWO,
    "THREE": Keycode.THREE,
    "FOUR": Keycode.FOUR,
    "FIVE": Keycode.FIVE,
    "SIX": Keycode.SIX,
    "SEVEN": Keycode.SEVEN,
    "EIGHT": Keycode.EIGHT,
    "NINE": Keycode.NINE,
    "ZERO": Keycode.ZERO,
    "MINUS": Keycode.MINUS,
    "EQUALS": Keycode.EQUALS,
    "LEFT_BRACKET": Keycode.LEFT_BRACKET,
    "RIGHT_BRACKET": Keycode.RIGHT_BRACKET,
    "BACKSLASH": Keycode.BACKSLASH,
    "POUND": Keycode.POUND,
    "SEMICOLON": Keycode.SEMICOLON,
    "QUOTE": Keycode.QUOTE,
    "GRAVE_ACCENT": Keycode.GRAVE_ACCENT,
    "COMMA": Keycode.COMMA,
    "PERIOD": Keycode.PERIOD,
    "FORWARD_SLASH": Keycode.FORWARD_SLASH,
    "CAPS_LOCK": Keycode.CAPS_LOCK,
    "F1": Keycode.F1,
    "F2": Keycode.F2,
    "F3": Keycode.F3,
    "F4": Keycode.F4,
    "F5": Keycode.F5,
    "F6": Keycode.F6,
    "F7": Keycode.F7,
    "F8": Keycode.F8,
    "F9": Keycode.F9,
    "F10": Keycode.F10,
    "F11": Keycode.F11,
    "F12": Keycode.F12,
    "PRINT_SCREEN": Keycode.PRINT_SCREEN,
    "SCROLL_LOCK": Keycode.SCROLL_LOCK,
    "PAUSE": Keycode.PAUSE,
    "INSERT": Keycode.INSERT,
    "HOME": Keycode.HOME,
    "PAGE_UP": Keycode.PAGE_UP,
    "END": Keycode.END,
    "PAGE_DOWN": Keycode.PAGE_DOWN,
    "RIGHT_ARROW": Keycode.RIGHT_ARROW,
    "LEFT_ARROW": Keycode.LEFT_ARROW,
    "DOWN_ARROW": Keycode.DOWN_ARROW,
    "UP_ARROW": Keycode.UP_ARROW,
    "KEYPAD_NUMLOCK": Keycode.KEYPAD_NUMLOCK,
    "KEYPAD_FORWARD_SLASH": Keycode.KEYPAD_FORWARD_SLASH,
    "KEYPAD_ASTERISK": Keycode.KEYPAD_ASTERISK,
    "KEYPAD_MINUS": Keycode.KEYPAD_MINUS,
    "KEYPAD_PLUS": Keycode.KEYPAD_PLUS,
    "KEYPAD_ENTER": Keycode.KEYPAD_ENTER,
    "KEYPAD_ONE": Keycode.KEYPAD_ONE,
    "KEYPAD_TWO": Keycode.KEYPAD_TWO,
    "KEYPAD_THREE": Keycode.KEYPAD_THREE,
    "KEYPAD_FOUR": Keycode.KEYPAD_FOUR,
    "KEYPAD_FIVE": Keycode.KEYPAD_FIVE,
    "KEYPAD_SIX": Keycode.KEYPAD_SIX,
    "KEYPAD_SEVEN": Keycode.KEYPAD_SEVEN,
    "KEYPAD_EIGHT": Keycode.KEYPAD_EIGHT,
    "KEYPAD_NINE": Keycode.KEYPAD_NINE,
    "KEYPAD_ZERO": Keycode.KEYPAD_ZERO,
    "KEYPAD_PERIOD": Keycode.KEYPAD_PERIOD,
    "KEYPAD_BACKSLASH": Keycode.KEYPAD_BACKSLASH,
    "APPLICATION": Keycode.APPLICATION,
    "POWER": Keycode.POWER,
    "KEYPAD_EQUALS": Keycode.KEYPAD_EQUALS,
    "F13": Keycode.F13,
    "F14": Keycode.F14,
    "F15": Keycode.F15,
    "F16": Keycode.F16,
    "F17": Keycode.F17,
    "F18": Keycode.F18,
    "F19": Keycode.F19,
    "F20": Keycode.F20,
    "F21": Keycode.F21,
    "F22": Keycode.F22,
    "F23": Keycode.F23,
    "F24": Keycode.F24,
    "CONTROL": Keycode.CONTROL,
    "LEFT_SHIFT": Keycode.LEFT_SHIFT,
    "SHIFT": Keycode.SHIFT,
    "LEFT_ALT": Keycode.LEFT_ALT,
    "OPTION": Keycode.OPTION,
    "LEFT_GUI": Keycode.LEFT_GUI,
    "GUI": Keycode.GUI,
    "WINDOWS": Keycode.WINDOWS,
    "COMMAND": Keycode.COMMAND,
    "RIGHT_CONTROL": Keycode.RIGHT_CONTROL,
    "RIGHT_SHIFT": Keycode.RIGHT_SHIFT,
    "RIGHT_ALT": Keycode.RIGHT_ALT,
}

# Initializing the HID keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Script file with commands
SCRIPT_FILE = "script.txt"


def send_text_as_keystrokes(text):
    """Sends text as simulated key presses."""
    for char in text:
        keyboard_layout.write(char)
        time.sleep(0.01)


def send_special_key(command):
    """Sends a special key or key combination based on the command."""
    keys = command.split("+")
    keycodes = [SPECIAL_KEYS[key] for key in keys if key in SPECIAL_KEYS]

    if keycodes:
        keyboard.press(*keycodes)
        time.sleep(0.1)
        keyboard.release_all()
        time.sleep(0.1)


def read_script_file(filename):
    """Reads the file and sends its content as keyboard input."""
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith("[") and line.endswith("]"):
                    # Special key combination
                    command = line[1:-1].upper()
                    send_special_key(command)
                else:
                    # Regular text
                    send_text_as_keystrokes(line)
                time.sleep(0.2)
    except OSError:
        print(f"Cannot open file: {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Run the function to read the script file
read_script_file(SCRIPT_FILE)

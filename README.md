
# Automated Keyboard Emulator

This Python script simulates keyboard input based on a predefined script file. The script reads a file (`script.txt`) containing both text and special key combinations, then sends them as keystrokes to the connected computer via USB HID.

### Features:
- **Text Input Simulation**: Sends text as regular keystrokes.
- **Special Key Simulation**: Supports sending special key combinations such as `CTRL+C`, `ALT+TAB`, `ENTER`, and more.
- **Configurable Input**: The input is read from a `script.txt` file, which can contain both text and key combinations.
- **USB HID Compatibility**: Works with USB HID devices to simulate a real keyboard.

### Requirements:
To run this script, you need to ensure that your environment is set up with the appropriate HID libraries for keyboard emulation.

### Usage:
1. **Script File**: Create a `script.txt` file where you specify the keystrokes or special key combinations. Example:
   - Regular text: `Hello, world!`
   - Special key: `[CTRL+ALT+DEL]`
   
   The script will read this file and send the corresponding keystrokes to the computer.

2. **Run the Script**: 
   - After setting up the `script.txt` file, CircuitPython run automatically script. The keystrokes will be sent as if typed by an actual keyboard.

### Example of `script.txt`:

```txt
[WIN+R]
https://www.youtube.com/watch?v=xvFZjo5PgG0
[ENTER]
```

### Key Mappings:
This script supports a wide range of keys, including:
- **Function Keys**: `F1`, `F2`, ..., `F24`
- **Arrow Keys**: `UP_ARROW`, `DOWN_ARROW`, `LEFT_ARROW`, `RIGHT_ARROW`
- **Special Keys**: `ENTER`, `ESC`, `TAB`, `SPACE`, `BACKSPACE`, etc.
- **Control Keys**: `CTRL`, `ALT`, `SHIFT`, `WINDOWS`, `COMMAND`, etc.
- **Number Pad Keys**: `KEYPAD_ONE`, `KEYPAD_TWO`, etc.

### Notes:
- Ensure that your device is capable of using USB HID (e.g., a microcontroller like an Adafruit Feather or Raspberry Pi Pico).
- The script sends simulated keystrokes to the computer as if they were typed by a physical keyboard.

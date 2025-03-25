# Automated Keyboard Emulator

This Python script simulates keyboard input based on a predefined script file. The script reads a file (`script.txt`) containing both text and special key combinations, then sends them as keystrokes to the connected computer via USB HID.

### Features:
- **Text Input Simulation**: Sends text as regular keystrokes.
- **Special Key Simulation**: Supports sending special key combinations such as `CTRL+C`, `ALT+TAB`, `ENTER`, and more.
- **Configurable Input**: The input is read from a `script.txt` file, which can contain both text and key combinations.
- **USB HID Compatibility**: Works with USB HID devices to simulate a real keyboard.
- **Built-in Safety Mechanism**: A fuse mechanism (on pin GP29) prevents execution if the fuse is not intact, indicated by a flashing red LED.

### Requirements:
- Microcontroller with HID support
- CircuitPython with `adafruit_hid` library installed
- `script.txt` file to define the keystrokes

### Usage:
1. **Script File**: Create a `script.txt` file where you specify the keystrokes or special key combinations. Example:
   - Regular text: `Hello, world!`
   - Special key: `[CTRL+ALT+DEL]`
   
   The script will read this file and send the corresponding keystrokes to the computer.

2. **Running the Script**:
   - Ensure the microcontroller is connected via USB.
   - If the safety fuse (GP29) is intact, the script will execute and send keystrokes.
   - If the fuse is broken, the built-in NeoPixel LED will flash red, and execution will halt.
   
3. **Example of `script.txt`**:

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

### Safety Feature:
- The script includes a hardware safety mechanism using a digital input on `GP29`. If the fuse is detected as broken (`LOW` signal), the execution halts, and a flashing red LED warns the user.

### Notes:
- Ensure that your device is capable of using USB HID (e.g., an RP2040-based board).
- The script sends simulated keystrokes to the computer as if they were typed by a physical keyboard.

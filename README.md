# Rubber Ducky Emulator for RP2040

This Python script turns an RP2040-based microcontroller into a USB Rubber Ducky-style keyboard emulator. It reads keystrokes from a predefined script file (`script.txt`) and simulates them as if they were typed by a real keyboard.

## Features

- **Automated Keystroke Injection** – Simulates text input and special key combinations.
- **Customizable Payloads** – Reads input commands from `script.txt`.
- **HID USB Compatibility** – Works with CircuitPython-supported HID devices.
- **Safety Mechanism** – A fuse button (GP29) prevents execution if pressed, indicated by flashing LED.
- **LED Status Indicators** – Uses the built-in NeoPixel LED for feedback.
- **Persistent Evil Mode** – Can toggle between normal and "evil" mode via non-volatile memory.
- **Sleep Command** – Supports a sleep command to pause execution for a specified duration.

## Requirements

- **Microcontroller**: RP2040-based board with USB HID support.
- **CircuitPython**: Installed with the `adafruit_hid` library.
- **Script File**: A `script.txt` file to define the keystrokes.

## How It Works

1. **Prepare the Script File**
   - The script reads from `script.txt`, which can include text and special key combinations.
   - Example:
     ```txt
     [WIN+R]
     [SLEEP 0.5]
     https://www.youtube.com/watch?v=xvFZjo5PgG0
     [ENTER]
     ```
   - **Sleep Command**: The `[SLEEP <time>]` command pauses execution for the specified number of seconds. Example: `[SLEEP 2]` will pause the script for 2 seconds before proceeding.

2. **Execution Process**
   - If the fuse button (GP29) is **not pressed** while starting, you are in selected mode.
   - While the device is starting, if the fuse button is **pressed**, you can change device mode.
   - LED status indicators:
     - 🟢 Green: 
        - 1 x blink: device in write/read mode (you can paste something to `script.txt`)
        - 2 x blink: changing evil mode to read/write
     - 🔴 Red:
        - 4 x blink: changing read/write mode to evil
     - 🔵 Blue:
        - 2 x blink: ready to execute

3. **Toggle Evil Mode**
   - Uses **non-volatile memory (NVM)** to switch between normal and "evil" mode.
   - Resets the microcontroller to apply changes.

4. **Sleep Command**
   - When a `[SLEEP <time>]` command is encountered in the script, the device pauses for the specified time in seconds. 
   - Example: `[SLEEP 5]` will pause for 5 seconds before continuing.

## Key Mappings

Supports a wide range of keys, including:

- **Function Keys**: `F1`–`F24`
- **Arrow Keys**: `UP_ARROW`, `DOWN_ARROW`, `LEFT_ARROW`, `RIGHT_ARROW`
- **Modifier Keys**: `CTRL`, `ALT`, `SHIFT`, `WINDOWS`, `COMMAND`
- **Special Keys**: `ENTER`, `ESC`, `TAB`, `SPACE`, `BACKSPACE`, `DELETE`, etc.
- **Numpad Keys**: `KEYPAD_ONE`, `KEYPAD_TWO`, etc.

## Notes

- Ensure your board supports USB HID (e.g., RP2040-based devices).
- The script executes keyboard commands **as if a human were typing them**, so use responsibly.
- The **sleep functionality** allows you to introduce pauses between actions in the script, which can be useful for timing-based operations or delaying actions.

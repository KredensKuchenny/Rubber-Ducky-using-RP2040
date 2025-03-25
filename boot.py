import storage
import microcontroller

if microcontroller.nvm[0] == 1:
  storage.enable_usb_drive()
else:
  storage.disable_usb_drive()
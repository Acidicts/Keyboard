# Keyboard

<img width="928" height="478" alt="image" src="https://github.com/user-attachments/assets/c0e37ced-7282-4d68-af96-1306a1b99b62" />
<img width="943" height="886" alt="Screenshot 2026-10-06 at 18 10 29" src="https://github.com/user-attachments/assets/c1622854-7cb4-44c2-8616-d82531954a9a" />
<img width="967" height="519" alt="image" src="https://github.com/user-attachments/assets/e205b905-674b-49c5-9a3e-9fcf0132d3e4" />

Sooo, this is a keyboard with a fun little oled display (via i2c) and rotary encoder with some rgb leds, following a modified ansi layout: `"` and `@` are swapped

### Features
- Powered via usb-c
- Wired keyboard
- RP2354A (2MB on onboard memory)

### Assembly
- The case is a bit bigger than most 3d printers so you may need a 3rd party service for it
1. I recommend using PCBA for the top layer as those parts may be difficult to solder
2. On arrival of your half made pcb, start with soldering on the diodes facing in the direction of the silkscreen diagram
3. After solder on the rgb leds matching the notch up to the silkscreen too
4. Finally solder on your key switches to the board (I didn't want to give anyone the pain of manually soldering hot swaps on)
5. Put on your keycaps to key switches
6. Use a soldering iron to put in a m3 heat insert into the hole in the case
7. Put the pcb in the case
8. use a m3 screw to firmly mount to case but be wary of the underneath components so use spacers for it

### Case
[case](/case/Case.step)

### Firmware
1. Download the latest release of circuitpython from [here](https://downloads.circuitpython.org/bin/seeeduino_xiao_rp2040/en_GB/adafruit-circuitpython-seeeduino_xiao_rp2040-en_GB-10.3.0.uf2)
2. whilst powering the board (by plugging in usbc) hold down the boot button(labelled as `SW1` and plug it into your computer. The board should show up as a USB drive called `RPI-RP2` or something similar.
3. Drag and drop the downloaded UF2 file onto the `RPI-RP2` drive. The board will reboot and show up as a USB drive called `CIRCUITPY`.
4. drag and drop the contents of the [`firmware`](./firmware) folder onto the `CIRCUITPY` drive.
5. Restart the board and it should now be ready to use.

### BOMs
| Name | Link |
| --- | --- |
| PCBA (included in addition parts) | [here](./BOMS/jlcpcb_pcb_BOM.csv) |
| LCSC List (included in addition parts) | [here](./BOMS/LCSC_BOM.csv) |
| Additional Parts | [here](./BOMS/Extra_Part_BOM.csv) |

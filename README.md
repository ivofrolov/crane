### Bastl Kastle Build Environment

Platformio project to build different flavours of [Bastl Instruments Kastle](https://github.com/bastl-instruments/kastle) which are organized in Arduino sketchbook manner.

It works by replacing default project source directory variable with `custom_src_dir` option from [platformio.ini](platformio.ini) `[env]` section before target runs.

So, for example, in order to build Kastle Drum firmware you should define paltformio project settings as follows

``` ini
[env]
platform = atmelavr
board = attiny85
framework = arduino
extra_scripts = pre:choose_src_dir.py
; and other shared options

[env:drum]
custom_src_dir = kastle/kastleDrum
src_filter = +<*> -<bastlAttinySamples/>

[env:clk]
custom_src_dir = kastle/kastleDRUM_CLK_LFO
```

then run `pio run -e drum` and `pio run -e clk` to build VCO and LFO.

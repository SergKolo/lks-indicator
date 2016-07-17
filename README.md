# lks-indicator

Indicator to display status of lock keys (Caps, Scroll, Num) for Linux (using AppIndicator).

GIF demonstration of lks-indicator:

![GIF demonstration of lks-indicator](http://i.imgur.com/FxSae8c.gif)

Licensed under the MIT license.

## Installation

- Download [ZIP](https://github.com/SergKolo/lks-indicator/archive/master.zip) and extract.

- Run `lock_keys_status.py`.

- Add `python /path/to/lock_keys_status.py` to system startup.

## Usage

When none of Scroll, Caps or Num lock are pressed, the circle will be green.

When one is pressed, the circle becomes red, and the following is displayed:

- *\[C\]* for *Caps Lock*
- *\[N\]* for *Num Lock*
- *\[S\]* for *Scroll Lock*

**Exiting:**

Click on the circle and choose *Quit*.

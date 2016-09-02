# lks-indicator

lks-indicator is an indicator app for Linux that displays status of Lock keys (Scroll, Caps and Num) in the panel.

It was originally written for Ubuntu Unity, and has been tested on Ubuntu 16.04 and Ubuntu Kylin 14.04, and Xubuntu 16.04.

Still, it will run fine on any desktop/distro that supports AppIndicator.

Screenshot with monochrome icon ( `-m` option )

![Screenshot](http://i.imgur.com/wJ23PwZ.png)

Regular ( red and green icons )

![Screenshot 2](http://i.imgur.com/9FmG65T.png)

## Motivation for the project

Originally this had been written as an answer for ByteCommander's question at [AskUbuntu](http://askubuntu.com): [Keyboard LED panel indicator for Unity Desktop](http://askubuntu.com/q/796985/295286). Eventually it has been decided to turn it into standalone project.


## Installation

### [![Ubuntu](https://www.pylint.org/assets/img/ubuntu.png)](https://ubuntu.com) Ubuntu and Debian

Debian/Ubuntu `deb` package: [Download `lks-indicator.deb`](https://github.com/SergKolo/lks-indicator/raw/master/debian/lks-indicator.deb)

### Manual

Run the included install script:

    sudo sh install.sh

And to uninstall:

    sudo sh install.sh --uninstall

## Usage
```
usage: lks-indicator [-h] [--show-all] [-m]
                     [--ignore-keys IGNORE_KEYS [IGNORE_KEYS ...]]

lks-indicator - Indicates on/off status of Lock keys.

optional arguments:
  -h, --help            show this help message and exit
  --show-all            Show all keys in label
  -m, --monochrome      Use monochrome icon
  --ignore-keys IGNORE_KEYS [IGNORE_KEYS ...]
                        Ignore specified keys (C, N or S)
```
### Overview of options and behavior

When none of Scroll, Caps or Num lock are pressed, the indicator will be green.

When one or more lock keys are active, the indicator becomes red, and the following is displayed:

- *\[C\]* for *Caps Lock*
- *\[N\]* for *Num Lock*
- *\[S\]* for *Scroll Lock*



The indicator menu has only one option - closing the indicator (*Quit*).

`--show-all` option will show all keys on the indicator and put specific letter into 
brackets do indicate that lock key being active.


`--ignore-keys` takes one or more capital letters C,N, or S separated by space, e.g. 
`--ignore-keys C N`. If this option is used, the indicator will ignore those keys being
activated 

## License

The indicator is provided under MIT license, copy of which is included with the source code

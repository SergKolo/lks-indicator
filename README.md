# lks-indicator

lks-indicator is an indicator app for Linux that displays status of Lock keys (Scroll, Caps and Num) in the panel.

It was originally written for Ubuntu Unity, and has been tested on Ubuntu 16.04 and Ubuntu Kylin 14.04, and Xubuntu 16.04.

Still, it will run fine on any desktop/distro that supports AppIndicator.

## Motivation for the project

Originally this had been written as an answer for ByteCommander's question at [AskUbuntu](http://askubuntu.com): [Keyboard LED panel indicator for Unity Desktop](http://askubuntu.com/q/796985/295286). Eventually it has been decided to turn it into standalone project.

## Demo
GIF demonstration of lks-indicator:

[![GIF demonstration of lks-indicator](http://i.imgur.com/FxSae8c.gif)](http://i.imgur.com/FxSae8c.gif)

## Installation

### [![Ubuntu](https://www.pylint.org/assets/img/ubuntu.png)](https://ubuntu.com) Ubuntu and Debian

Debian/Ubuntu `deb` package: [Download `lks-indicator-git.deb`](https://github.com/SergKolo/lks-indicator/raw/master/debian/lks-indicator-git.deb)

### Manual

Run the included install script:

    sudo sh install.sh

And to uninstall:

    sudo sh install.sh --uninstall

## Usage

When none of Scroll, Caps or Num lock are pressed, the indicator will be green.

When one or more lock keys are active, the indicator becomes red, and the following is displayed:

- *\[C\]* for *Caps Lock*
- *\[N\]* for *Num Lock*
- *\[S\]* for *Scroll Lock*

The indicator menu has only one option - closing the indicator (*Quit*).

The program has an option, `--show-all`, which makes it run so:

[![show-all no key pressed](http://i.imgur.com/LFmhJQ8.png)](http://i.imgur.com/LFmhJQ8.png)


[![show-all numlock on](http://i.imgur.com/CUnnsbh.png)](http://i.imgur.com/CUnnsbh.png)

## License

The indicator is provided under MIT license, copy of which is included with the source code

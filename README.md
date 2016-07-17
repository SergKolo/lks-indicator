#lks-indicator

##Description
Lock Keys Status indicator displays status of the Caps, Num, or Scroll lock keys. It is written for Ubuntu with Unity desktop , and has been tested on Ubuntu 16.04 and Ubuntu Kylin 14.04 , although Xubuntu users also have reported it as working.

## Motivation for the project
Originally this has been written as an answer for ByteCommander's question on Ask Ubuntu site: [Keyboard LED panel indicator for Unity Desktop](http://askubuntu.com/q/796985/295286) . Eventually it has been decided to turn it into standalone project. 

## Demo
GIF demonstration of lks-indicator:

![GIF demonstration of lks-indicator](http://i.imgur.com/FxSae8c.gif)

## Installation
For those who have git installed:

1. `cd /opt`
2. `sudo git clone https://github.com/SergKolo/lks-indicator.git`
3. `chmod -R +x  /opt/lks-indicator/`

To obtain zip file , press the green button above or `wget https://github.com/SergKolo/lks-indicator/archive/master.zip` in terminal
## Usage

When none of Scroll, Caps or Num lock are pressed, the indicator will be green.

When one or more lock keys are active, the indicator becomes red, and the following is displayed:

- *\[C\]* for *Caps Lock*
- *\[N\]* for *Num Lock*
- *\[S\]* for *Scroll Lock*

The indicator menu has only one option - closing the indicator.


## Contributors
- Sergiy Kolodyazhnyy
- bharadwaj-raju 

## License
The indicator is provided under MIT license, copy of which is included with the source code


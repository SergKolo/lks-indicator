#!/usr/bin/env python
#
###########################################################
# Author: Serg Kolo , contact: 1047481448@qq.com 
# Date: July 16,2012
# Purpose: Simple indicator of Caps, Num, and Scroll Lock
#          keys for Ubuntu
# 
# Written for: http://askubuntu.com/q/796985/295286
# Tested on: Ubuntu 16.04 LTS
###########################################################
# Copyright: Serg Kolo , 2016
#    
#     Permission to use, copy, modify, and distribute this software is hereby granted
#     without fee, provided that  the copyright notice above and this permission statement
#     appear in all copies.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
#     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#     FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#     DEALINGS IN THE SOFTWARE.


import glib
import subprocess
import appindicator
import gtk
import os

class LockKeyStatusIndicator( object ):
    def __init__(self):
             
        self.app = appindicator.Indicator('LKS', '', 
                          appindicator.CATEGORY_APPLICATION_STATUS)
        self.app.set_status( appindicator.STATUS_ACTIVE )
        
        self.update_label()
        
        self.app_menu = gtk.Menu()
        self.quit_app = gtk.MenuItem( 'Quit' )
        self.quit_app.connect('activate', self.quit)
        self.quit_app.show()
        self.app_menu.append(self.quit_app)
        
        self.app.set_menu(self.app_menu)
        
    def run(self):
        try:
            gtk.main()
        except KeyboardInterrupt:
            pass
    def quit(self):
        gtk.main_quit()
    
    def run_cmd(self,cmdlist):
        # function for running 
        try:
            stdout = subprocess.check_output(cmdlist)
        except subprocess.CalledProcessError:
               pass
        else:
            if stdout:
                return  stdout
    
    def key_status(self):
        label = ""
        status = []
        keys = { '3':'C', '7':'N', '11':'S' }
    
        for line in self.run_cmd( ['xset','q'] ).split("\n") :
            if "Caps Lock:" in line:
                status = line.split()
    
        for index in 3,7,11:
            if status[index] == "on" :
               label = label + " [" +  keys[ str(index)  ] + "] " 
            #else:
            #   label = label + keys[ str(index) ]
    
        return label
    
    def update_label(self):
         cwd = os.getcwd()
         red_icon = os.path.join(cwd,"red.png")
         green_icon = os.path.join(cwd,"green.png")
         label_text = self.key_status()
         if "[" in label_text:
              self.app.set_icon( red_icon )
         else:
              self.app.set_icon( green_icon  )
         
         self.app.set_label( label_text )
         glib.timeout_add_seconds(1,self.set_app_label )
    
    def set_app_label(self):
        self.update_label()

def main():

    indicator = LockKeyStatusIndicator()
    indicator.run()

if __name__ == '__main__':
    main ()


# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2020 Jake Thomas jake01756@gmail.com
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
### END LICENSE
import gi
gi.require_version('Gtk', '3.0')
from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('volume_finder')

from volume_finder_lib import Window
from volume_finder.AboutVolumeFinderDialog import AboutVolumeFinderDialog
from volume_finder.PreferencesVolumeFinderDialog import PreferencesVolumeFinderDialog
#from volume_finder.Assistant import Assistant
from volume_finder.WelcomeDialog import WelcomeDialog
assistant = 0
# See volume_finder_lib.Window.py for more details about how this class works
class Assistant(Gtk.Assistant):
    def __init__(self):
        Gtk.Assistant.__init__(self)
        self.set_title("Welcome Wizard")
        self.set_default_size(400, -1)
        Gtk.Assistant.connect("cancel", self.on_cancel_clicked)
        self.connect("close", self.on_close_clicked)
        self.connect("apply", self.on_apply_clicked)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.INTRO)
        self.set_page_title(box, "Welcome")
        label = Gtk.Label(label="An 'Intro' page is the first page of an Assistant. It is used to provide information about what configuration settings need to be configured. The introduction page only has a 'Continue' button.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONTENT)
        self.set_page_title(box, "Page 2: Content")
        label = Gtk.Label(label="The 'Content' page provides a place where widgets can be positioned. This allows the user to configure a variety of options as needed. The page contains a 'Continue' button to move onto other pages, and a 'Go Back' button to return to the previous page if necessary.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        self.complete = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(self.complete)
        self.set_page_type(self.complete, Gtk.AssistantPageType.PROGRESS)
        self.set_page_title(self.complete, "Page 3: Progress")
        label = Gtk.Label(label="A 'Progress' page is used to prevent changing pages within the Assistant before a long-running process has completed. The 'Continue' button will be marked as insensitive until the process has finished. Once finished, the button will become sensitive.")
        label.set_line_wrap(True)
        self.complete.pack_start(label, True, True, 0)
        checkbutton = Gtk.CheckButton(label="Mark page as complete")
        checkbutton.connect("toggled", self.on_complete_toggled)
        self.complete.pack_start(checkbutton, False, False, 0)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONFIRM)
        self.set_page_title(box, "Page 4: Confirm")
        label = Gtk.Label(label="The 'Confirm' page may be set as the final page in the Assistant, however this depends on what the Assistant does. This page provides an 'Apply' button to explicitly set the changes, or a 'Go Back' button to correct any mistakes.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.SUMMARY)
        self.set_page_title(box, "Summary")
        label = Gtk.Label(label="Thank you for taking the tour of Volume Finder. Your settings have been saved. To exit the tour please click 'Close'.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        def on_apply_clicked(self, *args):
            print("The 'Apply' button has been clicked")

        def on_close_clicked(self, *args):
            print("The 'Close' button has been clicked")
            Gtk.main_quit()

        def on_cancel_clicked(self, *args):
            print("The Assistant has been cancelled.")
            Gtk.main_quit()

        def on_complete_toggled(self, checkbutton):
            assistant.set_page_complete(self.complete, checkbutton.get_active())

class VolumeFinderWindow(Window):
    __gtype_name__ = "VolumeFinderWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(VolumeFinderWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutVolumeFinderDialog
        self.PreferencesDialog = PreferencesVolumeFinderDialog
        self.WelcomeDialog = WelcomeDialog
        global dialog
        dialog = WelcomeDialog

        # Code for other initialization actions should be added here.
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Unstable Volume Finder Development Build",
        )
        dialog.format_secondary_text(
            "You are currently running an Unstable Volume Finder Development Build. Please note that things will be broken."
        )
        dialog.run()
        dialog.destroy()
        dialog = Gtk.MessageDialog(
           transient_for=self,
           flags=0,
           message_type=Gtk.MessageType.QUESTION,
           buttons=Gtk.ButtonsType.YES_NO,
           text="Continue with unstable build?",
        )
        dialog.format_secondary_text(
        "If you continue the developer is not responsible for what happens to your computer."
        )
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            dialog.destroy()
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()
            dialog = Gtk.MessageDialog(
               transient_for=self,
               flags=0,
               message_type=Gtk.MessageType.INFO,
               buttons=Gtk.ButtonsType.OK,
               text="Unstable Volume Finder Development Build",
            )
            dialog.format_secondary_text(
               "You have chosen to quit Volume Finder. Stable Builds are coming soon."
            )
            dialog.run()
            dialog.destroy()
            quit()
            Gtk.main_quit()

        dialog.destroy()

    def on_mnu_welcome_activate(self, widget, data=None):
         class DialogExample(Gtk.Dialog):
            def __init__(self, parent):
                Gtk.Dialog.__init__(self, title="Welcome Wizard", transient_for=parent, flags=0)
                self.add_buttons(
                Gtk.STOCK_NO, Gtk.ResponseType.NO, Gtk.STOCK_YES, Gtk.ResponseType.YES
                )
                self.set_default_size(300, 300)
                label = Gtk.Label(label=
                    "Would you like to take a tour of Volume Finder and configure initial settings? You can do this at any time by choosing the \'Welcome Wizard\' option under the Help menu bar."
                )
                label.set_line_wrap(True)
                box = self.get_content_area()
                box.add(label)
                self.show_all()

         dialog = DialogExample(self)
         response = dialog.run()
         if response == Gtk.ResponseType.YES:
              #print("The OK button was clicked")
              dialog.destroy()
              #assistant = Assistant.Assistant()
              #assistant.show_all()
              ## Import Assistant Here
  
                #Assistant.run()
              assistant = Assistant()
              assistant.show_all()
              #Gtk.main()

         elif response == Gtk.ResponseType.NO:
              dialog.destroy()
              dialog = Gtk.MessageDialog(
                  transient_for=self,
                  flags=0,
                  message_type=Gtk.MessageType.INFO,
                  buttons=Gtk.ButtonsType.OK,
                  text="Information",
              )
              dialog.format_secondary_text(
                  "You can rerun the Welcome Wizard at any time via the Help menu."
              )
              dialog.run()
              dialog.destroy()
              Gtk.main()
         #dialog = WelcomeDialog()
         #dialog.show_all()
         #dialog.hide()
         #if self.WelcomeDialog is not None:
            #welcome = self.WelcomeDialog() # pylint: disable=E1102
            #response = welcome.run()
            #welcome.destroy()

    #def on_mnu_welcome(self, widget, data=None):
        #dialog = WelcomeDialog()
        #dialog.show()
#Gtk.main()
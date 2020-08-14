# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('volume_finder')

from volume_finder_lib import Window
from volume_finder.AboutVolumeFinderDialog import AboutVolumeFinderDialog
from volume_finder.PreferencesVolumeFinderDialog import PreferencesVolumeFinderDialog
from volume_finder.WelcomeDialog import WelcomeDialog

# See volume_finder_lib.Window.py for more details about how this class works
class VolumeFinderWindow(Window):
    __gtype_name__ = "VolumeFinderWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(VolumeFinderWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutVolumeFinderDialog
        self.PreferencesDialog = PreferencesVolumeFinderDialog
        self.WelcomeDialog = WelcomeDialog

        # Code for other initialization actions should be added here.
    
    #def on_mnu_welcome(self, widget, data=None):
        #dialog = WelcomeDialog()
        #dialog.show()
        #Gtk.main()

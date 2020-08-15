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

from gi.repository import Gtk # pylint: disable=E0611

from volume_finder_lib.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('volume-finder')

class WelcomeDialog(Gtk.Dialog):
    __gtype_name__ = "WelcomeDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated WelcomeDialog object.
        """
        builder = get_builder('WelcomeDialog')
        new_object = builder.get_object('welcome_dialog')
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.

        finish_initalizing should be called after parsing the ui definition
        and creating a WelcomeDialog object with it in order to
        finish initializing the start of the new WelcomeDialog
        instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self)

    def on_btn_ok_clicked(self, widget, data=None):
        """The user has elected to save the changes.
        
        Called before the dialog returns Gtk.ResponseType.OK from run().
        """
        pass

    def on_btn_cancel_clicked(self, widget, data=None):
        """The user has elected cancel changes.

        Called before the dialog returns Gtk.ResponseType.CANCEL for run()
        """
        pass


if __name__ == "__main__":
    dialog = WelcomeDialog()
    dialog.show()
    Gtk.main()

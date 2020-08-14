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

from locale import gettext as _

import logging
logger = logging.getLogger('volume_finder')

from volume_finder_lib.AboutDialog import AboutDialog

# See volume_finder_lib.AboutDialog.py for more details about how this class works.
class AboutVolumeFinderDialog(AboutDialog):
    __gtype_name__ = "AboutVolumeFinderDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutVolumeFinderDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.


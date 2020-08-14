#!/usr/bin/python
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

import sys
import os.path
import unittest
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from volume_finder import AboutVolumeFinderDialog

class TestExample(unittest.TestCase):
    def setUp(self):
        self.AboutVolumeFinderDialog_members = [
        'AboutDialog', 'AboutVolumeFinderDialog', 'gettext', 'logger', 'logging']

    def test_AboutVolumeFinderDialog_members(self):
        all_members = dir(AboutVolumeFinderDialog)
        public_members = [x for x in all_members if not x.startswith('_')]
        public_members.sort()
        self.assertEqual(self.AboutVolumeFinderDialog_members, public_members)

if __name__ == '__main__':    
    unittest.main()

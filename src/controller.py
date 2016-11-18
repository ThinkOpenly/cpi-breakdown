# -*- coding: utf-8 -*-

"""
Copyright (C) 2016 IBM Corporation

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    Contributors:
        * Rafael Sene <rpsene@br.ibm.com>
        * Daniel Kreling <dbkreling@br.ibm.com>
"""

import core
import events_reader
import commands


def run_cpi(binary_path, binary_args):
    for event in events_reader.get_events(core.get_processor()):
        ocount = "ocount -b"
        for item in event:
            ocount += " -e " + item
        print "\n" + "Running: " + ocount + " " + binary_path + binary_args
        core.execute(ocount + ' ' + binary_path + binary_args)
    return

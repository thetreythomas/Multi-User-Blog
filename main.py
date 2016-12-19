#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import jinja2
import webapp2
from signup import Signup, Welcome
from handler import Handler
from ascii import Ascii


class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping-list.html", items = items)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Signup),
                               ('/welcome', Welcome),
                               ('/ascii', Ascii)
                               ], debug=True)
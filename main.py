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
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


# here's a comment to test git

class MainHandler(webapp.RequestHandler):
    def get(self):
        import mechanize
        br = mechanize.Browser()
        br.set_handle_equiv(False)
        br.set_handle_robots(False)
        br.open("https://order.pizzanova.com/fcgi-bin/Weborder.pl")
        #self.response.out.write(br.response().get_data())
        br.select_form(nr=0)

        br["email"] = "7cubedproject@gmail.com"
        br["password"] = "velocity"
        br.submit()

        br.select_form(nr=0)

        """
        first_form = None
        for form in br.forms():
            first_form = form
        first_form["email"] = "gilbert.kf.leung@gmail.com"
        first_form["password"] = "12345"
        first_form.submit()
        """

        self.response.out.write(br.response().get_data())

        #self.response.out.write(br.title())
        #self.response.out.write(br.get_data())
        #br.select_form(name="address-entry-form")
        #self.response.out.write(br.form())


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity."""

import gtk
import logging

from gettext import gettext as _

from sugar.activity import activity 

class HelloWorldActivity(activity.Activity):
    """HelloWorldActivity class as specified in activity.info"""
    def __init__(self, handle):
        """Set up the HelloWorld activity."""
        activity.Activity.__init__(self, handle)

        # top toolbar with close button
        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # label with the text
        label = gtk.Label(_("Hello World!"))
        self.set_canvas(label)
        label.show()



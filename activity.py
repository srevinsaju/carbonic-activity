"""
carbonic on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC CORE AI
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""



import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Pango
from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem
from sugar3.graphics.style import FONT_FACE, FONT_SIZE
from graphics import Graphics, FONT_SIZES
from ccore import *

class CarbonicActivity(activity.Activity):


    def __init__(self, handle):

        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        # FONT DEFINITIONS
        FONT_FACE = 'Monospace'
        input_font = Pango.FontDescription('%s %d' % (FONT_FACE, int(FONT_SIZE * 1.2)))
        entry_font = Pango.FontDescription('%s %d' % (FONT_FACE, int(FONT_SIZE * 10.0 )))

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # label with the text, make the string translatable
        center_in_panel = Gtk.Alignment.new(0.5, 0, 0, 0)
        graphics = Graphics()
        first = 'methane'
        self._first_entry = graphics.add_entry(first)
        self._first_entry.override_font(input_font)
        self._spac1 = graphics.add_text(' ')

        print("LOG: #56, ", self._first_entry, self._first_entry )
        button = graphics.add_button(_("COMPUTE"), self.something )
        self._spac2 = graphics.add_text(' ')
        button.show()

        self.hold_hi3 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_hi3.override_font(input_font)

        self.hold_hi2 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_hi2.override_font(input_font)
        self.hold_hi1 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_hi1.override_font(input_font)
        self.hold0 = graphics.add_text(
            _("CH4"), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold0.override_font(input_font)
        self.hold_lo1 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_lo1.override_font(input_font)
        self.hold_lo2 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_lo2.override_font(input_font)
        self.hold_lo3 = graphics.add_text(
            _(" "), size="xx-large", bold=True, justify=Gtk.Justification.CENTER)
        self.hold_lo3.override_font(input_font)

        center_in_panel.add(graphics)
        graphics.show()
        self.set_canvas(center_in_panel)
        center_in_panel.show()

    def something(self, button_inst):
        #print("yo", text, t1,t2,t3)
        #print("ya", self._first_entry.get_text())
        val = self._first_entry.get_text()
        c = convertor(val)
        d = chkBond(c)
        displax(d)

        if len(d) == 1:

            self.hold_hi3.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')
            self.hold_hi2.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')
            self.hold_hi1.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')
            self.hold0.set_markup('<span size="xx-large"><b>' + d[0] + '</b></span>')
            self.hold_lo1.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')
            self.hold_lo2.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')
            self.hold_lo3.set_markup('<span size="xx-large"><b>' + "  " + '</b></span>')

        else:
            self.hold_hi3.set_markup('<span size="xx-large"><b>' + d[6] + '</b></span>')
            self.hold_hi2.set_markup('<span size="xx-large"><b>' + d[5] + '</b></span>')
            self.hold_hi1.set_markup('<span size="xx-large"><b>' + d[4] + '</b></span>')
            self.hold0.set_markup('<span size="xx-large"><b>' + d[0] + '</b></span>')
            self.hold_lo1.set_markup('<span size="xx-large"><b>' + d[1] + '</b></span>')
            self.hold_lo2.set_markup('<span size="xx-large"><b>' + d[2] + '</b></span>')
            self.hold_lo3.set_markup('<span size="xx-large"><b>' + d[3] + '</b></span>')

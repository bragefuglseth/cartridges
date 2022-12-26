# create_dialog.py
#
# Copyright 2022 kramo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

def create_dialog(parent_widget, heading, body, extra_option=None, extra_label=None):
    from gi.repository import Adw, Gtk

    dialog = Adw.MessageDialog.new(parent_widget, _(heading), body)
    dialog.add_response("dismiss",  _("Dismiss"))

    if extra_option:
        dialog.add_response(extra_option, _(extra_label))

    Gtk.Window.present(dialog)
    return dialog

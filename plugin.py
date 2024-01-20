# Copyright (C) 2023 Gerard Roche
#
# This file is part of NeoVintageousFiles.
#
# NeoVintageousFiles is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageousFiles is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageousFiles.  If not, see <https://www.gnu.org/licenses/>.

from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


class NeovintageousFilesNewFile(sublime_plugin.WindowCommand):

    def run(self):
        _run_command(self.window, 'side_bar_new', {'paths': []})

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)


class NeovintageousFilesNewFolder(sublime_plugin.WindowCommand):

    def run(self):
        _run_command(self.window, 'side_bar_new', {'paths': []})

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)


class NeovintageousFilesDuplicate(sublime_plugin.WindowCommand):

    def run(self):
        _run_command(self.window, 'side_bar_duplicate', {'paths': []})

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)


class NeovintageousFilesFind(sublime_plugin.WindowCommand):

    def run(self) -> None:
        self.window.run_command('show_panel', {
            'panel': 'find_in_files'
        })

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)


class NeovintageousFilesMove(sublime_plugin.WindowCommand):

    def run(self):
        _run_command(self.window, 'side_bar_move', {'paths': []})

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)


class NeovintageousFilesOpen(sublime_plugin.WindowCommand):

    def run(self, tab=None, split=None, vsplit=None) -> None:
        fname = self.window.active_view().file_name()
        if not fname:
            transient_view = self.window.transient_view_in_group(self.window.active_group())
            if not transient_view:
                return

            fname = transient_view.file_name()
            if not fname:
                return

        if vsplit:
            self.open_file_in_vertical_split(fname)
        elif split:
            self.open_file_in_horizontal_split(fname)
        elif tab:
            self.open_file_in_tab(fname)
        else:
            self.open_file_in_tab(fname)

    def is_enabled(self) -> bool:
        return _has_active_view(self.window)

    def open_file_in_vertical_split(self, fname: str) -> None:
        self.window.open_file(fname)
        self.window.run_command('carry_file_to_pane', {
            'direction': 'right'
        })

    def open_file_in_horizontal_split(self, fname: str) -> None:
        self.window.open_file(fname)
        self.window.run_command('carry_file_to_pane', {
            'direction': 'down'
        })

    def open_file_in_tab(self, fname: str) -> None:
        self.window.open_file(fname)


def _has_active_view(window) -> bool:
    return True if window.active_view() else False


def _run_command(window, command: str, args: None) -> None:
    """There is no api to get a path under the cursor.

    The only workaround I know, is the preview on click feature which opens the
    file under the cursor in a preview. The path can be retrieved from the
    preview view. Preview on click may need to be temporarily enabled.

    The preview is marked as readonly. So after a file command is run, if the
    active file is readonly then it's assumed to be the preview and closed.

    This is workaround and won't work properly in all cases.
    """
    with _save_preferences() as preferences:
        preview_on_click = preferences.get('preview_on_click')
        if not preview_on_click:
            # Temporarily set preview on click
            preferences.set('preview_on_click', True)

    if not preview_on_click:
        # Force preview on click to fire.
        window.run_command('move', {'by': 'lines', 'forward': True})
        window.run_command('move', {'by': 'lines', 'forward': False})

    # Run command.
    window.run_command(command, args)

    if not preview_on_click:
        # Reset preview on click if needed
        with _save_preferences() as preferences:
            preferences.set('preview_on_click', False)

        # Cleanup preview view.
        view = window.active_view()
        if view and view.is_read_only():
            view.close()

        # Put focus back on input.
        window.run_command('show_panel', {'panel': 'input'})


@contextmanager
def _save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


class NeovintageousTreeNewFile(sublime_plugin.WindowCommand):

    def run(self) -> None:
        _run_command(self.window, 'side_bar_new', {'paths': []})

    def is_enabled(self) -> bool:
        return _is_enabled(self.window)


class NeovintageousTreeNewFolder(sublime_plugin.WindowCommand):

    def run(self) -> None:
        _run_command(self.window, 'side_bar_new', {'paths': []})

    def is_enabled(self) -> bool:
        return _is_enabled(self.window)


class NeovintageousTreeDuplicate(sublime_plugin.WindowCommand):

    def run(self) -> None:
        _run_command(self.window, 'side_bar_duplicate', {'paths': []})

    def is_enabled(self) -> bool:
        return _is_enabled(self.window)


class NeovintageousTreeFind(sublime_plugin.WindowCommand):

    def run(self) -> None:
        self.window.run_command('show_panel', {
            'panel': 'find_in_files'
        })

    def is_enabled(self) -> bool:
        return _is_enabled(self.window)


class NeovintageousTreeMove(sublime_plugin.WindowCommand):

    def run(self) -> None:
        _run_command(self.window, 'side_bar_move', {'paths': []})

    def is_enabled(self) -> bool:
        return _is_enabled(self.window)


class NeovintageousTreeOpen(sublime_plugin.WindowCommand):

    def run(self, tab=None, split=None, vsplit=None):
        """
        Open file.

        :param tab:
            Open the selected file in a new tab
        :param split:
            Open the selected file in a horizontal split
        :param vsplit:
            Open the selected file in a vertical split

        Defaults to opening in a new tab.
        """
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
        return _is_enabled(self.window)

    def open_file_in_vertical_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {
            'direction': 'right'
        })

    def open_file_in_horizontal_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {
            'direction': 'down'
        })

    def open_file_in_tab(self, fname):
        self.window.open_file(fname)


def _run_command(window, command: str, args=None) -> None:
    """There is no api to get a name of a file under the cursor.

    The only workaround I know so far, and it's fragile at best, is using
    the fact that the "preview_on_click" feature opens the file under the
    cursor in a preview view. From here the file name can be discovered.

    If "preview_on_click" is disabled then it needs to be temporarily
    enabled and a "wibble wobble" workaround is used to trigger the
    preview_on_click feature.

    The preview file seems to be marked as readonly. So, after a file
    command is run, if the active file is readonly then it is assumed to be
    a preview and it is closed.

    **Known Issues**

    - Doesn't work if the file under cursor is a folder so don't do that.
    """
    preview_on_click = _ensure_file_under_cursor_is_open(window)
    window.run_command(command, args)
    _ensure_file_under_cursor_is_open_cleanup(window, preview_on_click)


def _ensure_file_under_cursor_is_open(window):
    preferences = _load_preferences()
    preview_on_click = preferences.get('preview_on_click')

    if not preview_on_click:
        preferences.set('preview_on_click', True)
        _save_preferences()

    # Force cursor repaint (Workaround). Helps scroll active file into view and
    # shakes off previous sidebar (highlighted) cursor position
    window.run_command('move', {'by': 'lines', 'forward': True})
    window.run_command('move', {'by': 'lines', 'forward': False})

    return preview_on_click


def _ensure_file_under_cursor_is_open_cleanup(window, preview_on_click) -> None:
    if not preview_on_click:
        preferences = _load_preferences()
        preferences.set('preview_on_click', False)
        _save_preferences()
        view = window.active_view()
        if view and view.is_read_only():
            view.close()


def _load_preferences():
    return load_settings('Preferences.sublime-settings')


def _save_preferences() -> None:
    save_settings('Preferences.sublime-settings')


def _is_enabled(window) -> bool:
    return True if window.active_view() else False

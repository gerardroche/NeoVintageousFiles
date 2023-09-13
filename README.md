# NeoVintageous Files

:sparkles: :rocket: Introducing single-key sidebar and goto file overlay commands, complementing [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous).

**:sparkles: :sparkles: :sparkles: Experimental :sparkles: :sparkles: :sparkles:**

## Installation

### Dependencies

Install through Package Control:

- [SideBarTools](https://packagecontrol.io/packages/SideBarTools) - Adds support for sidebar commands.
- [Origami](https://packagecontrol.io/packages/Origami) - Enhances the ability to open files in split view.

### Install

**Method 1: Using Package Control**

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "NeoVintageousFiles" and select it from the list of available packages.

**Method 2: Manual Installation**

1. Visit the [NeoVintageousFiles GitHub repository](https://github.com/gerardroche/NeoVintageousFiles).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "NeoVintageousFiles" folder from the extracted ZIP and paste it into the Packages folder.

**Method 3: Manual Git Repository Installation**

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/NeoVintageousFiles.git NeoVintageousFiles
   ```

## Key Bindings

**Sidebar Commands**

| Key                         | Description
| :-------------------------- | :------------------------
| `a`                         | Add a file.
| `A`                         | Add a folder.
| `d`                         | Duplicate a file.
| `f`                         | Open the find panel.
| `F2` or `m`                 | Move a file.
| `CTRL-v` or `s`             | Open file selection in a vertical split.
| `CTRL-x` or `i` or `CTRL-s` | Open file selection in a horizontal split.
| `CTRL-t` or `t`             | Open file selection in a new tab.

**Goto File Overlay Commands**

| Key                   | Description
| :-------------------- | :----------
| `CTRL-v`              | Open file selection in a vertical split.
| `CTRL-x` or `CTRL-s`  | Open file selection in a horizontal split.
| `CTRL-t`              | Open file selection in a new tab.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).

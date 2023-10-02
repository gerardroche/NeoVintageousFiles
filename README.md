# NeoVintageous Files

:sparkles: :rocket: Introducing NeoVintageous Files - your gateway to seamless file management with single-key sidebar and goto file overlay commands, designed to complement the power of [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous).

**:sparkles: :sparkles: :sparkles: Experimental :sparkles: :sparkles: :sparkles:**

## Installation

### Dependencies

Before you embark on your journey with NeoVintageous Files, make sure you have the following dependencies installed:

- [SideBarTools](https://packagecontrol.io/packages/SideBarTools) - This package adds essential support for sidebar commands.
- [Origami](https://packagecontrol.io/packages/Origami) - Enhance your Sublime Text experience by improving the ability to open files in split view.

### Install

Follow one of these methods to install NeoVintageous Files:

**Method 1: Using Package Control**

1. Launch Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to summon the Command Palette.
3. Type "Package Control: Install Package" and hit `Enter`.
4. In the input field, type "NeoVintageousFiles" and select it from the list of available packages.

**Method 2: Manual Installation**

1. Visit the [NeoVintageousFiles GitHub repository](https://github.com/gerardroche/NeoVintageousFiles).
2. Click on the "Code" button and choose "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and navigate to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "NeoVintageousFiles" folder from the extracted ZIP and paste it into the Packages folder.

**Method 3: Manual Git Repository Installation**

1. Fire up your terminal or command prompt.
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

Enhance your file management prowess with NeoVintageous Files and simplify your workflow with these intuitive single-key commands.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).

# NeoVintageousFiles

NeoVintageousFiles is a [NeoVintageous](https://github.com/gerardroche/NeoVintageousFiles) plugin for Sublime Text to enhance browsing files in the sidebar and overlays.

## Sidebar commands

| Key                         | Description
| :-------------------------- | :------------------------
| `<cr>`                      | Open file.
| `A`                         | Add a folder.
| `CTRL-t` or `t`             | Open file selection in a new tab.
| `CTRL-v` or `s`             | Open file selection in a vertical split.
| `CTRL-x` or `i` or `CTRL-s` | Open file selection in a horizontal split.
| `F2` or `m`                 | Move a file.
| `J`                         | Go to last child node.
| `P`                         | Go to root node.
| `a`                         | Add a file.
| `d`                         | Duplicate a file.
| `f`                         | Open the find panel.
| `h`                         | Close node.
| `j`                         | Down.
| `k`                         | Up.
| `l`                         | Open node.
| `p`                         | Go to parent node.
| `q`                         | Close sidebar.

## Overlay commands

Autocomplete, Goto File, Command Palette, etc.

| Key                   | Description
| :-------------------- | :----------
| `CTRL-t`              | Open file selection in a new tab.
| `CTRL-v`              | Open file selection in a vertical split.
| `CTRL-x` or `CTRL-s`  | Open file selection in a horizontal split.

## Installation

### Prerequisites

Install the following package dependencies:

- [SideBarTools](https://github.com/braver/SideBarTools)
- [Origami](https://github.com/SublimeText/Origami)

### Package Control installation

1. Open the Command Palette: `Ctrl+Shift+P` (Win/Linux) or `Cmd+Shift+P` (Mac).
1. Type "Package Control: Install Package" and press Enter.
1. In the input field, type "**NeoVintageousFiles**" and select it from the list of packages.
1. Restart Sublime Text.

### Git installation

1. Clone into the Sublime Text packages directory:

   Linux

   ```sh
   git clone https://github.com/gerardroche/NeoVintageousFiles.git ~/.config/sublime-text/Packages/NeoVintageousFiles

   ```

   Mac

   ```sh
   git clone https://github.com/gerardroche/NeoVintageousFiles.git ~/Library/Application Support/Sublime Text/Packages/NeoVintageousFiles
   ```

   Windows

   ```ps
   git clone https://github.com/gerardroche/NeoVintageousFiles.git %APPDATA%\Sublime Text\Packages\NeoVintageousFiles
   ```

1. Restart Sublime Text

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).

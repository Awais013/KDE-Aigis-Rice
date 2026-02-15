from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Crust(ColorScheme):
    progress_bar_color = 3

    def use(self, context):
        fg, bg, attr = default_colors

        # Browser
        if context.in_browser:
            if context.selected:
                bg = 1  # selected background
                attr = reverse
            elif context.directory:
                fg = 3  # directories
            elif context.executable:
                fg = 2  # executables
            elif context.marked:
                attr = bold

        # Titlebar
        elif context.in_titlebar:
            if context.hostname:
                fg = 2
            if context.directory:
                fg = 3

        # Statusbar
        elif context.in_statusbar:
            fg = 1
            attr = bold

        return fg, bg, attr


from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Aigis(ColorScheme):
    progress_bar_color = 137 # Brass

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = bold
                fg = 137 # Brass
                bg = 237 # Deep Grey
            else:
                attr = normal
                fg = 252 # Off-white
            
            if context.directory:
                fg = 144 # Sage Green (closest ANSI to #758e85)
                attr = bold
            elif context.executable and not any((context.media, context.container, context.fifo, context.socket)):
                fg = 137 # Brass
                attr = bold
            elif context.link:
                fg = 109 # Muted Blue/Teal

        elif context.in_titlebar:
            attr = bold
            if context.hostname:
                fg = 137 if context.bad else 144
            elif context.directory:
                fg = 144
            elif context.tab:
                if context.good:
                    bg = 144
                    fg = 235

        elif context.in_statusbar:
            if context.permissions:
                if context.good: fg = 144
                elif context.bad: fg = 131 # Muted Red
            if context.marked:
                attr |= bold
                fg = 137
            if context.message:
                if context.bad: fg = 131

        return fg, bg, attr

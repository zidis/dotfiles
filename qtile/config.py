from typing import List  # noqa: F401

import os
import re
import socket
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
	# Switch between windows in current stack pane
	Key([mod], "k", lazy.layout.down(),
		desc="Move focus down in stack pane"),
	Key([mod], "j", lazy.layout.up(),
		desc="Move focus up in stack pane"),
	Key([mod, "control"], "k", lazy.layout.shuffle_down(),
		desc="Move window down in current stack "),
	Key([mod, "control"], "j", lazy.layout.shuffle_up(),
		desc="Move window up in current stack "),

	# Switch window focus to other pane(s) of stack
	Key([mod], "space", lazy.layout.next(),
		desc="Switch window focus to other pane(s) of stack"),

	# Swap panes of split stack
	Key([mod, "shift"], "space", lazy.layout.rotate(),
		desc="Swap panes of split stack"),

	# Toggle between split and unsplit sides of stack.
	# Split = all windows displayed
	# Unsplit = 1 window displayed, like Max layout, but still with
	# multiple stack panes
	Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
		desc="Toggle between split and unsplit sides of stack"),
	Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
	# Launch dmenu
	Key([mod], "f", lazy.spawn("dmenu_run -p 'Run: '"), desc='Dmenu Run Launcher'),

	# Toggle between different layouts as defined below
	Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
	Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

	Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
	Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
	Key([mod], "r", lazy.spawncmd(),
		desc="Spawn a command using a prompt widget"),
]

group_names = [("WEB", {'layout': 'max'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'max'}),
               ("CHAT", {'layout': 'max'}),
               ("MUS", {'layout': 'max'}),
               ("TOR", {'layout': 'max'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "#555753",
                "border_normal": "#282828"
                }

layouts = [
	layout.Max(**layout_theme),
	layout.MonadTall(**layout_theme),
	#layout.Floating(**layout_theme)
	#layout.Stack(num_stacks=2),
]

colors = [["#282828", "#282828"], # panel background
          ["#f8f8f8", "#f8f8f8"], # group box active
		  ["#888A85", "#888A85"], # group box inactive
		  ["#404040", "#404040"], # group box highlight
          ["#ffffff", "#ffffff"], # font color for group names
          ["#555753", "#555753"], # border line focus
          ["#282828", "#282828"]] # border line normal

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# Default widget settings
widget_defaults = dict(
	font="Ubuntu Mono",
	fontsize = 12,
	padding = 3,
	foreground = colors[4],
	background = colors[0]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='/home/zidis/dotfiles/wallpapers/leaves/1.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [       
			widget.GroupBox(
				font="Ubuntu Mono",
				fontsize = 12,
				#margin_y = 3,
                #margin_x = 3,
                #padding_y = 3,
                #padding_x = 3,
                #borderwidth = 3,
				rounded = False,
                disable_drag = True,
                highlight_method = "line",
                highlight_color = colors[3],
				active = colors[1],
				inactive = colors[2]
				),
			widget.TextBox(
                text="~",
                ),
        	widget.CurrentLayout(),
            widget.Spacer(),
			#widget.TextBox(
                #text="~",
                #),
			#widget.WindowName(),
			widget.TextBox(
                text="",
                ),
			widget.Volume(),
			widget.TextBox(
                text="~",
                ),
			widget.KeyboardLayout(),
			widget.TextBox(
                text="~",
                ),
			widget.Clock(
				format = "%a %d/%m/%Y"
				),
			widget.TextBox(
                text="~",
                ),
			widget.Clock(
				format = "%H:%M",
				padding = 3
				),
            ],
            28,
            #margin=[0, -4, 18, -4],
        ),
        #bottom=bar.Gap(18),
        #left=bar.Gap(18),
        #right=bar.Gap(18),
    ),
]

# Drag floating layouts.
mouse = [
	Drag([mod], "Button1", lazy.window.set_position_floating(),
		start=lazy.window.get_position()),
	Drag([mod], "Button3", lazy.window.set_size_floating(),
		start=lazy.window.get_size()),
	Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
	# Run the utility of `xprop` to see the wm class and name of an X client.
	{'wmclass': 'confirm'},
	{'wmclass': 'dialog'},
	{'wmclass': 'download'},
	{'wmclass': 'error'},
	{'wmclass': 'file_progress'},
	{'wmclass': 'notification'},
	{'wmclass': 'splash'},
	{'wmclass': 'toolbar'},
	{'wmclass': 'confirmreset'},  # gitk
	{'wmclass': 'makebranch'},  # gitk
	{'wmclass': 'maketag'},  # gitk
	{'wname': 'branchdialog'},  # gitk
	{'wname': 'pinentry'},  # GPG key password entry
	{'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

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

groups = [Group(i) for i in "123456789"]

for i in groups:
	keys.extend([
		# mod1 + letter of group = switch to group
		Key([mod], i.name, lazy.group[i.name].toscreen(),
			desc="Switch to group {}".format(i.name)),

		# mod1 + shift + letter of group = switch to & move focused window to group
		Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
			desc="Switch to & move focused window to group {}".format(i.name)),
		# Or, use below if you prefer not to switch to that group.
		# # mod1 + shift + letter of group = move focused window to group
		# Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
		# desc="move focused window to group {}".format(i.name)),
	])

layout_theme = {"border_width": 2,
                "margin": 0,
                "border_focus": "#555753",
                "border_normal": "#2E3436"
                }

layouts = [
	layout.Max(**layout_theme),
	layout.MonadTall(**layout_theme),
	#layout.Stack(num_stacks=2),
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# Default widget settings
widget_defaults = dict(
	font="Ubuntu Mono",
	fontsize = 12,
	padding = 2,
	background= "#282828"
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
				rounded = True,
                disable_drag = True,
                highlight_method = "block",
                highlight_color = ['4d4d4d', '4d4d4d'],
				active = '#f8f8f8',
				inactive = '#888A85'
				),
        	#widget.CurrentLayoutIcon(
                #foreground="#d8d8d8",
                #background="#4d4d4d",
                #scale=0.5,
                #),
        	widget.CurrentLayout(
                foreground="#d8d8d8",
                #background="#4d4d4d",
                ),
            widget.Spacer(),
			widget.TextBox(
                text=" ",
                foreground="#d8d8d8",
                fontsize=15,
                ),
			widget.WindowName(),
			widget.TextBox(
                text="",
                foreground="#d8d8d8",
                #background="#4d4d4d",
                fontsize=15,
                ),
			widget.Volume(
                foreground="#d8d8d8",
                #background="#4d4d4d",
                padding=5
                ),
			widget.TextBox(
                text="",
                foreground="#d8d8d8",
                #background="#4d4d4d",
                fontsize=15,
                ),
			widget.KeyboardLayout(
                foreground="#d8d8d8",
                #background="#4d4d4d",
                padding=5
                ),
			widget.TextBox(
                text="",
                foreground="#d8d8d8",
                #background="#4d4d4d",
                fontsize=15,
                ),
			widget.Clock(
				format = "%a %d/%m/%Y",
                foreground="#d8d8d8",
                #background="#4d4d4d",
				padding = 5
				),
			widget.TextBox(
                text="",
                foreground="#d8d8d8",
                #background="#4d4d4d",
                fontsize=15,
                ),
			widget.Clock(
				format = "%H:%M",
                foreground="#d8d8d8",
                #background="#4d4d4d",
				padding = 5
				),
			widget.TextBox(
                text=" ",
                foreground="#d8d8d8",
                #background="#4d4d4d",
                fontsize=15,
                ),
            ],
            26,
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

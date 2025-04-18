# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.base import PaddingMixin
from qtile_extras.widget import WiFiIcon
from qtile_extras import widget
from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT, DEFAULT_LAYOUT
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration

from libqtile import hook

import os

@hook.subscribe.startup_once
def autostart():

    home = os.path.expanduser('~')
    os.system(home + '/.config/qtile/autostart.sh')

mod = "mod4"
terminal = guess_terminal()

from libqtile import widget
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupWidget
)

from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText,
    PopupSlider
)

def show_power_menu(qtile):
    controls = [
        PopupImage(
            filename="~/Imágenes/logout.png",
            pos_x=0.05,
            pos_y=0.1,
            width=0.2,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupImage(
            filename="~/Imágenes/bel.png",
            pos_x=0.3,
            pos_y=0.1,
            width=0.2,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename="~/Imágenes/sleep.png",
            pos_x=0.55,
            pos_y=0.1,
            width=0.2,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl suspend")
            }
        ),
        PopupImage(
            filename="~/Imágenes/off.png",
            pos_x=0.8,
            pos_y=0.1,
            width=0.2,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupText(
            text="Logout",
            pos_x=0.05,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Reboot",
            pos_x=0.3,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.55,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.8,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1200,
        height=150,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)


def show_graphs(qtile):
    controls = [
        PopupWidget(
            widget=widget.CPUGraph(),
            width=0.45,
            height=0.45,
            pos_x=0.05,
            pos_y=0.05
        ),
        PopupWidget(
            widget=widget.NetGraph(),
            width=0.45,
            height=0.45,
            pos_x=0.5,
            pos_y=0.05
        ),
        PopupWidget(
            widget=widget.MemoryGraph(),
            width=0.9,
            height=0.45,
            pos_x=0.05,
            pos_y=0.5
        )
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
        close_on_click=False
    )
    layout.show(centered=True)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Focus windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to the left"),
    Key([mod], "Right", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Down", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Up", lazy.layout.right(), desc="Move focus to the right"),
    Key([mod], "x", lazy.function(show_power_menu)),
        Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot with Flameshot"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod],"w", lazy.spawn("zen-browser"), desc='browser'),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_flodating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -show drun -show-icons -b"), desc="Launch Rofi run"),
    Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume",lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Disminuir volumen"),
    Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),desc="Silenciar o activar sonido"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod], "g", lazy.function(show_graphs)),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(f"{i+1}", label="") for i in range(9)]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Tile(
	ratio=0.5,
        margin=12,
        border_width=0,
        border_focus="#00b3ff",
        border_normal="#444444",
),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

space =  widget.TextBox(text="|", font="Font Awesome 6 Free Solid", fontsize=13,)

widget_defaults = dict(
    font="sans",
    fontsize=11,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
       top=bar.Bar(
            [
                widget.Spacer(length=7,
                                    #background='#282738',
                                ),
                widget.Image(
                              filename='~/Descargas/Arch Linux.png',
                              margin=3,
                              mouse_callbacks={
                                    'Button1': lambda: qtile.cmd_spawn('rofi -show drun -show-icons -b')
                                  },
                              #background='#282738',
                                ),
                widget.GroupBox(
			highlight_method='line',
			hide_unused='False',
			rounded='True',
		),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
               ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                
                widget.Systray(icon_size=13),
                space,
                widget.Volume(
                    update_interval=0.1,
                    step=5,
                    volume_app="amixer sget Master",
                    mute_command="amixer set Master toggle",
                    volume_up_command="amixer set Master 5%+",
                    volume_down_command="amixer set Master 5%-",
                    fmt='󰎈 {}',
                    foreground="#00f3ff",
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=12,
                ),
                space,
                widget.TextBox(
		text="󰍛",
		font="Font Awesome 6 Free Solid",
                fontsize=18,
                foreground="#00f3ff",
		),
                widget.CPU(
		    format="{load_percent}%",
		    foreground="#00f3ff",
		    font="JetBrainsMono Nerd Font Bold",
                    fontsize=12,
		    ),
		widget.TextBox(
		text="|",
		font="Font Awesome 6 Free Solid",
                fontsize=13,
		),
                widget.Memory(
		    format=" {MemPercent}%",
		    foreground="#00f3ff",
		    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
		),
		widget.TextBox(
                    text="|",
                    font="Font Awesome 6 Free Solid",
                    fontsize=13,
                ),
        widget.TextBox(
                    font = "Iosevka Nerd Font",
                    fontsize = 15,
                    text = " ",
                    foreground = "#00f3ff",
        ),
        widget.Wlan(
                        interface="wlan0",
                        check_connection_interval=5,
                        format="({percent:2.0%})",
                        font="JetBrainsMono Nerd Font Bold",
                        fontsize=12,
                        ),
		widget.TextBox(
                    text="|",
                    font="Font Awesome 6 Free Solid",
                    fontsize=12,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=12,
                    mouse_callbacks={
                    'Button1': lazy.spawn('/usr/bin/sh /home/graulerlowe/.config/qtile/scripts/popup_calendar.sh --popup')
                    },
                ),
                widget.Clock(
                    format='%I:%M %p',
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=12,
                mouse_callbacks={
                    'Button1': lazy.spawn('/usr/bin/sh /home/graulerlowe/.config/qtile/scripts/popup_calendar.sh --popup')
                },

                ),

		widget.TextBox(
                text="|",
                font="Font Awesome 6 Free Solid",
                fontsize=13,
                ),
                widget.TextBox(
                                    text="",
                                    font="Font Awesome 6 Free Solid",
                                    fontsize=18,
                                ),
                widget.Battery(
                                    font="JetBrainsMono Nerd Font Bold",
                                    fontsize=12,
                                    format='{percent:2.0%}',
                                ),
                widget.Spacer(
                                    length=7,
                            ),
            ],
            28,
                        border_color='#282738',
                        border_width=[0,0,0,0],
                        margin=[10,25,5,25],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 20

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"

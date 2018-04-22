# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Main module for the loading bar
    - ILoadingBar is an interface class which represents the loading bar;
    - StandardLoadingBar inherits from ILoadingBar and has customization.
"""


import sys

from .aloadingbar import ILoadingBar
from . import indicator
from . import background
from . import infos


__all__ = [
    'LoadingBar', 'InfoLoadingBar', 'VerboseLoadingBar',
    'MessageLoadingBar'
]


DEFAULT_DISPLAY_SIZE = 50


class LoadingBar(ILoadingBar):
    """
    Default loading bar.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, None)


class InfoLoadingBar(ILoadingBar):
    """
    Loading bar with speed, ETA, size downloaded info.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.StandardInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)


class MessageLoadingBar(LoadingBar):
    """
    Loading bar with a message to display info like filename, etc.
    """

    def __init__(self, tot_size):
        super().__init__(tot_size)

    def update(self, progression, msg):
        """
        Override update method.
        """
        s = self.update_loading_bar(progression)
        if s:
            s += '  ' + msg
            self.display(s)


class VerboseLoadingBar(ILoadingBar):
    """
    Verbose mode to display msg in the info label.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.VerboseInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)

    def update(self, progression, msg):
        s = self.update_loading_bar(progression)
        s += self.update_info(progression, msg)
        self.display(s)

    def update_info(self, progression, msg):
        """
        Override update method.
        """
        return self.info.display(progression, msg)

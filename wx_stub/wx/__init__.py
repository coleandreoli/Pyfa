"""Minimal wx stub to allow headless Pyfa use without a GUI."""


class Colour:
    def __init__(self, *args, **kwargs):
        pass


def GetTranslation(s):
    return s


def CallAfter(func, *args, **kwargs):
    func(*args, **kwargs)


class CommandProcessor:
    def __init__(self, *args, **kwargs):
        pass

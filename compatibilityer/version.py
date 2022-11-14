from importlib.metadata import version


try:
    __version__ = version("compatibilityer")
except Exception:
    __version__ = "unknown"

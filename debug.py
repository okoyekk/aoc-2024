import pprint


class Debug:
    """
    A utility class for quick debugging with easy enable/disable functionality.
    ===================================================== Quick start below
    import sys
    import os

    # Get the absolute path of the project root (folder A)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, project_root)

    from debug import Debug  # noqa: E402
    dbg = Debug(False)
    """
    
    def __init__(self, enabled=False):
        self.enabled = enabled
    
    def print(self, *args, **kwargs):
        if self.enabled:
            print(*args, **kwargs)
    
    def pp(self, *args, **kwargs):
        if self.enabled:
            pprint.pp(*args, **kwargs)
    
    def set_debug(self, enabled):
        self.enabled = enabled
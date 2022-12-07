__version__="0.0.1"

import os
from pathlib import Path

# Requires refl1d with webview to be installed in the jupyter env
def setup_refl1d():
    return {
        'command': ['python', '-m', 'refl1d.webview.server', '-p', '{port}'],
        'environment': {},
        'new_browser_tab': False,
        'timeout': 120,
        'launcher_entry': {
            'title': 'Refl1D',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'refl1d-icon.svg')
        }
    }

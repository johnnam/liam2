from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os

debug = os.environ.get("DEBUG", False)
input_directory = "."
output_directory = "."
skip_shows = False
assertions = "raise"
show_timings = True
autodump = None
autodump_file = None
autodiff = None

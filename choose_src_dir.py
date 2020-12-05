"""Replaces project source directory variable with user adjustable path.

Use ``custom_src_dir`` parameter in platformio.ini [env] section.
"""

from pathlib import Path


Import('env')

src_dir = env.GetProjectOption('custom_src_dir', default=None)
if src_dir:
    env.Replace(PROJECT_SRC_DIR=str(Path(env['PROJECT_DIR'], src_dir).resolve()))

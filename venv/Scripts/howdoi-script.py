#!C:\Bot_TEDDY\venv\Scripts\python.exe
# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'howdoi==2.0.20','console_scripts','howdoi'
__requires__ = 'howdoi==2.0.20'
import re
import sys

from howdoi.howdoi import command_line_runner

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(command_line_runner())
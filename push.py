#!/usr/bin/python3
"""
This module performs:
    - git add .
    - git commit
    - git push

The commit message is gotten from sys.argv

Example:
    push initial commit
"""


import os
import sys

commit_message = " ".join(s for s in sys.argv[1:])

os.system("git add .")
os.system('git commit -m "{}"'.format(commit_message))
os.system("git push -u origin master")

print("\n\nPushed with message: {}".format(commit_message))

#!/usr/bin/python3

import os
import sys

commit_message = " ".join(s for s in sys.argv[1:])

os.system("git add .")
os.system('git commit -m "{}"'.format(commit_message))
os.system("git push")

print("\n\nPushed with message: {}".format(commit_message))

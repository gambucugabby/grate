#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
import os
import subprocess
import filecmp
import sys
import time
import shutil
import Erlog


def ProcFiles(filename):
    with open(filename) as f:
        lines = f.readlines()

    print lines

#!/usr/bin/env python3.7

"""
List the top N on disk size dirs within the specified path
"""
import os, sys
if len(sys.argv) == 3:
    dir_name = sys.argv[1]
    num = sys.argv[2]
    
    exe = 'du -hs ' + dir_name + '* | sort -rh | head -' + num
    print exe
    os.system(exe)
else:
    print("\nPlease, provide path and number for list elements.")

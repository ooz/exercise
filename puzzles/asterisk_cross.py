#!/usr/bin/python
# coding: utf-8
'''
File: asterisk_cross.py
Author: Oliver Z.
Description:
    http://workplace.stackexchange.com/questions/39004/which-weak-algorithmic-strategies-i-have-that-lead-me-to-failing-coding-this-sim

Example:
$ python asterisk_cross.py 9
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
'''

import sys

def cross(size):
    for line_nr in range(size):
        line = [u" "] * size
        line[line_nr] = u"*"
        line[size-line_nr-1] = u"*"
        print u"".join(line)

def main(args):
    if len(args) != 1:
        print "Expected one number as an argument. Aborting!"
        sys.exit(1)

    size = int(args[0])
    cross(size)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)


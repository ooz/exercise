#!/usr/bin/python

# Instagram Unshredder challenge:
# http://instagram-engineering.tumblr.com/post/12651721845/instagram-engineering-challenge-the-unshredder
#
# Author: Oliver Z. <info@oliz.io>
# Date:   2011/11/20
# Note:   Basic idea:
#         1. Metric: Pairwise pixel difference between two pixel columns
#         2. Shred width: the width with the worst overall metric for the img
#         3. Unshredding: similar to StraightMergesort by finding
#                         pairs, 4-tupels, 8-tupels, etc. of unshredded
#                         sub-images.
#         Chosen algorithmic compactness over performance!
# TODO:   Greyscale conversion may be obstructive: remove it!
# LOC:    107 (counted by sloccount)

from PIL import Image
from collections import deque
import sys

# CONSTANTS ##################################################################
# '''
# Voodoo param: the more "diagonal" lines there are in the image
#               the higher this parameter should be.
#               Can be passed as parameter to the Deshred script
#               (overwrites the default value in that case).
# '''
DEFAULT_SHAKINESS = 2

GREYSCALE_MODE  = "L"
MAX_PIXEL_VALUE = 255

# FUNCTIONS ##################################################################
def list2chunks(l, chunkSize):
    chunks = range(0, len(l) / chunkSize)
    return map(lambda i: l[ (i * chunkSize) : ((i + 1) * chunkSize) ], chunks)

def image2ColumnList(img):
    imgData = img.getdata()
    chunks = list2chunks(list(imgData), img.size[0])              # List of rows
    return zip(*chunks)                                           # List of columns

# ''' l, r - two lists of equal length containing numbers '''
def colDiff(l, r):
    return map(lambda pair: abs(pair[0] - pair[1]), zip(l, r))

# ''' Normalized pairwise pixel difference between two columns of pixels. '''
def diffMetric(l, r):
    return sum(colDiff(l, r)) / float((len(l) * MAX_PIXEL_VALUE))

def rotate(l, n):
    d = deque(l)
    d.rotate(n)
    return list(d)

# '''
# Similar to #diffMetric(l, r).
# It chooses the minimum metric after shaking the pixel columns slightly.
# '''
def diffMetricShaky(l, r, shakiness):
    normal      = diffMetric(l, r)
    rotatedUp   = diffMetric(l, rotate(r, (-1 * shakiness)))
    rotatedDown = diffMetric(l, rotate(r, shakiness))
    return min(normal, rotatedUp, rotatedDown)

# ''' Returns all image columns that are next to a cut '''
def colsAtCuts(imgCols, shredWidth):
    colsToCheck = []
    for colNr in range(0, len(imgCols)):
        #   Column left of a cut          or Column right of a cut
        if ((colNr + 1) % shredWidth == 0 or colNr % shredWidth == 0):
            colsToCheck.append(imgCols[colNr])
    return colsToCheck

def applyMetricPairwise(colList):
    return map(lambda fstCol: diffMetric(colList[fstCol * 2], colList[fstCol * 2 + 1]),
               range(0, len(colList) / 2))

divisors = lambda n: filter(lambda x: n % x == 0, range(2, n / 2 + 1))

# '''
# Determine shred width by choosing the width with the overall worst metric at
# the shred border.
# Problem:  If the shred width is 32, shred of width 64 yield bad metric results
#           too.
# Solution: The algorithm is conservative, so a new (greater) width must
#           significantly worsen the metric. Worst case: assumption of a smaller
#           shred width (like 16 instead of 32).
# '''
def computeShredWidth(imgCols):
    maxMetricValue = 0.0
    maxMetricDiff  = 0.0
    shredWidth     = 0

    candidates = divisors(len(imgCols))                           # Since all shreds are of even length and fully divide the image
    for widthCandy in candidates:

        colsToCheck    = colsAtCuts(imgCols, widthCandy)[1:-1]    # Don't need the first and the last column for shredWidth determination
        colMetrics     = applyMetricPairwise(colsToCheck)
        avgMetricValue = sum(colMetrics) / float(len(colMetrics))

        if (maxMetricValue == 0.0):
            maxMetricValue = avgMetricValue
        else:
            if (avgMetricValue > maxMetricValue + maxMetricDiff):
                maxMetricDiff  = avgMetricValue - maxMetricValue
                maxMetricValue = avgMetricValue
                shredWidth     = widthCandy

    return shredWidth

# '''
# Returns a shred permutation vector for unshredding the image.
# The basic idea is similar to StraightMergesort:
# 1. Find all pairs of shreds yielding best metric results
# 2. Find all 4-Tupels        yielding best metric results
#    by combining the pairs from 1.
# 3. Find all 8-Tupels [...] and so on.
#
# Also works with a shred number that is not a power of 2.
# '''
def findDeshredPermu(shreds, shakiness):
    permu = map(lambda x: [x], range(0, len(shreds)))
    while (len(permu) > 1):
        newPermu = []
        while (permu != []):
            a = permu.pop(0)
            if (permu != []):
                minDiff = 1.0
                abConcat = True                                   # concat "a + b", otherwise "b + a"
                bestPartner = []
                for b in permu:
                    abDiff = diffMetricShaky(shreds[a[-1]][1], shreds[b[0]][0], shakiness)
                    baDiff = diffMetricShaky(shreds[b[-1]][1], shreds[a[0]][0], shakiness)
                    if (abDiff < minDiff):
                        minDiff = abDiff
                        bestPartner = b
                        abConcat = True
                    if (baDiff < minDiff):
                        minDiff = baDiff
                        bestPartner = b
                        abConcat = False
                if (abConcat):
                    newPermu.append(a + bestPartner)
                else:
                    newPermu.append(bestPartner + a)
                permu.remove(bestPartner)
            else:
                newPermu.append(a)
        permu = newPermu
    return permu[0]

def correctImage(img, permu, shredWidth):
    correct = Image.new(img.mode, img.size)
    for i in range(0, len(permu)):
        topLeftX = permu[i] * shredWidth
        region = img.crop((topLeftX             , 0          ,
                           topLeftX + shredWidth, img.size[1]))
        correct.paste(region, (i * shredWidth, 0))
    return correct

# MAIN #######################################################################
if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 2 or len(args) > 3):
        print "Deshred usage: $ Deshred <infile> <outfile> [<shakiness value>]"
    else:
        img     = Image.open(args[0])
        imgGrey = img.convert(GREYSCALE_MODE)
        imgCols = image2ColumnList(imgGrey)

        shredWidth   = computeShredWidth(imgCols)
        shreds       = list2chunks(colsAtCuts(imgCols, shredWidth), 2)
        shakiness    = DEFAULT_SHAKINESS
        if (len(args) == 3):
            shakiness = int(args[2])
        deshredPermu = findDeshredPermu(shreds, shakiness)

        deshredImg = correctImage(img, deshredPermu, shredWidth)
        deshredImg.save(args[1])


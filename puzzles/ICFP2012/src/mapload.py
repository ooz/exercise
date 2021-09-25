import sys

from minemap import Map

class MapLoader:
    def __init__(self):
        pass

    def __padLine(self, line, maxLength):
        if len(line) < maxLength:
            return self.__padLine(line + " ", maxLength)
        return line

    def __mapFromInputLines(self, lines, metalines):
        if lines == []:
            return None
        lines.reverse()
        maxLength = max(map(lambda l: len(l), lines))
        lines = map(lambda l: self.__padLine(l, maxLength), lines)
        water = 0
        flood = 0
        proof = 10
        growth = 25
        razors = 0
        trampos = []
        for ml in metalines:
            elems = ml.split(" ")
            if len(elems) >= 2:
                if "Waterproof" in elems:
                    proof = int(elems[1])
                elif "Flooding" in elems:
                    flood = int(elems[1])
                elif "Water" in elems:
                    water = int(elems[1])
                elif "Growth" in elems:
                    growth = int(elems[1])
                elif "Razors" in elems:
                    razors = int(elems[1])
                elif "Trampoline" in elems:
                    trampos.append((elems[1], elems[3]))

        return Map(lines, [water, flood, proof, growth, razors, trampos])

    def mapFromStdin(self):
        lines = sys.stdin.readlines()
        strippedLines = map(lambda l: l.rstrip(), lines)
        lines = []
        metalines = []
        endOfMapData = False
        for l in strippedLines:
            if (l == ""):
                endOfMapData = True
            else:
                if (not endOfMapData):
                    lines.append(l)
                else:
                    metalines.append(l)

        return self.__mapFromInputLines(lines, metalines)

    def mapFromFile(self, path):
        f = open(path, 'r')
        lines = []
        metalines = []
        endOfMapData = False
        for line in f:
            stripped = line.rstrip()
            if (stripped == ""):
                endOfMapData = True
            else:
                if (not endOfMapData):
                    lines.append(stripped)
                else:
                    metalines.append(stripped)

        f.close()
        return self.__mapFromInputLines(lines, metalines)



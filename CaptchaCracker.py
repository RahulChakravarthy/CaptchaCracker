import os
from PIL import Image
import sys as System
import re


def parseFile():
    # read file
    file = open(System.argv[1], "r")
    lines = file.readlines()
    file.close()
    # Strip all new lines and whitespace replace spaces with ","
    listedLines = list()
    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', ',')
        lines[index] = line.replace(' ', ',')
        listedLines.extend(lines[index].split(","))

    imageLines = list()
    for entry in listedLines:
        entry = re.sub("[^0-9]", "", entry)  # Strip non numerics
        imageLines.append(entry)

    imageLines = list(map(int, imageLines))
    zipImageIterable = zip(*[imageLines[i::3] for i in range(3)])  # Group into 3 sized tuples representing RGB code
    return list(zipImageIterable)


def writeFile(image=Image.Image):
    # Write file
    image.save(os.path.dirname(System.argv[1])+ "\\" + os.path.basename(os.path.splitext(System.argv[1])[0]) + "-output.png")


def createImage(arrayOfRGBs=list):
    output = Image.new("RGB", (60, 30))
    output.putdata(arrayOfRGBs)
    return output


def main():
    outputImage = createImage(parseFile())
    writeFile(outputImage)

main()

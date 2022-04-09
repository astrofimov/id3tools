#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0
# renamer.py - renamer script
# Copyright (C) 2022 Alexander Trofimov <molochmail@gmail.com>
import sys
try:
    from mutagen import id3
except ModuleNotFoundError:
    print("[E] please install mutagen package: # pip3 install mutagen")
    sys.exit(-1)
import os

if len(sys.argv) < 3:
    print("[E] Command line example: #renamer <input folder> <output folder>")
    print("[E] <input folder> absolute or relative path")
    print("[E] <output folder> absolute or relative path")
    sys.exit(-2)

print("[I] Input directory:", sys.argv[1])
print("[I] Output direcotry:", sys.argv[2])

if not os.path.exists(sys.argv[1]):
    print("[E] Input directory does not exists or access is not granted")
    sys.exit(-3)

if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])
else:
    print("[W] Output directory already exists")


for fname in os.listdir(sys.argv[1]):
    if ".mp3" in fname or ".MP3" in fname:
        fpi = sys.argv[1] + "/" + fname
        print("[I] Processing file:", fpi)
        tags = id3.ID3(fpi)
        band = str(tags['TPE1'])
        print(band)
        song = str(tags['TIT2'])
        print(song)
        fi = open(fpi, 'br')
        fpo = sys.argv[2] + "/[" + band + "]-[" + song + "].mp3"
        fo = open(fpo, 'bw')
        fo.write(fi.read())
        fo.close()
        fi.close()

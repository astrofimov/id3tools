#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0
# tagformer.py - tag former script
# Copyright (C) 2022 Alexander Trofimov <molochmail@gmail.com>
import sys
try:
    from mutagen import id3
except ModuleNotFoundError:
    print("[E] please install mutagen package: # pip3 install mutagen")
    sys.exit(-1)
import os

if len(sys.argv) < 5:
    print("[E] Command line example:")
    print("[E] # renamer <input folder> <output folder> <band name> <cut>")
    print("[E] <input folder> absolute or relative path")
    print("[E] <output folder> absolute or relative path")
    print("[E] <band name> to be set as an Artist in ID3 tag")
    print("[E] <cut> number of characters to be ignored in front of file name")
    sys.exit(-2)

print("[I] Input directory:", sys.argv[1])
print("[I] Output direcotry:", sys.argv[2])

if not os.path.exists(sys.argv[1]):
    print("[E] Input directory does not exists or access is not granted")
    sys.exit(-3)

if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])
else:
    print("[W] NOTE: Output directory already exists, existing files might be corrupted")

band = sys.argv[3]
print("[I] Band:", band)
cut = int(sys.argv[4])
for fname in os.listdir(sys.argv[1]):
    if ".mp3" in fname or ".MP3" in fname:
        fpi = sys.argv[1] + "/" + fname
        print("[I] Processing file:", fpi)
        fpo = sys.argv[2] + "/" + fname
        fi = open(fpi, "br")
        fo = open(fpo, "bw")
        fo.write(fi.read())
        fo.close()
        fi.close()
        song = fname[cut:-4]
        print(song)
        tags = id3.ID3(fpo)
        tags['TPE1'] = id3.TPE1(encoding=3, text=band)
        tags['TIT2'] = id3.TIT2(encoding=3, text=song)
        tags.save(fpo)

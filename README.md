# id3tools
A couple of tools to arrange MP3 collection.
Dependency:
1. Mutagen
Tools list:
1. renamer.py - reads <input folder> and creates files in <output folder> with
 names using the following pattern [ARTIST]-[TITLE].mp3.
2. tagformer.py - reads <input folder> and creates files in <output folder>
 with the same names, but with tag containing the following data: ARTIST is
 equal to file name without prefix and .mp3 ending; TITLE is set to <band>
 name.

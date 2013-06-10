#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    podtag.py
#
#    Copyright 2013 Mike Harley <VestedSkeptic@gmail.comm>
#         
#    podtag is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    podtag is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    with these source files.  If not, see <http://www.gnu.org/licenses/>.

import argparse, sys, os
from mutagen.easyid3 import EasyID3

podcast_dir = "D:\\audio files\\c_on_ipod\\podcasts"
podcast_mapping = {}

# *********************************************************
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--i",     nargs='?', default='podcast.txt',         metavar='input_file',                 help="text file containing podcast tag info, default is 'podcast.txt'")
    args = parser.parse_args()
    
    podcast_input_file = podcast_dir + "\\" + args.i
    try:
        iFile = open(podcast_input_file)
    except  IOError:
        print "ERROR: Input file [%s] does not exist" % (podcast_input_file)
        sys.exit()

    # read iFile for podcast info and store in dictionary
    for line in iFile:
        splitMarker = ","
        sp = str.rsplit(str.strip(line), splitMarker, 1)
        if len(sp) == 2:
            podcast_mapping[str.strip(sp[0])] = str.strip(sp[1])         
        
    mp3_count = 0
    
    # get directories and confirm there is a matching entry in podcast_mapping
    dirlist = os.listdir(podcast_dir)
    for d in dirlist:
        full_dir = "\\".join([podcast_dir, d])
        if os.path.isdir(full_dir):
            if not podcast_mapping.has_key(d):
                print "ERROR: '%-30s' does not have an entry in '%s'" % (d, args.i)
            else:
                mp3_count += update_mp3_tags_in_directory(full_dir, podcast_mapping[d])
    
    iFile.close()
    if mp3_count:
        print " "
        print "%s mp3 files processed." % (mp3_count)
    print " "
    
    raw_input("Press key to continue.")
    

# *********************************************************
def update_mp3_tags_in_directory(directory, tag):
    count = 0

    filelist = os.listdir(directory)
    for f in filelist:
        audio = EasyID3(directory+"\\"+f);

        audio['artist'] = unicode(tag);
        audio['album'] = unicode(tag);
        audio['title'] = unicode(f);

        audio.save()
        
        count += 1
    
    return(count)

# *********************************************************        
if __name__ == "__main__":
    main()
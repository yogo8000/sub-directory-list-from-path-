import sys
import os
import DirectoryToList as D2L
import DirectoryToPathImplementingOSWalk as D2LOSWALK

for i in range(1, len(sys.argv)):
    try:
        directory_path = sys.argv[i]
        directory_list_1 = D2L.create_list_from_directory(directory_path)
        directory_list_2 = D2LOSWALK.directory_to_list(directory_path)

        if directory_list_1 != directory_list_2:
            print "Wrong answer"
        else:
            print "Passed test"
    except Exception as e:
        print e

#/user/bin/
import os, glob
# Define directory to look for file type
os.chdir("/Users/sharadtiwari1/Downloads/")
count = 0
#You may change the file ext to get desired file type
for file in glob.glob("*.zip"): 
    print(file)
    count += 1

print "Total number of file %d" %(count) #
    

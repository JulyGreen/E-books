import os
import sys
import re

def listyoudir( level, path ):  
    for i in os.listdir(path):  
        if os.path.isdir(path + '\\' + i):
            print '  '*(level+1) + i  
            listyoudir(level+1, path + '\\' + i)
        else:
            #print i
            if( i.endswith( ".c" ) or i.endswith( ".h" ) ):
                print '  '*(level+1) + i, ':',
                afile = open( path + '\\' + i )
                lines = afile.readlines( 200 )
                for line in lines:
                    m = re.match( r'\s*#include\s*[<"](.*)[">]', line )
                    if m:
                        print m.group(1),
                print
                    
print "Please input project directory:"
rootpath = sys.stdin.readline().strip()
stream = open( 'output.txt', 'w' )
os.dup2(stream.fileno(), 1)
os.dup2(stream.fileno(), 2)
stream.close()        
rootpath = os.path.abspath( rootpath )  
print rootpath  
listyoudir( 0, rootpath )
#! /usr/bin/env python

import sys 
import fnmatch
import os
#import numpy as np
from labelFile import LabelFile, LabelFileError
from pprint import pprint
import re
from pprint import pprint
def getBBox(shapes):
        s = []
        #for label, points, line_color, fill_color in shapes:
            #shape = Shape(label=label)
            # for x, y in points:
            #     print  x,y 

def main():
  db_name=sys.argv[1] # database name 
  annotations_dir=os.environ['DATABASES']+os.sep+db_name+os.sep+"pics"
  print "Annotations path: " , annotations_dir 
  for subdir, dirs, files in os.walk(annotations_dir):
        for file_ in files:
          #print  "file:", file_     
          #if fnmatch.fnmatch(file_, '*.'+LabelFile.getSuffix()):
          if LabelFile.isLabelFile(file_):
                 try:
                        filename=os.path.join(subdir, file_)
                        labelFile = LabelFile(filename)
                        if  LabelFile.isLabelFile(labelFile.imagePath):
                               print "image",labelFile.imagePath
			       # fix image path and save 
			       #labelFile.imagePath = labelFile.imagePath.replace(LabelFile.getSuffix(),".jpg")
			       labelFile.imagePath = re.sub(LabelFile.getSuffix()+'$',".jpg",labelFile.imagePath)
			       #print labelFile.imagePath
			       #pprint(labelFile.__dict__)
			       labelFile.ssave(filename)
			       
                        getBBox(labelFile.shapes)

                 except LabelFileError, e:
                        print "%s, Make sure %s is a valid label file."%(e,file_)
                        return False
                
                #imageData = self.labelFile.imageData
                

if __name__ == "__main__":
       main()
       

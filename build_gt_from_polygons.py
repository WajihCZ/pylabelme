#! /usr/bin/env python

import sys 
import fnmatch
import os
#import numpy as np
from labelFile import LabelFile, LabelFileError
from pprint import pprint


def getBBox(shapes):
        boxes = []
        for label, points, line_color, fill_color in shapes:
		x_min=x_max=points[0][0]
		y_min=y_max=points[0][1]
		#print points
		for x, y in points:
			 #x=float(x)
			 #y=float(y)
			 #print x,y
			 if(x>x_max):x_max=x
			 else :
				 if(x<x_min):x_min=x
			 if(y>y_max):y_max=y 
			 else :
				 if(y<y_min):y_min=y
			 # print "---------------",x_min,y_min,x_max,y_max
			 
		boxes.append((label,x_min,y_min,x_max,y_max))
	return boxes

def main():

  db_name=sys.argv[1] # database name 
  gt_output_fn=sys.argv[2]
  annotations_dir=os.environ['DATABASES']+os.sep+db_name+os.sep+"pics"
  pics_dir=os.environ['DATABASES']+os.sep+db_name+os.sep+"pics/"
  gt_output_path=os.environ['DATABASES']+os.sep+db_name+os.sep+gt_output_fn

  print "Annotations path: " , annotations_dir 
  annotated_im_nbr=0
  with open(gt_output_path, 'w') as f:
    for subdir, dirs, files in os.walk(annotations_dir):
        for file_ in files:
          #print  "file:", file_     
          #if fnmatch.fnmatch(file_, '*.'+LabelFile.getSuffix()):
          if LabelFile.isLabelFile(file_):
                 try:
                        filename=os.path.join(subdir, file_)
                        labelFile = LabelFile(filename)
                        if  LabelFile.isLabelFile(labelFile.imagePath):
                               print "there is a problem with image path : ",labelFile.imagePath
			
			for bbox in  getBBox(labelFile.shapes):
				f.write ("%s %s %d %d %d %d %s\n" % (bbox[0],labelFile.imagePath.replace(pics_dir,''),float(bbox[1]),float(bbox[2]), float(bbox[3]),float(bbox[4]),bbox[0]))

                 except LabelFileError, e:
                        print "%s, Make sure %s is a valid label file."%(z)
                        return False
		 annotated_im_nbr+=1
                
                #imageData = self.labelFile.imageData
  print "annotated images nbr :" , annotated_im_nbr
                

if __name__ == "__main__":
       main()
       

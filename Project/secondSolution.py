#Yinghao Lin

#input: output of previous

#output: 76 files 

import xlrd
import xlwt
from xlwt import Workbook
from numpy import *
from pylab import plot, show
from hurst import compute_Hc
import statistics
from scipy.stats import kurtosis
from scipy.stats import skew
import pandas as pd
import scipy as sc
import timeit
start=timeit.timeit()
loc = ("C:\\Users\lyh2i\\Desktop\\2019 Spring\\csc 498 data mining\\testing.xls")
file = ["sz1_pre","sz2_pre","sz3_pre","sz4_pre","sz5_pre","sz6_pre","sz7_pre","sz8_pre","sz1_ict","sz2_ict","sz3_ict","sz4_ict","sz5_ict","sz6_ict","sz7_ict","sz8_ict"]
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0
features = ["Energy","Variance","Min","Max","Mean","LineLength","StdDev","Kurtosis","Skew","Entropy","Hurst"]
for i in range(1,77):
    WB= Workbook()

    sheet1 = WB.add_sheet("sheet 1")
    
    filename = "EC"+str(i)
    #this for loop will write the feature name for each file 
    for F in range(len(features)):
        sheet1.write(0,F,features[F]+str(filename))
    count = 0
    for x in range(16):
        for y in range(11):
            value = sheet.cell_value(i+1,y+11*count)
            sheet1.write(1+x,y,value)
        count +=1
        if(x<8):
            sheet1.write(1+x,11,"pre")
        else:
            sheet1.write(1+x,11,"ict")
    sheet1.write(0,11,"class label")
    
        
    
    
    count = count +1
    WB.save(filename+".xls")
    print (count)
 
print(timeit.timeit()-start)

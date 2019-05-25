#Yinghao Lin

#input: 16 files

#output: 1 files
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
import time
def Burst(a):
    lags = range(2, 20)
    tau = [sqrt(std(subtract(a[lag:], a[:-lag]))) for lag in lags]
    m = polyfit(log(lags), log(tau), 1)
    return m[0]*2.0

def Average(n):
    return sum(n)/len(n)

def Variance(n):
    mean = Average(n)
    sum1 = 0.0
    for i in n:
        sum1+=(i-mean)**2    
    return (sum1/(len(n)-1))

def LineLength(n):
    sum = 0
    for i in range(2,len(n)):
        sum += abs(n[i]-n[i-1])
    return sum
    
def ent(data):
    p_data= data.value_counts()/len(data) # calculates the probabilities
    entropy=sc.stats.entropy(p_data)  # input probabilities to get the entropy 
    return entropy
def Energy(n):
    total = 0
    #The summation just means each x^2 added into the larger final value.
    for i in n:
        sqr = i**2
        total += sqr
    final = total/len(n)
    return final
    
file = ["sz1_pre","sz2_pre","sz3_pre","sz4_pre","sz5_pre","sz6_pre","sz7_pre","sz8_pre","sz1_ict","sz2_ict","sz3_ict","sz4_ict","sz5_ict","sz6_ict","sz7_ict","sz8_ict"]
#print ("enter the name of data file(ex: sz1_ict):")
#Name= input()
#print ("enter the number of file(ex:1,2,3 ):")
#count = input()
#print (Name)
#print (count)
#loc = ("C:\\Users\\lyh2i\\Desktop\\epilepsy\\"+Name+".xlsx")
#print (loc)
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
#WB = Workbook()
#sheet1 = WB.add_sheet("sheet 1")

temp = []
time1 =[]
WB = Workbook()
sheet1 = WB.add_sheet("sheet 1")
count = 1
for d in file:
    loc = ("C:\\Users\\lyh2i\Desktop\\2019 Spring\\csc 498 data mining\\data\\"+d+".xlsx")
    print("reading",count," file",d,"at",loc,"start processing")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for z in range(11):
        sheet1.write(0,(int(count)-1)*11+z ,d)
    
    sheet1.write(1,(int(count)-1)*11 ,"energy")
    sheet1.write(1,(int(count)-1)*11 +1,"Variance")
    sheet1.write(1,(int(count)-1)*11 +2,"Min")
    sheet1.write(1,(int(count)-1)*11 +3,"Max")
    sheet1.write(1,(int(count)-1)*11 +4,"Mean")
    sheet1.write(1,(int(count)-1)*11 +5,"LineLength")
    sheet1.write(1,(int(count)-1)*11 +6,"std dev")
    sheet1.write(1,(int(count)-1)*11 +7,"kurtosis")
    sheet1.write(1,(int(count)-1)*11 +8,"skew")
    sheet1.write(1,(int(count)-1)*11 +9,"entropy")
    sheet1.write(1,(int(count)-1)*11 +10,"Hurst")
    for r in range(sheet.nrows):
        for c in range(sheet.ncols):
            temp.append(sheet.cell_value(r,c))
            
     
        
        start = time.time()
        Energy(temp)
        #Variance(temp))
        min(temp)
        max(temp)
        Average(temp)
        LineLength(temp)
        statistics.pstdev(temp)
        kurtosis(temp)
        skew(temp,axis=0,bias=True)
        #df ='00'+pd.Series(temp).astype(str)
        #sheet1.write(r+2,(int(count)-1)*11+9,ent(df))
            
        #Burst(temp)
        #sheet1.write(r+2,(int(count)-1)*11+10,)
        #sheet1.write(r+2,(int(count)-1)*11+11,)
        time1.append(time.time()-start)
        temp = []
    print("reading",count," file",d,"at",loc,"process is over")
    count +=1 
    

print(Average(time1))
WB.save("testing.xls")















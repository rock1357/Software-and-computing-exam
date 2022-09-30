import numpy as np
import csv

'c=number of row to skip in the acqusition files, delimiter= symbol between the [time,Voltage/current] columns'
'filename_acquisition=name of the experiment file where NPs are stimulated to oxidize/reduce'
'filename_noise= name of the file where only noise is recorded in order to extract the standard deviation'
c=10
delimiter_=';'
filename_acquisition='ele3_300mV_50k_1min_after10sbiason.txt'
filename_noise='ele3_300mV_50k_1min_after10sbiason.txt'
'--------------------------------------------------------------------------------------------'

test=0; 'if test is =0 it will activate the interactive user mode, otherwise it will activate the developer mode: no needs to insert parameters and pytests available for finding proiblems'

if test==0:
    
    
    

    'step 1: asking for the file-name of the NPs experiment and for the recording of the noise trace coming from the electrode'
    
    filename_acquisition=str(input('A) put the file name of the acqusition:  '))
    filename_noise=str(input('B) put the file-name of the noise acquisition:  '))
    delimiter_=str(input('C) insert the kind of delimiter between time and current data columns in the data file ( , or ; ) :'))
   
    'step 2: the csv library allow to open the data file as string in order to read it and understand how many rows there are before the real data'
    with open(filename_acquisition, 'r') as f:
        i=1
        f_csv = csv.reader(f,delimiter=',')
        for line in f_csv:
            print('D) here will be shown the current row number of your data file for checking the number from wich time and current data start:  ')
            print(str(line))
            print('this is the first row of the file')
            s=input('D.1) do you want to show the next row [y=yes] , [n=no]? ')
            if s=='y':
                
                i=i+1
                print('this is the ',i,' row of the file')
                 
            else:
                c=int(input('E) select how many rows to skip in your csv file before float numbers of the chronoameprometric registration start:'))
                
                break
        #insert a warning for the case of non string name 



    
'step 3: extracting the data as float numbers'
print('PROCESSING: importing the data of your recorded chronoamperometric experiment...')
#c=input('write the number of rows of your file data from which the numerical data starts from:')
data = np.genfromtxt(filename_acquisition, delimiter=delimiter_,skip_header=c)

print('PROCESSING: importing the data of your recorded noise (no bias)...')
data2 = np.genfromtxt(filename_noise, delimiter=delimiter_,skip_header=c)

'step 4: calling the data as t and V for the experiment and tn and Vn for the noise acquisition'

t=data[:,0]
V=data[:,1]

tn= data2[:,0]
Vn= data2[:,1]

'step 4.1: testing if the data are read as float numbers'

def test_data_are_float():
    
    for i in range(0,len(t)):
        
        assert type(t[i])==np.float64
        assert type(V[i])==np.float64
    for i in range(0,len(tn)):
        assert type(tn[i])==np.float64
        assert type(Vn[i])==np.float64


        
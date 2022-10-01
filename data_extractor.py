import numpy as np
import parameter_setter as ps
import plot_shower as pls
'step 0: are you an user or a pogrammer decided to improove the program?'
test=1; 'if test is =0 it will activate the interactive user mode, otherwise it will activate the developer mode: no needs to insert parameters and pytests available for finding proiblems'

if test==1:
    print('***^^STARTING PYTHON CHRONOAMPEROMETRIC txt/csv DATA IMPORTER(PROGRAMMER MODE: test=1)^^*** \n')
else:
    print('***^^STARTING PYTHON CHRONOAMPEROMETRIC txt/csv DATA IMPORTER:(USER MODE: test=0)^^***')

if test==1:
    c=10;'c=number of row to skip in the acqusition files'
    print('-the number of columns to skip was automatically set to:',c)
    delimiter_=';'; ' delimiter= symbol between the [time,Voltage/current] columns'
    print('-the delimiter of your file was automatically set as:',delimiter_)
    filename_acquisition='ele3_300mV_50k_1min_after10sbiason.txt'; 'filename_acquisition=name of the experiment file where NPs are stimulated to oxidize/reduce'
    print('-the file-name of your chronoamperometric experiment is:',filename_acquisition)
    filename_noise='ele3_300mV_50k_1min_after10sbiason.txt'; 'filename_noise= name of the file where only noise is recorded in order to extract the standard deviation'
    print('-the file-name of your noise registration is:',filename_noise,'\n')


def test_be_sure_your_file_are_txt_or_csv():
    assert 'csv' or 'txt' in filename_acquisition
    assert 'csv' or 'txt' in filename_noise
    





'--------------------------------------------------------------------------------------------'



if test==0:

    'step 1.0: asking for the file-name of the NPs experiment and for the recording of the noise trace coming from the electrode'
    
    filename_acquisition=str(input('A) put the file name of the acqusition: '))
    filename_noise=str(input('B) put the file-name of the noise acquisition: '))
    delimiter_=str(input('C) insert the kind of delimiter between time and current data columns in the data file ( , or ; ) : '))
    c=int(input('E) select how many rows to skip in your csv file before float numbers of the chronoameprometric \n   registration start: '));




   
    'step 1.1: the csv library allow to open the data file as string in order to read it and understand how many rows there are before the real data'
   # with open(filename_acquisition, 'r') as f:
         
   #     i=1
    #    f_csv = csv.reader(f,delimiter=delimiter_)
        
        
     #   print('D) here will be shown the current row number of your data file for checking \n   the number from wich time and current data start:  ');
      #  for line in f_csv:
       #     print('this is the ',i,' row of the file--->',str(line),'<---');
            
        #    s=str(input('D.1) do you want to show the next row [y=yes] , [n=no]? '));
         #   if s=='y':
                
          #      i=i+1;
                
                 
           # else:
            #    c=int(input('E) select how many rows to skip in your csv file before float numbers of the chronoameprometric registration start:'));
                
             #   break
        #insert a warning for the case of non string name 
        #correct the problem of file reading



    
'step 1.2: extracting the data as float numbers'

print('PROCESSING: importing the data of your recorded chronoamperometric experiment...')
data = np.genfromtxt(filename_acquisition, delimiter=delimiter_,skip_header=c)

print('PROCESSING: importing the data of your recorded noise (no bias)... \n')
data2 = np.genfromtxt(filename_noise, delimiter=delimiter_,skip_header=c)

def test_extracted_data_should_be_time_and_volt_or_amp_so_2xN_dimension():
    assert np.size(data, 1)==2;'make sure the array contains 2 columns: time and Volt/Ampere'
    assert np.size(data2, 1)==2;'make sure the array contains 2 columns: time and Volt/Ampere'

    


'step 1.3: calling the data as t and V for the experiment and tn and Vn for the noise acquisition'

t=data[:,0]
V=data[:,1]

tn= data2[:,0]
Vn= data2[:,1]


def test_the_length():
    assert len(t)==len(V)
    assert len(tn)==len(Vn)





'testing if the data are read as float numbers'

def test_extracted_data_are_float():
    
    for i in range(0,len(t)):
        
        assert type(t[i])==np.float64
        assert type(V[i])==type(t[i])

    for i in range(0,len(tn)):
        assert type(tn[i])==np.float64
        assert type(Vn[i])==type(tn[i])
        assert tn[i]!=np.nan
        assert Vn[i]!=np.nan
        
def test_data_are_not_nan():
    
    for i in range(0,len(t)):
        assert t[i]!=np.nan
        assert V[i]!=np.nan
    

    for i in range(0,len(tn)):
        assert tn[i]!=np.nan
        assert Vn[i]!=np.nan
    
if test==1:
    print('***^^ENDING PYTHON CHRONOAMPEROMETRIC txt/csv DATA IMPORTER:(PROGRAMMER MODE: test=1)^^*** \n')
else:
    print('***^^ENDING PYTHON CHRONOAMPEROMETRIC txt/csv DATA IMPORTER:downloading of the data (USER MODE: test=0)^^*** \n')

pls.plot_shower(t,V,0,tn,Vn)

ps.parameter_setter(t,V,tn,Vn,test)

        
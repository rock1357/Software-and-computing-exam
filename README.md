# Software-and-computing-exam

This program is made in order to select and integrate the peaks present in a chronoamperometric time trace; the chronoamperometric time trace is a trace that
show the current peaks related with the impact of nanoparticles against the working electrode.
The oxidation/reduction of such NPs, as consequence of the impact, is stimulated by the presence of:
a) chathalist molecules
b) bias use.
Then the goal is to make a software able to extract the peaks that are more probable to be realted to NPs discharge processes and not to the 
background noise.
This aim is reached by the program that we are going to present.
It really start with the definition of a parameter: "test".
It should be chosen == 0 or different from 0.
If it is equal to 0 it means we want to use the  "user operation mode", that is the modality for who wants only to exploit the program functionality, without knowing the code of the program
or without having the wish to modify it.
If test is not 0 we can exploit the programmer mode; it is a faster way to reproduce the code in which we can skip to write the answer to the questions 
that help the user to understand what is going on during the execution in the user modality (test=0). In this way we can focus only on the fixing of an eventual bug.

In the programmer mode we should be sure, before to play the program, to have written:
a) In the data_extractor.py module:
a.1)  c=10;'c=number of row to skip in the acqusition files' -> line 13 
a.2)  delimiter_=','; ' delimiter= symbol between the [time,Voltage/current] columns'-> line 15 
a.3)  filename_acquisition->name of the experiment chronoamperometric registration file where NPs were stimulated to oxidize/reduce->line 17
a.4)  filename_noise->filename_noise= name of the file where only noise is recorded-> we can know the standard deviation of the noise at the electrode-> line 19
a.5)

b) In the parameter_setter.py module we have to set:
b.1) The gain of the eventual amplification step in order to bring the data to the real dimension unit->line 16.
b.2) The time interval of the part of the total trace we want to analyze (it is possible to select the whole trace by putting t1=0 and t2=duration)-> lines 51 and 52.
b.3) The k factor (for positive or negative analysis) is a parameter that will be multiplied for the standard deviation value of the noise trace; this value (called noise=k*std(V_noise)) will be used as noise delimiting level for the height constraint->line 91 and 92
b.4) The time constraint for peak selection.
b.5) The desire if we want to scan the positive (V>0 side) or the negative (V<0) part of the trace.

c) Negative/postive_scanner.py module:
-Here we don't have to select any parameter because they were almost all already written in the previous module.
This module will simply apply an alghoritm where the trace is scanned, starting from the first value of V>0 up to the last value of V>0 of the whole trace.
Suppose we selected to scan the negative part of the trace.
When a value V<noise (noise is negative here because k_factor is set to be <0) is found, the algorithm come back to the first preceeding value V>0 and here 
set the starting point of that peak.
Done that, it go forward up to the second V>0 ( at the right of the min value of the peak) completing the peak delimitation.
In the middle all the peak points are saved in a new array.
So the peaks are selected in height in this module!
After the whole selected trace was scanned, the current module will invoce the negative_peak_levelling() method.

d) Negative_peak_levelling.py module:
-Here the peak are selected in time duration. If the time duration is higher than the time_constraint one, choosen in the parameter_setter.py module by the user, then the peak will be extracted.
The starting and ending point of each selected peak is set to 1e-30 ( a value close enough to zero). Although we want to level all the peak at V=0 level we can not
use the initialization V(start_of_the_peak)=V(end_...)=0 because for the plotting we want that all the value that are =0 should be eliminated from the trace.
This is done by changing theme in nan (not a number) with an ending for loop. In this way the 1e-30 values of  the extracted peak are left unchanged.

e) integrato.py module:
-Here we conclude the peaks analysis by making an integration of the heihgt and time selected peaks! 
Here is important to set previously the parameters:
-density of the element constituting the NPs
-atomic/molecular weight of the element constituting the NPs
In fact it will be asked to the user if he want also to calculate the diameters of the peaks and this can be posibbile only if he knows these two quantities.

NB) between one module and the other will be activated the plot_shower() method which can plot all the graphs at the end of each process in order to make the 
programmer/user to be able to see the results in a pictorial way.





import matplotlib.pyplot as plt
import pandas as pd

def plot_shower(t1,V1,a,t2=0,V2=0):
    if a==0:
        'plot of the total time trace-figure divided by the gain'
        # plotting the points 
        plt.plot(t1,V1)
      
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')
      
        # giving a title to my graph


        plt.title('total time trace')
      
    # function to show the plot
        plt.show()
        
        'now we reinitialize the V and t variables with the choosen time range'





        'plot of the noise trace'
        # plotting the points 
        plt.plot(t2,V2)
      
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')
      
        # giving a title to my graph
        plt.title('your noise trace')
      
        # function to show the plot
        plt.show()
        return 0
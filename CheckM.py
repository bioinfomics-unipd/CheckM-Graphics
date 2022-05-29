#Python
engine='python'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from matplotlib.backends.backend_pdf import PdfPages
from os import listdir
from os.path import isfile, join

parser=argparse.ArgumentParser(description="Graphical visualization of MAGs quality." 
"\nCreate a Folder called CheckM_inputs containing the file(s) to analyze (in the form of CheckM outputs) and place it in the same directory of the script."
"\nOne pdf is generated for each input file." "\n" 
"( GP=A*Completeness - B*Contamination + C*(Contamination * (strain_heterogeneity/100)) + D*log(N50) + E*log(size) )")

parser.add_argument('-A',type=float, action='store', default=1, help='an int or float value for Global Parameter calculation, default value is set to 1')
parser.add_argument('-B',type=float, action='store', default=5, help='an int or float value for Global Parameter calculation, default value is set to 5')
parser.add_argument('-C',type=float, action='store', default=1, help='an int or float value for Global Parameter calculation, default value is set to 1')
parser.add_argument('-D',type=float, action='store', default=0.5, help='an int or float value for Global Parameter calculation, default value is set to 0.5')
parser.add_argument('-E',type=float, action='store', default=0, help='an int or float value for Global Parameter calculation, default value is set to 0')
args=parser.parse_args()


#Calculate global parameter for each bin and add column to the dataframe
def global_parameter(data, A=1, B=5, C=1, D=0.5, E=0):
    """
    function to calculate a global parameter representing the global quality of the MAGs.
    GP=A*Completeness - B*Contamination + C*(Contamination * (strain_heterogeneity/100)) + D*log(N50) + E*log(size)
    the values by  default are set to A=1; B=5; C=1; D=0.5; E=0
    """
    data['GP']=round((A*data['Completeness']
            -B*data['Contamination']
            +C*(data['Contamination']*data['Strain heterogeneity']/100)
            +D*np.log10(data['N50 (scaffolds)'])
            +E*np.log10(data['Genome size (bp)'])), 2)
    
# Global Parameter graph
def GP_graph(data):
    #global_parameter(data)
    
    GP_plot=data[['Bin Id', 'GP']].plot(figsize= (20,25),
        x= 'Bin Id',
        kind = 'barh',
        title = 'Global Parameter',
        mark_right = True)
    for index, value in enumerate(data['GP']):
        GP_plot.text(value +3, index , str(value))
        
    plt.title('Global Parameter', fontsize= 30)
    plt.ylabel('Bin Id', fontsize =20)
    plt.xlabel('Percentage(%)',fontsize =20)
    return GP_plot

#Contamination vs Completeness, GC content, Genome size   
def scatterplotting(data):
    plt.figure(figsize=(20,25))
    scatterplot = sns.scatterplot(x=data['Completeness'],
                y=data['Contamination'],
                size=data['Genome size (bp)'],
                hue=data['GC'],
               sizes=(200,1500),
               palette='Blues')
    title = 'Quality MAGs scatterplot'
    plt.title(title, fontsize=30)
    plt.xlabel('Completeness',fontsize=26)
    plt.ylabel('Contamination',fontsize=26)    
    plt.legend(loc='upper right',fontsize=25)
    return scatterplot

#N50 graph    
def N50_graph(data):
    N50_plot=data[['Bin Id', 'N50 (scaffolds)']].plot(figsize= (20,25),
        x= 'Bin Id',
        kind = 'barh',
        title = 'N50',)
    plt.title('N50 (scaffolds)', fontsize= 30)
    plt.ylabel('Bin Id', fontsize =20)
    plt.xlabel('N50 (bp)',fontsize =20)
    plt.legend(fontsize=25)
    return N50_plot

    
#   
def WS_contamination(data):

    Markers= data[['Bin Id','# markers','0','1','2','3','4','5+','Completeness']]
    Markers['0%']= (Markers['0']/Markers['# markers']) * 100
    Markers['1%']= (Markers['1']/Markers['# markers']) * 100
    Markers['2%']= (Markers['2']/Markers['# markers']) * 100
    Markers['3%']= (Markers['3']/Markers['# markers']) * 100
    Markers['4%']= (Markers['4']/Markers['# markers']) * 100
    Markers['5+%']= (Markers['5+']/Markers['# markers']) * 100

    Markers_p= Markers.loc[:,['Bin Id','1%','2%','3%','4%','5+%','0%']]

    Mcn_means= pd.DataFrame([[Markers_p['1%'].mean(), Markers_p['2%'].mean(),Markers_p['3%'].mean(), Markers_p['4%'].mean(),
            Markers_p['5+%'].mean(), Markers_p['0%'].mean()]], columns= [1,2,3,4,'5+',0])

    Mcn_means_plot= Mcn_means.plot(figsize= (20,2),
        kind = 'barh',
        stacked = True,
        title = 'Whole sample contamination',
        mark_right = True)
    plt.xlabel('Markers copy number(%)',fontsize =20)
    plt.title('Whole sample contamination', fontsize= 30)
    plt.legend(loc='lower left', fontsize=10)
    return Mcn_means_plot

#
def bins_contamination(data):
    
    #data.sort_values(by= ['GP', 'Completeness'], ascending= False, inplace= True)
    Markers= data[['Bin Id','# markers','0','1','2','3','4','5+','Completeness']]
    Markers['0%']= (Markers['0']/Markers['# markers']) * 100
    Markers['1%']= (Markers['1']/Markers['# markers']) * 100
    Markers['2%']= (Markers['2']/Markers['# markers']) * 100
    Markers['3%']= (Markers['3']/Markers['# markers']) * 100
    Markers['4%']= (Markers['4']/Markers['# markers']) * 100
    Markers['5+%']= (Markers['5+']/Markers['# markers']) * 100

    Markers_p= Markers.loc[:,['Bin Id','1%','2%','3%','4%','5+%','0%']]
    Markers_p_plot = Markers_p.plot(figsize= (20,25),
        x = 'Bin Id',
        kind = 'barh',
        stacked = True,
        title = 'Contamination %',
        mark_right = True)

    plt.ylabel('Bin Id', fontsize =20)
    plt.xlabel('Markers copy number(%)',fontsize =20)
    plt.legend(loc='lower left', fontsize=20)
    plt.title('Markers copy numbers', fontsize= 30)
    return Markers_p_plot


#global_parameter(data, A=1, B=5, C=1, D=0.5, E=0) #Calculate global parameter and add a column DataFrame
    
def Graphs(data, txt):
    
    #global_parameter(data, A=1, B=5, C=1, D=0.5, E=0) #Calculate global parameter and add a column DataFrame

    with PdfPages(txt+'.pdf') as pdfP:

        GP_Graph=GP_graph(data)
        fig_GP=GP_Graph.get_figure()
        pdfP.savefig(fig_GP, 
                     bbox_inches ="tight")

        scatterplot_Graph=scatterplotting(data)
        fig_scatterplot=scatterplot_Graph.get_figure()
        pdfP.savefig(fig_scatterplot, 
                    bbox_inches ="tight")

        N50_Graph=N50_graph(data)
        fig_N50= N50_Graph.get_figure()
        pdfP.savefig(fig_N50,
                    bbox_inches ="tight")

        bins_Graph=bins_contamination(data)
        fig_bins=bins_Graph.get_figure()
        pdfP.savefig(fig_bins, 
                     bbox_inches ="tight")

        WS_Graph=WS_contamination(data)
        fig_WS=WS_Graph.get_figure()
        pdfP.savefig(fig_WS,
                    bbox_inches ="tight")
        
        
files = [f for f in listdir('./CheckM_inputs') if isfile(join('./CheckM_inputs', f))]

for txt in files:
    data = pd.read_csv('./CheckM_inputs/'+ txt, sep= '	', skiprows=6, skipfooter=1)
    global_parameter(data, A=args.A, B=args.B, C=args.C, D=args.D, E=args.E)
    data.sort_values(by= ['GP', 'Completeness'], ascending= False, inplace= True)
    Graphs(data, txt)


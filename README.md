# checkM-Graphics
Script for the Microbial Metagenomics laboratory, A.Y. 2021/2022.
***
## Citations
This code was developed as part of a project carried out during the course of Microbial Metagenomics (Molecular Biology master degree) at the University of Padova. The project was supervised by Prof. Stefano Campanaro, Dr. Maria Silvia Morlino, Dr. Edoardo Bizzotto, and Dr. Gabriele Ghiotto.
***
### Overview
CheckM provides a set of tools for assessing the quality of genomes recovered from isolates, single cells, or metagenomes. It provides robust estimates of genome completeness and contamination by using collocated sets of genes that are ubiquitous and single-copy within a phylogenetic lineage. It uses a broader set of marker genes specific to the position of a genome within a reference genome tree and information about the collocation of these genes. CheckM has implemented the previous methods for assessing genome quality that were ad hoc and generally made use of a limited number of marker genes conserved across all bacterial or archeal genomes.
***
The checkM-Graphics software allows the graphical visualization of the previously obtained CheckM outputs. Our program selects the most valuable parameters calculated, such as Completeness, GC content and genome size and combines them together to have a clear understanding of MAGs’ quality. Through scatterplots and barplots the user can easily understand the sample characteristic and detect any correlation between the parameters used. 
An additional parameter is calculated and plotted with respect to the ones of CheckM: the Global Parameter (GP). GP can be used to estimate MAGs quality without having to take into account any other, useful to compare different samples quality. The script autonomously generates one pdf file for each given input, several input can be analysed in a single run.  
***
### Software requirements
Run the script within the Python environment. Required libraries are Numpy, Pandas, Matplotlib.pyplot, Seaborn, Argparse, PyPDF2, matplotlib.backends.backend_pdf, listdir(from os), isfile, join (from os.path). 
***
### Using CheckM-Graphics
Set the environment: create a folder called CheckM_inputs containing the file to analyze (in the form of CheckM outputs) and place it in the same directory of the script. At the end one pdf is generated for each input file.
***
### Basic usage (input and output)
The script takes as input the data derived from CheckM analysis and return as output a pdf with the graphical view of the MAGs quality. In particular, it contains firstly a graph with the values of the Global Parameter for each bin. The GP is a value informative of the MAGs quality. Secondly, it is produced a scatterplot with Completeness vs Contamination, including the info about GC content and genome size as colours and dot sizes. Moreover, it is generated a barplot of the N50 scaffolds values per each bin. The last graph produced is informative about the markers copy numbers, both for each bin and for the global data of the sample.
***
### Optional Parameters
The Global Parameter function uses some constants that are set to a default values. However these constants can be changed by the users to give different weights to the variables (Completeness, Contamination, Strain Heterogeneity, N50) in order to choose which variables influence more the Global Parameter. 
![image](https://user-images.githubusercontent.com/106092160/170744140-871fa686-fcdc-47f6-801a-5361c36dee59.png)

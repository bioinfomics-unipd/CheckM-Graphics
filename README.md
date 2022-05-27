# checkM-Graphics
Script for the Microbial Metagenomics laboratory, A.Y. 2021/2022.
***
## Citations
This code was developed as part of a project carried out during the course of Microbial Metagenomics (Molecular Biology master degree) at the University of Padova. The project was supervised by Prof. Stefano Campanaro, Dr. Maria Silvia Morlino, Dr. Edoardo Bizzotto, and Dr. Gabriele Ghiotto.
***
### Overview
CheckM provides a set of tools for assessing the quality of genomes recovered from isolates, single cells, or metagenomes. It provides robust estimates of genome completeness and contamination by using collocated sets of genes that are ubiquitous and single-copy within a phylogenetic lineage. It uses a broader set of marker genes specific to the position of a genome within a reference genome tree and information about the collocation of these genes. CheckM has implemented the previous methods for assessing genome quality that were ad hoc and generally made use of a limited number of marker genes conserved across all bacterial or archeal genomes.
***
Our Script allows to obtain a graphical visualization of checkM outputs. It is possible to have a clear first impression of your MAGs quality. The script autonomously generates one pdf file for each given input, several input can be analysed in a single run.  
***
### Software requirements
Run the script within the Python environment. Required libraries are Numpy, Pandas, Matplotlib.pyplot, Seaborn, Argparse, matplotlib.backends.backend_pdf, listdir(from os), isfile, join (from os.path)
### Using CheckM-Graphics
Set the environment: create a folder called CheckM_inputs containing the file to analyze (in the form of CheckM outputs) and place it in the same directory of the script. At the end one pdf is generated for each input file.
### Optional Parameters
The Global Parameter function uses some constants that are set to a default values. However these constants can be changed by the users to give different weights to the variables (Completeness, Contamination, Strain Heterogeneity, N50) in order to choose which variables influence more the Global Parameter. 

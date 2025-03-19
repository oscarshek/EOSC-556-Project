# eosc-556-project
## Title: 
AEM survey in Western Australia

## Authors: 
Oscar and Thaysa 

## Description: 
This project aims to identify any seawater intrusion using airborne electromagneitc (AEM) survey in Western Australia region avaliable on https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146345. Methods including forward simulation and inversion on selected stations and flight paths will be explored. Results will then be cmopared with works done by the Contractor (SkyTEM) and the authority (Geoscience Australia). 

## Content (add names and links to the notebooks)
1. Forward simulation
2. Inversion for single station 
3. Inversion for a flight line?

## Installation: 
To be able to run the Jupyter notebooks for the project code, 

a. Install a Python distribution (like Anaconda or miniforge).
b. Create a conda environment with all the Python packages needed (for example, SimPEG).
c. Activate this conda environment and run JupyterLab to start coding.

1. Python 
Install Python from Python distribution like miniforge and Anaconda that allow users to install new Python libraries and also create environments. 

Install miniforge: https://github.com/conda-forge/miniforge#install
Install Anaconda: https://docs.anaconda.com/anaconda/install

2. Create project conda environment
a. Download the environment.yml file from project repository
b. Create the conda environment by running
```
conda env create -f environment.yml
conda activate environment
```
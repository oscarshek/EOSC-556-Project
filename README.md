# eosc-556-project
## Title: 
Airborne Electromagnetic (AEM) survey in Western Australia

## Authors: 
Oscar and Thaysa 

## Description: 
This project aims to identify any seawater intrusion using airborne electromagneitc (AEM) survey in Western Australia region avaliable on https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146345. Methods including forward simulation and inversion on selected stations and flight paths will be explored. Results will then be cmopared with works done by the Contractor (SkyTEM) and the authority (Geoscience Australia). 

## Data 
The data used in this project is uploaded in the "release" of this repository. It contains the processed and normalised data along two flight lines (IDs: 101102 and 101201), and waveform details used during the survey for both low monent and high moment transmitter. 

## Content
1. [forward_simulation.ipynb](/Notebook/forward_simulation.ipynb): runs forward simulation with different physical inputs and waveforms
2. [AusAEM_WA.ipynb](/Notebook/AusAEM_WA.ipynb): runs inversion for single station along the flight line 
3. Inversion for a flight line (working on it)

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

## References 
1. Cockett, R., Kang, S., Heagy, L. J., Pidlisecky, A., & Oldenburg, D. W. (2015). SimPEG: An open source framework for simulation and gradient based parameter estimation in geophysical applications. Computers & Geosciences.

2. Lindsey J. Heagy, Rowan Cockett, Seogi Kang, Gudni K. Rosenkjaer, Douglas W. Oldenburg, A framework for simulation and inversion in electromagnetics, Computers & Geosciences, Volume 107, 2017, Pages 1-19, ISSN 0098-3004, http://dx.doi.org/10.1016/j.cageo.2017.06.018.
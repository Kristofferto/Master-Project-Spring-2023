# Masterproject
Codes for my masters degree in plasma and space physics.

These are the codes used in my master project in Plasma and Space Physics. Here I will provide a brief description of the codes, in the sequence they should be used. 

### SWARM_Data_Retrieval.py ###
Program that reads downloaded CDF files from the IPIR data product available from ESA. The desired parameters are stored locally in arrays. Separated by satellites. 

### MLT_conversion.py ###
program used to generate the magnetic local time (MLT) and magnetic latitude (MLAT) from the locally stored satellite data. 

### PCP_std.py ###
This program locates the polar cap patches (PCPs) and their corresponding trailing and leading edge. A linear regression is then conducted and the standard deviation 
ratios are calculated using the standard deviation of each PCP edge. The ratios are stored locally, along with their indices. 

### PCP_std_plots.py ###
Program used to create the statistical plots. This code is a mess. 

### PCP_climatology.py ###
Program used to conduct the polar cap patch occurrence rate study. It locates the polar cap patches, counts the daily occurrence, and calculates the hours spent in orbit
above polar regions. 

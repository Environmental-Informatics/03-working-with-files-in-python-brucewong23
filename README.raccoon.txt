Processing script: Evaluate_Raccoon_Life.py

This script takes an input file of a simulated raccoon behavior model and store
its information in a dictionary with appropriate pairing of header and values
columns of number are converted to proper type.
These columns' average, sum are calculated, distance traveled was calculated 
with X, Y coordinates and stored back into the same dictionary.
Average energy and loction (average X and Y) with other relevant information
was retrieved and stored in a final output dictionary.
A new report file with a header block of general information and statistics 
including the outcome of the raccoon/simulation was created, additional hourly 
information came after the header block formated into a tab-delimited table.

Input file: 2008Male00006.txt
Output file: Georges_life.txt
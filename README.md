# Monte Carlo Simulations for Risk Assessments
This code has been used in support of my MSc thesis in the Royal Holloway, University of London, Information Security Program.

## How to run
Run you main.py and the script will prompt you to input:
- Number of cycles for the simulation: usually around 10000 is an acceptable number, up to you.
- Minimum Likelihood, Maximum Likelihood, Minimum Impact and Maximum Impact, all of which depend on your use case. If you
a 5x5 risk matrix then the input shall be >=1 and <=5.
- Name of your choice to store the plot in png format. Do not include extension in the name.

## Output
The script is going to output:
1. simulation.log with that will be kept for all simulation you run until deletion
2. .png image with the plotted graph
3. python console will printout some information as well.

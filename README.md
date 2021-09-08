# Metabolic coessentiality analysis and network modeling

Code corresponding to genetic coessentiality analysis in ______. For all issues, please contact finleyl@mskcc.org.

<p float="left">
<img src="https://user-images.githubusercontent.com/89219026/132436412-7377465d-2986-461d-a749-a13691b544a0.png" width="350">.    
<img src=https://user-images.githubusercontent.com/89219026/132436423-dab5f635-aa87-41f0-b9fb-1d17d5eb18f3.png width="500">
</p>

### Data availability
DepMap essentiatility data can be downloaded from https://depmap.org/portal/download/. \
Genes used in our analysis corresponding to gene ontology (GO) terms can be found in **go_metabolism.xlsx** \
Genes corresponding to TCA cycle genes and top TCA co-dependencies can be found in **TCA_codependencies.xlsx** 

### Code for coessentiality analysis and visualization
All code used can be found in **codependency.py**. Three separate functions are provided:
  1) Subsetting DepMap coessentiatilty data and generating correlation matrices
  2) Generating heatmaps from correlation matrices
  3) Generating network diagrams from correlation matrices.

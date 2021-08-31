# Metabolic coessentiality analysis and network modeling

Code corresponding to genetic coessentiality analysis in [INSERT PUB HERE]. For all issues, please contact [insert email here].

[INSERT PRETTY PICTURE OF FINAL FIGURE HERE]


### Data availability
DepMap essentiatility data can be downloaded from https://depmap.org/portal/download/. \
Genes used in our analysis corresponding to gene ontology (GO) terms can be found in **go_metabolism.xlsx** \
Genes corresponding to TCA cycle genes and top TCA co-dependencies can be found in **TCA_codependencies.xlsx** 

### Code for coessentiality analysis and visualization
All code used can be found in **codependency.py**. Three separate functions are provided:
  1) Subsetting DepMap coessentiatilty data and generating correlation matrices
  2) Generating heatmaps from correlation matrices
  3) Generating network diagrams from correlation matrices.

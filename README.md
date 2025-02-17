This repository contains the raw data, scripts, and brief walkthroughs for recreating the figures from the paper skandiver: a divergence-based analysis tool for identifying intercellular mobile genetic elements. 

Prior to running scripts, please ensure skandiver, MobileElementFinder, and geNomad are set up and properly configured in your testing environment. Instructions for installation and setup of each software can be found here: 
* [skandiver](https://github.com/YoukaiFromAccounting/skandiver/tree/main)
* [MobileElementFinder](https://pypi.org/project/MobileElementFinder/)
* [geNomad](https://portal.nersc.gov/genomad/quickstart.html)

## Figure 3
Comparison of mobile element finding profiles of skandiver, MobileElementFinder (MEFinder), and geNomad: the three tools find different sets of putative genetic mobile elements.<br />
[data](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/tree/main/data/fig3)<br />
[script](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/pipeline_for_barcodes.ipynb)
<br />
<br />
<img width="828" alt="Figure3_v4" src="https://github.com/YoukaiFromAccounting/skandiver-paper-figures/assets/14861442/0de8c897-413a-4371-b869-9486e2b292ae">

## Figure 5
Recall of mobile element finding software on known plasmid database.<br />
[data](https://datadryad.org/stash/dataset/doi:10.15146/R33X2J)<br />
[script](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/pipeline_for_frankenplasmid.ipynb)<br />
[script](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/pipeline_for_naked_plasmids.ipynb)
<br />
<br />
<img width="380" alt="Figure5_vnew" src="https://github.com/YoukaiFromAccounting/skandiver-paper-figures/assets/14861442/9791bdfd-8533-4316-aaaa-da99d3016545">

## Table 1
skandiver, MobileElementFinder, and geNomad correctly do not identify known conserved elements as mobile.<br />
[data](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/data/table1/ncbi_accessions_conservedelements.txt)<br />
[script](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/pipeline_for_falsediscovery.ipynb)
<br />
<br />
<img width="800" alt="Table1" src="https://github.com/YoukaiFromAccounting/skandiver-paper-figures/assets/14861442/b46d762b-4e25-4261-8e53-7ee001fd600e">


## Figure 6
skandiver scales well to larger datasets.<br />
[data](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/tree/main/data/fig6a)<br />
[data](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/tree/main/data/fig6b)<br />
[script](https://github.com/YoukaiFromAccounting/skandiver-paper-figures/blob/main/pipeline_for_benchmarking.ipynb)
<br />
<br />
<img width="565" alt="Fig6_v1" src="https://github.com/YoukaiFromAccounting/skandiver-paper-figures/assets/14861442/4ef40dce-38cb-4046-bee9-570b263aa6af">

## Supplemental Figure 1
Overlap of mobile element finding profiles of skandiver, MobileElementFinder (MEFinder), and geNomad: the three tools find different sets of putative genetic elements. 
<br />
<br />
<br />
<img width="500" alt="SuppFig1" src="https://github.com/YoukaiFromAccounting/skandiver-paper-figures/assets/14861442/86611c7a-122f-4d90-8185-5834850caedf">


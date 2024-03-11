# Development of a Hidden Markov Model for Early Pathogen Classifier
## Description: 
The course project developed a method to identify new pathogens by analyzing the di-nucleotide 
composition of genomic sequences. It used two comparative models and a large dataset to compute 
loglikelihood ratios. These ratios help determine the chance of a sequence belonging to a new 
virus. This technique could distinguish new viruses from known ones quickly, which is crucial 
during pandemics like Coronavirus. It can speed up the discovery of pathogens and guide the 
creation of specific treatments and preventive strategies.


## Task breakdown:
1. UPGMA Tree <br>
a. Find the smallest evaluation distance and update the upgrade matrix. <br>
b. Return a correct matrix. <br>
c. Draw the Tree. <br>

2. HMM Model<br>
a. Using the provided data to calculate the log-likelihood of the coding model. <br>
b. Output the classification result on the header of the original sequence. <br>
c. Use the same model mutated pathogen sequence and evaluate the result. <br>


## Result:
In the results, nineteen true coding sequences are misclassified as non-coding. This misclassification is 
attributed to the increased divergence of the pathgon_mut sequences, which reflects a greater evolutionary 
distance. Over time, this divergence may introduce significant genetic variation, where mutations accumulate, 
potentially altering key sequence features, such as codon usage patterns, regulatory elements, or sequence 
motifs, essential for accurate classification. In consequence, those evolutionary changes in sequence make 
the prediction deviate from the original patterns encoded in the data and lead to misclassifications.


## Evaluation:
Using the likelihood ratio (cScore/nScore) in each sequence, we establish a ranking indicating a sequence's 
inclination towards coding or non-coding. This ratio serves as a continuous score upon which we can set various 
thresholds to depict between coding and non-coding predictions. When the likelihood ratio exceeds a given 
threshold, the sequence is predicted as coding; otherwise, it is indicated as non-coding. We can construct 
the ROC curve by iteratively adjusting this threshold and calculating each cutoff's corresponding true and 
false positive rates. In the ROC curve, we can incline sensitivity by picking up a lower threshold that 
classifies more sequences as coding, accepting more false positives for a higher true positive rate closer to 
the ROC curve's top right and, in contrast, for specificity. The chosen cutoff will be on the elbow point in 
the top left of the curve, optimizing the trade-off and maximizing the TPR while minimizing the FPR.


## Summary: 
The course project is centered on functional genomics, employing a hidden Markov model alongside phylogenetic 
analysis to elucidate the evolutionary connections between pathogen sequences. A classifier is constructed to 
detect whether a mutated pathogen belongs to the same lineage, based on the patterns in its dinucleotide 
composition. The model's accuracy is assessed using the ROC curve, revealing that over extended mutation periods, 
the model's reliability dwindles, approaching a random guess threshold. This outcome underlines the importance 
of considering both the timing and lineage of sequence data in pathogen modeling, given the rapid mutation rates.

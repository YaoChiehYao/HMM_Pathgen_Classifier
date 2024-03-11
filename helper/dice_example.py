import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Define the two-state Markov model parameters
transition_matrix = np.array([[0.95, 0.05],
                              [0.05, 0.95]])
states = ["Fair", "Loaded"]
initial_state = [1, 0]  # Start with the Fair die

# Probabilities for a fair and loaded die
fair_probs = np.full((6,), 1/6)
loaded_probs = np.array([1/10, 1/10, 1/10, 1/10, 1/10, 1/2])

# Number of simulations and rolls
num_simulations = 100
num_rolls = 15

# Record the number of sixes in each simulation
sixes_count_fair = []
sixes_count_loaded = []

# Run the simulations
np.random.seed(0)  # For reproducibility
for _ in range(num_simulations):
    # Start with a fair die
    current_state = np.random.choice(states, p=initial_state)
    sixes_fair = 0
    sixes_loaded = 0

    for _ in range(num_rolls):
        if current_state == "Fair":
            roll = np.random.choice([1, 2, 3, 4, 5, 6], p=fair_probs)
            if roll == 6:
                sixes_fair += 1
            current_state = np.random.choice(states, p=transition_matrix[0])
        else:  # Loaded die
            roll = np.random.choice([1, 2, 3, 4, 5, 6], p=loaded_probs)
            if roll == 6:
                sixes_loaded += 1
            current_state = np.random.choice(states, p=transition_matrix[1])

    sixes_count_fair.append(sixes_fair)
    sixes_count_loaded.append(sixes_loaded)

# Calculate the frequencies of sixes for each die
freq_fair = [sixes_count_fair.count(i) for i in range(num_rolls+1)]
freq_loaded = [sixes_count_loaded.count(i) for i in range(num_rolls+1)]

# Plot the distribution of sixes for fair and loaded die
plt.figure(figsize=(14, 7))
plt.bar(range(num_rolls+1), freq_fair, color='orange', alpha=0.7, label='Fair')
plt.bar(range(num_rolls+1), freq_loaded,
        color='grey', alpha=0.7, label='Loaded')
plt.xlabel('Sixes rolled out of 15 rolls')
plt.ylabel('Frequency out of 100 simulations')
plt.legend()
plt.title('Distribution of Sixes for Fair and Loaded Die')
plt.show()

# Now, we'll prepare the data for the ROC curve by calculating TPR and FPR
# For the ROC curve, we'll consider the loaded die predictions

# Thresholds are the number of sixes rolled, so we'll calculate TPR and FPR for each possible value
tprs = []  # True positive rates
fprs = []  # False positive rates

# We will treat the loaded die as the positive class
for threshold in range(num_rolls+1):
    # True positives (TP): loaded die results >= threshold
    tp = sum(count >= threshold for count in sixes_count_loaded)
    # False negatives (FN): loaded die results < threshold
    fn = sum(count < threshold for count in sixes_count_loaded)
    # False positives (FP): fair die results >= threshold
    fp = sum(count >= threshold for count in sixes_count_fair)
    # True negatives (TN): fair die results < threshold
    tn = sum(count < threshold for count in sixes_count_fair)

    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    tprs.append(tpr)
    fprs.append(fpr)

# Plot the ROC curve
plt.figure(figsize=(10, 5))
plt.plot(fprs, tprs, marker='o', linestyle='-', color='blue')
# Diagonal line for reference
plt.plot([0, 1], [0, 1], linestyle='--', color='darkgrey')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

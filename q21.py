# Bayesian Inference Example - numeric version

# Given numbers
P_D = 0.02
P_notD = 0.98
sensitivity = 0.95
specificity = 0.90

# False positive rate
P_pos_given_notD = 1 - specificity

# Posterior probability
P_D_given_pos = (sensitivity * P_D) / (sensitivity*P_D + P_pos_given_notD * P_notD)

print("Posterior probability P(D|Positive) ≈", round(P_D_given_pos, 3))

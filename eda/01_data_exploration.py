import pandas as pd
import matplotlib.pyplot as plt

# Load and explore dataset
df = pd.read_csv('../data/sample.csv')
print(df.describe())
df.hist(figsize=(12, 8))
plt.tight_layout()
plt.savefig('../output/distributions.png')
// Added: new utility function
# Add: input validation
# Updated logic for better readability
// v1.11 - minor update

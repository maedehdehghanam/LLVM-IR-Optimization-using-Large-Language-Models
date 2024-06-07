import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read the CSV file
file_path = './dataset/llvm-ir-loop-optimized-llvm-ir-.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Specify the column name to analyze
column_name = 'llvm-ir'  # Replace with your actual column name

# Step 3: Calculate string lengths
df['length'] = df[column_name].astype(str).apply(len)

# Step 4: Plot the distribution
plt.figure(figsize=(10, 6))
plt.hist(df['length'], bins=range(df['length'].min(), df['length'].max() + 1), edgecolor='black')
plt.title(f'Distribution of String Lengths in Column: {column_name}')
plt.xlabel('Length of Strings')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(df['length'].min(), df['length'].max() + 1))

# Show the plot
plt.show()
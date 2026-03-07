import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_file = snakemake.input[0]

gc_plot = snakemake.output[0]
len_plot = snakemake.output[1]
qual_plot = snakemake.output[2]

df = pd.read_csv(input_file)

print("\nSummary Statistics\n")

print("GC Content")
print(df["gc_content"].describe())

print("\nRead Length")
print(df["read_length"].describe())

print("\nMean Quality")
print(df["mean_quality"].describe())

sns.histplot(df["gc_content"], bins=50)
plt.title("GC Content Distribution")
plt.xlabel("GC Content (%)")
plt.ylabel("Reads")
plt.savefig(gc_plot)
plt.clf()

sns.histplot(df["read_length"], bins=50)
plt.title("Read Length Distribution")
plt.xlabel("Read Length")
plt.ylabel("Reads")
plt.savefig(len_plot)
plt.clf()

sns.histplot(df["mean_quality"], bins=50)
plt.title("Quality Score Distribution")
plt.xlabel("Mean Quality Score")
plt.ylabel("Reads")
plt.savefig(qual_plot)
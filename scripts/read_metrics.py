import gzip
import pandas as pd
from Bio import SeqIO

input_fastq = snakemake.input[0]
output_csv = snakemake.output[0]

records = []

def mean_quality(q):
    return sum(q) / len(q)

with gzip.open(input_fastq, "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        seq = record.seq
        quals = record.letter_annotations["phred_quality"]

        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100
        mean_q = mean_quality(quals)

        records.append([record.id, length, gc, mean_q])

df = pd.DataFrame(
    records,
    columns=[
        "read_id",
        "read_length",
        "gc_content",
        "mean_quality"
    ]
)

print("\nFirst few reads:")
print(df.head())

df.to_csv(output_csv, index=False)
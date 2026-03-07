# Long-Read Sequencing QC Pipeline

## Overview

This project implements a reproducible **bioinformatics pipeline** for performing **quality control (QC) on long-read sequencing data**.

The pipeline processes raw FASTQ files and generates:

* Quality control analysis using **NanoPlot**
* Per-read statistics
* Visualization of key sequencing metrics
* Summary statistics for interpretation

The workflow is implemented using **Snakemake** and runs inside a **Conda environment**, ensuring full reproducibility.

---

## Input

Raw sequencing data in **FASTQ format**.

Example used in this project:

```
barcode77.fastq.gz
```

---

## Pipeline Steps

### 1. Quality Control

The pipeline uses **NanoPlot**, a tool specifically designed for long-read sequencing technologies such as Oxford Nanopore.

NanoPlot generates:

* Read length distributions
* Quality score distributions
* Read length vs quality plots
* Yield statistics

Output:

```
results/nanoplot/NanoPlot-report.html
```

---

### 2. Custom Read Metrics

A Python script calculates the following metrics for **each read**:

* GC Content (%)
* Read Length
* Mean Read Quality Score

Output:

```
results/read_metrics.csv
```

Example:

```
read_id,read_length,gc_content,mean_quality
read_1,206,54.8,20.6
```

---

### 3. Data Visualization

Using the computed metrics, the pipeline generates distribution plots for:

* GC Content
* Read Length
* Mean Read Quality

Output plots:

```
results/gc_distribution.png
! [gc_distribution](results/gc_distribution.png)
results/read_length_distribution.png
! [read_length_distribution](results/read_length_distribution.png)
results/quality_distribution.png
! [quality_distribution](results/quality_distribution.png)
```

---

## Workflow

Pipeline DAG:

![DAG](dag.png)


---

## Summary Statistics (Example Dataset)

| Metric             | Value    |
| ------------------ | -------- |
| Number of Reads    | 81,011   |
| Mean Read Length   | 1,038 bp |
| Median Read Length | 547 bp   |
| N50                | 1,761 bp |
| Mean GC Content    | 53%      |
| Mean Quality Score | 17.9     |

---

## Interpretation

The dataset shows characteristics typical of **Oxford Nanopore long-read sequencing**:

* GC content distribution is approximately normal.
* Read length distribution shows a long tail with very long reads.
* Quality scores are within the expected range for Nanopore sequencing.

No major quality issues were detected.

---

## Recommendation

The sequencing data appears suitable for downstream analysis.

Recommended next step:

```
Genome alignment (e.g., minimap2)
```

Example command:

```
minimap2 -ax map-ont reference.fasta reads.fastq > alignment.sam
```

---

## Installation

Clone the repository:

```
git clone https://github.com/happymealinthebuilding/longread_qc_pipeline.git
cd longread_qc_pipeline
```

Create environment and run pipeline:

```
snakemake --snakefile workflow/Snakefile --use-conda --cores 2
```

---

## Requirements

* Python
* Snakemake
* Conda
* NanoPlot
* pandas
* matplotlib
* seaborn

All dependencies are defined in:

```
envs/qc_env.yml
```

---

## Author

Azra Tuncay

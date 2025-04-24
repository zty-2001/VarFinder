# VarFinder

**VarFinder** is a versatile Perl-based toolkit designed to **identify and annotate causal mutations** from genetic screening experiments. It supports both single-end and paired-end sequencing reads and includes functions to remove background (parental) mutations and annotate variants with genomic features.

---

## 🧰 Features

- Detect mutations in mutant samples with customizable depth and mutation ratio filters
- Remove background (parental) mutations
- Annotate variants using gene models (GFF3) and coding sequences (CDS)
- Identify shared mutations across mutant populations when parental data is unavailable

---

## ⚠️ Requirements

Make sure the following tools are installed and accessible in your `$PATH`:

- [`bcftools`](https://github.com/samtools/bcftools) **v1.17**
- [`samtools`](https://github.com/samtools/samtools) **v1.17**

---

## 🧬 Usage

### Step 1. Identify mutations in mutants

**Single-end reads:**

```bash
perl VarFinder_mutant [Mutant] [Mutant_1.fq] [Genome.fas] [MaxDepth] [MinDepth] [MutationRate(0-100)]

**Paired-end reads:**

```bash
perl VarFinder_mutant [Mutant] [Mutant_1.fq,Mutant_2.fq] [Genome.fas] [MaxDepth] [MinDepth] [MutationRate(0-100)]

### Step 2. Identify mutations in the parental sample

**Single-end reads:**

```bash
perl VarFinder_parent [Parent] [Parent_1.fq] [Genome.fas]

**Paired-end reads:**

```bash
perl VarFinder_parent [Parent] [Parent_1.fq,Parent_2.fq] [Genome.fas]

### Step 3. Remove parental (background) mutations from mutant results

```bash
perl bkRemover.pl [Mutant.vcf] [Parent.vcf] [Cleaned.vcf]

### Step 4. Annotate cleaned variants

```bash
perl VarAnnotate.pl [Cleaned.vcf] [GFF3_file] [CDS.fasta] [Annotate.csv]

### 📁 File Overview

File	Description
VarFinder_mutant	Mutation calling script for mutant samples
VarFinder_parent	Mutation calling script for parental samples
bkRemover.pl	Removes shared mutations between parent and mutant
VarAnnotate.pl	Annotates mutations with genomic features
bkFinder.pl	Finds shared mutations between mutants

###📌 Notes
All inputs should be properly formatted FASTQ and reference FASTA/GFF3/CDS files.

For best results, use high-quality sequence data and verified reference genome annotations.

### 📬 Contact
For questions, bug reports, or feature requests, please open an issue or contact the maintainer at zenglpbio@gmail.com







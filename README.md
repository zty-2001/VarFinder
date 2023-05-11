VarFinder is a versatile toolkit to identify and annotate causal mutations of genetic screens.

Remind: bcftools-1.17 and samtools-1.17 are required to successfully run VarFinder.

1.Identify mutations in the mutant, and exclude noisy mutations with customized mutation ratio, sequence depth:

#Single-end
$perl VarFinder_mutant [Mutant] [Mutant_1.fq] [PATH/Genome.fas] [MaxmumDepth] [MinimumDepth] [cutoffMutationRate(0-100)]

#Paired-end
$perl VarFinder_mutant [Mutant] [Mutant_1.fq, Mutant_2.fq] [Genome.fas] [MaxmumDepth] [MinimumDepth] [cutoffMutationRate(0-100)]

#Identify parental mutations:

#Single-end
$perl VarFinder_parent [Parent] [Parent_1.fq] [Genome.fas]

#Paired-end
$perl VarFinder_parent [Parent] [Parent_1.fq,Parent_2.fq] [Genome.fas]

#Exclude parental mutations from the results of mutants
$perl bkRemover.pl [Mutant.-depth.-MutRatio.vcf] [Parent.vcf] [Cleaned.vcf]

#Annotate mutations:
$perl VarAnnotate.pl [Cleaned.vcf] [PATH/GFF3_file] [PATH/cds.fas] [Annotate.csv]

#In case the parental genome is not available, VarFinder provides an alternative way to identify potential parental mutations by searching for common mutations in mutations of different F2 mutant population:

$bkFinder.pl [Mutant1.vcf] [Mutant2.vcf] Overlap_Mutant1_2.vcf
$bkFinder.pl [Mutant3.vcf] [Mutant2.vcf] Overlap_Mutant2_3.vcf
$bkFinder.pl [Mutant3.vcf] [Mutant1.vcf] Overlap_Mutant1_3.vcf
$bkFinder.pl [Mutant1_2.vcf] [Mutant2_3.vcf] Overlap_Mutant.1.vcf
$bkFinder.pl [Mutant1_3.vcf] [Mutant2_3.vcf] potentail_bk.vcf

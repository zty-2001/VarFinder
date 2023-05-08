#!usr/bin/perl
print "\nWelcome to use this Perl script to remove background variants from your Mutant\n";
#print "\nWritten by Liping Zeng!\nVersion 1.0\tLast update: 02/03/2023\n";
#print "Contact: zenglpbio at gmail.com\n\n\n";

if (@ARGV != 3) {print "Usage: perl .pl Mutant.vcf\tBackground.vcf\toutput\n\n"};

($input1, $input2, $output)=@ARGV;
open FILE1, "$input1"; ##vcf file of mutant
open FILE2, "$input2"; ##vcf file of background mutations
open RESULT, ">>$output"; 

##vcf file of mutant
while(<FILE1>){chomp;
	if($_=~/^#/){next;}else{
	@arr=split /\t/,$_;
	$pos="$arr[0]"."_"."$arr[1]";
	$hash{$pos}=$_;
	}
}close FILE1;

##vcf file of background mutations
while(<FILE2>){chomp;
	if($_=~/^#/){next;}else{
        @arr2=split /\t/,$_;
        $pos2="$arr2[0]"."_"."$arr2[1]";
        $hash2{$pos2}=$_;
	}
}close FILE2;


foreach $key(keys %hash){
	unless(exists $hash2{$key}){
	print RESULT "$hash{$key}\n";}
}close RESULT;

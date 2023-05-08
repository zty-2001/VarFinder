#!usr/bin/perl
##This script is for remove out EMS mutations with mutation rates e.g. <0.8 (80%)
###Author: Liping Zeng
###zenglpbio@gmail.com

($input,$output,$opt1)=@ARGV;
##$opt1 for percent level, e.g. 0.8 (remove out mutations with mutation rates <80%) or 1
if (@ARGV != 2) {print "Usage: perl .pl input\toutput\n"};

open FILE, "$input";
open TEMP, ">>$output";

while(<FILE>){  chomp;
        if($_ =~ /^#/){print TEMP "$_\n";
        }else{ $_=~s/DP4=/ /g;
        @arr=split / /, $_;

        @temp=split /;/,$arr[1];
        @DP4=split /,/,$temp[0];
        $sum = $DP4[0] + $DP4[1] + $DP4[2] + $DP4[3];
        $sum_mutant=$DP4[2] + $DP4[3]; 
        $percent=100 * $sum_mutant / $sum;
        $_ =~ s/ /DP4=/g;
        $hash{$_}=$percent;
        }
}close FILE;

foreach $key(sort{$hash{$b}<=>$hash{$a}}keys%hash){
        if($hash{$key} >= $opt1){print TEMP "$key\t$hash{$key}\n"; }
} 
close TEMP;

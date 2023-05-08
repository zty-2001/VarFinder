#!usr/bin/perl
##This script is for remove out mutations by using sequencing depth (>100 and <10)
###Author: Liping Zeng
###zenglpbio@gmail.com

($input,$output,$opt1,$opt2)=@ARGV;
##$opt1 for the maximum depth of the sequence 
##$opt2 for the mimimum depth of the sequence

if (@ARGV != 4) {print "Usage: perl .pl input\toutput\tMax\tMin\n"};

open FILE, "$input";
open TEMP, ">>$output";

while(<FILE>){  chomp;
        if($_ =~ /^#/){print TEMP "$_\n";
        }else{ $_=~s/DP4=/ /g;
        @arr=split / /, $_;

        @temp=split /;/,$arr[1];
        @DP4=split /,/,$temp[0];
        $sum = $DP4[0] + $DP4[1] + $DP4[2] + $DP4[3]; 
        $_ =~ s/ /DP4=/g;
        $hash{$_}=$sum;
        }
}close FILE;

foreach $key(sort{$hash{$b}<=>$hash{$a}}keys%hash){
        if($hash{$key} < $opt1 && $hash{$key} > $opt2){print TEMP "$key\n"; }
} 
close TEMP;

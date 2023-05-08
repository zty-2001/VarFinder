#!usr/bin/perl
##e.g: 1,2,3 are samples. By comparing 1 and 2, 1 and 3, 2 and 3, the combined repeat are background.
##I need to do the perl 3 times, if I have 3 samples.

($input1, $input2,$output)=@ARGV;
open FILE1, "$input1"; ##AB61
open FILE2, "$input2";

open RESULT, ">>$output";

while(<FILE1>){chomp;
	if($_=~/^#/){next;}else{
	@arr=split /\t/,$_;
	$pos="$arr[0]"."_"."$arr[1]";
	$hash{$pos}=$_;
	}
}close FILE1;

while(<FILE2>){chomp;
	if($_=~/^#/){next;}else{
        @arr2=split /\t/,$_;
        $pos2="$arr2[0]"."_"."$arr2[1]";
        $hash2{$pos2}=$_;
	}
}close FILE2;



foreach $key(keys %hash){
	if(exists $hash2{$key}){
	print RESULT "$hash{$key}\n";}
}close RESULT;

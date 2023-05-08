#!/usr/bin/perl -w
#Download genome from online database

($species_name,$path)=@ARGV;
if($#ARGV==-1){
        print "type \"-h\" for more information\n\n";
        exit;
}

foreach $n((0 .. $#ARGV)){
	if($ARGV[$n] eq "-h" || $ARGV[$n] eq "-help"){
		print "\nNotice: Please find the online path from Ensmbl FTP";
		print "\nUsage:\n\tPerl DownloadGenome.pl species_name EnsemblFTP_path\n";
		exit;
	}
}

if($path !~ /ensemblgenomes/){
	print "\t\nPlease provide the Ensembl FTP address\n";
}

##rsync download genome from Ensembl FTP


if($path !~ /^ftp/){
	print "\nError:\tPlease provide FTP address without the http://\n\n";
	exit;
}else{
	system ("rsync -av rsync://$path ./");	
}
#system ("rsync -av rsync://$path ./");
print "\nProcessing:\tGenome has been downloaded\n";

@file2=split/\//,$path;
system ("mkdir $species_name");
system ("mv $file2[-1] $species_name"); ##genome file

print "\nProcessing:\tUnpress genome file\n\n";

system ("gunzip -c $species_name/$file2[-1] >$species_name/$species_name.fas");
#}elsif($ARGV[$n] eq ""){
#}

print "\nProcessing:\tindex genome\n\n";
system ("bwa index $species_name/$species_name.fas");
system ("samtools faidx $species_name/$species_name.fas");
#system ("mkdir $species_name");
#system ("mv $species_name.* $species_name");
system ("rm $species_name/$file2[-1]");
print "\n\tGenome of $species_name has been downloaded and index files have been built\n\n";

system ("mv $species_name ../Genome"); #Move the new genome file to the existed Genome folder
print "\n\tFinished!\tPlease check you file in the Genome/$species_name folder\n\n";


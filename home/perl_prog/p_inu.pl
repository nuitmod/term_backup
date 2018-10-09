#!/usr/bin/env perl

use strict;

print "input some data\n";
my sub in_func {
  while(my $line=<STDIN>){
    chomp($line);
    last if ($line eq "q");
    print "$line\n";
    print "You input a $line, for exit input q\n";
  }
}

in_func;

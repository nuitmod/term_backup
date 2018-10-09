#!/usr/bin/perl

use strict;

# создаем файловый дескриптор
open FID, "input.txt"
  or die "Failed to open input.txt: $!\n";

my $i = 0;
print "line ".++$i.": $_" while(<FID>);
close FID; # закрываем файловый дескриптор

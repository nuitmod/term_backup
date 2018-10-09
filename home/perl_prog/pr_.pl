#!/usr/bin/env perl

system('pwd');

sub iiww {
  print "a function\n"};

iiww();

sub wh_proc {
  $i=1;
  while($i<=8){
    print "i = $i ";
    system('pwd');
    sleep 1;
    $i+=1;
  }
}

wh_proc();

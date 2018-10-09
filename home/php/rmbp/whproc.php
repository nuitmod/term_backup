#!/usr/bin/env php
<?php

function iproc()
{
  $i=1;
  while($i<=9)
  {
    $dat="i=$i "; // + system('pwd');
    print $dat; system('pwd');
    $i++; system('sleep 0.6');
    //sleep(1);
  }
}

iproc();


?>

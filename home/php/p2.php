<?php

function wh(){
  $i=0;
  while($i<10){
    echo "i : ".$i."\n";
    $i++;
  }
}

function interv($x){
  while (1) {
    system($x);
    system('sleep 1');
  }
}

$y="pwd";

wh();
interv($y);

//wh();

?>

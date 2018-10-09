<?php
//function cmd(){
  unset($argv[0]);

  echo implode(' ', $argv), "\n";

  print_r($argv);
//}
//fopen();
//cmd();

while ($input != "q"){
  echo "Input something: ";
  $input=trim(fgets(STDIN, 1024));
    echo "\n", $input, "\n";
    system('sleep 0.6');
    if($input != "q"){
//      system('sleep 0.5');
      echo "enter q for exit"."\n";
    }
//  system('sleep 0.6'); 
}
?>

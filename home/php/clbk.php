<?php

function ww($data, $callback){
  if($data){
    echo "a callb fun : \n";
    $callback();
  }else{
   echo "unnright!\n";
  }
}

ww(1==1, function(){
  system('pwd');
  }
);

?>

#!/usr/bin/env php
<?php

class ww{

  public function __construct(){
    echo "a construct fun\n";
  }

  public function get_data($dat){
    echo "inner fun\n";
    echo "$dat\n";

  }
}

//ww::get_data();
$w1=new ww();
$w1->get_data('innoir');


?>

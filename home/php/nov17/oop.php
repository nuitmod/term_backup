<?php

class Wmn {
  public $name;
  public $job;

  public function showwm(){
    echo $this->name." is ".$this->job."!\n";
  }
}

$wm1 = new Wmn();
$wm1->name="Ruth";
$wm1->job="programmer";

$wm2 = new Wmn();
$wm2->name="Maud";
$wm2->job="security";

$wm1->showwm();
$wm2->showwm();

?>

<?php

// comp
$array = ["batu" => 0, "kertas" => 1, "gunting" => 2];

$comp = array_rand($array);

// suit

function suit(?string $maunyaapa)
{

    $player = $maunyaapa;
    global $comp;

    if ($player == $comp)
    {
        echo "comp memi1ih $comp sehingga Seri!" . PHP_EOL;
    } elseif ($player == "gunting" and $comp == "kertas")
    {
        echo "comp memilih $comp sehingga kamu menang" . PHP_EOL;
    } elseif ($player == "batu" and $comp == "gunting")
    {
        echo "comp memilih $comp sehingga kamu menang!" . PHP_EOL;
    } elseif ($player == "kertas" and $comp == "batu")
    {
        echo "comp memilih $comp sehingga kamu menang!" . PHP_EOL;
    } elseif ($player = "" or $player != "gunting" or $player != "batu" or $player != "kertas") {
        echo "input invalid!" . PHP_EOL;
    } else
    {
        echo "comp memilih $comp jadi kamu kalah!" . PHP_EOL;
    }
    
}

suit("batu");
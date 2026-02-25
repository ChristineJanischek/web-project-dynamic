<?php

class BmiRechner {
    private $gewicht;
    private $groesse;
    private $bmi;
    private $kategorie;

    public function __construct($gewicht = null, $groesse = null) {
        if ($gewicht !== null && $groesse !== null) {
            $this->setWerte($gewicht, $groesse);
        }
    }

    public function setWerte($gewicht, $groesse) {
        $this->gewicht = (float) $gewicht;
        $this->groesse = (float) $groesse;
        $this->berechne();
    }

    public function getGewicht() {
        return $this->gewicht;
    }

    public function getGroesse() {
        return $this->groesse;
    }

    public function getBmi() {
        return round((float) $this->bmi, 2);
    }

    public function getKategorie() {
        return $this->kategorie;
    }

    private function berechne() {
        $groesseInMetern = $this->groesse / 100;
        $this->bmi = $this->gewicht / pow($groesseInMetern, 2);
        $this->bestimmeKategorie();
    }

    private function bestimmeKategorie() {
        if ($this->bmi < 18.5) {
            $this->kategorie = 'Untergewicht';
        } elseif ($this->bmi < 25) {
            $this->kategorie = 'Normalgewicht';
        } elseif ($this->bmi < 30) {
            $this->kategorie = 'Übergewicht';
        } else {
            $this->kategorie = 'Adipositas';
        }
    }
}

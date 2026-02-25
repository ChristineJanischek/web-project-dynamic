<?php

class NotenRechner {
    private $noten = [];
    private $durchschnitt = 0.0;

    public function __construct($bwl = null, $mathe = null, $deutsch = null, $englisch = null) {
        if ($bwl !== null && $mathe !== null && $deutsch !== null && $englisch !== null) {
            $this->setNoten($bwl, $mathe, $deutsch, $englisch);
        }
    }

    public function setNoten($bwl, $mathe, $deutsch, $englisch) {
        $this->noten = [
            'BWL' => (float) $bwl,
            'Mathe' => (float) $mathe,
            'Deutsch' => (float) $deutsch,
            'Englisch' => (float) $englisch,
        ];
        $this->berechneDurchschnitt();
    }

    public function getNoten() {
        return $this->noten;
    }

    public function getDurchschnitt() {
        return round($this->durchschnitt, 2);
    }

    public function pruefeNachhilfe() {
        $nachhilfeFaecher = [];
        foreach ($this->noten as $fach => $note) {
            if ($note > 4.0) {
                $nachhilfeFaecher[] = $fach;
            }
        }

        return $nachhilfeFaecher;
    }

    private function berechneDurchschnitt() {
        if (count($this->noten) === 0) {
            $this->durchschnitt = 0.0;
            return;
        }

        $this->durchschnitt = array_sum($this->noten) / count($this->noten);
    }
}

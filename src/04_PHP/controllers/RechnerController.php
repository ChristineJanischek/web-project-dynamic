<?php

class NotenRechnerController {
    private $model;
    private $view;

    public function __construct(NotenRechner $model, RechnerView $view) {
        $this->model = $model;
        $this->view = $view;
    }

    public function handleRequest($action = 'index.php') {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $this->verarbeiteNoten($action);
            return;
        }

        $this->view->renderForm($action);
    }

    private function verarbeiteNoten($action) {
        $bwl = $_POST['bwl'] ?? null;
        $mathe = $_POST['mathe'] ?? null;
        $deutsch = $_POST['deutsch'] ?? null;
        $englisch = $_POST['englisch'] ?? null;

        if (!$this->istGueltigeEingabe($bwl, $mathe, $deutsch, $englisch)) {
            $this->view->renderFehler('Bitte geben Sie für alle Fächer eine gültige Note zwischen 1,0 und 6,0 ein.');
            $this->view->renderForm($action, $bwl, $mathe, $deutsch, $englisch);
            return;
        }

        $this->model->setNoten($bwl, $mathe, $deutsch, $englisch);
        $this->view->renderErgebnis(
            $this->model->getNoten(),
            $this->model->getDurchschnitt(),
            $this->model->pruefeNachhilfe()
        );
        $this->view->renderForm($action, $bwl, $mathe, $deutsch, $englisch);
    }

    private function istGueltigeEingabe(...$noten) {
        foreach ($noten as $note) {
            if (!is_numeric($note)) {
                return false;
            }
            $wert = (float) $note;
            if ($wert < 1.0 || $wert > 6.0) {
                return false;
            }
        }

        return true;
    }
}

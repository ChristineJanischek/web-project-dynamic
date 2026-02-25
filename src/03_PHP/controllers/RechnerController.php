<?php

class BmiRechnerController {
    private $model;
    private $view;

    public function __construct(BmiRechner $model, RechnerView $view) {
        $this->model = $model;
        $this->view = $view;
    }

    public function handleRequest($action = 'index.php') {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $this->verarbeiteBmi($action);
            return;
        }

        $this->view->renderForm($action);
    }

    private function verarbeiteBmi($action) {
        $gewicht = $_POST['gewicht'] ?? null;
        $groesse = $_POST['groesse'] ?? null;

        if (!$this->istGueltigeEingabe($gewicht, $groesse)) {
            $this->view->renderFehler('Bitte geben Sie ein Gewicht in kg und eine Größe in cm größer als 0 ein.');
            $this->view->renderForm($action, $gewicht, $groesse);
            return;
        }

        $this->model->setWerte($gewicht, $groesse);
        $this->view->renderErgebnis(
            $this->model->getBmi(),
            $this->model->getKategorie(),
            $this->model->getGewicht(),
            $this->model->getGroesse()
        );
        $this->view->renderForm($action, $gewicht, $groesse);
    }

    private function istGueltigeEingabe($gewicht, $groesse) {
        return is_numeric($gewicht)
            && is_numeric($groesse)
            && (float) $gewicht > 0
            && (float) $groesse > 0;
    }
}

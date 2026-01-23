<?php

class RechnerController {
    private $model;
    private $view;

    public function __construct(RechnerModel $model, RechnerView $view) {
        $this->model = $model;
        $this->view = $view;
    }

    public function handleRequest($action = '') {
        $this->model->setWerte($_POST['werte'] ?? null);
        $message = $this->erzeugeAnleitung();
        $this->view->renderFormMitAnleitung($message, $action);
    }

    public function getAnleitungMessage() {
        return $this->erzeugeAnleitung();
    }

    private function erzeugeAnleitung() {
        return "<ol><h2>Vorgehensweise - Do it!</h2>\n" .
               "<li>Die Formular-Komponenten geh&ouml;ren in die Form-Datei!</li>\n" .
               "<li>Die Bibliothek (lib.php) ist im head des Frameworks inkludiert!</li>\n" .
               "<li>Die Bibliothek (lib.php), das ist die Modell-Datei.</li>\n" .
               "<li>Die Steuerung von Ereignissen (Action) geh&ouml;rt in die Controller-Datei!</li>\n" .
               "</ol><br><br><br>";
    }
}

<?php

class RechnerView {
    public function renderAnleitung($message) {
        echo $message;
    }

    public function renderForm($action = '') {
        echo <<<HTML
<h2>Rechner Formular</h2>
<form method="post" action="{$action}">
    <label for="werte">Wert:</label>
    <input type="text" id="werte" name="werte" required>
    <button type="submit">Senden</button>
</form>
HTML;
    }

    public function renderFormMitAnleitung($message, $action = '') {
        $this->renderAnleitung($message);
        $this->renderForm($action);
    }

    public function renderFormular() {
        echo '<h2>Rechner Formular</h2>';
        echo '<form method="post" action="view_rechnerinput.php">';
        echo '    <label for="werte">Wert:</label>';
        echo '    <input type="text" id="werte" name="werte" required>';
        echo '    <button type="submit">Berechnen</button>';
        echo '</form>';
    }

    public function renderErgebnis($wert) {
        if ($wert !== null && $wert !== '') {
            echo '<div class="ergebnis">';
            echo '    <h3>Ergebnis:</h3>';
            echo '    <p>Eingegebener Wert: ' . htmlspecialchars($wert) . '</p>';
            echo '</div>';
        }
    }
}

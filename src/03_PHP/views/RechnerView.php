<?php

class RechnerView {
    public function renderForm($action = 'index.php', $gewicht = '', $groesse = '') {
        $gewichtWert = htmlspecialchars((string) $gewicht, ENT_QUOTES, 'UTF-8');
        $groesseWert = htmlspecialchars((string) $groesse, ENT_QUOTES, 'UTF-8');

        echo <<<HTML
<section id="content" class="bmi-card">
    <h2>BMI-Rechner (MVC Musterlösung)</h2>
    <p>Geben Sie Gewicht und Größe ein, um Ihren BMI zu berechnen.</p>
    <form method="post" action="{$action}" class="bmi-form">
        <div class="form-group">
            <label for="gewicht">Gewicht (kg)</label>
            <input type="number" id="gewicht" name="gewicht" min="1" step="0.1" value="{$gewichtWert}" required>
        </div>

        <div class="form-group">
            <label for="groesse">Größe (cm)</label>
            <input type="number" id="groesse" name="groesse" min="1" step="0.1" value="{$groesseWert}" required>
        </div>

        <button type="submit">BMI berechnen</button>
    </form>
</section>
HTML;
    }

    public function renderErgebnis($bmi, $kategorie, $gewicht, $groesse) {
        $bmiText = number_format((float) $bmi, 2, ',', '.');
        $gewichtText = number_format((float) $gewicht, 1, ',', '.');
        $groesseText = number_format((float) $groesse, 1, ',', '.');
        $kategorieText = htmlspecialchars($kategorie, ENT_QUOTES, 'UTF-8');

        echo <<<HTML
<section class="bmi-result" aria-live="polite">
    <h3>Ihr Ergebnis</h3>
    <p><strong>Gewicht:</strong> {$gewichtText} kg</p>
    <p><strong>Größe:</strong> {$groesseText} cm</p>
    <p><strong>BMI:</strong> {$bmiText}</p>
    <p><strong>Kategorie:</strong> {$kategorieText}</p>
</section>
HTML;
    }

    public function renderFehler($message) {
        $fehler = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');
        echo "<section class=\"bmi-error\"><p>{$fehler}</p></section>";
    }
}

<?php

class RechnerView {
    public function renderForm($action = 'index.php', $bwl = '', $mathe = '', $deutsch = '', $englisch = '') {
        $bwlWert = htmlspecialchars((string) $bwl, ENT_QUOTES, 'UTF-8');
        $matheWert = htmlspecialchars((string) $mathe, ENT_QUOTES, 'UTF-8');
        $deutschWert = htmlspecialchars((string) $deutsch, ENT_QUOTES, 'UTF-8');
        $englischWert = htmlspecialchars((string) $englisch, ENT_QUOTES, 'UTF-8');

        echo <<<HTML
<section id="content" class="noten-card">
    <h2>Notenrechner (MVC Musterlösung)</h2>
    <p>Geben Sie die Noten für BWL, Mathe, Deutsch und Englisch ein.</p>
    <form method="post" action="{$action}" class="noten-form">
        <div class="form-group">
            <label for="bwl">BWL</label>
            <input type="number" id="bwl" name="bwl" min="1" max="6" step="0.1" value="{$bwlWert}" required>
        </div>

        <div class="form-group">
            <label for="mathe">Mathe</label>
            <input type="number" id="mathe" name="mathe" min="1" max="6" step="0.1" value="{$matheWert}" required>
        </div>

        <div class="form-group">
            <label for="deutsch">Deutsch</label>
            <input type="number" id="deutsch" name="deutsch" min="1" max="6" step="0.1" value="{$deutschWert}" required>
        </div>

        <div class="form-group">
            <label for="englisch">Englisch</label>
            <input type="number" id="englisch" name="englisch" min="1" max="6" step="0.1" value="{$englischWert}" required>
        </div>

        <button type="submit">Notendurchschnitt berechnen</button>
    </form>
</section>
HTML;
    }

    public function renderErgebnis($noten, $durchschnitt, $nachhilfeFaecher) {
        $durchschnittText = number_format((float) $durchschnitt, 2, ',', '.');

        $notenZeilen = '';
        foreach ($noten as $fach => $note) {
            $notenZeilen .= '<li><strong>' . htmlspecialchars($fach, ENT_QUOTES, 'UTF-8') . ':</strong> '
                . number_format((float) $note, 1, ',', '.') . '</li>';
        }

        if (count($nachhilfeFaecher) > 0) {
            $faecher = implode(', ', array_map(function ($fach) {
                return htmlspecialchars($fach, ENT_QUOTES, 'UTF-8');
            }, $nachhilfeFaecher));
            $hinweis = '<p class="nachhilfe-ja"><strong>Nachhilfe erforderlich:</strong> ' . $faecher . '</p>';
        } else {
            $hinweis = '<p class="nachhilfe-nein"><strong>Nachhilfe erforderlich:</strong> nein</p>';
        }

        echo <<<HTML
<section class="noten-result" aria-live="polite">
    <h3>Ihr Ergebnis</h3>
    <ul class="noten-liste">{$notenZeilen}</ul>
    <p><strong>Notendurchschnitt:</strong> {$durchschnittText}</p>
    {$hinweis}
</section>
HTML;
    }

    public function renderFehler($message) {
        $fehler = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');
        echo "<section class=\"bmi-error\"><p>{$fehler}</p></section>";
    }
}

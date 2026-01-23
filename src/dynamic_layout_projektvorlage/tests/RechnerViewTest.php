<?php

use PHPUnit\Framework\TestCase;

class RechnerViewTest extends TestCase {
    public function testRenderAnleitung() {
        $view = new RechnerView();
        ob_start(); // Output buffering
        $view->renderAnleitung("Test Message");
        $output = ob_get_clean();
        $this->assertStringContainsString("Test Message", $output);
    }
}

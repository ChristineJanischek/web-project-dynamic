<?php

use PHPUnit\Framework\TestCase;

class RechnerModelTest extends TestCase {
    public function testSetAndGetWerte() {
        $model = new RechnerModel();
        $model->setWerte(100);
        $this->assertEquals(100, $model->getWerte());
    }
}

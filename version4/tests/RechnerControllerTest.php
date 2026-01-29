<?php

use PHPUnit\Framework\TestCase;

class RechnerControllerTest extends TestCase {
    public function testHandleRequest() {
        $model = $this->createMock(RechnerModel::class);
        $view = $this->createMock(RechnerView::class);
        $controller = new RechnerController($model, $view);

        $model->expects($this->once())
              ->method('setWerte')
              ->with($this->anything());

        $view->expects($this->once())
             ->method('renderAnleitung');

        $_POST['werte'] = 100;
        $controller->handleRequest();
    }
}


<?php
require_once __DIR__ . '/../models/RechnerModel.php';
require_once __DIR__ . '/../views/RechnerView.php';
require_once __DIR__ . '/../controllers/RechnerController.php';

$model = new NotenRechner();
$view = new RechnerView();
$controller = new NotenRechnerController($model, $view);
$controller->handleRequest('index.php');
?>







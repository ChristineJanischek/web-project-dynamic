
<?php
require_once __DIR__ . '/../models/RechnerModel.php';
require_once __DIR__ . '/../views/RechnerView.php';
require_once __DIR__ . '/../controllers/RechnerController.php';

$model = new BmiRechner();
$view = new RechnerView();
$controller = new BmiRechnerController($model, $view);
$controller->handleRequest('index.php');
?>
 </section>




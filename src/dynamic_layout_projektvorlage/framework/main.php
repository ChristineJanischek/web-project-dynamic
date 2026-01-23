
<?php
require_once __DIR__ . '/../models/RechnerModel.php';
require_once __DIR__ . '/../views/RechnerView.php';
require_once __DIR__ . '/../controllers/RechnerController.php';

$model = new RechnerModel();
$view = new RechnerView();
$controller = new RechnerController($model, $view);
?>

<section id="anleitung">
	<h2>Anleitung</h2>
	<p><?php $view->renderAnleitung($controller->getAnleitungMessage()); ?></p>
</section>


 
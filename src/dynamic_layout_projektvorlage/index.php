<!DOCTYPE html>
<html lang="de">
  <head>
	<!-- Hier soll die Head (head.php) mit dem include-Befehl eingebettet werden -->
	<?php include 'layouts/head.php';?>	
    
  </head>
    <body>
    	<div class="container">
		    <header>
		      <!-- Die Inhalt (header.php) ist mit dem include-Befehl eingebettet-->
				<?php include 'layouts/header.php';?>
			</header>
		    <nav>
		      <!-- Die Inhalt (nav.php) ist mit dem include-Befehl eingebettet-->
				<?php include 'layouts/nav.php';?>
			</nav> 

			<aside>
        		Screenshot
			</aside>			
		  	<main>
        		<!-- Die Inhalt (main.php) ist mit dem include-Befehl eingebettet-->
        		<?php include 'layouts/main.php';?>
		    </main>	
		    <footer>
		        <!-- Die Inhalt (footer.php) ist mit dem include-Befehl eingebettet-->
        		<?php include 'layouts/footer.php';?>	
		    </footer>	    
	    </div>   
    </body>
</html>
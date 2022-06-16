<html>
<body>
<?php 
	$datei = fopen("Code.txt","w");
	fwrite($datei, $_GET["Code"]);
	fclose($datei);
	echo "Ihr Code wurde uebermittelt";
?>
</body>
</html>

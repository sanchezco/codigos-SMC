  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <div id="chart_div"></div>
  <div id="chart_div2"></div>
  <div id="chart_div3"></div>
  
  <?php 
	include ('connectBD.php');
	include ('funciones.php');
    // Conexion con la base de datos
    $conexion = conectarBD();
    
    $valor_temp1 = obtener_valores(1, $conexion);
    //var_dump ($valor_temp1);die();
    $valor_temp2 = obtener_alarma(1, $conexion);//alarma 
	
    $valor_temp3 = obtener_valores(2, $conexion); 
    
	desconectarBD($conexion);
    
    header("Refresh: 20; URL='googlechart.php'");

  ?>

<script>
    google.charts.load('current', {packages: ['corechart', 'line']});
		google.charts.setOnLoadCallback(drawBasic1);
    google.charts.load('current', {packages: ['corechart', 'line']});
        google.charts.setOnLoadCallback(drawBasic2);
    google.charts.load('current', {packages: ['corechart', 'line']});
        google.charts.setOnLoadCallback(drawBasic3);

function drawBasic1() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'datetime');
      data.addColumn('number', 'cm');

	  data.addRows(<?php echo $valor_temp1;?>);

     var options = {
        title: 'SCM: Sensor de distancia',
        curveType: 'function',
        legend: { position: 'bottom' }, 

        vAxis: {
          title: 'Distancia',
          viewWindow: {
              max:300,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);         
    }
	
function drawBasic2() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Alarma');

	  data.addRows(<?php echo $valor_temp2;?>);

     var options = {
        title: 'SCM: Alarma distancia',
        curveType: 'function',
        legend: { position: 'bottom' }, 
        
        vAxis: {
          title: 'Alarma',

        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));
      chart.draw(data, options);      
    } 
	
function drawBasic3() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Celsius');

	  data.addRows(<?php echo $valor_temp3;?>);

     var options = {
        title: 'SCM: Sensor de temperatura',
        curveType: 'function',
        legend: { position: 'bottom' }, 
        
        vAxis: {
          title: 'Temperatura',

        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div3'));
      chart.draw(data, options);      
    }  

 </script>

    
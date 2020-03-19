// codigo completo con las graficas de temperatura, distancia y las alarmas

  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <div id="chart_div"></div>
  <div id="chart_div2"></div>
  <div id="chart_div3"></div>
  <div id="chart_div4"></div>
  <div id="chart_div5"></div>
  <div id="chart_div6"></div>

  <?php
	//incluimos los archivos necesarios
	include ('connectBD.php');
	include ('funciones.php');
    // Conexion con la base de datos
    $conexion = conectarBD();

    $valor_distancia = obtener_valores(1, $conexion);        // distancia
	$valor_alarmadist = obtener_alarma(1, $conexion);        // alarma distancia
	$valor_alarma_distancia = obtener_doble(1, $conexion);   // alarma y distancia

	$valor_distancia = obtener_valores(2, $conexion);        // temperatura
	$valor_alarmatemp = obtener_alarma(2, $conexion);        // alarma temperatura
	$valor_alarma_temperatura = obtener_doble(2, $conexion);   // alarma y distancia

	desconectarBD($conexion);

    header("Refresh: 20; URL='a.php'"); // Actualizamos la pagina cada 20seg

  ?>

<script>
    google.charts.load('current', {packages: ['corechart', 'line']});
	google.charts.setOnLoadCallback(drawBasic1);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic2);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic3);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic4);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic5);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic6);

function drawBasic1() { // represento la distancia

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'datetime');
      data.addColumn('number', 'cm');

	  data.addRows(<?php echo $valor_distancia;?>);

     var options = {
        title: 'SMC: Sensor de distancia',
        curveType: 'function',
        legend: { position: 'bottom' },

		//hAxis: {title: 'Tiempo',

        vAxis: {
          title: 'Distancia (cm)',
          viewWindow: {
              max:300,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }

function drawBasic2() { // represento la alarma de distancia

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Alarma');

	  data.addRows(<?php echo $valor_alarmadist;?>);

     var options = {
        title: 'SMC: Alarma distancia',
        curveType: 'function',
        legend: { position: 'bottom' },

        vAxis: {
          title: 'Alarma',
			minValue: 0,
			viewWindow: {
              max:1,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));
      chart.draw(data, options);
    }

function drawBasic3() { // represento la alarma y la distancia juntas

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'cm');
	  data.addColumn('number', 'Alarma');
	  data.addRows(<?php echo $valor_alarma_distancia;?>);

    var options = {
          title: 'SMC: Alarma & Distancia',
          hAxis: {title: 'Tiempo',

		  titleTextStyle: {color: '#333'}},
          vAxis: {
			minValue: 0,
			viewWindow: {
              max:300,
              min:0
            }
			}
        };
	  var chart = new google.visualization.AreaChart(document.getElementById('chart_div3'));
      chart.draw(data, options);
    }

function drawBasic4() { // represento la temperatura

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'datetime');
      data.addColumn('number', 'Celsius');

	  data.addRows(<?php echo $valor_distancia;?>);

     var options = {
        title: 'SMC: Sensor de temperatura',
        curveType: 'function',
        legend: { position: 'bottom' },

        vAxis: {
          title: 'Temperatura (ºC)',
          viewWindow: {
              max:100,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div4'));
      chart.draw(data, options);
    }

function drawBasic5() { // represento la alarma de temperatura

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Alarma');

	  data.addRows(<?php echo $valor_alarmatemp;?>);

     var options = {
        title: 'SMC: Alarma temperatura',
        curveType: 'function',
        legend: { position: 'bottom' },
        vAxis: {
          title: 'Alarma',
			minValue: 0,
			viewWindow: {
              max:1,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div5'));
      chart.draw(data, options);
    }

function drawBasic6() { // represento la alarma y la temperatura juntas

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Celsius');
	  data.addColumn('number', 'Alarma');
	  data.addRows(<?php echo $valor_alarma_temperatura;?>);

    var options = {
          title: 'SMC: Alarma & Temperatura',
          hAxis: {title: 'Tiempo',

		  titleTextStyle: {color: '#000'}},
          vAxis: {
			minValue: 0,
			viewWindow: {
              max:100,
              min:0
            }
			}
        };
	  var chart = new google.visualization.AreaChart(document.getElementById('chart_div6'));
      chart.draw(data, options);
    }
 </script>

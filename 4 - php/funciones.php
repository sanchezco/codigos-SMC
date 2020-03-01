<?php
//Devuelve un array multidimensional con el resultado de la consulta
    function getArraySQL($conexion, $sql){
        //generamos la consulta
        if(!$result = mysqli_query($conexion, $sql)) die();
        $rawdata = array();
        //guardamos en un array multidimensional todos los datos de la consulta
        $i=0;
        while($row = mysqli_fetch_array($result))
        {   
            // guardamos en rawdata todos los vectores/filas que nos devuelve la consulta
            // $rawdata[$i] = $row;
			
			array_push($rawdata, $row);
            $i++;
        }
        //devolvemos rawdata
        return $rawdata;
    }

    function obtener_valores($id_sensor, $conexion){ 
	// función que con el sensorid, y la conexion (archivo connectBD), obtengo el dato del sensor
        $arrayDatos = array(); //inicializa un array
        $sql = "SELECT time, data FROM data Where idsensor = ". $id_sensor; 
		$data = getArraySQL($conexion, $sql); 
		
	    foreach($data as $row){
		// varibale x= tiempo e y= data
            $dAux = array($row['time'], intval($row['data']));
            array_push($arrayDatos, $dAux);
        }
        return json_encode($arrayDatos);
		//return $arrayDatos;
    }
	
    function obtener_alarma($id_sensor, $conexion){ 
    //funcion para obtener las alarmas en función del sensorid
        $arrayDatos = array();
        $sql = "SELECT time, alarma FROM data Where idsensor = ". $id_sensor;
		$data = getArraySQL($conexion, $sql); 

	    foreach($data as $row){
			// varibale x= tiempo e y= alarma
            $dAux = array($row['time'], intval($row['alarma']));
            array_push($arrayDatos, $dAux);
        }
        return json_encode($arrayDatos);
        //return $arrayDatos;
    }
	
	 function obtener_doble($id_sensor, $conexion){ 
	// Representamos en la misma función la alarma junto con los datos del sensor id
        $arrayDatos = array();
        $sql = "SELECT time, data,alarma FROM data Where idsensor = ". $id_sensor;
		$data = getArraySQL($conexion, $sql); 

	    foreach($data as $row){
			// variable x= tiempo, y1= data e y2= alarma
            $dAux = array($row['time'], intval($row['data']), intval($row['alarma'])*100);
            array_push($arrayDatos, $dAux);

        }

        return json_encode($arrayDatos);
        //return $arrayDatos;
       
    }
	?>
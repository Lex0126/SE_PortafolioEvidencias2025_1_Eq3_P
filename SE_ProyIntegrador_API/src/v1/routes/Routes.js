const express = require('express');
const controller = require('../../controllers/sensorController');

const router = express.Router();

// GET - Obtener todos los registros del sensor
// http://localhost:3000/api/v1/sensores1
router.get('/sensores1', controller.getAll_records);
// http://localhost:3000/api/v1/devices
router.get('/devices',controller.getAllDevices);
// http://localhost:3000/api/v1/devices-records
router.get("/devices-records", controller.getDevicesAndRecords);

////////////////////////////////////////////////////////////post

// http://localhost:3000/api/v1/insert-device
router.post('/insert-device',controller.insertDevice);   /*
  "id_type": 1,
  "id_signal_type": 1,
  "name": "Dispositivo Ejemplo"
}
  */ 

// http://localhost:3000/api/v1/sensores
router.post('/sensores', controller.insertRecord);
 /*{
  "id_device": 1,
  "current_value": 25.5
}
  */

// http://localhost:3000/api/v1/device-with-record
router.post('/device-with-record', controller.insertDeviceAndRecord);

/* {
  "id_type": 2,
  "id_signal_type": 1,
  "name": "Dispositivo Nuevo",
  "current_value": 18.7
}
  */



/////put

// http://localhost:3000/api/v1/update-device
router.put('/update-device', controller.updateDevice);
/* */


module.exports = router;

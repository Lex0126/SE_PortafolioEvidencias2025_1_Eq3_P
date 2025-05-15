
const services = require('../services/sensorService')

const getAll_records = async function(req,res){

    const resultado = await services.getAll_records()    
        res.status(201).send(resultado)
}

const getAllDevices = async (req, res) => {
    try {
        const devices = await services.getAll_devices();
        res.json(devices);
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener dispositivos', detalle: error.message });
    }
};


const insertDevice = async (req, res) => {
    try {
        const { id_type, id_signal_type, name } = req.body;
        const result = await services.insertDevice(id_type, id_signal_type, name);
        res.status(201).json({ message: "Dispositivo insertado correctamente", data: result });
    } catch (error) {
        res.status(500).json({ error: "Error al insertar el dispositivo", detalle: error.message });
    }
};


const insertRecord = async (req, res) => {
   const result = await services.insertRecord(req, res);
};


const insertDeviceAndRecord = async (req, res) => {
  try {
    const { id_type, id_signal_type, name, current_value } = req.body;
    const response = await services.insertDeviceAndRecord(id_type, id_signal_type, name, current_value);
    res.status(201).json({ message: 'Inserción correcta', data: response });
  } catch (error) {
    res.status(500).json({ error: 'Error al insertar dispositivo y registro', detalle: error.message });
  }
}
const getDevicesAndRecords = async (req, res) => {
  try {
    const data = await services.getDevicesAndRecords();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: "Error al obtener dispositivos y registros", detalle: error.message });
  }
};

const updateDevice = async (req, res) => {
  try {
    const { id_device, id_type, id_signal_type, name } = req.body;
    const result = await services.updateDevice(id_device, id_type, id_signal_type, name);
    res.json(result);
  } catch (error) {
    res.status(500).json({
      error: 'Error al actualizar el dispositivo',
      detalle: error.message
    });
  }
};


module.exports = {
    getAll_records,
    getAllDevices,
    getDevicesAndRecords,

    insertRecord,
    insertDevice,
    insertDeviceAndRecord,

    updateDevice,
}


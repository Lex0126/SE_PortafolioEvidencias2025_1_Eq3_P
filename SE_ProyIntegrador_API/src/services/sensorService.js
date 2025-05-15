const bd = require("../models/SensorSP")

const getAll_records = async function(){    
    const resp = await bd.Sp_SelectALL_records()
    return resp
}
const getAll_devices = async function(){    
  
    const resp = await bd.Sp_GetAllDevices()
    return resp
}
const insertDevice = async (id_type, id_signal_type, name) => {
    const resp = await bd.Sp_Insert_Device(id_type, id_signal_type, name);
    return resp;
}
const insertDeviceAndRecord = async (id_type, id_signal_type, name, current_value) => {
  return await bd.Sp_InsertDeviceAndRecord(id_type, id_signal_type, name, current_value);
}
const getDevicesAndRecords = async () => {
  return await bd.Sp_GetDevicesAndRecords();
};
//SELECT * FROM .. WHERE ... ID
const updateDevice = async (id_device, id_type, id_signal_type, name) => {
    const resp = await bd.Sp_Update_Device(id_device, id_type, id_signal_type, name);
    return resp;
};

//INSERT
const insertRecord = async (req, res) => {
   try {
       const { id_device, current_value } = req.body;
       const response = await bd.Sp_Insert_SensorRecords(id_device, current_value); 
       res.status(201).json({ message: 'Registro insertado correctamente', data: response });
   } catch (error) {
       res.status(500).json({ error: 'Error al insertar registro', detalle: error.message });
   }
}

//INSERT


module.exports = {
    getAll_records,
    getAll_devices,
    getDevicesAndRecords,

    insertRecord,
    insertDevice,
    insertDeviceAndRecord,

    updateDevice,
    
}


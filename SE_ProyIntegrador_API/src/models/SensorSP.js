const { getConnection } = require('./conexion');

const Sp_SelectALL_records = async function () {
  const conn = await getConnection();
  const [rows] = await conn.query('CALL Sp_SelectALL_records()');
  return rows[0]; 
};
const Sp_GetAllDevices = async () => {
    const conn = await getConnection();
    const [rows] = await conn.query('CALL SP_SelectAll_Devices()');
    return rows[0];
};

const Sp_Insert_Device = async (id_type, id_signal_type, name) => {
    const conn = await getConnection();
    await conn.query('CALL SP_Insert_Device(?, ?, ?)',  [id_type, id_signal_type, name]);
    return { Resultado: "Insercion Correcta" };
   
};
const Sp_InsertDeviceAndRecord = async (id_type, id_signal_type, name, current_value) => {
  const conn = await getConnection();
  await conn.query('CALL SP_InsertDeviceAndRecord(?, ?, ?, ?)', [id_type, id_signal_type, name, current_value]);
  return { Resultado: "Insercion correcta" };
};

const Sp_GetDevicesAndRecords = async () => {
  const conn = await getConnection();
  const [rows] = await conn.query('CALL SP_GetDevicesAndRecords()');
  return rows[0];  
};


const Sp_Insert_SensorRecords = async function (id_device, current_value) {
    const conn = await getConnection();
    await conn.query('CALL SP_Insert_Device_Record(?, ?)', [id_device, current_value]);
    return { Resultado: "Insercion Correcta" };
};
const Sp_Update_Device = async (p_id_device, p_id_type, p_id_signal_type, p_name) => {
  const conn = await getConnection();
  await conn.query('CALL SP_Update_Device(?, ?, ?, ?)', [
    p_id_device,
    p_id_type,
    p_id_signal_type,
    p_name
  ]);
  return { message: 'Dispositivo actualizado correctamente' };
};



module.exports = {
  Sp_SelectALL_records,
  Sp_GetAllDevices,
  Sp_GetDevicesAndRecords,



  Sp_Insert_SensorRecords,
  Sp_Insert_Device,
  Sp_InsertDeviceAndRecord,

  Sp_Update_Device,
};

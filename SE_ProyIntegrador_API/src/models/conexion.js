const mysql = require('mysql2/promise'); // <-- Esto es CLAVE

async function getConnection() {
  try {
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root', // ← Reemplaza esto
      password: 'lexiss0126', // ← Y esto
      database: 'DB_PROYECTO_SE_UNIDAD_4' // ← Y esto
    });

    console.log("Conectado a la base de datos MySQL.");
    return connection;
  } catch (error) {
    console.error("Error de conexion:", error.message);
    return null;
  }
}

module.exports = { getConnection };

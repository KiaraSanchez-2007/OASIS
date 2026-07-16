import os
import sqlite3
from datetime import datetime


class BaseDatos:

    def __init__(self):

        # Carpeta raíz del proyecto OASIS
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        # Crear carpeta DATABASE si no existe
        ruta_database = os.path.join(base_dir, "DATABASE")

        os.makedirs(ruta_database, exist_ok=True)

        # Ruta completa del archivo SQLite
        ruta_db = os.path.join(
            ruta_database,
            "oasis.db"
        )

        # Conexión
        self.conexion = sqlite3.connect(
            ruta_db,
            check_same_thread=False
        )

        self.cursor = self.conexion.cursor()

        self.crear_tablas()

    def crear_tablas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS conversaciones(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT,

            usuario TEXT,

            mensaje TEXT

        )

        """)

        self.conexion.commit()

    def guardar_mensaje(self, usuario, mensaje):

        self.cursor.execute("""

        INSERT INTO conversaciones(
            fecha,
            usuario,
            mensaje
        )

        VALUES(?,?,?)

        """, (

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            usuario,

            mensaje

        ))

        self.conexion.commit()

    def total_conversaciones(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM conversaciones"
        )

        return self.cursor.fetchone()[0]
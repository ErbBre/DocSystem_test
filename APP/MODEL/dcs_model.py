"""
=====================================================
  Módulo: dcs_model.py (Model)
  Descripción:
      Este módulo maneja la lógica de datos del sistema.
      Se encarga de la conexión con la base de datos y la gestión
      de la información, incluyendo consultas, inserciones y actualizaciones.

  Funcionalidades principales:
      - Definir estructuras de datos y clases representativas.
      - Gestionar la conexión con la base de datos.
      - Implementar CRUD (Create, Read, Update, Delete).

  Uso:
      from APP.MODEL.dcs_model import ModeloDB
      self.db.verificar_usuario(usuario, contrasena)
  
  Requisitos:
      - Base de datos compatible:
        * Supabase: pip install supabase
        * SQLite
      - Librerías necesarias: Supabase, sqlite3.

  Autor(es): 
    - Breyner Morales
  Versión: 1.0.0
  Última actualización: [17/03/2025]
=====================================================
"""
class ModeloDB:
    def __init__(self):
        """Conexion con supabase"""
        pass

    def set_alta_user(self,data_user):
        """Metodo para dar de alta a un usuario"""
        print(data_user)
    def set_baja_user(self,data_user):
        """Metodo para dar de baja a un usuario"""
        print(data_user)
        
    def get_user_verify(self, usuario, contrasena):
        """Verifica si el usuario existe en la base de datos(Supabase)."""
        print(usuario,contrasena)
        
        return False
    

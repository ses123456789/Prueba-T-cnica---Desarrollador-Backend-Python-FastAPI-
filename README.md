# Prueba-T-cnica---Desarrollador-Backend-Python-FastAPI-
# Instrucciones de ejecución  
1. Clonar el repositorio.
2. Crear y activar entorno virtual.  
   Desde el bash dentro de la carpeta del proyecto usar el siguiente comando el cual crea el entrono virtual con python 3.11: python -m venv venv  
   Seguidamente se debe activar el entrono virtual con el siguiente comando:  
     windows: venv\Scripts\activate  
     Linux/ MacOS: source venv/bin/activate  
  Si se activo correctamente el entrono la consola debera verse así:  
  <img width="741" height="24" alt="image" src="https://github.com/user-attachments/assets/ce30f455-f0f6-4c79-aa48-dca4fe8e8da4" />

3. Instalar dependencias.  
   Con el siguiente comando se instalaran todas las dependencias usadas en el proyecto: pip install -r requirements.txt
   
4. Ejecutar Docker Compose.  
   El siguiente comando levanta un contenedor con PostgreSQL listo para usar y un segundo contenedor fastappi_app el cual ejecutar tu aplicación FastAPI dentro de Docker, permitiendo una comunicación estable con la DB de PostgreSQL.
<img width="580" height="274" alt="image" src="https://github.com/user-attachments/assets/ae193b4a-c76b-4991-9e87-da62897c1c3a" />

5. Ejecutar migraciones.
   
   Para ejecutar las migraciones se hace uso del siguiente comando: alembic upgrade head
   Las migraciones tienen la función de crear las tablas necesarias (users, tasks) y despues de su ejecución crean un usuario inicial.
   <img width="1351" height="258" alt="image" src="https://github.com/user-attachments/assets/3cb98f7b-4cce-4177-803d-add7c71be108" />

   Esta es la información del usuario:
   
   username: admin  
   password: admin123
   <img width="1343" height="423" alt="image" src="https://github.com/user-attachments/assets/e50c9785-09f9-4598-8394-90421c039367" />

6. Ejecutar la aplicación.
   Finalmente para ejecutar la aplicación se utiliza el comando: uvicorn app.main:app --reload
<img width="1284" height="131" alt="image" src="https://github.com/user-attachments/assets/7193325a-44a5-4d05-bec3-44dd8dd9bbbe" />

La aplicación se encuentra en: http://127.0.0.1:8000/docs  
Toda la API fue probada en Swagger.  



   




# 🐍 Proyecto CRUD en Django con MySQL  

📌 **Descripción**  
Este es un proyecto del **SENA** que implementa un **CRUD de usuarios** en **Django** con conexión a **MySQL**.  
Utiliza **Django Rest Framework (DRF)** para crear una API REST y permite **crear, leer, actualizar y eliminar usuarios** con contraseñas cifradas.  

---

## 📂 **Instalación y Configuración**  

### ✅ 1. Clonar el repositorio  
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
### ✅ 2. Crear y activar el entorno virtual
```bash
python -m venv mi_entorno
source mi_entorno/bin/activate  # Linux/macOS
mi_entorno\Scripts\activate      # Windows
```
### ✅ 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### ✅ 4. Configurar la base de datos en settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_base_de_datos',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### ✅ 5. Ejecutar migraciones
```bash
python manage.py makemigrations usuarios
python manage.py migrate
```
### ✅ 6. Iniciar el servidor
```bash
python manage.py runserver
Accede en el navegador: http://127.0.0.1:8000/
```
### 🚀 **Endpoints de la API**
📌 Listar Usuarios
GET /api/usuarios/

📌 Crear Usuario
POST /api/usuarios/
```bash
{
    "nombre": "Usuario nuevo",
    "correo": "jusuario@example.com",
    "contraseña": "secreta123"
}
```
📌 Obtener un Usuario por ID
GET /api/usuarios/{id}/

📌 Actualizar Usuario
PUT /api/usuarios/{id}/
```bash
{
    "nombre": "Juan Actualizado",
    "correo": "juan.nuevo@example.com",
    "contraseña": "nuevaClave456"
}
```
📌 Eliminar Usuario
DELETE /api/usuarios/{id}/

###  **🛠️ Tecnologías Utilizadas**
🐍 Python
🌐 Django
🗄️ MySQL
🔄 Django Rest Framework
📩 Postman


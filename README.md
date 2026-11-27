# IEI_N4_C1
Clases de Backend con Django

## Proyectos Backend con Django
1. **Creación del Ambiente (environment) Virtual.**
    ```
    python -m venv nombre_ambiente
    ```

2. **Activación del Ambiente Virtual.**
    ```
    .\Activate
    ```
    - Si obtenemos un error de permisos para ejecutar scripts, le daremos permisos especiales a nuestro terminal mediante la siguiente instrucción:
    ```
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
## Recetario API

Proyecto en Django para gestionar recetas y categorías. Incluye un CRUD web completo con vistas basadas en clases (CBV), formularios personalizados (`ModelForm`) y una API REST conectada a MySQL.

## Rutas disponibles

* **Inicio:** `/`
* **Recetas (CRUD):** `/recetas/` (listar, crear, ver detalle, editar y eliminar)
* **Categorías (CRUD):** `/categorias/` (listar, crear, ver detalle, editar y eliminar)
* **API REST:** `/api/` (`/api/recetas/` y `/api/categorias/`)
* **Panel Admin:** `/admin/`

## Instalación y uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/thewolf301/IEI_N4_C1-Maycol.git](https://github.com/thewolf301/IEI_N4_C1-Maycol.git)
   cd IEI_N4_C1-Maycol
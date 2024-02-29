# TODO:

[] Agregar toml para manejar dependencias https://github.com/Rviewer-Challenges/skeleton-py-flask-rest/blob/main/pyproject.toml

# Proyecto E-commerce con Flask

Este proyecto es un esqueleto básico para una aplicación de e-commerce utilizando Flask y Jinja. Incluye una grilla de productos y una barra lateral de filtros. Es ideal para practicar y aprender más sobre el desarrollo web con Python.

## Estructura del Proyecto 🗂️

El proyecto está organizado de la siguiente manera:

- `__init__.py`: Archivo principal que inicia la aplicación Flask.
- `templates/`: Carpeta que contiene los archivos HTML de Jinja.
  - `base.html`: Template base que incluye la estructura común de la página (aun no existe, hay que crearlo).
  - `index.html`: Página principal que muestra la grilla de productos.
  - `product_card.html`: Template para una tarjeta de producto individual.
- `static/`: Carpeta para archivos estáticos como CSS y JavaScript (aun no existe, hay que crearla).

## Tareas

1. **Ejecutar el Proyecto**: Configura tu entorno y ejecuta la aplicación.
2. **Renderizar Productos Dinámicamente**: Utiliza respuestas de una API para mostrar productos.
3. **Separar Templates**: Divide los templates en partes más pequeñas (por ejemplo, `product_card.html`).
4. **Agregar Paginación**: Usa parámetros de consulta para implementar la paginación.
5. **Agregar Filtros**: Implementa filtros de productos utilizando parámetros de consulta.

## Requisitos

- Python 3.x
- Flask
- Requests (para consultas a APIs)

## Configuración del Entorno

1. Instala Python 3.x en tu sistema si aún no lo tienes.
2. Crea un entorno virtual:

Mac os

```bash
python3 -m venv venv
```

Windows

```
py -3 -m venv .venv
```

## Ejecutar la Aplicación

Para iniciar la aplicación, ejecuta:

```bash
flask --app flaskr run --debug
```

Esto iniciará un servidor local en `http://127.0.0.1:5000/` donde podrás ver la aplicación.

## Desarrollo 🧑‍💻

### 1. Renderizar Productos Dinámicamente

Utilizando Jinja en `index.html` para iterar sobre una lista de productos obtenida de una API y mostrar cada producto usando `product_card.html` (crear el archivo y luego importarlo desde index.html usando `include`)

### 2. Separar Templates

Crea templates más pequeños para componentes reutilizables. Por ejemplo, usa `product_card.html` para cada producto en la grilla.

### 3. Agregar Paginación

Implementa la paginación en `index.html` manejando parámetros de consulta como `?page=2` para cargar diferentes conjuntos de productos.

### 4. Agregar Filtros

Permite a los usuarios filtrar productos por categoría, precio, etc., utilizando la barra lateral de filtros y actualizando la grilla de productos basada en los parámetros de consulta.

## Referencias 📚

La documentacion de Jinja esta piola y tanto en ingles como español:

- https://jinja.palletsprojects.com/en/3.1.x/templates/#template-designer-documentation
- https://jinja.palletsprojects.com/en/3.1.x/templates/#include
- https://jinja.palletsprojects.com/en/3.1.x/templates/#extends

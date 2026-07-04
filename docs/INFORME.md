# Informe del Proyecto: Migrador de Base de Datos

## 1. Introducción
El proyecto "Migrador BD" es una herramienta que facilita la transformación y migración de esquemas y datos entre distintos motores de bases de datos. Está construido con Python (Flask) en el backend y permite a los usuarios exportar desde bases de datos relacionales y no relacionales a múltiples destinos.

## 2. Diagramas de Software (UML)

### 2.1 Diagrama de Casos de Uso
Muestra la interacción de los actores con el sistema.

```mermaid
usecaseDiagram
    actor Usuario
    actor Administrador
    
    package "Sistema Migrador BD" {
        usecase "Subir Script SQL" as UC1
        usecase "Seleccionar Motor Destino" as UC2
        usecase "Iniciar Migración" as UC3
        usecase "Descargar Script Migrado" as UC4
        usecase "Verificar Reportes" as UC5
    }
    
    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
    Usuario --> UC4
    Administrador --> UC5
```

### 2.2 Diagrama de Secuencia
Muestra el flujo paso a paso de una migración.

```mermaid
sequenceDiagram
    actor Usuario
    participant InterfazWeb
    participant ControladorAPI
    participant DetectorBD
    participant Transformador
    participant Cargador
    
    Usuario->>InterfazWeb: Sube archivo SQL origen
    InterfazWeb->>ControladorAPI: POST /api/v1/migrations/start
    ControladorAPI->>DetectorBD: detectar(archivo)
    DetectorBD-->>ControladorAPI: Motor detectado (ej. MySQL)
    ControladorAPI->>Transformador: parse_and_transform(archivo)
    Transformador-->>ControladorAPI: Datos extraídos (Esquema + Datos)
    ControladorAPI->>Cargador: generar_export(motor_destino)
    Cargador-->>ControladorAPI: Archivo convertido (ej. MongoDB JSON)
    ControladorAPI-->>InterfazWeb: JSON con Job ID
    InterfazWeb-->>Usuario: Muestra progreso
    Usuario->>InterfazWeb: Clic en Descargar
    InterfazWeb->>ControladorAPI: GET /api/v1/migrations/download
    ControladorAPI-->>InterfazWeb: Archivo transformado
```

### 2.3 Diagrama de Clases
Muestra las entidades clave del backend.

```mermaid
classDiagram
    class DetectorBaseDatos {
        +detectar(ruta_archivo: str): tuple
        -buscar_marcas_mongo(texto: str): bool
    }
    
    class CargadorDestino {
        +motor: str
        +ruta_salida: str
        +crear_estructura(esquema: dict)
        +cargar_tabla(tabla: str, df: DataFrame)
        +generar_export(motor: str)
    }
    
    class SqlParser {
        +parse(ruta_archivo: str)
        +get_esquemas()
        +get_tablas()
    }
    
    SqlParser --> DetectorBaseDatos : Usa para detectar dialecto
    CargadorDestino --> SqlParser : Recibe estructura parseada
```

### 2.4 Diagrama de Componentes
Muestra los módulos físicos del software.

```mermaid
componentDiagram
    package "Frontend" {
        [Interfaz de Usuario (HTML/JS)]
    }
    
    package "Backend (Flask)" {
        [API REST]
        [Módulo Extracción]
        [Módulo Transformación]
        [Módulo Carga]
    }
    
    [Interfaz de Usuario (HTML/JS)] --> [API REST] : HTTP/JSON
    [API REST] --> [Módulo Extracción]
    [API REST] --> [Módulo Transformación]
    [API REST] --> [Módulo Carga]
    [Módulo Carga] --> [Base de Datos Temporal (SQLite)]
```

### 2.5 Arquitectura de Software e Infraestructura (Despliegue)
Muestra cómo se despliega la aplicación.

```mermaid
deploymentDiagram
    node "Cliente" {
        [Navegador Web]
    }
    
    node "Servidor de Aplicación (Ubuntu)" {
        node "Docker Container: Web" {
            [Gunicorn + Flask]
        }
        node "Docker Container: Worker" {
            [Celery/Airflow Worker]
        }
    }
    
    node "Servidor de Base de Datos" {
        database "SQLite / MySQL" {
            [Migraciones Temporales]
        }
    }
    
    [Navegador Web] -- HTTPS --> [Gunicorn + Flask]
    [Gunicorn + Flask] -- Tareas Async --> [Celery/Airflow Worker]
    [Celery/Airflow Worker] -- Lee/Escribe --> [Migraciones Temporales]
```

## 3. Estrategia de Pruebas
- **Pruebas Unitarias e Integración**: Implementadas con `pytest`. Aseguran el correcto funcionamiento de la detección y carga de BD.
- **Pruebas BDD**: Implementadas con `behave` utilizando escenarios Gherkin para la validación funcional.
- **Pruebas de Interfaz de Usuario**: Automatizadas usando `playwright` (pytest-playwright) verificando que el servidor web se levanta y la UI responde.
- **Pruebas de Mutación**: Configuración preparada con `mutmut` para verificar la resiliencia de los tests.

## 4. Análisis Estático y CI/CD
El proyecto emplea GitHub Actions (`ci_pipeline.yml`) para centralizar la verificación en cada *Push* / *Pull Request*:
- **SonarCloud**: Detecta Code Smells y Bugs.
- **Semgrep**: Analiza seguridad de código de forma rápida.
- **Snyk**: Revisa dependencias (`requirements.txt`) en busca de vulnerabilidades conocidas.
- Todo esto, junto a los reportes de pruebas, se publica automáticamente en GitHub Pages.

## Bibliografía
- Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- Documentación oficial de Flask: https://flask.palletsprojects.com/
- Guía de Mermaid JS: https://mermaid.js.org/

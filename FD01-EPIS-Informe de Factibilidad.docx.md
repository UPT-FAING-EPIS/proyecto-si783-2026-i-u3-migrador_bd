![C:\\Users\\EPIS\\Documents\\upt.png][image1]

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

 **Proyecto *Migrador BD*** 

Curso: *Base de Datos II*

Docente: *Mag. Patrick José Cuadros Quiroga*

Integrantes:

***Halanocca Rojas, Usher Damiron			(2023076795)***  
***LLica Mamani, Jimmy Mijair				(2023076795)***

**Tacna – Perú**  
***2026***

# **Sistema *Migrador de BD***

# **Informe de Factibilidad**

# 

# **Versión *3.0***

| CONTROL DE VERSIONES |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | ----- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 3.0 | MPV | ELV | ARV | 10/10/2020 | Versión Original |

**INDICE GENERAL**

[1\.	Descripción del Proyecto	3](#descripción-del-proyecto)

[2\.	Riesgos	3](#riesgos)

[3\.	Análisis de la Situación actual	3](#análisis-de-la-situación-actual)

[4\.	Estudio de Factibilidad	3](#estudio-de-factibilidad)

[4.1	Factibilidad Técnica	4](#factibilidad-técnica)

[4.2	Factibilidad económica	4](#factibilidad-económica)

[4.3	Factibilidad Operativa	4](#factibilidad-operativa)

[4.4	Factibilidad Legal	4](#factibilidad-legal)

[4.5	Factibilidad Social	5](#factibilidad-social)

[4.6	Factibilidad Ambiental	5](#factibilidad-ambiental)

[5\.	Análisis Financiero	5](#análisis-financiero)

[6\.	Conclusiones	5](#conclusiones)

**Informe de Factibilidad**

1. Descripción del Proyecto  
   1. Nombre del proyecto

   Migrador DB Enterprise – Sistema Integral de Migración de Bases de Datos

   2. Duración del proyecto

   El proyecto tiene una duración estimada de 5 meses (marzo – julio 2026), correspondiente al ciclo académico 2026-I, incluyendo las tres unidades de desarrollo.

   3. Descripción 

          Migrador DB Enterprise es un sistema integral de migración de bases de datos de nivel corporativo. En su núcleo, permite la extracción, transformación y carga (ETL) de estructuras complejas (tablas, vistas, triggers y procedimientos almacenados) entre múltiples motores de bases de datos mediante un algoritmo eficiente de procesamiento por bloques (Chunking RAM). El sistema soporta la migración entre motores relacionales (MySQL, PostgreSQL, Microsoft SQL Server, Oracle, SQLite), motores NoSQL (MongoDB, Elasticsearch, Apache Cassandra, Redis) y formatos de archivo (CSV, Excel, JSON).

   

           El sistema incluye autenticación segura con soporte OAuth (Google y GitHub), control de roles (administrador/usuario), integración directa con repositorios de GitHub para almacenamiento de exportaciones, detección automática del tipo de base de datos a partir del contenido del archivo, interfaz web interactiva con comunicación en tiempo real vía WebSocket y foro de comunidad.

           En la tercera unidad del proyecto se incorporaron dos integraciones de alto valor para entornos empresariales y de desarrollo profesional:

           \-Apache Airflow – MigradorDBOperator: Un operador personalizado para Apache Airflow (\`migradordb-airflow\`) que permite orquestar y programar flujos de trabajo de migración de bases de datos como DAGs (Directed Acyclic Graphs). Las organizaciones pueden así automatizar migraciones periódicas (diarias, semanales) integrándolas en sus pipelines de datos existentes sin intervención manual.

   

           \- Extensión oficial de VS Code: Una extensión para Visual Studio Code (\`Migrador DB v1.0.2\`) publicada en el marketplace que permite al desarrollador migrar archivos de bases de datos (\`.sqlite\`, \`.db\`, \`.sql\`) directamente desde el explorador de archivos del IDE, con progreso en vivo y descarga automática del archivo resultante, sin necesidad de abrir el navegador.

   

           La importancia del proyecto radica en la necesidad de las organizaciones de migrar datos entre diferentes sistemas de gestión de bases de datos de manera eficiente, segura y sin pérdida de información. Con las integraciones de la Unidad 3, el sistema trasciende la interfaz web y se convierte en una plataforma extensible, embebible en cualquier entorno de trabajo profesional.

1.4 Objetivos

       1.4.1 Objetivo general

Desarrollar un sistema integral de migración de bases de datos que permita la extracción, transformación y carga de datos entre múltiples motores de bases de datos de forma automatizada, segura y eficiente, extensible a entornos de orquestación de datos y de desarrollo de software integrado.

        1.4.2 Objetivos Específicos  
  	      \- Implementar un módulo de extracción capaz de conectar y leer datos desde archivos SQLite, scripts SQL (MySQL, PostgreSQL, SQL Server, Oracle), JSON, CSV y Excel.  
        \- Desarrollar un módulo de transformación que adapte los datos al esquema del motor destino, incluyendo limpieza de datos y mapeo de tipos.  
        \- Construir un módulo de carga que genere exportaciones compatibles con más de 15 motores de bases de datos destino, incluyendo formatos SQL, JSON, NDJSON, CQL y comandos Redis.  
        \- Implementar un sistema de detección automática del tipo de base de datos basado en análisis de contenido del archivo.  
        \- Integrar autenticación segura con soporte para registro local, verificación por email y OAuth con Google y GitHub.  
        \- Desarrollar una interfaz web interactiva con actualizaciones en tiempo real mediante WebSocket.  
        \- Implementar integración con GitHub para almacenamiento y versionamiento de las exportaciones.  
        \- Desarrollar e integrar el operador \`MigradorDBOperator\` para Apache Airflow, permitiendo la orquestación y programación automatizada de flujos de migración de bases de datos como DAGs.  
        \- Publicar y distribuir una extensión oficial para Visual Studio Code que permita ejecutar migraciones directamente desde el IDE con soporte de progreso en tiempo real y descarga automática del resultado.

2. Riesgos

*{Señale los riesgos que pudieran afectar el éxito del proyecto.}*

3. Análisis de la Situación actual  
   1. Planteamiento del problema

        En el entorno actual de desarrollo de software y administración de sistemas, las organizaciones frecuentemente necesitan migrar datos entre diferentes motores de bases de datos. Esta necesidad surge por diversas razones: actualización de tecnología, consolidación de sistemas, migración a la nube, cambio de proveedor de base de datos, o integración entre sistemas heterogéneos.

2. Consideraciones de hardware y software

        **Hardware requerido:**

        \- Servidor o equipo con mínimo 4 GB de RAM (8 GB recomendado para entornos con Airflow)

        \- 10 GB de almacenamiento disponible para archivos temporales de migración

        \- Conexión a internet para funcionalidades OAuth, GitHub y publicación en marketplace de VS Code

        **Software requerido (sistema web – Unidades 1 y 2):**

        \- Python 3.12+ como lenguaje de desarrollo

        \- Flask 2.3.3 como framework web

        \- SQLAlchemy 2.0.23 para abstracción de bases de datos

        \- Flask-SocketIO 5.3.0 para comunicación en tiempo real

        \- Authlib 1.2.0 para OAuth

        \- Pandas 2.1.1 para manipulación de datos

        \- Gunicorn 21.2.0 para servidor de producción

        \- Nginx como proxy reverso en producción

        **Software adicional requerido (Unidad 3 – Integraciones):**

        \- Apache Airflow 2.x: Plataforma de orquestación de workflows para la integración del \`MigradorDBOperator\`.

        \- GitHub Actions.

        \- Skills 

        \- \`axios\` ^1.6.0 y \`form-data\` ^4.0.0: Dependencias de la extensión para comunicación HTTP con la API.

        \- VS Code Extension CLI (\`vsce\`): Herramienta para empaquetar y publicar la extensión (\`.vsix\`).

4. Estudio de Factibilidad

El estudio de factibilidad se realizó evaluando las dimensiones técnica, económica, operativa, legal, social y ambiental del proyecto Migrador DB Enterprise en sus tres unidades de desarrollo. Los resultados demuestran que el proyecto es viable en todas las dimensiones evaluadas, y que las integraciones incorporadas en la Unidad 3 (Apache Airflow y extensión de VS Code) refuerzan significativamente el valor técnico y económico del sistema.

1. Factibilidad Técnica

       El proyecto es técnicamente factible dado que utiliza tecnologías maduras y ampliamente documentadas en sus tres componentes principales:

        **A. Sistema Web ETL (Unidades 1 y 2\)**

        Lenguaje de programación:  
        \- Python 3.12: Lenguaje de alto nivel con amplio ecosistema para manejo de datos y desarrollo web.

        Framework web:  
        \- Flask 2.3.3: Microframework web ligero y flexible.  
        \- Flask-SocketIO 5.3.0: Extensión para WebSocket con soporte para comunicación bidireccional en tiempo real.

        Base de datos intermedia:  
        \- SQLite: Base de datos embebida para almacenamiento temporal durante el proceso ETL.  
        \- SQLAlchemy 2.0.23: ORM para abstracción de acceso a datos.

        Bibliotecas de procesamiento:  
        \- Pandas 2.1.1: Manipulación y transformación de datos tabulares.  
        \- NumPy 1.26.4: Operaciones numéricas de soporte.  
        \- OpenPyXL 3.1.3: Lectura/escritura de archivos Excel.

        Autenticación y seguridad:  
        \- Authlib 1.2.0: Implementación de OAuth 2.0 para Google y GitHub.  
        \- Werkzeug 2.3.7: Hashing seguro de contraseñas con scrypt.  
        \- Bcrypt 4.0.1: Algoritmo de hashing adicional.

        Infraestructura de producción:  
        \- Gunicorn 21.2.0: Servidor WSGI para producción.  
        \- Eventlet 0.33.3: Servidor asíncrono para WebSocket.  
        \- Nginx: Proxy reverso y servidor de archivos estáticos.  
        \- Supervisor: Gestión de procesos en producción.

        **B. Operador Apache Airflow – \`MigradorDBOperator\` (Unidad 3\)**

        \- Apache Airflow 2.x: Plataforma de orquestación de flujos de trabajo de datos líder en la industria, utilizada por organizaciones como Airbnb, Twitter y NASA.  
        \- \`MigradorDBOperator\`: Operador personalizado (\`BaseOperator\`) que se conecta a la API REST de Migrador DB Enterprise para iniciar, monitorear y validar trabajos de migración desde dentro de un DAG de Airflow.  
        \- El operador soporta configuración de parámetros como \`source\_file\_path\`, \`target\_engine\`, \`output\_file\_path\`, \`api\_base\_url\` y \`poll\_interval\_seconds\`, permitiendo migraciones automatizadas y periódicas sin intervención humana.  
        \- El paquete \`migradordb-airflow\` se distribuye a través de PyPI (\`pip install migradordb-airflow\`), garantizando su accesibilidad e integración en cualquier entorno Airflow existente.

        **C. Extensión de Visual Studio Code (Unidad 3\)**

        \- TypeScript 5.1+ y Node.js 18+: Ecosistema estándar para desarrollo de extensiones de VS Code.  
        \- VS Code Extension API (^1.80.0): API oficial que permite registrar comandos, menús contextuales y paneles de notificación dentro del IDE.  
        \- \`axios\` ^1.6.0: Cliente HTTP para comunicación asíncrona con la API REST de Migrador DB Enterprise.  
        \- \`form-data\` ^4.0.0: Biblioteca para construcción de peticiones \`multipart/form-data\` necesarias para el envío de archivos de base de datos.  
        \- La extensión se distribuye como paquete \`.vsix\` (v1.0.2, publisher: \`jimmyllica\`) y permite migrar archivos \`.sqlite\`, \`.db\` y \`.sql\` con clic derecho desde el explorador de VS Code.  
        \- La URL del servidor es configurable desde los ajustes del IDE (parámetro \`migradorDb.apiUrl\`), por defecto apuntando al servidor de producción (\`http://178.238.228.92:100\`).

        Todos los componentes son de código abierto o basados en herramientas con licencias permisivas y están disponibles para su uso sin costo de licenciamiento.

2. Factibilidad Económica

El propósito del estudio de viabilidad económica es determinar los beneficios económicos del proyecto en contraposición con los costos. A continuación, se presentan los costos actualizados considerando las tres unidades de desarrollo, incluyendo la integración de Apache Airflow y la extensión de VS Code incorporadas en la Unidad 3\.

1. Costos Generales 

| Descripción | Cantidad | Costo Unitario (S/.) | Costo Total (S/.) |
| :---- | :---- | :---- | :---- |
| Papel bond A4 | 1 millar | 25.00 | 25.00 |
| USB 32GB | 2 | 30.00 | 60.00 |
| Útiles de escritorio | 1 set | 15.00 | 15.00 |
| Total |  |  | 100.00 |

   2. Costos operativos durante el desarrollo 

| Descripción | Costo Mensual (S/.) | Meses | Costo Total (S/.) |
| :---- | :---- | :---- | :---- |
| Servicio de Internet | 80.00 | 5 | 400.00 |
| Energía eléctrica | 50.00 | 5 | 250.00 |
| Total |  |  | 600.00 |

      3. Costos del ambiente

| Descripción | Costo Mensual (S/.) | Meses | Costo Total (S/.) |
| :---- | :---- | :---- | :---- |
| VPS Ubuntu (2 CPU, 4GB RAM) |  40.00 | 5 | 200.00 |
|  Dominio web (.com) | 50.00 | 1(anual) | 50.00 |
| Certificado SSL (Let's Encrypt) | 0 | \- | 0 |
|  Cuenta de publicador VS Code Marketplace | 0 | \- | 0 |
| Cuenta PyPI para publicación de \`migradordb-airflow\` | 0 | \- | 0 |
| Total |  |  | 250.00 |

      4. Costos de personal

   

        Organización y roles:

        \- LLica Mamani, Jimmy Mijair: Desarrollador Backend/ETL, responsable del motor de migración, módulo de extracción/transformación/carga, integración con Airflow y publicación del paquete PyPI.

        \- Halanocca Rojas, Usher Damiron: Desarrollador Frontend/Auth, responsable de la interfaz web, autenticación OAuth, WebSocket y desarrollo de la extensión de VS Code.

Horario de trabajo: Lunes a viernes, sesiones de trabajo de 3 horas/día (12 horas/semana por integrante).

|  Rol | Integrante | Horas/Semana | Semanas | Costo/Hora (S/.) | Costo Total (S/.) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Desarrollador Backend/ETL \+ Airflow | LLica Mamani, Jimmy Mijair | 12 | 20 | 15.00 | 3,600.00 |
|  Desarrollador Frontend/Auth \+ VS Code Ext. ´+ GitHubActions | Halanocca Rojas, Usher Damiron | 12 | 20 | 15.00 | 3,600.00 |
| Total |  |  |  |  | 7,200.00 |

5. Costos totales del desarrollo del sistema 

| Concepto | Costo (S/.) |
| :---- | :---- |
| Costos Generales | 100.00 |
| Costos Operativos | 650.00 |
| Costos del Ambiente | 250.00 |
| Costos de Personal  | 7,200.00 |
| TOTAL | 8,200.00 |

   3. Factibilidad Operativa

        El sistema Migrador DB Enterprise es operativamente factible en sus tres componentes:

        \- Interfaz intuitiva: La aplicación web presenta una interfaz paso a paso que guía al usuario en el proceso de migración (subir archivo → seleccionar destino → ejecutar migración → descargar resultado).  
        \- Detección automática: El sistema detecta automáticamente el tipo de base de datos del archivo subido, eliminando la necesidad de que el usuario tenga conocimiento técnico sobre el formato del archivo.  
        \- Actualizaciones en tiempo real: El uso de WebSocket permite que el usuario observe el progreso de la migración en tiempo real, tanto desde la interfaz web como desde las notificaciones de VS Code.  
        \- Extensión de VS Code accesible: La extensión permite a los desarrolladores ejecutar migraciones con clic derecho sobre cualquier archivo de base de datos en el explorador del IDE, eliminando la fricción de cambiar entre aplicaciones. El resultado migrado se descarga y abre automáticamente.  
        \- Orquestación con Airflow: El \`MigradorDBOperator\` permite a los equipos de ingeniería de datos integrar migraciones recurrentes (diarias, semanales) dentro de sus pipelines de datos existentes sin modificar la lógica central del sistema de migración.  
        \- Documentación completa: El proyecto incluye documentación técnica detallada (READMEs, GUIA\_DE\_USO.md) para despliegue, configuración de OAuth, uso del operador Airflow y configuración de la extensión de VS Code.  
        \- Capacidad del equipo: Los integrantes del equipo poseen las competencias necesarias en Python, Flask, bases de datos, TypeScript y desarrollo de extensiones de IDE.

        Lista de interesados:  
        \- Administradores de bases de datos  
        \- Desarrolladores de software e ingenieros de datos  
        \- Equipos de ingeniería de datos que usan Apache Airflow  
        \- Empresas que requieren migración periódica y automatizada de datos  
        \- Docentes y estudiantes de ingeniería de sistemas

4. Factibilidad Legal

        El proyecto no presenta conflictos legales dado que:

        \- Todas las tecnologías utilizadas son de código abierto con licencias permisivas (MIT, BSD, Apache 2.0), incluyendo Apache Airflow (Apache 2.0) y el ecosistema de extensiones de VS Code (MIT).  
        \- El sistema no almacena datos sensibles de terceros; los archivos subidos son procesados y el usuario descarga el resultado.  
        \- La implementación de OAuth cumple con los estándares de autenticación de Google y GitHub.  
        \- El sistema cumple con la Ley N° 29733 (Ley de Protección de Datos Personales del Perú) al implementar cookies seguras, sesiones con HTTPOnly y SameSite, y hashing de contraseñas.  
        \- La extensión de VS Code fue desarrollada y publicada bajo el nombre del publicador \`jimmyllica\` cumpliendo con los Términos de Servicio del Visual Studio Marketplace de Microsoft.  
        \- El paquete \`migradordb-airflow\` publicado en PyPI no infringe ninguna marca registrada de la Apache Software Foundation, siendo un operador de terceros compatible con Airflow según las directrices de la comunidad.

5. Factibilidad Social

        El proyecto tiene un impacto social positivo al:

        \- Democratizar el acceso a herramientas de migración de bases de datos, ofreciendo una alternativa gratuita y de código abierto a soluciones comerciales costosas.  
        \- Facilitar el aprendizaje sobre procesos ETL y arquitectura de bases de datos para estudiantes de ingeniería.  
        \- Promover buenas prácticas de desarrollo de software mediante código documentado y estructurado.

6. Factibilidad Ambiental

        El impacto ambiental del proyecto es mínimo:

        \- Al ser un sistema web, no requiere distribución física de software.  
        \- El uso de VPS compartido minimiza el consumo energético comparado con infraestructura dedicada.  
        \- La migración automatizada reduce el tiempo de proceso y, por tanto, el consumo de recursos computacionales comparado con procesos manuales.

5. Análisis Financiero

   1. Justificación de la Inversión

*5.1.1 Beneficios* del Proyecto

           El beneficio se calcula considerando el margen económico generado por la herramienta respecto a los costos de oportunidad de haber contratado soluciones comerciales equivalentes.

            **Beneficios tangibles:**

            \- Reducción del tiempo de migración de bases de datos de días/semanas a minutos/horas.

            \- Eliminación del costo de licencias de herramientas comerciales de migración (estimado en $500 – $5,000 USD anuales por herramienta como AWS DMS o Azure Database Migration Service).

            \- Reducción de errores humanos en el proceso de migración en un estimado del 80% gracias a la automatización.

            \- Soporte para más de 15 motores de bases de datos destino (SQLite, PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Snowflake, Amazon Redshift, Azure SQL, IBM Db2, BigQuery, MongoDB, Elasticsearch, Redis, Cassandra, MongoDB Atlas) en una sola herramienta.

            \- \[Unidad 3\] Automatización de migraciones recurrentes vía Apache Airflow: elimina horas-hombre de supervisión manual en procesos periódicos de migración (estimado: 8 horas/semana ahorradas por equipo de datos).

            \- \[Unidad 3\] Reducción del tiempo de migración para desarrolladores individuales de \~15 minutos (acceso web) a \~2 minutos (extensión VS Code con 1 clic).

            **Beneficios intangibles:**

            \- Mejora en la eficiencia operativa del equipo de desarrollo/DBA.

            \- Disponibilidad de información migrada de forma oportuna y precisa.

            \- Mejora en la toma de decisiones al facilitar la consolidación de datos entre sistemas heterogéneos.

            \- Ventaja competitiva al ofrecer una solución multi-motor, multi-plataforma y sin precedentes en el mercado de código abierto.

            \- Aumento en la confiabilidad del proceso de migración al ser automatizado, auditable y orquestable.

            \- \[Unidad 3\] Integración con el ecosistema de herramientas más usadas en ingeniería de datos (Airflow) y desarrollo de software (VS Code), aumentando la adopción y el alcance del sistema.

            \- Valor agregado al producto académico convirtiéndolo en una plataforma extensible de nivel profesional.

5.1.2 Criterios de Inversión  
   
*5.1.2.1 Relación Beneficio/Costo (B/C)*

               Considerando un ahorro anual estimado de S/. 10,000.00 (por eliminación de licencias, reducción de horas-hombre en migraciones manuales y valor generado por las integraciones de la Unidad 3\) frente a un costo total de desarrollo actualizado de S/. 8,200.00:

                B/C \= 10,000.00 / 8,200.00 \= 1.22

                Al ser B/C \> 1, el proyecto se acepta.

                El costo de oportunidad del capital (COK) utilizado es del 10% anual, representando la tasa de retorno que podría haberse obtenido en una alternativa de inversión de riesgo equivalente.

                    *5.1.2.2 Valor Actual Neto (VAN)*

          Con una tasa de descuento del 10% (COK) y un horizonte de evaluación de 3 años:

    VAN \= \-8,200 \+ (10,000/1.10) \+ (10,000/1.21) \+ (10,000/1.331)  
                VAN \= \-8,200 \+ 9,090.91 \+ 8,264.46 \+ 7,513.15  
                VAN \= S/. 16,668.52

         Al ser VAN \> 0, el proyecto genera valor positivo y se acepta.

*5.1.2.3 Tasa Interna de Retorno (TIR)*  
   La TIR calculada para el proyecto actualizado es de aproximadamente 115%, lo cual es significativamente mayor que el costo de oportunidad del capital (COK \= 10%).

           Al ser TIR (115%) \> COK (10%), el proyecto se acepta.

          Este valor de TIR refleja el incremento en el beneficio anual estimado atribuible a las integraciones de la Unidad 3, que amplían el alcance del sistema a audiencias profesionales adicionales (ingenieros de datos con Airflow y desarrolladores con VS Code).

6. Conclusiones

  \- Técnicamente factible: Se dispone de todas las tecnologías necesarias: Python, Flask, SQLAlchemy y Pandas para el motor ETL; Apache Airflow para la orquestación de pipelines; y TypeScript/Node.js para la extensión de VS Code. Todas son de código abierto, maduras y ampliamente documentadas.

    \- Económicamente factible: El costo total actualizado de S/. 8,200.00 (incrementado por la extensión del periodo de desarrollo a 5 meses y los nuevos componentes de la Unidad 3\) sigue siendo accesible. Los indicadores financieros actualizados (B/C \= 1.22, VAN \= S/. 16,668.52, TIR ≈ 115%) confirman la rentabilidad y el retorno positivo del proyecto.

    \- Operativamente factible: El equipo de desarrollo tiene las competencias necesarias en todas las tecnologías involucradas. El sistema está diseñado para ser intuitivo en sus tres puntos de acceso: interfaz web, extensión de VS Code y operador de Airflow.

    \-Legalmente factible: No existen conflictos con regulaciones legales nacionales ni con los términos de servicio de las plataformas de distribución (VS Code Marketplace, PyPI). Se cumplen las normas de protección de datos personales (Ley N° 29733).

    \- Social y ambientalmente responsable: El proyecto democratiza el acceso a herramientas de migración de nivel empresarial, reduce la brecha tecnológica entre organizaciones grandes y pequeñas, y tiene un impacto ambiental mínimo al operar íntegramente como software en la nube.

    Las integraciones desarrolladas en la Unidad 3 (operador Airflow y extensión VS Code) representan un salto cualitativo significativo: el sistema deja de ser una herramienta web aislada para convertirse en una plataforma extensible integrable en los flujos de trabajo profesionales de ingeniería de datos y desarrollo de software.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGgAAACMCAYAAACQyew1AAAlQ0lEQVR4Xu1dB3xT1f4vMtxPhaYFlMdToUmLjNybpC0tpOyC7FLa5qaAgKIoIKLiroooPicCbdKiiFvecz/X8684GU3asmQpQxEQypBVoOv8f7+Te29Ozk3StA0t8Pr9fH6f3Jx9zvfsGRHRhCaEA4m9EvOV74QEayflWxTFlijKfwWtLrvoYfiJbNa8mTPioos6wHczkOYtL70oizPahPoiZdSg2xOTEmfgd3/7sH8q6tYRgyanpKUu8Jr0wWW9po+uEKW+B7qOTC4bNf/2qpYXXvh45sv3kBYtWiTxhptQD2Qsmlme2K/Xjb0H9+s68tFJJ6wjrFcOf2DCPvjewJvl0LLXtFFl9jceIHFDE8jIF6YS/E59bHwV6EXyhptQB5jN5jaYqAk9E6alvzSj3Dpy4BfSa/dXp96WXgTazZL7JV+XIJjH8/ZkXBXRMkJIun1EZebLd5Me6VaCJQjdE2z9qlq1aqXnLTShlgCC2mKCDrhpZJntldlk0OTRZMDEUb+PeGTSscFTx+5KSkr6O2+HxYWXXphiuSn1MLqRtnA6sc4cQwka/dIdpMfYlJO8+SbUARl5M6uyIOePeuIWmrjD7h9Peib3vLdnz556i8l0D2+eA3YO0q7qoHtdqerwd6zzLvob0bJlD95CE2pAenp6cyg5PZJET+nokz740YyFd5KxC+4kGbkzacLSEvH01OPYHvH2/eHiNpcPHzrvZgJtEuk2uhcZs2gGdUOU+le3uLjFFN58E4IgZeSgu5JNpuuS+vb6nP5PS12X2KvnZyMemVg2as7NZUPulFYnWpPH8PZqQpvr2v1LIbf//Tb6i0QZM/uW82abEAQjHpu0z9K7Z5+ROZPKc3JyLoAe23ZUHzB+5M+82dqg1aWtZpqyB5Ded6bRqm5MLpSi1++nAtoX8eabEABZ+bOqrUP6FtqWzK5OnTJmxZAZWSuHzLR90Wf0oHl90gZO5M3XBs0vuSQVS44EpBhSLWp12TEh9hhvtgkBIL16Hxl+/wSS6ZhFEw96bfuz8u8mw3Mm7UlfMKNePa8LWrS4R2fosB/d7Tc7k7rfZVgisS29D0vRxbz5JvjBqCdvrRw2exwZ/dStQNR4MvzBCZ724tnbq0VRvIQ3X0tcpYvp8I11RhrpB+1QxuK7ydh8uUcXEdGNN9wEP0ga2Kf7qLlTylOnpGNPjYyFHlx/29CXI3IiLuDN1gHNQSLTFk2npHRK6aFWcxEtWvTkDTeBQWJiogF+mvUamPIW/u9vH7YFf4fdN/5Iz9Q+1/fNuPElHwt1R1v9IHO1DapSwdaXktP33kySMiu9qTcXDEl9krr0HtF/SJ/01H/jDPWYF6aVW63Wf6Q9M/Xk2JemV1pHDZrM26kj2iZMHvLXkLmTSPd0qzp47Tam12HeYBMYxMfHRwMZFdbBfd4f/eSUo1mL7yEDJ6ftGQrtESZgXFxcK95OHfFg+67X/ohuIklKFXfF1ZELeYNNYACl5SIJelMDJ42uwF8cnyBJ0mv3k76jBz3Dm68rmjdvPvBqofMRJKXryCRKzuA5N1Vf2UH3KW+2CRyGP3TTsZGPTCKjHptM0l+YRvAb2qCdvLl6IgVJ6Z7Wmwz75xSSMnMMyXzlHuhu9zz7qziy3NqCV6sP3E4xEsTpdghHixeKpORFkax5XiTF80XidojVLofoducKgwihk5oRFovl2izn3ZXDH7iJDJwwErvZpf369WuDemazuXdSfHyyrw+1x1Udo7bjQBXl+t7dSNaSe2kpanXZxemykWYuhxAP8gNIVfFLnjCXvADhXkjDfRLC/W7RYmN7H4frCUgnzcqwBuvnCAN3LLHWe9qjcJGpg8spHlr/uInss1rIQSHev4jxZPsEM0aaQGLcptjHTsLk7KRXQO2DjGkjt6Ja8uC+/0nq35uurNYHOPfWb9ow8ubiG8m9+RM93W1rd9pjLHSYhkG4q3+dYiIHRD/hlaU0MZ5sfMhEwOzp4rwe3Xk/6oLip4WpvJoG+/vEDyl+XlzJq4cKAmMVyF1fbHxYJAcs2ogFk98yzUjSJmu/pMfEoeIlu4ZZyJ5UC829oP5N2lO3nOqbMWTpgG7dLuX9DRUtWlzw4OsFNxIsFX+MAPcHWUj30b3I4McnVHw0t+vWbZPNmnAFkwOmeLJllom4nULxhpy6d2KKF4lLSnuY1QwaEH91Tb5qf7IFPBTv4/VqwoqChNZFuUJFac8gJaYGOWCOJyvni9VPzLnFR/33dDNZnW8m0otTT1uSk+N4v0PBsmURzb99sUf19km+JLw8006+eclcvb9e4baQogViddFCo7qhJVS4Fgk3YkY8IFgSeD2/OGC0VP6WYcHiq27QqAkrHELXdXPEaqyy+MAfHjCYHHvgEXLqP5+R8uISUl7oIsfuf4gcShmgMUsFcmXpxv8jhwfd6KO+r3c8ceeJBNqpa3j/QwGUwnJMCJ+w9Uslh9xfkwMJCdpwgBxKTiHHZswip1esIuUla8jpL78ixx+fSw4PHqYxi7LpPqj2FgsDeb8DwZUnTtk2xZNheL2AOHr79M/Rwu6hWJKEI4W5pht4MyzAzKeb7zVpAnv8n8+S6qoqUl1dHVCqjhwlh4eO9LF35JapPmbKlrzm1QfyoL36Cv3FcRMflkCAandRaYKXnBPPPu/jx4n5C33CcMjan1Tu2asJLy9li5do4v3rrVhVi24ssXw4FKzNt1xT5BB+w2od7Rwek7mZN0PhzhPu5tWqysv3KJ5hlbP1TpOn9+IUtoG8BZ7PLnQIOS6nsGPNsyL5M8U3gEcmTSFVZWWayASTk2+8rdovcxZo9KsrKsjRm2/1JMBtkABO4ePUm9P8R4oDhHneptmeDPRXWiapOnlS4/7p775X/T8+7xmNflApLyfH7n3AJw32J8WTdU+ZkKjd4P8c6MXeA80Gdnq2FOWKBMNTmuA1X3n8RCUf7kKHcVjEL7eZyK6fni3TeAqROJTcx8dTFOyR/TESZJif+lpMIBUbftZGIEQ59dXX1J1daWZsA6n88vkMUlVZrpo5/X/fUDNb7jKRgvzhBJfHN0NXHqrjKZBpbkeBBJkKCSFgJL9/0Thzw+MecsqWLPX6ByV7x7ePqv78eqtspuAVTbhClcrdu8mh+GRNumBNtAvS7M++2jQ7ZEkiVQcOaNwq3fRh2ab7TSTioGA5uQO6uVs+ucVvdXTyg4/IQT+e8oL1Mm+/quIU2ePOJ2uW9qOJgD0nHAdhl3rDu2PIsb0lGv/Klr5Ou97oJpZe7IIXOUxk7xpv4h6deQ/V3wgR+O4l8c+ND0JXfmAvUn5oL5Ujuc+TbdAR+GmB8eS6J0Vq9og0QbV/8NcvSRF0OH6daiYH4pXMBXF45DFteA78Qja+b6dhxrCX4PgN4lKyJIX8/tMzpOLUUa0dR4EmfTRiSoSaYrEmzVB2fPMI2ToDuvlCfHXEge4JVyuWtk43k/Vvj4Qce1pjiQo6duoUqVi3gZSvdtFvjQdVlUD2rQS6jeSP4doc4yOQKD9D4pYssZLK8hOqG9s/nkWwGigCN35Pl90As+vnmMjmjyaqYdk8x0p2D/HoH0rsrdovy1+s+lG80ESqTnnis/3rB8naZ4Aws6dDgDkbw4n+bHojU7VfVVlB1r81lPqHmUQTbkb2DrBQ0jYsS6cZ0ictUE6fhk6Rm1SsWUuqT0C1X1mpNUMF4vPRZIKZTXFb7dUdNJpnqx72h0DnQv246QM/jgSXfevfgYQ1ATG1G0vs7wUJucBEDu/8nhz5o5DsGuMlFgeE6+YB2f08///sZyFbP5tGq731b41QzQUiCBMfI7/j28fJHpnM/cnxp9fOE6v39fb6gwm9b91b5ETpJlKcZ6b+8OEMJnthPFW8QCS7Vs2n/vFpE0yO/L6CFDktvhnaGL/Up0EqNVrmsx7+Mg2qloJ4cnR3kcZBXjD3l7zah/Ze+IAfNFqOlQqWl470iO/s4yHgsDE+DfTVDskm6AmufSNV6wbIjmwzWflPU/UuS0I1Dg7Xz4Uqc3FPVT8gQVAS1zwnklJPVXZq/RPivl9v0/Y4UUpeTSHrn2D0jPFH9gvxN5OIHJ+FQqx1SsX4J0G/lHdjpx3TLYGUl2nbFV7KDm0jxS8nE2xrWDeg5HzG+qfigDH+JtYgRmrDoyZK1NZP7wCyCkn5iYO0CsQcjB5gbsa2ZX8vH/Y3QwRSiGfTYI34q6vpOmgLD6Hd7TCS/+V2P0RjwKG62fiACUv5H/h/y0zo4IwOXMUhkdhu4DeUlv047cT2nFj5zWamHQ9P+C1lpUK8yIczEP4ymk0wdixS3EI/MFNs+vAmcmL/JppWKOVlh8nxP9eRbf+9B4hJIuueNNHeHhuOUiHhCd59Hxwxm9tgAPkI7B5qpo0y5kil54O5ePeNTHUkxr+/3Fr3yVYgdhm6g9Mta58OnpjQSys9EG+ejuHAKlJDkIjVpkh2jhXn4vQRds15d1CQ9J9zTHS6hqoZLav4cIUKzJBAVK7iNlaTmMGV9MKOxs8PY6bShgU6BJVHevTW1DJ+gR5BYt3ljyh/8kX3FHKdwUaiDPZ6iz42i+R2G0g290qkOQwTGRtrLDmYQbBX9sQd/Ui0bL7DDTayNCeZ/PCChaxa1J/KiheTyMdPJxCh51jV3ZkTUgm0O7QRxioF3cTGHTsNW/snkje79Sc9YjM04amLXGOQyFvd+2nSyZ8AoRVQpT0H44WAg9qg+MNk6oANFjrEO44J2SFMxAST6Fg7iTVlEIOYqdGrrXQ2ZpIu5gzSNlbS6IVb2gJR87pq21TsPkOV/t5Bs7kLn971QlTMuG58IJqk9sKna9jgQ1Cs7VZevwmBodNLbzcRdBajwQnSxdqDLi5Fd7NfqjPYP4o0SK/g/yi99F6kXpqIaihRejvt69P/eumDyFjbU9ScISuR6sdK/XR6+1eM+U/QzdadJHWpoZ049BJQ/w7kvYgIbSOrM0hvqPYNtn9BuD/z/vf472se9aQP8BvDC/4/5vFbei3KIDF2JXrqAtwY4OtCYJwVBEHA74qIS28VZch+JEK8pSVE7IAuxpZN9fTSr/gLAT19TdyY1mB2vseOJ8Cgvo/ag246qNGZ3agY+0hIkA91BtsTUYZxdE8ckHHI4xslYB/8NAPi/S6DQ+Z4GAnEb3Dn2bZxUhz4uwbcGw3/5/LmdbHSf0Gf7h6CMOyWf0mkwSbqumRcD9+bo/W2PuDfk9S8Xqr4G8RFtW+QTkbGSGMhruXR+qxhirpstoEJMkg+6+eRhvEiqFdHGrKt+EvNG6RcDNhVXSZ0gEgO9ahhAL0jc4ag47T0dB7fQ8eQAG78hW7S72szoyHye63WHDrWgkTeD/9/Yd1jAfrLkfQofbZaHQNhx67oaruKNacAMx2490PHjiOuhPDQk3sYvss6jdHJ35BxPH4jaehWpN4+3WM7vTnY+aqdeMslkDaa7Vvg7juNSpAuzt4pqpOU0BpyaWRsphHVoruM6wOR2AIJvjPCM6vQjNrVS06qj9WgXjpBc1xclgXVImOliUDKRsVdNN8uLpuetAN3VrbRZ5vaxEhmqoml1GDfCkSUKeZZYIKCngPcL2bUAiYQlgZM9Ci97csIGl5amlXz8jedHQFze8Ht2aBGa4bWncddjXpKWHk0OkGBgGbbG0bSbVORnbOHwH96CCvakH0fVk3w/wtKrrfUuaD9kassrC7lEmbIHg3k9WrdOSMWiCqKjM026jrb6W4aIDkQQaSNfuLlwGRLtB/R0XoRuF/Bm2OAGag6urM9Hv9E68f/Q/E/6obMaCUjQNznt4nJMmCGZEkLBiC0oQmy3c7r+wMkyE/KN0TMDYm5HksClhiI8FoIOB6nx8TcDDn3VvwFtz+ianppHsiW1l2yY1EdOwjQrrTD7+g4+wS0i+5jqVL8UBAVI9nRLpj9Xodudhp3Pfj7H7TLm2WBbZT32/4ZuhGRk3MB+PUp2r2is+06xQ3o2AxGfXD/Dq8L/tEIBNlDIqgJHgBB7zY0QTXmmiZ4AWnWRNDZjIYnSC9N4/WbEBiNQFB2E0G1AHQ+ljUoQd4B2tkFl0N4yu0QXtuwrO77pM8EYMDcRBACCKp0OcTDQNJqXq8x0USQDJdTxPk5JEodz5wNgDTDydqGIygqwARlY0MhqMhpyiQ5/ufoGgMNT5A6HVM7ROvH9cGlhNoK704gKAStXmhuu9phDmqP9yMUUSZua4tzhiCcklfdCF00G8sDQSFozWvdLnU5jHfx+iz8+FOzMDPttUFUgxNkyL6T1w8FDUUQnrWt6XyTH39qljoTJP1bcYPXCxt8CbLP5PVDQUMRhMcRC/OEebw+Cz/+1CxNBPmV2hO0MO4y6G4HHUz78admOXcIkoLW74HQUARBN7ud2ykGPbLvx5+apa4E6aX3FDd4vbAhTAS9gVPvOr20ShN534R41yvSO7w7gaB2sx3Gm5S7FwKB9QPC84kmDP7CI2+CqS3OGYIU0AU1PhEY4c2HCrUEOYWdnFZQXNUlowMfhnCERwGQ28AE6W2zeP3a4EwR5HaIlXirCVRvy3i9YDgPCco+KwmCEnTMnSeM5dVrwpkmSKe3vx8utwLinCDIIdbpQqTzjiDwUHN8vzYIJ0FQrW135wsSfgNBx8FyM7wpBao6ep9CKDgPCfJs7KsrwkkQAohZgoe68DYRF72NSsD3g0JGE0Ecwk0QAi9x8pxkE3J4vZpw5gmSPgiXWwFxthKU47lhayPIt3iXW5FT2AadhS94c8Fw/hEUY7uX168NwkkQVGe/KjeLQAn6C39X55sHuRzG731NBkYTQRzCSRAL3JPAq4WC848gg302q4fTKrxALg54BjOcBNEtwn7caBubPYQ3GwhngiBoC9UlGZ1B+rA+boWEQAS5ncJ76lFzTlj7LM5Xgsiy9OZQtU6DuB/CLr+iDunV0ARl0xsZsaQgEVC1YNe2jBXIQQFPEtSGoCg8/BREIHdu5O1ToafvtOZZUfyoD0GYBoW5JiOkw89s5jw7CIIeVKHTRE/R8Vj1uuVvvJqCWhHkRz9covhRV4JcBWISZMRKhpjjkDl/KFnS/coip2m4Yq7xCIJRe7HTZOXNIr58JvDlr+cLQUBISyDkNiBpb5HDZF813/K3IofwOOpBqVJfmdR5zsUGdave4Nqg+xX1NblCXwjoWgjot6yAGj3n6Q/nC0EscDyGd2m784Q8vOUR2yFFr8EJitRLD/D6PL5zCO14NQXnI0E8IJMWKN+NShBucWLNKVieE/hipfOFoMJXTPhOeI2AjszHNblVbwQiyO0QD2LDyIqnRyPsYu2zqCVBR4KJTm8/zdtHgUQ5wZvlRfGjrgQVFRg7uZzCzy6nuBLaoX9D3L/034treIIeVNQhMD4nmyGgHymBZNVZ1IagmhDViOOgFc8lXKx8AyH/9vbmBJ+j+I1AULZKkILlC+Pa0pMFmHuc4inIXbG8GQXnC0EI+k6FZ5kdiakochgTeTONTpArzzjTW7RrXig7Xwj6cbH+cqZKU0+0I1x5YpLyze4aYs2EFSxBMEp/CNXoTIJD2KIG0mm8A+tlKk5jwM2N5wtBCDlT/gqlB7vXHnEIDrc8s46AdrJxCEJgb82fQACV93g0OJ8IWrZMe5ETwu0wqVcVNDxBMZK6pFzyQne/D55DSJoF6mqfTwQV5prSoLZQp3VWO4RZbqfpv64CMUVRky/RqNGtesGHIIP0iKLuppOj4mmthGeytCY0JkGFTlMmxH+7ixmUY7W/Ii/haqhB9itqjUBQtkoQkuHtXvoKa5/F+UKQO1dM/2x+pwt5dURRvmdODhHVmAQBEZFYD/Oy4rlrLg70KhUEWOITIZQE8YfGJAjjB6XnFLQ397hzhQToHHXDttflGQuqe/QagSB7Dq/PAx8v4tUURMZmZ/CJEEqC+EM4CFJutgokvHkWEM+5fM0BUrUirzteUUYBYcTLmGp0q14IhaCS/O5dYJD6PlR71cGquGi9fRifCKEmCI9wEESvF/PjRqjhwVlsiPP7dMonT5iH62SsfoMTBAOvRxV1KM5di5zCpwopKBDQalAPeK5HF5OdzCcClyBBj46wCAdB8o2RGjeY8IQMXPYuchiH4etlilqjEYQ9FiBij0qMQ1i32mGmUx04BeLjAAO8kI9PBC5BGpSgqM62/rx9Ljw1Ap+SK3KKbm9aeCdLG40gBRCgS1xOI9bFnwNJNryKZb1DuJ41w0K+ZVGTEIq07iQFXC7nEQ6CImPtk3j7rPDmFWyFHhzOGkCcy9X2h+7PEN8ohMyqmGsEgmyP8fosICfNxLM6vLqC9obsNnwisILXX/J2AiEcBOnwblM/bijCm1ewJtdkxOpcJmaB+1kxUlnyZgG9uM9qcqve8CEo1q4ShEu9rDkFUOSv49UY0AtmAwm/7y4YwkEQmN/E22eE3qcaDFtft/wNenPjoOR8AkQtLX65hw5+f1T0G40g8K0ZlJavIXDvQKO4Gor6Aba7uWFZut9xEMJPQjCivdo4EMJE0F+8fUUgs5Ty5hW48npkQQn63p0vTGDVsYvtZiZLo/D+U9k91lxYER07rosa6Fi7WoxxDYQlhRV8nZh1gwW4U8Enhlekk7z5QAgTQRr7TFiCXsxU5DRN9DfnyE6iRjUEQbpO9PZ16km0QZqjqEMO+lqpzrCDoIwBcGS9PsiavU5v/z9tYniFNx8I9SUIr27m7bKi83NLvYLivPjOq53ifbhIt+Jd7+oqYuUiYzflG0j+vLbxqjXa6Id7I6KXvlXUgaBDhU5TWkle939gQFe91O1aKFWLgawTwdqhKL2tK58YrEBXXLNq6w/1JSjgzlRZdHHj2/J2FOBDwXiyHOJbxtce0B65FXPgxzbFPdZ+2KEGWk/fTaAodpoGr84XRpX42Sy/Kl8I+oA4nxg+CWOwn+LN+0N9COrYcfxFvD1eeDssCp3Cv5Yv91ZvOC78cXHPy4sc5lQg7S1FHdKrXHavxg5HvcAEXB0ls3Ut7qx0eyYLV2H3s5DbPMEDqrk/+QRhRRfCDff1ISiKvmyitev1376ct8MC4vkmDCd2LfezJsbOcqtu6qVjrJmwQw243n5aUYOiPNvl2Wql6SRALlJLmj/gwxd8ovByOYyZeHss6kqQ5xUWrT1WomPs1/L26gLGzYBb0cICHTNeUNSAHIGS4RAqgKwNQMrydbld6QsjUEeryxJ+Yc2hD1gEE7zfB18V4a0qqAtB0dH2S6O81Y5fwX11vL26ANswxs2Pef2wArrXBYpnihrdOJJrps/PQLV2B0gVyOsgnyBxXtv+wd4EFUx019s78XYRtSXoqrjsv8PAsZI3rxUpi7dbF0D7M0aNg0Eaz+uHFW3wSkvZM1Yd2yE61e7pvXwNcszzLQQc5HmR3hwSo1qbQFrR+Xk5K1SCrug4Ht8FUufEgotUpwsx/IE9/hgZmxXaW6l1RadOqRcqnnXsPl5tGIGMVz3VnGdvGM4wlBR494XVBF1n+x3aRAoo1ZAT50d3s0eh3ZoIgsROYM/nhCKeZ22CAwfo2MWu6fJacO+Q4i6vd0YQpc4AeKsAHKAWOY0+7zm4nMLHcikq37As7jJWzx/w2Ro+oUKUkEpfqKKLzfZ7II3FyrwenbE6h/i1dOcLdGIXp7VwbYw3q7qtt4elTasRkBt30IgYpLWKGk6Y0sA6hLchZ00tWWK9Uu7F0e44VHn0TaAa0Ayqg8N8gjWohHCsBoHzj8V5Is2gQMp4OSN2BdK+YxfqEIzbvi/cnylgDlM8ZdUhcPtd+SLd0AiBfZgG2mmkx/VxpM2aDYycCyAD/KxJuAYQ6FKH9CaSci5XEYj3sRUFcXTOkR4izjN+rZilvUXZ/baxto5eV84k6EuPHk/bG7JjFGUYlKqDSqjefsfA4/wUlJ61uF6v6IUCcPtlPgHPpLTtnB1woz+PFc95JoAhTo+xREEm3IVqMFhXnxKFUjPc44eEMwghrxLXG1CfHkSPoUpSX4+ny99O8X1cdsAAFzkE+vyZApyzY//XBHwSDfzYzSdmWEVvfzeilg+d4wxBkcPYe+Uiz+mNlQuFeIjzVk81J6oDeASkz07Zr02s+hkH3rioRJKNYElewtV0ktTpXaz6ySkagJxTcj1NH/CrDeikqt6+S5O4dZdqcO/Ta64Z4zP7HAqwM+RTvTmEI/BLB9E7llgvwkNcitk4pqaJign99vywQfEcz1+y6nTz/HK6eV694AKrOBwr0fX7PNHvADJU4FjCM0UkfQF+b9Phg7r0NmFlLCVVwf9ToH4Q9ZEMHCBigvFu1QYQ7iyIyxXK/yKnKVuJ36p8i2ZKCPwspeHR2/fweg0CmhNlkiKY+rXQITygEgMN6JrcRDpewZyG00GorjpyDkFdUnAIamfC08YK5RDnxazZKzqOuFItPbV4eyKsYGeCdfps+nitAtzZUphnUt93WJUriDi7jRFc7RAmKzcknksAgpYqcYDf3bjvANVx0c7NXWILafODv8zboMA6XM0lUJqUJ5wRhcwtGzCATVNK1Or87j1QDaq8Mzure4aAMyRA1HqmhphbtLhne/Yyj+vEW65Q00Uf+qXsZwTs+X/INQtZveJ8MYuul3jaoNPrCm6IRnU8NojVAmv2XAPUAENd8hUwLm5JBdKh2FuzSI+yeo2BC5hSpNlwCMTgFuBy3OCH/3HeCnt5ypzduYxlyyKaA0F//CAvrSDaX+97SoI132iAXJLPFOmdrF5RgXHYmsUmI37jiTOcYMRct0Ee7MF3ck2Leo0FyFwr/e3WYeFeJI5k/0NaHFfTIkays3qNiiimR9cmJrMvqwf19INKnS3Lerku/69cj7/Bmj9bACX9JIavcJHJzOv5A8Q9hyk9R3n9RkW03qauE+E4hB8EQkRbrszr/g+8pgu/6TRJvogXLhHcx405FRJkF4zQM1h7jQkIz3S8pBbDuCa32w28Pgtca2IzKe495800OnSe1+flxtH+O6+P++WKYZAKJWcORL5ALj0u1FuWE9dKKWHsLERDAU/KwdAAt4r9BhnnVQwrhsnlNE7BM6iesPmOdRg08wyU5bgb7G/yBs4OWK24v0BdSo7WSz5jo59yu0VBROmavEteDnfL18hA5JdTwhzCQNzPAL9fsnbPJAqdPXpCid6J39A7WyCHC0sOLp98BWF52SUfscEOTnGepTtrHzLmCiZj4ppP44x7QkE7g83nIFR0l3F9WP11BfHR8pkivCGeTizifTdy5Ok6yuql5jb4n7UXbihvC+HcIfhVRasx+QJCJEUOz5sg7TDToDr8rlvxnPdYIwK61FPY+EZdm0mHEmc1oIg/ywS6Ovr6TJ8NjRD5SJoAeeIA+t8hbMb/yg2FhQ5hKf7fOj/V5/T0aoex9/Il2v1ntQGu1+CvS94rgZ2VFQXGTjQ8TnErVfM8UFiN7Q/+h/Asx2ECf5o7MkYay5KDm0NY/bMa0FFwsYFvo89sz+pD6XkXV2FxBC7n1hJUpxOqclvEmkeUeE4M4KD3XSBzMKrhW3VKovNQrodGM4VO40TICD+55DcdZHfUi8+hiqXtjLKXHL7fUcKAjxX+uMDoE/52BknwKTl6yWeq55xAlN5m84kEt0tTXiZ3uuWzrCuh+sOBrUyYZlkCEvFu1GNuGn7clS+OwG+8Gwgbc6w6sYF3ydUWNPL0kicore+hG8rtH+DP19Qes+tIWRKRq9y/swQyaAZkbGDjFQlk8YbOGUBkZnA5bSNvBslwOYViTBw54SfzZhCgvkk283f5974ip3gvftO7gRzC8/jteeTW06jL9tQT50W5guhRE9/FCVvZHdqThCo0kf53CD+CnVWaOx7S05vDQPwYG5+2dXyZ+KxClMF2CxupQAeicOqEV2OBnQo6deQU9+EvtgmQkLkMEX8C0VVYTRblC6sUdWzb8Bv3jeMT0qjmzhNdQMQucGuNJ1OI9EQfqJVhG7gs3Tcs0dfZo6CNwRsc1XhEx9l9BuTnNPw0qOpSeaiQE/JtGMyaFDIhMT/05Hq8llNcqZh1yZO0ygk/N90jIRz4WF79hKpxEf5iJwFIlVd7xYcKX9Yel0nHksPWAiCt46Q43tw5D7oSapCqvCTZT7c3ZKibToIBD4N5ElG40UfdIRQqpQN/lWl/SGy8np/g2Av/r6FnljxVoUdfmIUzGLLZ2ewREhZ4mJndJoxhDnZe6JxHdDfchiQd5XLkF7jdijerwI1TQ/SQlDeBGb0/ILFPeEqCWA0l6j+oDp0Ci0yoehUAax9K04dIoqKnBd3U7/Yt9drZkfMVzaAdKvMlSaqKjLVN5w2ywF7f8oXeHapuubOA5OF/IOMQruTiN57sQz188FYxD93l+cp3METps5/mMhBu0qQ37f8vAUnys19aqtLF4utegUsUDyAikj5wsRg6A/nCBCBqIFSJQ5XZgpBAj8FIz2jDQ9vL53nj/zPAvW+QO/fxiSLvzHmjdedxPlMr4Ubrztmx0MZ8GeV/f/emYOeS/qcQbbAN1VZ7stCDVlLuZTFZkbUpWX5htbaAgWW7aL39rQCk4DDgL13n8XTvRBM4YK8Jx0l8ovkkoN6+Uxdjn63TZw/Sdcm4PjBpy5rjNWN49RleGxAwA3iJ2XHGz++cL6DbfvGm3JBOwtVdcINjpF5aegVz1qkJtYTnjKf0SqA3Gmov0lFdrO2FUA5pNaEO0OmzBkHJWgRt0xaolvZ7pmC8A2AqUPJwAwftgOjtG7CHdi5WX/8PWKdOv1UPct4AAAAASUVORK5CYII=>
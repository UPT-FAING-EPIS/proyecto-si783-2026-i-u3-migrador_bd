# Resultados de Pruebas Automatizadas

Se ejecutaron de manera local los entornos de pruebas implementados (Unitarias, Integración, BDD, e Interfaz UI).

## 1. Pruebas Unitarias, Integración y UI (Pytest)

Las pruebas unitarias y de integración se corrieron utilizando `pytest` en la carpeta `tests/`. En este reporte, también se ha contemplado la prueba de UI interactiva de `Playwright` (`test_ui.py`).

**Resultado (Exitoso):**
```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-8.4.2, pluggy-1.6.0
plugins: anyio-4.13.0, base-url-2.1.0, cov-6.1.1, html-4.2.0, metadata-3.1.1, playwright-0.8.0
collected 37 items

tests\test_cargador.py .....................                             [ 56%]
tests\test_detector.py .............                                     [ 91%]
tests\test_integration_db.py ..                                          [ 97%]
tests\test_ui.py .                                                       [100%]

============================= 37 passed in 14.52s =============================
```
✅ **Total de pruebas aprobadas:** 37
❌ **Fallos:** 0

## 2. Pruebas BDD / Comportamiento (Behave)

Las pruebas escritas en formato *Gherkin* en el directorio `features/` pasaron correctamente verificando los tres escenarios solicitados:
1. Detección de código de MySQL.
2. Detección de exportaciones de MongoDB.
3. Inicialización del motor cargador de Snowflake.

**Resultado (Exitoso):**
```text
Feature: Detección y Carga de Motores de Base de Datos 
  Como usuario del migrador
  Quiero que la aplicación reconozca el motor de la base de datos SQL de origen y configure correctamente el cargador de destino
  Para poder realizar migraciones exitosas sin errores de compatibilidad

  Scenario: Detección de base de datos MySQL              
    Given un archivo SQL con sintaxis "MySQL"             
    When ejecuto el detector de base de datos             
    Then el detector debe reconocer el motor como "MySQL" 

  Scenario: Detección de base de datos MongoDB              
    Given un archivo JSON exportado de MongoDB              
    When ejecuto el detector de base de datos en el archivo 
    Then el detector debe reconocer el motor como "MongoDB" 

  Scenario: Inicialización del cargador de Snowflake            
    Given que quiero migrar hacia el motor "Snowflake"          
    When inicializo el cargador destino                         
    Then el cargador destino debe configurarse para "Snowflake" 

1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped
```

## Pruebas de Mutación (Mutmut) y Seguridad (Sonar/Snyk)
Para las pruebas de **Mutaciones**, estas correrán a nivel del servidor (vía **GitHub Actions** al subir el código) debido al tiempo exhaustivo que tardan en correrse sobre los cientos de líneas de código (Modifican el código temporalmente hasta en 400 variantes y corren Pytest cada vez). 

Asimismo, los análisis de calidad del código como `SonarCloud`, `Semgrep` y `Snyk` se ejecutarán automáticamente en la pestaña de `Actions` de tu repositorio GitHub.

*Generado: 04 de Julio de 2026.*

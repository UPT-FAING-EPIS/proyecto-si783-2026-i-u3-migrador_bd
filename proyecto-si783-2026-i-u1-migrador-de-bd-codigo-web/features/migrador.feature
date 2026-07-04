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

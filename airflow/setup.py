from setuptools import setup, find_packages

setup(
    name='migradordb-airflow',
    version='1.0.0',
    description='Apache Airflow Operator for Migrador DB Enterprise. Un sistema de migración de base de datos es el proceso de transferir datos, esquemas y configuraciones desde un entorno de almacenamiento de origen a uno de destino. Esto se realiza para modernizar infraestructura, adoptar soluciones en la nube, cambiar de motor tecnológico o consolidar centros de datos.',
    author='MigradorDB Team',
    packages=find_packages(),
    install_requires=[
        'apache-airflow>=2.0.0',
        'requests>=2.25.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Apache Airflow',
    ],
    python_requires='>=3.7',
)

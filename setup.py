import sys
from cx_Freeze import setup, Executable

# Dependencias del programa
build_exe_options = {
    "packages": ["arcade", "math", "random"],
    "include_files": ["game_object.py", "img"]
}

# Configuración del ejecutable
setup(
    name="Asteroids versión Noah",
    version="1.0",
    description="Versión de Noah sobre Asteroids, el objetvo del jeugo es ver cuantos puntos logras obtener antes de morir",
    options={"build_exe": build_exe_options},
    executables=[Executable("mainAsteroids.py", base=None)]
)

import os.path
from setuptools import Extension, setup


try:
    from Cython.Build import cythonize

except ImportError:
    FILE_EXTENSION = "c"

else:
    FILE_EXTENSION = "pyx"


EXTENSIONS = [
    Extension(
        "genesis.simulation.fast", [
            os.path.join("genesis", "simulation", f"fast.{FILE_EXTENSION}"),
            os.path.join("genesis", "simulation", "c_simulation.c"),
        ]
    )
]


if FILE_EXTENSION == "pyx":
    EXTENSIONS = cythonize(EXTENSIONS)


setup(ext_modules=EXTENSIONS)

from setuptools import Extension, setup


try:
    from Cython.Build import cythonize

except ImportError:
    FILE_EXTENSION = "c"

else:
    FILE_EXTENSION = "pyx"


extensions = [
    Extension(
        "fast", [f"simulation\\fast.{FILE_EXTENSION}", "simulation\\c_simulation.c"]
    )
]


if FILE_EXTENSION == "pyx":
    extensions = cythonize(extensions)


setup(ext_modules=extensions)

from setuptools import Extension, setup


try:
    from Cython.Build import cythonize

except ImportError:
    FILE_EXTENSION = "c"

else:
    FILE_EXTENSION = "pyx"


extensions = [
    Extension(
        "genesis.simulation.fast", [
            f"genesis\\simulation\\fast.{FILE_EXTENSION}",
            "genesis\\simulation\\c_simulation.c",
        ]
    )
]


if FILE_EXTENSION == "pyx":
    extensions = cythonize(extensions)


setup(ext_modules=extensions)

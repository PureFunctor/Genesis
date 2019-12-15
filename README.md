# Genesis
A small app written in Python (and some C), that attempts to find the mean amount of rolls it would take in order to obtain every PUR card in every Sound Voltex Generator -Real Model- card set.

# Usage
The simulation algorithm has implementations in both Python and C; the latter is wrapped in Cython in order to be used as a C extension.

**In order to use the faster implementation written in C:**
```sh
# Navigate to genesis
cd genesis

# Build the extension
python setup.py build_ext -b simulation

# Run the application
python genesis.py
```
*If the extension isn't built, the application would instead use the slower implementation written in Python.*

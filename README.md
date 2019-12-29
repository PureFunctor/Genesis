# Genesis
A small app written in Python (and some C), that attempts to find the mean amount of rolls it would take in order to obtain every PUR card and every card in each Sound Voltex Generator -Real Model- card set. Additionaly, the mean amount of duplicate cards aggregated from the fulfillment of one of the two conditions is also computed.

# Usage
The simulation algorithm has implementations in both Python and C; the latter is wrapped in Cython in order to be used as a C extension.

**In order to use the faster implementation written in C:**
```sh
# Build the extension
python setup.py build_ext --inplace

# Navigate to genesis
cd genesis

# Run the application
python genesis.py
```
*If the extension isn't built, the application would instead use the slower implementation written in Python.*

# Genesis
A small app written in Python (and some C), that attempts to find the mean amount of rolls it would take in order to obtain every PUR card and every card in each Sound Voltex Generator -Real Model- card set. Additionaly, the mean amount of duplicate cards aggregated from the fulfillment of one of the two conditions is also computed.

# Usage
The simulation algorithm has implementations in both Python and C, with the latter being wrapped in Cython to be used as a C extension. You can skip building the C extension, as the application falls back to the Python implementation.

```sh
# Build the extension
> python setup.py build_ext --inplace

# Run the application
> cd genesis
> python genesis.py
```

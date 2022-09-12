# Installation 
Since the package is still far from being properly developed, is is not available via `pip`. Just clone the repo to your local machine and add the path to the folder to your `$PATH` variable:

``` 
git clone https://github.com/krasser-millionaer/makeinp.git
echo "export PATH=$PATH:$(pwd)/makeinp" >> ~/.bashrc
source ~/.bashrc
```


# General functions of the makeinp module

## Extracting geometry from files
The current version of the module supports the following structure formats:
* XMOL-formatted `xyz` (any number of consecutive structures)    
* Any single-job orca file, including single point calculations, optimizations etc.

## Simple inputs 
`makeinp.py` takes the file with the geometry as a required positional argument. To make simple input from 
Disclaimer: ifm's support team provides code examples and helper scripts with the idea of accelerating the development process for customers.
We do not guarantee that these scripts will be updated to reflect the lifecycle of ifm's various software packages.

# How to run `start_algodebug.py`
The python script `start_algodebug` is designed to be run on CLI level. It provides a further layer of simplification around the `ifmO3r` python packages functions.  

## run without argumemts
To run the script:  
This will start the data recording. All data (imager at port 2) will be recorded until the user terminates the thread via `CRTL + C`
```
python start_algodebug.py
```

## run with user defined arguments
Alternatively one can run the script with user defined parameters via the argument parsing implementation of `start_algodebug`, e.g.:  
This example will start a algo debug recording with a length of 60 seconds for two heads connected to the physical ports 2, and 3.
```
python start_algodebug.py --numSeconds 60 --portIndices 2 3
```

This example command will start a algo debug recording with a length of 10 seconds for one head connected to the physical ports 2 after configuring it with the supplied `json` configuration file.
```
python  start_algodebug.py --numSeconds 10 --portIndices 2 --conf="config.json"
```
## check all possible available arguments at CLI level
```
python start_algodebug.py --help 
```
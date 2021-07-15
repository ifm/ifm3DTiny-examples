Disclaimer: ifm's support team provides code examples and helper scripts with the idea of accelerating the development process for customers.
We do not guarantee that these scripts will be updated to reflect the lifecycle of ifm's various software packages.

# How to save a data stream with the helper script `save_data_stream.py`

## requirements
Required python packages:
+ `ifmO3r`
+ (all dependent packages of the `ifmO3r` package)
+ Python `version >= 3.8` 

## run save_data_stream
The `save_data_stream.py` python script is used as a helper tool when recording data for a predifined number of seconds. This script can be used to record algo debug data or normal data streams.
For further flexibility see the functions `save_data_stream()` and `save_algo_debug_data()` as part of the `ImageLogger` class, along with the tutorial on [ifm3d.com](https://ifm3d.com).

**Typical use:**  
Start the script via:
```
python save_data_stream.py
```

To see all available argument parsing parameters:
```
python save_data_stream.py --help

usage: save_data_stream.py [-h] [--type {normal,debug}] [--ip IP]
                           [--timeout TIMEOUT] [--numSeconds NUMSECONDS]
                           [--loglevel {DEBUG,INFO,WARNING,ERROR}]
                           [--filename FILENAME]
                           [--portIndices [PORTINDICES [PORTINDICES ...]]]
                           [--conf CONF]

optional arguments:
  -h, --help            show this help message and exit
  --type {normal,debug}
                        The type of data to save (normal data stream or
                        algo-debug data)
  --ip IP               ip address of VPU
  --timeout TIMEOUT     timeout to be used in the get function
  --numSeconds NUMSECONDS
                        number of seconds to be recorded
  --loglevel {DEBUG,INFO,WARNING,ERROR}
  --filename FILENAME   target filename. If not given, a file will be
                        created in the current directory.
  --portIndices [PORTINDICES [PORTINDICES ...]]
                        VPU ports to be recorded
  --conf CONF           head configuration via json file, default is
                        config.json in the cwd


## Cheatsheet: required python setup to run this script
1. activate your python environment  
    cmd: `o3r-venv\Scripts\activate`  
    powershell: `.\o3r-venv\Scripts\activate`
2. navigate to folder where the python script `start_save_datastream.py` exists
3. run the script from CLI level: see [run start-save_datastream](#run-start_save_datastream)
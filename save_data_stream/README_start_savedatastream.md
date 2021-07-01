Disclaimer: ifm's support team provides code examples and helper scripts with the idea of accelerating the development process for customers.
We do not guarantee that these scripts will be updated to reflect the lifecycle of ifm's various software packages.

# How to save a data stream with the helper script `start_save_datastream.py`

## requirements
Required python packages:
+ `ifmO3r`
+ (all dependent packages of the `ifmO3r` package)
+ Python `version >= 3.8` 

## run start_save_datastream
The `start_save_datastream.py` python script is used as a helper tool when recording continous data sets with a predefined format, length, and VPU - Head combination.
For further flexibility see the function and it's arguments `save_data_stream()` as part of the `ImageLogger` class.

**Typical use:**  
Start the script via:
```
python start_save_datastream.py
```

To see all available argument parsing parameters:
```
python start_save_datastream.py --help

usage: start_save_datastream.py [-h] [--ip IP] [--timeout TIMEOUT] [--numSeconds NUMSECONDS]
                                [--loglevel {DEBUG,INFO,WARNING,ERROR}] [--filename FILENAME]
                                [--portIndices [PORTINDICES [PORTINDICES ...]]] [--conf CONF]

optional arguments:
  -h, --help            show this help message and exit
  --ip IP               ip address of VPU
  --timeout TIMEOUT     timeout to be used in the get function
  --numSeconds NUMSECONDS
                        number of seconds to be recorded
  --loglevel {DEBUG,INFO,WARNING,ERROR}
  --filename FILENAME   target filename. If not given, a file will be created in the current directory.
  --portIndices [PORTINDICES [PORTINDICES ...]]
                        VPU ports to be recorded.
  --conf CONF           head configuration via json file, default is config.json in the cwd
```


## required python setup to run this script
1. activate your python environment  
    cmd: `o3r-venv\Scripts\activate`  
    powershell: `.\o3r-venv\Scripts\activate`
2. navigate to folder where the python script `start_save_datastream.py` exists
3. run the script from CLI level: see [run start-save_datastream](#run-start_save_datastream)
# ThreadTheNeedle
Developing tools for performance debugging in Linux based operating systems. 
The tool built can be run by executing the python script `demo1.py`

### Requirements
For `demo1.py` to run, only the following columns/fields must be enabled in the `top` command: 
* `PID` 
* `USER` 
* `S` 
* `TIME+` 
* `P`

#### To enable/disable columns, do the following:
* Run the `top` command
* While it's running, press `f`
* Select/unselect columns by pressing `d`
* Once done selecting/unselecting press `q`
* To save the changes, press `shift + w`

### How to run the tool
Run `python3 demo1.py` and enter the PID for the process for which performance debugging is to be done.  
Enter a refresh rate (in seconds), this is the rate at which information will be refreshed in `top` 
For example, refresh rate of `0.01` implies that information is updated every `0.01 seconds` in `top`

### TODO
- [ ] Give visuals for all threads of a process
- [ ] Write a shell script to automate editing the configuration of `top`
- [ ] Figure out how to get more granularity in data collected
- [ ] Try and use SystemTap for collecting data

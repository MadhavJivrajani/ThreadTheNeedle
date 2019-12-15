# ThreadTheNeedle
Building performance debugging tools to detect frequency of core migrations and dTLB/iTLB misses per thread of a given process in real time as a mini-project under Centre for Cloud Computing and Big Data at PES University.  
 
`tool1` is used to detect `dTLB/iTLB misses` in real time for any thread ID of a running process.  
`tool2` is used to detect the number of `core migrations` in real time for any given thread ID of a running process. 

### Requirements
Dependencies:  
* `top`
* `perf`  

#### For `tool1` or `tool2` to run, only the following columns/fields must be enabled in the `top` command: 
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


#### To install `perf`:   
`sudo apt install linux-tools-$(uname -r) linux-tools-generic`    


### How to run the tools  
The method specified below works for `tool1` and `tool2`:     
* Open the tool1 / tool2 folder.     
* Run the following command : `sudo python3 server.py`    
*  Vist `127.0.0.1:3000` in the browser    
* Now enter the PID in the corresponding field     
* Now click the Update threads and select the thread to be analyzed.    
* Click start thread button and wait for around 5 seconds for the dynamic graph to be displayed.    
* To end the process, click on End Thread.     
     
### TODO   
- [ ] Give visuals for all threads of a process  
- [ ] Write a shell script to automate editing the configuration of `top`
- [ ] Figure out how to get more granularity in data collected
- [ ] Try and use SystemTap for collecting data

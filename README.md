# IP
A simple script to look up and save machine ip address.


## Disclaimer
This code is posted for informational purposes only. Use this code at your own risk.

If you find any bug in running the code, free feel to contact me at gaochi0500@gmail.com. I will make effect to fix it, but I cannot guarantee the fix in time. 

## Code Purpose

A simple script to look up and save machine ip address.


## Installation and Usage

### Useage
```python
cgao$ python ip.py 
```
### Output
A file 'myIP.txt' will be saved in current directory.


## Suggestions

You can use crontab to make this script running in the backgroud at a preferred frequency (like 10 minutes).

You'd better change the saved filename with absolute path, otherwise it will be saved in the execution path, not the executed file's path.

For example, if you run the code like:
```python
cgao$ pwd
/Users/cgao
cgao$ python ~/github/IP/ip.py 
```

## License

Copyright (c) 2013-2015 Chi Gao. See the LICENSE file for license rights and limitations (MIT).

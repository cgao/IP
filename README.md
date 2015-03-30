# IP
A simple script to look up and save machine ip addres

### Useage
```python
cgao$ python ip.py 
```
### Output
A file 'myIP.txt' will be saved in current directory.


### Suggestions
You can use crontab to make this script running in the backgroud at a preferred frequency (like 10 minutes).

You'd better change the saved filename with absolute path, otherwise it will be saved in the execution path, not the executed file's path.

For example, if you run the code like:
```python
cgao$ pwd
/Users/cgao
cgao$ python ~/github/IP/ip.py 
```

'myIP.txt' will be saved in /Users/cgao/, instead of /Users/cgao/github/IP/

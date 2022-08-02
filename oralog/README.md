### Search text in oracle alert log

##### Configuration:

includeWords - include these words  
excludeWords - exclude these words  
sourceLog - path to alert log  
saveState - "True" will save last event timestamp, next run will begin from this timestamp

##### Usage:
```
$ python oralog.py
$ python oralog.py > out.txt
```

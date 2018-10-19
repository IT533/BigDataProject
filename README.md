# BigDataProject
create virtual environment
```
python3 -m venv venv
```
active virtual environment
```
source venv/bin/activate
```
deactivate virtual environment
```
deactivate
```

run command
```
python3 src/example.py input/README.rst > output/counts
```

merge input files
```
python3 src/mergefile.py
```

jupyter notebook
```
jupyter notebook BigDataProject.ipynb
```

# To be analyzed
### Parameters
vID, uper, category, days, len, views, rates, comments, relatedID

### Paterns
Counts,<br>
Max Min,<br>
Inverted index,<br>
Filter, Grep,<br>
Top 10 Video: views, cate, uper<br>

## Linear Regression with MapReduce
Assumption: Our model is linear

Attributes: length, views, rate, ratings, comments

Predict: category (Music, Entertainment)

### Steps
* Data Scrubbing

    clearning data

    split data (training data, testing data)

* Model Training (MapReduce)

    linear regression with MapReduce

* Model testing


# Tools for Data
Python Interactive Console(python3, ~~python2~~)
```
python3
```

import tools
```
from tools import datascrub
```
tutorial for tools usage
```
help(datascrub)
```


# Python MapReduce Running on hadoop
## Implement MapReduce
source: [https://wiki.apache.org/hadoop/](https://wiki.apache.org/hadoop/)

* Hadoop Streaming

	[MRJob](https://pythonhosted.org/mrjob/)

	```
	python mrjob/examples/mr_word_freq_count.py README.rst -r hadoop > counts
	```

* Hadoop Pips

	pyinstaller, ~~py2bin~~

	To upload the binary files to HDFS, the command syntax is:

	```
	bin/hadoop fs -put build/c++-examples/Linux-i386-32/bin /examples/bin
	```

	run

	```
	bin/hadoop pipes -conf src/examples/pipes/conf/word.xml -input in-dir -output out-dir
	```

* Java MapReduce

	[Jython](http://www.jython.org/Project/index.html)

	```
	bin/hadoop jar src/examples/python/wc.jar in-dir out-dir
	```

## Hadoop Streaming
Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.

command on python3
```
python3 example.py README.rst -r hadoop > counts
```
is equivalent to
```
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar
    -files hdfs:///user/cloudera/tmp/mrjob/example.cloudera.20181014.220550.321660/files/example.py#example.py,hdfs:///user/cloudera/tmp/mrjob/example.cloudera.20181014.220550.321660/files/mrjob.zip#mrjob.zip,hdfs:///user/cloudera/tmp/mrjob/example.cloudera.20181014.220550.321660/files/setup-wrapper.sh#setup-wrapper.sh
    -input hdfs:///user/cloudera/tmp/mrjob/example.cloudera.20181014.220550.321660/files/README.rst
    -output hdfs:///user/cloudera/tmp/mrjob/example.cloudera.20181014.220550.321660/output
    -mapper sh -ex setup-wrapper.sh python3 example.py --step-num=0 --mapper
    -combiner sh -ex setup-wrapper.sh python3 example.py --step-num=0 --combiner
    -reducer sh -ex setup-wrapper.sh python3 example.py --step-num=0 --reducer
```
| Parameter                                   | Optional/Required   |
| -------------------------------------:      | ------------------: |
| -file filename                              | Optional            |
| -input directoryname or filename            | Required            |
| -output directoryname                       | Required            |
| -combiner streamingCommand or JavaClassName | Optional            |
| -mapper executable or JavaClassName         | Required            |
| -reducer executable or JavaClassName        | Required            |

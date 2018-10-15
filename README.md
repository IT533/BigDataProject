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

Attributes: category, length, views, rate, ratings, comments

Predict: Age

### Steps
* Data Scrubbing

    clearning data

    split data (training data, testing data)

* Model Training (MapReduce)

    linear regression with MapReduce

* Model testing



# Python MapReduce Running on hadoop
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

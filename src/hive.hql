# Create hive database
CREATE DATABASE youtube;

USE youtube;


# Create a table to store data
CREATE TABLE page_video
(   video_id STRING,
    uploader STRING,
    age INT,
    category STRING,
    length INT,
    views INT,
    rate FLOAT,
    ratings INT,
    comments INT,
    related_IDs STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;


# Load data onto table
LOAD DATA LOCAL INPATH '/home/cloudera/Desktop/allfile.txt.new'
OVERWRITE INTO TABLE page_video;


# users Top 10
SELECT video_id, views
FROM page_video
ORDER BY views DESC
LIMIT 10;


# category number
SELECT category, COUNT(video_id)
FROM page_video
GROUP BY category;


# ave
SELECT AVG(length) AS length_ave, AVG(views) AS views_ave, AVG(rate) as rate_ave, AVG(ratings) AS ratings_ave, AVG(comments) AS comments_ave
FROM page_video;

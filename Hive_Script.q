CREATE EXTERNAL TABLE IF NOT EXISTS group_data (
  Article STRING,
  Dates STRING,
  Views STRING,
  Total_Views INT,
  Popularity INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
LOCATION 's3://kaioutput/finalout/';

INSERT OVERWRITE DIRECTORY '${OUTPUT}/top100views' SELECT Article, Total_Views FROM group_data ORDER BY Total_Views DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/top100popularity' SELECT Article, Popularity FROM group_data ORDER BY Popularity DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/computer' SELECT * FROM group_data WHERE Article RLIKE '.*(computer).*' ORDER BY Total_Views DESC;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/star' SELECT * FROM group_data WHERE Article RLIKE '.*(star).*' ORDER BY Total_Views DESC;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/virus' SELECT * FROM group_data WHERE Article RLIKE '.*(virus).*' ORDER BY Total_Views DESC;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/dog' SELECT * FROM group_data WHERE Article RLIKE '.*(dog).*' ORDER BY Total_Views DESC;

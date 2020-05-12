# MapReduce Application
## Introduction
This project is to analyze the popularity of Wikipedia articles. It ranks English Wikipediapages according to total page views and popularity trend. AWS Elastic MapReduce platform with Hadoop streaming is the favorable platform to run this program.
## Details
The first pair of MapReduce would read the data from standard input and aggregate the transformed data by date and article name. Each line of the output should look like:
<pre><code>Modern_art}20160601 50</code></pre>
Where 'Modern_artis' the article title, '}' is a separator, '20160601' is the date, and '50' is the number of page views. It'll exclude all articles that are not wriiten in English and whose title starts with Media, Special, Talk, User, User_talk, Project, Project_talk, File, File_talk, MediaWiki, MediaWiki_talk, Template, Template_talk, Help, Help_talk, Category, Category_talk, Portal, Wikipedia, or Wikipedia_talk.<br>
<br>
The second MapReduce would read the output from the first pair and exclude any article that has less than 10 total page views from the results. Each line of the output should look like:
<pre><code>Modern_art\t[20160601,20160604]\t[50,75]\t125\t25</code></pre>
In this example, Modern_artis the article name. The dates in the first set of brackets aredates when the corresponding page was accessed. The dates in the second set of brackets arethe page views for each date. The next number is the total sum of page views. The finalnumber is the article’s popularity trend, which is calculated as the sum of page views during days 3-5 of the month minus the sum of page views during days 1-2 of the month. 
## Instruction
### Create an AWS EMR for streaming program using AWS CLI
Example:
<pre><code>aws emr create-cluster \
	--applications Name=Hadoop Name=Hive \
	--steps Type=STREAMING,Name='Streaming Program',ActionOnFailure=CONTINUE,Args=[-files,s3://elasticmapreduce/samples/mapper.py,-mapper,reducer.py,-reducer,aggregate,-input,s3://elasticmapreduce/samples/wiki/input,-output,s3://mybucket/wiki/output] \
    --release-label emr-5.29.0 \
    --use-default-roles \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge \
    --auto-terminate</code></pre>
The second pair of MapReduce only need one master node.
### Create an AWS EMR with Hive steps
Example:
<pre><code>aws emr create-cluster \
    --steps Type=HIVE,Name='Hive program',ActionOnFailure=CONTINUE,ActionOnFailure=TERMINATE_CLUSTER,Args=[-f,s3://elasticmapreduce/samples/hive-script.q,-d,INPUT=s3://elasticmapreduce/samples/hive-ads/input,-d,OUTPUT=s3://mybucket/hive-ads/output,-d,LIBS=s3://elasticmapreduce/samples/hive-ads/output] \
    --applications Name=Hive \
    --release-label emr-5.29.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge </code></pre>

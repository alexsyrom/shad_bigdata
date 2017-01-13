ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

CREATE TABLE parsed_text_log (
	    ip STRING,
	    date TIMESTAMP,
	    url STRING,
	    status SMALLINT,
	    referer STRING,
	    user_agent string
)
STORED AS TEXTFILE;

INSERT OVERWRITE TABLE parsed_text_log
SELECT 
    ip,
    from_unixtime(unix_timestamp(date ,'dd/MMM/yyyy:HH:mm:ss')),
    url,
    CAST(status AS smallint),
    referer,
    user_agent
FROM access_log
WHERE day='2016-12-01';

create table successful_log as
select * from parsed_text_log
where status=200;

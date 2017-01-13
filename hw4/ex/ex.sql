ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

INSERT OVERWRITE TABLE parsed_text_log
SELECT 
    ip,
    from_unixtime(unix_timestamp(date ,'dd/MMM/yyyy:HH:mm:ss')),
    CAST(status AS smallint),
    url,
    referer
FROM access_log
WHERE day='2016-12-01';

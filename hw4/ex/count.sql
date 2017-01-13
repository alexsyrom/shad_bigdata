ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

SELECT count(distinct ip), count(1)
FROM access_log
WHERE day='2016-12-01' AND status='200';

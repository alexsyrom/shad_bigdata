ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

SELECT lpad(hour(date_ts), 2, '0') AS h, count(1) AS hits
FROM successful_log
GROUP BY hour(date_ts)
ORDER BY hits DESC, h ASC
LIMIT 10;

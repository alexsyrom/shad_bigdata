ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

select * from successful_log
order by ip ASC, date ASC
limit 1;

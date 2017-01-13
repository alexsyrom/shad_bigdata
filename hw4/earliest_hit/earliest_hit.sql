ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

select ip, from_unixtime(unix_timestamp(date_ts), 'dd/MMM/yyyy:HH:mm:ss'), url, status, referer, user_agent from (select * from successful_log
order by ip ASC, date_ts ASC
limit 1) answer_table;

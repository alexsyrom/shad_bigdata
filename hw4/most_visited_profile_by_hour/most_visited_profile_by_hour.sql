ADD JAR /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hive/lib/hive-contrib.jar;

use asyromyatnikov;

drop table if exists user_hit; 

create table user_hit (
	hit_hour smallint,
	username string,
	counter bigint
);

insert overwrite table user_hit
select 
	hour(date_ts),
	regexp_extract(url, '^/(id\\d+)', 1),
	count(1)
from successful_log
group by hour(date_ts), regexp_extract(url, '^/(id\\d+)', 1);

select lpad(hit_hour, 2, '0') as h, username as u from
(select *, row_number() over (partition by hit_hour order by counter desc, username asc) as rn
from user_hit where username!='') t 
where rn=1
order by h asc;


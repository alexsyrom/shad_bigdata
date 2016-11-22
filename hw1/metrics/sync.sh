#!/usr/bin/env bash
rsync -avzh ~/hdfs/hw1/metrics/users_by_country/results ~/src/shad_bigdata/hw1/metrics/users_by_country/ 
rsync -avzh ~/hdfs/hw1/metrics/total_users/results ~/src/shad_bigdata/hw1/metrics/total_users/ 
rsync -avzh ~/hdfs/hw1/metrics/average_session_time/results ~/src/shad_bigdata/hw1/metrics/average_session_time/ 

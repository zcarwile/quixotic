create view events_by_hour as 
select count(id) as event_count,
tags,
DATE_ADD(DATE_FORMAT(start, "%Y-%m-%d %H:00:00"),INTERVAL IF(MINUTE(start) < 30, 0, 1) HOUR) AS event_hour 
from event 
group by event_hour, tags
order by event_hour asc;

create view events_by_day as 
select count(id) as event_count,
tags, 
DATE_FORMAT(start, "%Y-%m-%d") AS event_day 
from event 
group by event_day, tags 
order by event_day asc;

create view events_by_hour2 as
select count(id) as event_count,
tags,
STR_TO_DATE(DATE_ADD(DATE_FORMAT(start, "%Y-%m-%d %H:00:00"),INTERVAL IF(MINUTE(start) < 30, 0, 1) HOUR), "%Y-%m-%d %H:00:00") AS event_hour
from event
group by event_hour, tags
order by event_hour asc;

create view events_by_day2 as
select count(id) as event_count,
tags,
STR_TO_DATE(DATE_FORMAT(start, "%Y-%m-%d"),"%Y-%m-%d") AS event_day
from event
group by event_day, tags
order by event_day asc;

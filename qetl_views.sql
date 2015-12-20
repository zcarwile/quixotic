create view events_by_hour as select count(id) as event_count, DATE_ADD(DATE_FORMAT(start, "%Y-%m-%d %H:00:00"),INTERVAL IF(MINUTE(start) < 30, 0, 1) HOUR) AS event_hour from event group by event_hour order by event_hour asc ;

create view events_by_day as select count(id) as event_count, DATE_FORMAT(start, "%Y-%m-%d") AS event_day from event group by event_day order by event_day asc;

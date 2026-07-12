create database Traffic_Crash_Analysis;

use traffic_crash_analysis;

select * from crash_data;

##1

select distinct(weather_condition) from crash_data;

select weather_condition, crash_type, count(*) as total_crashes from crash_data 
group by weather_condition, crash_type order by total_crashes desc limit 5;

##2

select street_name,count(*) as Injuries from crash_data where crash_type like "Injury%" group by street_name order by injuries desc limit 10; 

##3

select crash_type, round((sum(injuries_total)/count(*))*100,2) as percentage from crash_data group by crash_type having crash_type like "INJURY%";

##4
select crash_month, crash_hour, total_crashes from(
select crash_month, crash_hour, count(*) as total_crashes , 
dense_rank() over(partition by crash_month order by count(*) desc) as ranked from crash_data
group by crash_month, crash_hour)as tab
where ranked=1;

##5

select prim_contributory_cause,count(*) as total_crash from crash_data where crash_hour>=18 group by prim_contributory_cause order by total_crash desc limit 5;

##6

select distinct(lighting_condition) from crash_data;

select lighting_condition,avg(injuries_total) as average_injury from crash_data group by lighting_condition having lighting_condition like "daylight%" or lighting_condition like "darkness%";

## 7

select traffic_control_device,avg(injuries_total) as average_injury from crash_data group by traffic_control_device order by average_injury desc limit 1;

##8

select location,count(*) as frequency from crash_data group by location order by frequency desc limit 5;

##9

select street_name,count(*) as crashes, round(sum(injuries_total)/count(*),2) as injury_rate from crash_data group by street_name having crashes>100 order by injury_rate desc limit 5;

##10
select year,crash_type,total_crash from(
select year,crash_type, count(*) as total_crash , dense_rank() over (partition by year order by count(*) desc) as ranked from crash_data group by year,crash_type) as tab
where ranked=1; 

##11
select crash_day_of_week, round(avg(total_crash),2) as average from
(select crash_day_of_week,crash_hour,count(*) as total_crash from crash_data group by crash_day_of_week,crash_hour order by crash_day_of_week) as tab
group by crash_day_of_week
order by average desc limit 1;

##12

select case when crash_hour between 4 and 11 then "Morning"
when crash_hour between 12 and 16 then "Afternoon"
when crash_hour between 17 and 20 then "Evening" else "Night" end as time_bucket,
sum(injuries_total) as injuries
from crash_data
group by time_bucket
order by injuries desc limit 1;

## 13
select crash_type,prim_contributory_cause from
(select crash_type, prim_contributory_cause, count(*) as total , 
dense_rank() over(partition by crash_type order by count(*) desc) as ranked from crash_data 
group by crash_type,prim_contributory_cause) as tab
where ranked<=3;

##14

select year, count(*) as current_total_crashes , lag(count(*)) over(order by year) as previous_year_crashes,
round((count(*)- lag(count(*)) over(order by year)) *100 / lag(count(*)) over(order by year),2) as growth_rate
from crash_data
group by year;

##15

select round(latitude,2) as latitude, round(longitude,2) as longitude, count(*) as total
from crash_data 
group by round(latitude,2),round(longitude,2)
order by total desc limit 10;

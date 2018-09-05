
with #temp as
(
select count(distinct id) as DDR_Total from consumer
where POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
) ,
#temp2 as
(
SELECT count(distinct consumer_id) as DDR_Active_Users
    FROM dbo.Activity_App
    WHERE app_startup >0
		and consumer_id in (select id from consumer 
where POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
)
select (DDR_Total - DDR_Active_Users) as Device_Reg_Inactive	
from #temp, #temp2
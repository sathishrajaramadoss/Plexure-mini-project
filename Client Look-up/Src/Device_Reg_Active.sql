/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '08-03-2018'*/
SELECT count(distinct consumer_id) as Device_Reg_Active
    FROM dbo.Activity_App
    WHERE app_startup >0
	and consumer_id in (select id from consumer 
where POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
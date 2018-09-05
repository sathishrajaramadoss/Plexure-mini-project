/*DECLARE   @STARTDATE DATETIME,@ENDDATE DATETIME

SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE =  '07-09-2018'*/

SELECT count(distinct consumer_id) as Reg_Email_Active_Users
FROM dbo.Activity_App 
WHERE app_startup >0
    and consumer_id in (SELECT Id FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>'' 
	and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
	and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
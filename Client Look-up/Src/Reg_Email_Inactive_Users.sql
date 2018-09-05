/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '07-10-2018'*/

select count(distinct id) as Reg_Email_Inactive_Users
from dbo.Consumer 
where EmailAddress is not null and EmailAddress<>'' 
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
and id not in (
select distinct consumer_id from Activity_app where app_startup>0 
and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
and consumer_id is not null)
/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '07-08-2018'*/

with #temp as
(
SELECT count(distinct consumer_id) as Reg_Email_Active_Users
FROM dbo.Activity_App 
WHERE app_startup >0
    and consumer_id in (SELECT Id FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>'' 
	and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
	and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
) ,
#temp2 as
(
SELECT  count(distinct bb.consumer_id) as Redmeers_Active_Users_Email
FROM dbo.Activity_App as aa
inner join Activity_Offer as bb
on aa.consumer_id=bb.consumer_id    
WHERE bb.offer_redemption>0 
and aa.app_startup>0 
and bb.consumer_id in (SELECT Id FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>'' 
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and bb.source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
)
select (Reg_Email_Active_Users - Redmeers_Active_Users_Email) as Non_Redmeers_Active_Users_Email
from #temp, #temp2
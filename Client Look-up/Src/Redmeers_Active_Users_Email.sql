/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '07-07-2018'*/

SELECT  count(distinct bb.consumer_id) as Redmeers_Active_Users_Email
FROM dbo.Activity_App as aa
inner join Activity_Offer as bb
on aa.consumer_id=bb.consumer_id    
WHERE bb.offer_redemption>0 
and aa.app_startup>0 
and bb.consumer_id in (SELECT Id FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>'' 
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and bb.source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
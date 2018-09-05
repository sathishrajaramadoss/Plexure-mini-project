
with #temp as
(
SELECT count(distinct consumer_id) as Device_Reg_Active
    FROM dbo.Activity_App
    WHERE app_startup >0
		and consumer_id in (select id from consumer 
where POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112)
) ,
#temp2 as
(
SELECT  count(distinct aa.consumer_id) as Device_Active_Redeemers
FROM dbo.Activity_App as aa
inner join Activity_Offer as bb
on aa.consumer_id=bb.consumer_id    
WHERE bb.offer_redemption>0 
and aa.app_startup>0 
and aa.consumer_id in (SELECT Id FROM dbo.Consumer WHERE POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and (creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112))
and aa.consumer_id is not NULL)
and (bb.source_activity_date_device between convert(integer, convert(varchar,@STARTDATE),112) and convert(integer, convert(varchar,@ENDDATE),112))
and aa.consumer_id is not NULL
)
select (Device_Reg_Active - Device_Active_Redeemers) as Device_Active_NonRedeemers	
from #temp, #temp2
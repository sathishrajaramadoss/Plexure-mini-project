
with #temp as
(
SELECT count(distinct id) as Reg_Email_Users
     FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>''
	 and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
) ,
#temp2 as
(
SELECT COUNT(distinct id) as Un_Reg_Email_Users FROM CONSUMER 
	 WHERE LASTKNOWNDEVICEID NOT IN (
		SELECT LASTKNOWNDEVICEID
		FROM dbo.Consumer 
		WHERE EmailAddress is not null and EmailAddress<>'')
	 and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
)
select (Reg_Email_Users + Un_Reg_Email_Users) as Total_Users
from #temp, #temp2
/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME

SET @STARTDATE ='06-01-2018'
SET @ENDDATE =  '07-11-2018'*/

SELECT count(id) as Total_Email_Users
     FROM dbo.Consumer WHERE EmailAddress is not null and EmailAddress<>''
	 and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
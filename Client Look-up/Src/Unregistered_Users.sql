/*DECLARE @STARTDATE Date,
@ENDDATE Date

SET @STARTDATE ='06-01-2018'
SET @ENDDATE =  '07-13-2018'*/

SELECT COUNT(id) as Unregistered_Users FROM CONSUMER
         WHERE LASTKNOWNDEVICEID NOT IN (
                SELECT LASTKNOWNDEVICEID
                FROM dbo.Consumer
                WHERE EmailAddress is not null and EmailAddress<>'')
         and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '07-05-2018'*/
select count(distinct id) as Device_Reg_Total from consumer
where POWER(convert(bigint, 2), 62 % 63) & TagGroup1Flags > 0
and creationdate between convert(datetime, convert(varchar,@STARTDATE),112) and convert(datetime, convert(varchar,@ENDDATE),112)
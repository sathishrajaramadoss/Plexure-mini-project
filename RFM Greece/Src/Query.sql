select consumer_id as Customers,
sale_id as Transaction_Id,
Total_amount as Sales_Amount,
convert(date,date_occurred) as Date_Occurred
from [Sale_Header] aa
inner join consumer bb
on aa.[consumer_id]=bb.[Id]
where convert(varchar(100),date_occurred,101) <= DATEADD(month,6,GETDATE())
and (POWER(convert(bigint, 2), 189 % 63) & TagGroup4Flags  > 0)

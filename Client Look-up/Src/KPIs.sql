/*DECLARE @STARTDATE DATETIME,
@ENDDATE DATETIME
SET  @STARTDATE ='06-01-2018'
SET  @ENDDATE = '07-06-2018'*/
select sum(CumulativeAppStartups) as App_start_up,
		sum(CumulativeAdvertisementImpressions) as Adv_Impressions,
		sum(CumulativeAdvertisementClicks) as Adv_Clicks,
		sum(CumulativeOfferImpressions) as Offer_Impressions,
		sum(CumulativeOfferClickThroughs) as Offer_Clicks,
		sum(CumulativeOfferRedemptions) as Offer_Redemptions,
		sum(CumulativeOfferInstoreRedemptions) as Offer_Instore_Redemptions,
		sum(CumulativePushMessagesSent) as Push_Msg_Sent,
		sum(CumulativePushMessageSeen) as Push_Msg_Seen,
		sum(CumulativePushMessageClicked) as Push_Msg_Clicked,
		sum(CumulativeLoyaltyCardImpressions) as Loyalty_Card_Impressions,
		sum(CumulativeLoyaltyCardInstancesActivated) as Loyalty_Card_Instance_Activated,
		sum(CumulativeLoyaltyCardPointsCreated) as Loyalty_Card_Points_Created,
		sum(CumulativeLoyaltyCardRewardsActivated) as Loyalty_Card_Rewards_Activated,
		sum(CumulativeAppPageImpressions) as App_Page_Impressions,
		sum(CumulativeButtonClicks) as Button_Clicks
from report.reporting
where [OccurredOn] between convert(date, convert(varchar,@STARTDATE),112) and convert(date, convert(varchar,@ENDDATE),112)
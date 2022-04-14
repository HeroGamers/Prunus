import aiohttp
import datetime
import dateutil.parser
import dateutil.tz
from Util import logger
# import asyncio
# import json

API_ENDPOINT = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
# https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions
params = {"locale": "en-US", "country": "US", "allowCountries": "US"}


async def get_free_games():
    games = []
    try:
        elements = []
        async with aiohttp.ClientSession() as session:
            async with session.get(API_ENDPOINT, params=params) as response:
                res_json = await response.json()
                if response.status == 200:
                    # print(json)
                    try:
                        elements = res_json['data']['Catalog']['searchStore']['elements']
                    except KeyError:
                        logger.logDebug("Error getting JSON elements - Status code: " +
                                        str(response.status) + " - Response: " + str(res_json))
                    # print(elements)

                else:
                    logger.logDebug("Error getting request - Status code: " + str(response.status) +
                                    " - Response: " + str(res_json))
        if elements:
            now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
            # print(f"{len(elements)} elements found")
            for element in elements:
                added = False
                # print("=== Checking " + element["title"] + " ===")
                # print(element)
                if "promotions" in element and element["promotions"] and "promotionalOffers" in element["promotions"]:
                    # print("has promotionaloffers")
                    for promotionalOffer in element["promotions"]["promotionalOffers"]:
                        # print("promotionaloffer loop")
                        if added:
                            break
                        if "promotionalOffers" in promotionalOffer:
                            # print("promotionaloffer has promotional offer")
                            for innerPromotionalOffer in promotionalOffer["promotionalOffers"]:
                                # print("inner promotional offer loop")
                                print(innerPromotionalOffer)
                                if "discountSetting" in innerPromotionalOffer and "discountPercentage" in innerPromotionalOffer["discountSetting"]:
                                    # print("offer has discount setting and percentage")
                                    if "startDate" in innerPromotionalOffer and "endDate" in innerPromotionalOffer:
                                        # print("offer has start and enddate")
                                        if innerPromotionalOffer["discountSetting"]["discountPercentage"] == 0:
                                            # print("offer has discount 0")
                                            startDate = dateutil.parser.isoparse(innerPromotionalOffer["startDate"])
                                            endDate = dateutil.parser.isoparse(innerPromotionalOffer["endDate"])
                                            if startDate <= now <= endDate:
                                                # print("offer is valid now")
                                                element["startDate"] = startDate.replace(tzinfo=None)
                                                element["endDate"] = endDate.replace(tzinfo=None)
                                                games.append(element)
                                                added = True
                                                break
            # this is smarter than the for loop stuff, but I'd like to add the start and enddates to the object root,
            # so using the above solution
            # games = [
            #     game for game in elements
            #     if (
            #             "promotions" in game
            #             and game["promotions"]
            #             and "promotionalOffers" in game["promotions"]
            #             and [
            #                 promotionalOffer for promotionalOffer in game["promotions"]["promotionalOffers"]
            #                 if "promotionalOffers" in promotionalOffer
            #                 and [
            #                     innerPromotionalOffer for innerPromotionalOffer in promotionalOffer["promotionalOffers"]
            #                     # time for the actual check of the game :)
            #                     if "discountSetting" in innerPromotionalOffer
            #                     and "discountPercentage" in innerPromotionalOffer["discountSetting"]
            #                     and "startDate" in innerPromotionalOffer
            #                     and "endDate" in innerPromotionalOffer
            #                     and innerPromotionalOffer["discountSetting"]["discountPercentage"] == 0
            #                     and dateutil.parser.isoparse(innerPromotionalOffer["startDate"]) <= now <= dateutil.parser.isoparse(innerPromotionalOffer["endDate"])
            #                 ]
            #             ]
            #     )
            # ]
            # get product slugs
            for game in games:
                if "productSlug" not in game or not game["productSlug"]:
                    if "customAttributes" in game:
                        for attribute in game["customAttributes"]:
                            if "key" in attribute and attribute["key"] == "com.epicgames.app.productSlug":
                                game["productSlug"] = attribute["value"]
                                break
                    if "productSlug" not in game or not game["productSlug"]:
                        if "catalogNs" in game and "mappings" in game["catalogNs"]:
                            for mapping in game["catalogNs"]["mappings"]:
                                if "pageType" in mapping and mapping["pageType"] == "productHome":
                                    game["productSlug"] = mapping["pageSlug"]
                                    break
    except Exception as e:
        logger.logDebug("Error while getting games from epic games: " + str(e))
        # print("Error while getting games from epic games: " + str(e))

    logger.logDebug(f"found {len(games)} free games!")
    # print(json.dumps(games, indent=4))
    return games

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     games = get_free_games()
#     loop.run_until_complete(games)

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from enum import Enum
from typing import Dict
from botbuilder.ai.luis import LuisRecognizer
from botbuilder.core import IntentScore, TopIntent, TurnContext

from booking_details import BookingDetails


class Intent(Enum):
    BOOK_FLIGHT = "Book"
    CANCEL = "Cancel"
    GET_WEATHER = "GetWeather"
    NONE_INTENT = "NoneIntent"


def top_intent(intents: Dict[Intent, dict]) -> TopIntent:
    max_intent = Intent.NONE_INTENT
    max_value = 0.0

    for intent, value in intents:
        intent_score = IntentScore(value)
        if intent_score.score > max_value:
            max_intent, max_value = intent, intent_score.score

    return TopIntent(max_intent, max_value)


class LuisHelper:
    @staticmethod
    async def execute_luis_query(
        luis_recognizer: LuisRecognizer, turn_context: TurnContext
    ) -> (Intent, object):
        """
        Returns an object with preformatted LUIS results for the bot's dialogs to consume.
        """
        result = None
        intent = None

        try:
            recognizer_result = await luis_recognizer.recognize(turn_context)

            intent = (
                sorted(
                    recognizer_result.intents,
                    key=recognizer_result.intents.get,
                    reverse=True,
                )[:1][0]
                if recognizer_result.intents
                else None
            )

            if intent == Intent.BOOK_FLIGHT.value:
                result = BookingDetails()
                print('Prout1')

                # We need to get the result from the LUIS JSON which at every level returns an array.
                to_entities = recognizer_result.entities.get("$instance", {}).get(
                    "VilleArr", []
                )
                if len(to_entities) > 0:
                    print('Prout1')
                    result.destination = to_entities[0]["text"].capitalize()
                    # if recognizer_result.entities.get("VilleArr", [{"$instance": {}}])[0][
                        # "$instance"
                    # ]:
                        # print('Prout2')
                        # result.destination = to_entities[0]["text"].capitalize()
                        # print('Prout2b')
                    # else:
                        # print('Prout3')
                        # result.unsupported_airports.append(
                            # to_entities[0]["text"].capitalize()
                        # )

                print(result.destination)
                print('Prout2')
                from_entities = recognizer_result.entities.get("$instance", {}).get(
                    "VilleDep", []
                )
                if len(from_entities) > 0:
                    result.origin = from_entities[0]["text"].capitalize()
                    # if recognizer_result.entities.get("VilleDep", [{"$instance": {}}])[0][
                        # "$instance"
                    # ]:
                        # result.origin = from_entities[0]["text"].capitalize()
                    # else:
                        # result.unsupported_airports.append(
                            # from_entities[0]["text"].capitalize()
                        # )


                print(result.origin)
                print('Prout3')
                budget_entities = recognizer_result.entities.get("$instance", {}).get(
                    "Budget", []
                )
                if len(budget_entities) > 0:
                    result.budget = budget_entities[0]["text"].capitalize()
                    # if recognizer_result.entities.get("Budget", [{"$instance": {}}])[0][
                        # "$instance"
                    # ]:
                        # result.budget = budget_entities[0]["text"].capitalize()
                    # else:
                        # result.unsupported_airports.append(
                            # budget_entities[0]["text"].capitalize()
                        # )

                # This value will be a TIMEX. And we are only interested in a Date so grab the first result and drop
                # the Time part. TIMEX is a format that represents DateTime expressions that include some ambiguity.
                # e.g. missing a Year.
                print(result.budget)
                print('Prout4')
                date_entities = recognizer_result.entities.get("datetime", [])
                print(date_entities)
                if date_entities:
                    timex = date_entities[0]["timex"]

                    if timex:
                        if date_entities[0]["type"]=='date':
                            datetime = timex[0].split("T")[0]
                            result.travel_date_dep = datetime
                        if date_entities[0]["type"]=='daterange':
                            datetime_str = timex[0].split("(")[1].split(",")[0]
                            datetime_end = timex[0].split(",")[1]
                            result.travel_date_dep = datetime_str
                            result.travel_date_arr = datetime_end
#                        result.travel_date_dep = datetime

                else:
                    result.travel_date_dep = None

        except Exception as exception:
            print(exception)

        return intent, result

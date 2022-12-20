#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "1b4130ff-d5ba-4c40-a183-fd9e76d6f993")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "550ab39c266b4d0a98d7275dfbcf4bca")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "chatbot-da.cognitiveservices.azure.com")
	#LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "francecentral.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "32589889-3ace-44a3-80a5-5641c7f66a77"
    )

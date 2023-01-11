import asyncio
import aiounittest
from config import DefaultConfig
import os
from botbuilder.ai.luis import LuisApplication


class MyTest(aiounittest.AsyncTestCase):

    # some regular test code
    def test_connect(self):
        CONFIG = DefaultConfig()
        luis_application = LuisApplication( CONFIG.LUIS_APP_ID, CONFIG.LUIS_API_KEY, "https://" + CONFIG.LUIS_API_HOST_NAME,)
        self.assertTrue(True)

    def test_something(self):
        CONFIG = DefaultConfig()
        LUIS_APP_ID = "1b4130ff-d5ba-4c40-a183-fd9e76d6f993000"
        luis_application = LuisApplication( LUIS_APP_ID, CONFIG.LUIS_API_KEY, "https://" + CONFIG.LUIS_API_HOST_NAME,)
        self.assertTrue(True)
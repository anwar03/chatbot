from botbuilder.core import (
    TurnContext,
    ActivityHandler,
    RecognizerResult,
    MessageFactory,
)
from botbuilder.ai.luis import (
    LuisApplication,
    LuisPredictionOptions,
    LuisRecognizer
)
import json
from ..config import Config
from ..weather import Weather


class LuisBot(ActivityHandler):
    def __init__(self):
        self.config = Config()
        self.luis_app = LuisApplication(
            self.config.luis_app_id,
            self.config.luis_endpoint_key,
            self.config.luis_endpoint,
        )
        self.luis_option = LuisPredictionOptions(
            include_all_intents=True,
            include_instance_data=True,
        )
        self.Luis_recognizer = LuisRecognizer(
            application=self.luis_app,
            prediction_options=self.luis_option,
            include_api_results=True
        )

    async def on_message_activity(self, turn_context: TurnContext):

        weather = Weather()
        luis_result = await self.Luis_recognizer.recognize(turn_context)
        # intent = LuisRecognizer.top_intent(luis_result)
        intent = self.Luis_recognizer.top_intent(luis_result)
        result = luis_result.properties["luisResult"]
        json_str = json.loads((str(result.entities[0])).replace("'", "\""))
        entity = json_str.get("entity")
        weather_info = weather.get_weather_info(entity)

        # await turn_context.send_activity(f"Entity  {result.entities[0]}")
        await turn_context.send_activity(f"Top Intent : {intent}")
        await turn_context.send_activity(f"Entity  {entity}")
        await turn_context.send_activity(f"{weather_info}")

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


class LuisBot(ActivityHandler):
    def __init__(self):
        luis_app = LuisApplication(
            "d212d63f-740b-49f5-ac91-03557416e6e5",
            "b63e448fcf634ecbb0444fcd9ae244f8",
            "https://westus.api.cognitive.microsoft.com/",
        )
        luis_option = LuisPredictionOptions(
            include_all_intents=True,
            include_instance_data=True,
        )
        self.Luis_reg = LuisRecognizer(luis_app, luis_option, True)

    async def on_message_activity(self, turn_context: TurnContext):
        luis_result = await self.Luis_reg.recognize(turn_context)
        intent = LuisRecognizer.top_intent(luis_result)
        await turn_context.send_activity(f"Top Intent : {intent}")
        result = luis_result.properties["luisResult"]
        await turn_context.send_activity(f"Luis Result {result.entities[0]}")

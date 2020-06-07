from botbuilder.core import TurnContext
from botbuilder.schema import ActivityTypes

class EchoBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == ActivityTypes.conversation_update:
            await turn_context.send_activity("Hello Welcome to Echo Bot")
        if turn_context.activity.type == ActivityTypes.message:
            await turn_context.send_activity(turn_context.activity.text)
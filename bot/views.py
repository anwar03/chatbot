
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from botbuilder.schema import Activity
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    ConversationState,
    UserState,
    MemoryStorage
    )
import asyncio
import json
from .echobot import EchoBot
from .handler.activityHandler import ActiveHandler
from .middleware.middleware1 import Middleware1
from .state.stateBot import StateBot


botadaptersettings = BotFrameworkAdapterSettings("", "")
botadapter = BotFrameworkAdapter(botadaptersettings)
botadapter.use(Middleware1())

loop = asyncio.get_event_loop()
# EchoBot is the first bot for testing purpose
# ebot = EchoBot()
# ActiveHandler() is the testing bot for
# "how to manage bot with activityHandler."
# ahbot = ActiveHandler()

memory_store = MemoryStorage()
conversation_state = ConversationState(memory_store)
user_state = UserState(memory_store)

statebot = stateBot(conversation_state, user_state)


@csrf_exempt
def messages(request):

    if request.method == "POST":
        jsonmessage = json.loads(request.body)
        activity = Activity().deserialize(jsonmessage)

        # loop = asyncio.set_event_loop(asyncio.new_event_loop())
        async def turn_call(turn_context):
            # await ebot.on_turn(turn_context)
            await statebot.on_turn(turn_context)

        task = loop.create_task(
            botadapter.process_activity(activity, "", turn_call)
            )
        loop.run_until_complete(task)

        return HttpResponse("It's working")
    else:
        HttpResponse("Invalid request method")

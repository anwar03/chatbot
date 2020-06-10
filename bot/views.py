
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
from .dialog import BotDialog
from .luis import LuisBot

botadaptersettings = BotFrameworkAdapterSettings("", "")
botadapter = BotFrameworkAdapter(botadaptersettings)
# botadapter.use(Middleware1())

# loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()

# EchoBot is the first bot for testing purpose
# bot = EchoBot()
# ActiveHandler() is the testing bot for
# "how to manage bot with activityHandler."
# bot = ActiveHandler()

# this section for state management stage so comment out for dialog section
# memory_store = MemoryStorage()
# conversation_state = ConversationState(memory_store)
# user_state = UserState(memory_store)
# bot = StateBot(conversation_state, user_state)

# this section for dialog management stage
# memory_store = ConversationState(MemoryStorage())
# bot = BotDialog(memory_store)

memory_store = ConversationState(MemoryStorage())
bot = LuisBot()


@csrf_exempt
def messages(request):

    if request.method == "POST":
        jsonmessage = json.loads(request.body)
        activity = Activity().deserialize(jsonmessage)

        auth_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")

        async def turn_call(turn_context):
            await bot.on_turn(turn_context)

        task = loop.create_task(
            botadapter.process_activity(activity, auth_header, turn_call)
            )
        loop.run_until_complete(task)

        return HttpResponse("It's working")
    else:
        HttpResponse("Invalid request method")

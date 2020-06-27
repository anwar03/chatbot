
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
from .handle.activityHandler import ActiveHandler
from .middlewares.middleware1 import Middleware1
from .state.stateBot import StateBot
from .dialog import BotDialog
from .luis import LuisBot
from .qna import QnaBot

botadaptersettings = BotFrameworkAdapterSettings("", "")
botadapter = BotFrameworkAdapter(botadaptersettings)

loop = asyncio.get_event_loop()

bot = LuisBot()


@csrf_exempt
def messages(request):

    try:
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
            return HttpResponse("Invalid request method")
    except RuntimeError as r:
        print("RunTime Error: ", r)
        return HttpResponse({"RunTime error": r})
    except Exception as e:
        print("Exception Error: ", e)
        return HttpResponse({"Exception Error: ", e})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
import asyncio
import json
from .echobot import EchoBot
from .activityHandler import ActiveHandler

botadaptersettings = BotFrameworkAdapterSettings("", "")
botadapter = BotFrameworkAdapter(botadaptersettings)
loop = asyncio.get_event_loop()
#ebot = EchoBot()
ebot = ActiveHandler()

@csrf_exempt
def messages(request):

    if request.method == "POST":
        jsonmessage = json.loads(request.body)
        activity = Activity().deserialize(jsonmessage)

        #loop = asyncio.set_event_loop(asyncio.new_event_loop())
        async def turn_call(turn_context):
            await ebot.on_turn(turn_context)
        
        task = loop.create_task(botadapter.process_activity(activity, "", turn_call))
        loop.run_until_complete(task)

        return HttpResponse("It's working")
    else:
        HttpResponse("Invalid request method")
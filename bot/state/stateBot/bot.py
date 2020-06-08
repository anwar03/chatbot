from botbuilder.core import (
    TurnContext,
    ActivityHandler,
    ConversationState,
    UserState)

from ..dataModel import ConState, UserProfile, EnumUser


class StateBot(ActivityHandler):
    def __init__(self, constate: ConversationState, userstate: UserState):
        self.constate = constate
        self.userstate = userstate

        self.conprop = self.constate.create_property("constate")
        self.userprop = self.userstate.create_property("userstate")

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        await self.constate.save_changes(turn_context)
        await self.userstate.save_changes(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        conmode = await self.conprop.get(turn_context, ConState)
        usermode = await self.userprop.get(turn_context, UserProfile)

        if(conmode.profile == EnumUser.NAME):
            conmode.profile = EnumUser.PHONE
            await turn_context.send_activity("Please enter the name")
        elif(conmode.profile == EnumUser.PHONE):
            usermode.name = turn_context.activity.text
            conmode.profile = EnumUser.EMAIL
            await turn_context.send_activity("Please enter your number")
        elif(conmode.profile == EnumUser.EMAIL):
            usermode.phone = turn_context.activity.text
            conmode.profile = EnumUser.DONE
            await turn_context.send_activity("Please enter your email")
        elif(conmode.profile == EnumUser.DONE):
            usermode.email = turn_context.activity.text
            info = usermode.name + " " + usermode.phone + " " + usermode.email
            await turn_context.send_activity(info)
            # conmode.profile = EnumUser.NAME

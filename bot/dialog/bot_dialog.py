from botbuilder.core import (
    TurnContext,
    ActivityHandler,
    ConversationState,
    MessageFactory,
    )
from botbuilder.dialogs import (
    DialogSet,
    WaterfallDialog,
    WaterfallStepContext,
    )
from botbuilder.dialogs.prompts import (
    TextPrompt,
    NumberPrompt,
    PromptOptions,
    )


class BotDialog(ActivityHandler):
    def __init__(self, conversation: ConversationState):
        self.con_state = conversation
        self.state_prop = self.con_state.create_property("dialog_set")
        self.dialog_set = DialogSet(self.state_prop)
        self.dialog_set.add(TextPrompt("text_prompt"))
        self.dialog_set.add(NumberPrompt("number_prompt"))
        self.dialog_set.add(WaterfallDialog("main_dialog", [
            self.get_user_name, self.get_modile_number,
            self.get_email, self.complated
        ]))

    async def get_user_name(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt("text_prompt",
                PromptOptions(
                    prompt=MessageFactory.text("Please enter the name")
                ))

    async def get_modile_number(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt("number_prompt",
                PromptOptions(
                    prompt=MessageFactory.text("Please enter the mobile no")
                ))

    async def get_email(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt("text_prompt",
                PromptOptions(
                    prompt=MessageFactory.text("PLease enter the email id")
                ))

    async def complated(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.end_dialog()

    async def on_turn(self, turn_context: TurnContext):
        dialog_context = await self.dialog_set.create_context(turn_context)

        if dialog_context.active_dialog is not None:
            await dialog_context.continue_dialog()
        else:
            await dialog_context.begin_dialog("main_dialog")

        await self.con_state.save_changes(turn_context)

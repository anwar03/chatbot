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
    PromptValidatorContext,
    )


class BotDialog(ActivityHandler):
    def __init__(self, conversation: ConversationState):
        self.con_state = conversation
        self.state_prop = self.con_state.create_property("dialog_set")
        self.dialog_set = DialogSet(self.state_prop)
        self.dialog_set.add(TextPrompt("text_prompt"))
        self.dialog_set.add(NumberPrompt(
            "number_prompt",
            self.is_valid_mobile_number
        ))
        self.dialog_set.add(WaterfallDialog("main_dialog", [
            self.get_user_name, self.get_modile_number,
            self.get_email, self.complated
        ]))

    async def is_valid_mobile_number(
        self,
        prompt_valid: PromptValidatorContext
    ):
        if(prompt_valid.recognized.succeeded is False):
            await prompt_valid.context.send_activity(
                "Hey please enter the number"
            )
            return False
        else:
            value = str(prompt_valid.recognized.value)
            if len(value) < 11:
                await prompt_valid.context.send_activity(
                    "Please enter the valid mobile number"
                )
                return False
        return True

    async def get_user_name(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt(
            "text_prompt",
            PromptOptions(
                prompt=MessageFactory.text("Please enter the name")
            )
        )

    async def get_modile_number(self, waterfall_step: WaterfallStepContext):
        name = waterfall_step._turn_context.activity.text
        waterfall_step.values["name"] = name

        return await waterfall_step.prompt(
            "number_prompt",
            PromptOptions(
                prompt=MessageFactory.text("Please enter the mobile no")
            )
        )

    async def get_email(self, waterfall_step: WaterfallStepContext):
        mobile = waterfall_step._turn_context.activity.text
        waterfall_step.values["mobile"] = mobile

        return await waterfall_step.prompt(
            "text_prompt",
            PromptOptions(
                prompt=MessageFactory.text("Please enter the email id")
            )
        )

    async def complated(self, waterfall_step: WaterfallStepContext):
        email = waterfall_step._turn_context.activity.text
        waterfall_step.values["email"] = email
        name = waterfall_step.values["name"]
        mobile = waterfall_step.values["mobile"]
        profile_info = f"name: {name}, email: {email}, mobile: {mobile}"
        await waterfall_step._turn_context.send_activity(profile_info)
        return await waterfall_step.end_dialog()

    async def on_turn(self, turn_context: TurnContext):
        dialog_context = await self.dialog_set.create_context(turn_context)

        if dialog_context.active_dialog is not None:
            await dialog_context.continue_dialog()
        else:
            await dialog_context.begin_dialog("main_dialog")

        await self.con_state.save_changes(turn_context)

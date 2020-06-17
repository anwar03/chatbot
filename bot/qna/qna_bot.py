from botbuilder.core import TurnContext, ActivityHandler, MessageFactory
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint


class QnaBot(ActivityHandler):
    def __init__(self):
        qna_enpoint = QnAMakerEndpoint(
            "72e97083-2783-4e2c-a3ae-cac7d785a973",
            "21a6fbca-8f7f-4ecf-8f47-704ddee75aaa",
            "https://yogyabot.azurewebsites.net/qnamaker")
        self.qna_maker = QnAMaker(qna_enpoint)

    async def on_message_activity(self, turn_context: TurnContext):
        response = await self.qna_maker.get_answers(turn_context)
        print('called QnA bot')
        if response and len(response) > 0:
            await turn_context.send_activity(
                MessageFactory.text(response[0].answer)
            )

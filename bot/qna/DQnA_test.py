import os
import time
from django.http import HttpResponse
from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import (
    QnAMakerRuntimeClient
)
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import (
    QnADTO,
    MetadataDTO,
    CreateKbDTO,
    UpdateQnaDTO,
    OperationStateType,
    UpdateKbOperationDTO,
    UpdateKbOperationDTOAdd,
    UpdateKbOperationDTOUpdate,
    UpdateKbOperationDTODelete,
    EndpointKeysDTO,
    QnADTOContext,
    PromptDTO
)
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from msrest.authentication import CognitiveServicesCredentials


class Dqna:
    def __init__(self):
        # key 1
        # self.authoring_key = "ed87a27ac70e424a9db8743f1a690427"
        # key2
        # authoring_key = "3eb0af5a673b49ca981011bdfaa3fbce"
        self.authoring_key = "3eb0af5a673b49ca981011bdfaa3fbce"
        self.resource_name = "yogyabot"

        self.authoringURL = f"https://{self.resource_name}.cognitiveservices.azure.com"
        self.queryingURL = f"https://{self.resource_name}.azurewebsites.net"
        print("resource_name: ", self.resource_name)
        print("authoring_key: ", self.authoring_key)
        print("authoringURL: ", self.authoringURL)
        print("queryingURL: ", self.queryingURL)
        self.kb_id = "91f2cc7b-fc39-4d5f-b75a-f8f2ba83f0a0"
        self.client = QnAMakerClient(
            endpoint=self.authoringURL,
            credentials=CognitiveServicesCredentials(self.authoring_key)
        )

    def _monitor_operation(self, client, operation):
        for i in range(20):
            if operation.operation_state in [OperationStateType.not_started, OperationStateType.running]:
                print("Waiting for operation: {} to complete.".format(operation.operation_id))
                time.sleep(5)
                operation = client.operations.get_details(operation_id=operation.operation_id)
            else:
                break
        if operation.operation_state != OperationStateType.succeeded:
            raise Exception("Operation {} failed to complete.".format(operation.operation_id))
        return operation

    def create_kb(self):

        qna = QnADTO(
            answer="You can use our REST APIs to manage your knowledge base.",
            questions=["How do I manage my knowledgebase?"],
            metadata=[MetadataDTO(name="Category", value="api")]
        )

        qna1 = QnADTO(
            answer="Yes, You can use our [REST APIs](https://docs.microsoft.com/rest/api/cognitiveservices/qnamaker/knowledgebase) to manage your knowledge base.",
            questions=["How do I manage my knowledgebase?"],
            metadata=[
                MetadataDTO(name="Category", value="api"),
                MetadataDTO(name="Language", value="REST"),
            ]
        )

        qna2 = QnADTO(
            answer="Yes, You can use our [Python SDK](https://pypi.org/project/azure-cognitiveservices-knowledge-qnamaker/) with the [Python Reference Docs](https://docs.microsoft.com/python/api/azure-cognitiveservices-knowledge-qnamaker/azure.cognitiveservices.knowledge.qnamaker?view=azure-python) to manage your knowledge base.",
            questions=["Can I program with Python?"],
            metadata=[
                MetadataDTO(name="Category", value="api"),
                MetadataDTO(name="Language", value="Python"),
            ]
        )
        urls = [
            "https://docs.microsoft.com/en-in/azure/cognitive-services/qnamaker/faqs",
            "https://www.w3schools.com/python/python_intro.asp",
        ]

        create_kb_dto = CreateKbDTO(
            name="QnA Maker FAQ from quickstart",
            qna_list=[qna, qna1, qna2],
            urls=urls,
            enable_hierarchical_extraction=True,
            default_answer_used_for_extraction="No answer found.",
            language="English"
        )
        create_op = self.client.knowledgebase.create(create_kb_payload=create_kb_dto)

        create_op = self._monitor_operation(client=self.client, operation=create_op)
        self.kb_id = create_op.resource_location.replace("/knowledgebases/", "")
        print("Created KB with ID: {}".format(self.kb_id))

        return HttpResponse({"knowledge_base_ID : ": self.kb_id})

    def update_kb(self):

        qna = QnADTO(
            answer="You can use our REST APIs to manage your knowledge base.",
            questions=["How do I manage my knowledgebase?"],
            metadata=[MetadataDTO(name="Category", value="api")]
        )

        qna1 = QnADTO(
            answer="Yes, You can use our [REST APIs](https://docs.microsoft.com/rest/api/cognitiveservices/qnamaker/knowledgebase) to manage your knowledge base.",
            questions=["How do I manage my knowledgebase?"],
            metadata=[
                MetadataDTO(name="Category", value="api"),
                MetadataDTO(name="Language", value="REST"),
            ]
        )

        qna2 = QnADTO(
            answer="Yes, You can use our [Python SDK](https://pypi.org/project/azure-cognitiveservices-knowledge-qnamaker/) with the [Python Reference Docs](https://docs.microsoft.com/python/api/azure-cognitiveservices-knowledge-qnamaker/azure.cognitiveservices.knowledge.qnamaker?view=azure-python) to manage your knowledge base.",
            questions=["Can I program with Python?"],
            metadata=[
                MetadataDTO(name="Category", value="api"),
                MetadataDTO(name="Language", value="Python"),
            ]
        )

        qna3 = UpdateQnaDTO(
            answer="goodbye",
            questions=[
                "bye",
                "end",
                "stop",
                "quit",
                "done"
                ],
            metadata=[
                MetadataDTO(name="Category", value="Chitchat"),
                MetadataDTO(name="Chitchat", value="end"),
            ]
        )

        qna4 = UpdateQnaDTO(
            answer="Hello, please select from the list of questions or enter a new question to continue.",
            questions=[
                "hello",
                "hi",
                "start"
            ],
            metadata=[
                MetadataDTO(name="Category", value="Chitchat"),
                MetadataDTO(name="Chitchat", value="begin"),
            ],
            context=QnADTOContext(

                is_context_only=False,
                prompts=[

                    PromptDTO(
                        display_order=1,
                        display_text="Use REST",
                        qna_id=1

                    ),
                    PromptDTO(
                        display_order=2,
                        display_text="Use .NET NuGet package",
                        qna_id=2
                    ),
                ]
            )
        )

        urls = [
            "https://docs.microsoft.com/en-in/azure/cognitive-services/qnamaker/faqs",
            "https://www.w3schools.com/python/python_intro.asp",
            "https://docs.microsoft.com/azure/cognitive-services/QnAMaker/troubleshooting",
        ]

        update_kb_operation_dto = UpdateKbOperationDTO(
            add=UpdateKbOperationDTOAdd(
                qna_list=[qna, qna1, qna2],
                urls=[],
                files=[]
            ),
            delete=None,
            update=UpdateKbOperationDTOUpdate(
                name="Demo",
                qna_list=[],
                urls=[]
            )
        )
        update_op = self.client.knowledgebase.update(
            kb_id=self.kb_id,
            update_kb=update_kb_operation_dto
        )
        self._monitor_operation(client=self.client, operation=update_op)
        print("Updated.")
        # return HttpResponse({"knowledge_base_ID : ": self.kb_id})

    def publish_kb(self):
        self.client.knowledgebase.publish(kb_id=self.kb_id)
        print("Published.")
        # return HttpResponse({"knowledge_base_ID : ": self.kb_id})

    def download_kb(self):
        kb_data = self.client.knowledgebase.download(kb_id=self.kb_id, environment="Prod")
        print("Downloaded. It has {} QnAs.".format(len(kb_data.qna_documents)))
        # return HttpResponse({"knowledge_base_ID : ": self.kb_id})

    def delete_kb(self):
        client.knowledgebase.delete(kb_id=self.kb_id)
        print("Deleted.")
        # return HttpResponse({"knowledge_base_ID : ": self.kb_id})

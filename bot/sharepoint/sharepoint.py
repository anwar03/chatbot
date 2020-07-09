import requests
import re
import json
import pdfkit
import html
import os
from bs4 import BeautifulSoup
from shareplum import Office365
from shareplum import Site
from shareplum import folder
from shareplum.request_helper import get, post
from shareplum.site import Version


class ShareData:
    def __init__(self):
        self._username = 'YogyaBot@yogyassl.onmicrosoft.com'
        self._password = 'Chatbot2020%'
        self._site = 'https://yogyassl.sharepoint.com'
        self._url = 'https://yogyassl.sharepoint.com/sites/YogyaDemo'
        self._session = requests.Session()
        self.authcookie = Office365(
            self._site,
            username=self._username,
            password=self._password).GetCookies()
        self._session.cookies = self.authcookie
        self.site = Site(
            self._url,
            version=Version.v365, authcookie=self.authcookie
            )

        # print(self.authcookie)

    def site_data(self):
        # print(self._session)
        # self.folder = self.site.Folder('SitePages')
        # self.files = self.folder.files
        # for item in self.files:
        #     # print(item["Name"])
        #     # print(item["Title"])
        #     # print(item["ServerRelativeUrl"])
        #     # print()
        #     url = self._site+item["ServerRelativeUrl"]

        #     print("url: ", url)
        #     self.r = self._session.get(url)

        #     g = open('aspx/'+item["Name"], 'w')
        #     g.write(self.r.text)
        #     g.close()

        #     html_name = item["Name"].split('.')[0]+".html"
        #     pdf_name = item["Name"].split('.')[0]+".pdf"

        #     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #     HOME_DIR = os.path.realpath(os.path.join(BASE_DIR, '..'))
        #     HTML_DATA_URL = os.path.join(HOME_DIR, 'html/')
        #     PDF_DATA_URL = os.path.join(HOME_DIR, 'pdf/')

        #     html_path = os.path.join(HTML_DATA_URL, html_name)
        #     pdf_path = os.path.join(PDF_DATA_URL, pdf_name)
        #     print("pdf path: ", pdf_path)
        #     f = open(html_path, 'w')
        #     # with open(html_path) as f:
        #     innerHTML = re.search(r'(\\"innerHTML\\":\\")(.*)(\\"},{)', self.r.text)
        #     if innerHTML:
        #         text = innerHTML.group(2).encode().decode("unicode-escape")
        #         text = BeautifulSoup(text, features="lxml")
        #         f.write(text.prettify())
        #     else:
        #         text = "This url is empty"
        #         f.write(text)
        #         print("doesn't match : ", text)

        #     f.close()
        #     with open(html_path) as g:
        #         print("html_path: ", g)
        #         pdfkit.from_file(g, pdf_path)

        jstring = """
        "Content" : {"CanvasContent1":"[{\"controlType\":4,\"id\":\"3dc72d63-5351-411f-8aba-4334ffaf88ce\",\"position\":{\"zoneIndex\":0.5,\"sectionIndex\":1,\"controlIndex\":1,\"sectionFactor\":12,\"layoutIndex\":1},\"emphasis\":{},\"innerHTML\":\"\u003ch3\u003ehow are you??\u003cbr\u003e\u003c/h3\u003e\u003cp\u003eYou can specify all wkhtmltopdf options. You can drop âââ in option name. If option without value, use None, False or ââ for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. âcustom-header Authorization secret) we may use a 2-tuple (see example below).\u003cbr\u003e\u003c/p\u003e\"},{\"controlType\":3,\"id\":\"7f84a4c8-47f2-43b7-ad96-b43bb5430251\",\"position\":{\"zoneIndex\":1,\"sectionIndex\":1,\"controlIndex\":1.5,\"layoutIndex\":1},\"webPartId\":\"20745d7d-8581-4a6c-bf26-68279bc123fc\",\"emphasis\":{},\"addedFromPersistedData\":true,\"reservedHeight\":341,\"reservedWidth\":1180,\"webPartData\":{\"id\":\"20745d7d-8581-4a6c-bf26-68279bc123fc\",\"instanceId\":\"7f84a4c8-47f2-43b7-ad96-b43bb5430251\",\"title\":\"Events\",\"description\":\"Display upcoming events\",\"serverProcessedContent\":{\"htmlStrings\":{},\"searchablePlainTexts\":{\"title\":\"how are you??\\n\\nYou can specify all wkhtmltopdf options. You can drop âââ in option name. If option without value, use None, False or ââ for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. âcustom-header Authorization secret) we may use a 2-tuple (see example below).\"},\"imageSources\":{},\"links\":{\"baseUrl\":\"/sites/YogyaDemo\"},\"componentDependencies\":{\"layoutComponentId\":\"8ac0c53c-e8d0-4e3e-87d0-7449eb0d4027\"}},\"dataVersion\":\"1.2\",\"properties\":{\"selectedListId\":\"a6a5922c-2cf3-4801-ad6e-cd937e01a454\",\"selectedCategory\":\"\",\"dateRangeOption\":0,\"startDate\":\"\",\"endDate\":\"\",\"isOnSeeAllPage\":false,\"layout\":\"Filmstrip\",\"dataSource\":7,\"sites\":[],\"maxItemsPerPage\":20,\"layoutId\":\"FilmStrip\",\"dataProviderId\":\"Event\",\"webId\":\"e7f8ccac-efd2-4867-90be-8c4e293b737b\",\"siteId\":\"3d3db0f8-9a1b-466d-ba1d-3b321ca0493d\"}}},{\"controlType\":0,\"pageSettingsSlice\":{\"isDefaultDescription\":true,\"isDefaultThumbnail\":true}}]","LayoutWebpartsContent":"[{\"id\":\"cbe7b0a9-3504-44dd-a3a3-0e5cacd07788\",\"instanceId\":\"cbe7b0a9-3504-44dd-a3a3-0e5cacd07788\",\"title\":\"Title area\",\"description\":\"Title Region Description\",\"serverProcessedContent\":{\"htmlStrings\":{},\"searchablePlainTexts\":{},\"imageSources\":{},\"links\":{}},\"dataVersion\":\"1.4\",\"properties\":{\"title\":\"Events\",\"imageSourceType\":4,\"layoutType\":\"FullWidthImage\",\"textAlignment\":\"Left\",\"showTopicHeader\":false,\"showPublishDate\":false,\"topicHeader\":\"\",\"authors\":[{\"id\":\"i:0#.f|membership|yogyabot@yogyassl.onmicrosoft.com\",\"upn\":\"YogyaBot@yogyassl.onmicrosoft.com\",\"email\":\"YogyaBot@yogyassl.onmicrosoft.com\",\"name\":\"Yogya Bot\",\"role\":\"Developer\"}],\"authorByline\":[\"i:0#.f|membership|yogyabot@yogyassl.onmicrosoft.com\"]},\"reservedHeight\":228}]","AlternativeUrlMap":{"MediaTAThumbnailPathUrl":"https://ukwest1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat={.fileType}&cs=UEFHRVN8U1BP&docid={.spHost}/_api/v2.0/sharePoint:{.resourceUrl}:/driveItem&w={.widthValue}&oauth_token=bearer%20{.oauthToken}","MediaTAThumbnailHostUrl":"https://ukwest1-mediap.svc.ms","PublicCDNEnabled":"False","PrivateCDNEnabled":"False"}}
        """
        jstring = "{" + jstring + "}"
        jstring = jstring.encode().decode("unicode-escape")
        # print(jstring)
        data = json.dumps(jstring)
        data = json.loads(data)
        # soup = BeautifulSoup("aspx/Events.aspx", features="lxml")
        g = open("aspx/Events.json", 'w')
        g.write(data.CanvasContent1)
        g.close()
        # print(data)

    def test(self):
        jstring = """
        "Content" : {"CanvasContent1":"[{\"controlType\":4,\"id\":\"3dc72d63-5351-411f-8aba-4334ffaf88ce\",\"position\":{\"zoneIndex\":0.5,\"sectionIndex\":1,\"controlIndex\":1,\"sectionFactor\":12,\"layoutIndex\":1},\"emphasis\":{},\"innerHTML\":\"\u003ch3\u003ehow are you??\u003cbr\u003e\u003c/h3\u003e\u003cp\u003eYou can specify all wkhtmltopdf options. You can drop âââ in option name. If option without value, use None, False or ââ for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. âcustom-header Authorization secret) we may use a 2-tuple (see example below).\u003cbr\u003e\u003c/p\u003e\"},{\"controlType\":3,\"id\":\"7f84a4c8-47f2-43b7-ad96-b43bb5430251\",\"position\":{\"zoneIndex\":1,\"sectionIndex\":1,\"controlIndex\":1.5,\"layoutIndex\":1},\"webPartId\":\"20745d7d-8581-4a6c-bf26-68279bc123fc\",\"emphasis\":{},\"addedFromPersistedData\":true,\"reservedHeight\":341,\"reservedWidth\":1180,\"webPartData\":{\"id\":\"20745d7d-8581-4a6c-bf26-68279bc123fc\",\"instanceId\":\"7f84a4c8-47f2-43b7-ad96-b43bb5430251\",\"title\":\"Events\",\"description\":\"Display upcoming events\",\"serverProcessedContent\":{\"htmlStrings\":{},\"searchablePlainTexts\":{\"title\":\"how are you??\\n\\nYou can specify all wkhtmltopdf options. You can drop âââ in option name. If option without value, use None, False or ââ for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. âcustom-header Authorization secret) we may use a 2-tuple (see example below).\"},\"imageSources\":{},\"links\":{\"baseUrl\":\"/sites/YogyaDemo\"},\"componentDependencies\":{\"layoutComponentId\":\"8ac0c53c-e8d0-4e3e-87d0-7449eb0d4027\"}},\"dataVersion\":\"1.2\",\"properties\":{\"selectedListId\":\"a6a5922c-2cf3-4801-ad6e-cd937e01a454\",\"selectedCategory\":\"\",\"dateRangeOption\":0,\"startDate\":\"\",\"endDate\":\"\",\"isOnSeeAllPage\":false,\"layout\":\"Filmstrip\",\"dataSource\":7,\"sites\":[],\"maxItemsPerPage\":20,\"layoutId\":\"FilmStrip\",\"dataProviderId\":\"Event\",\"webId\":\"e7f8ccac-efd2-4867-90be-8c4e293b737b\",\"siteId\":\"3d3db0f8-9a1b-466d-ba1d-3b321ca0493d\"}}},{\"controlType\":0,\"pageSettingsSlice\":{\"isDefaultDescription\":true,\"isDefaultThumbnail\":true}}]","LayoutWebpartsContent":"[{\"id\":\"cbe7b0a9-3504-44dd-a3a3-0e5cacd07788\",\"instanceId\":\"cbe7b0a9-3504-44dd-a3a3-0e5cacd07788\",\"title\":\"Title area\",\"description\":\"Title Region Description\",\"serverProcessedContent\":{\"htmlStrings\":{},\"searchablePlainTexts\":{},\"imageSources\":{},\"links\":{}},\"dataVersion\":\"1.4\",\"properties\":{\"title\":\"Events\",\"imageSourceType\":4,\"layoutType\":\"FullWidthImage\",\"textAlignment\":\"Left\",\"showTopicHeader\":false,\"showPublishDate\":false,\"topicHeader\":\"\",\"authors\":[{\"id\":\"i:0#.f|membership|yogyabot@yogyassl.onmicrosoft.com\",\"upn\":\"YogyaBot@yogyassl.onmicrosoft.com\",\"email\":\"YogyaBot@yogyassl.onmicrosoft.com\",\"name\":\"Yogya Bot\",\"role\":\"Developer\"}],\"authorByline\":[\"i:0#.f|membership|yogyabot@yogyassl.onmicrosoft.com\"]},\"reservedHeight\":228}]","AlternativeUrlMap":{"MediaTAThumbnailPathUrl":"https://ukwest1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat={.fileType}&cs=UEFHRVN8U1BP&docid={.spHost}/_api/v2.0/sharePoint:{.resourceUrl}:/driveItem&w={.widthValue}&oauth_token=bearer%20{.oauthToken}","MediaTAThumbnailHostUrl":"https://ukwest1-mediap.svc.ms","PublicCDNEnabled":"False","PrivateCDNEnabled":"False"}}
        """
        jstring = "{" + jstring + "}"
        jstring = jstring.encode().decode("unicode-escape")
        # print(jstring)
        data = json.dumps(jstring)
        # data = json.loads(data)
        # soup = BeautifulSoup("aspx/Events.aspx", features="lxml")
        g = open("aspx/Events.json", 'w')
        g.write(data)
        g.close()

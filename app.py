from flask import Flask, render_template, request
from DocumentRetrievalModel import DocumentRetrievalModel as DRM
from ProcessedQuestion import ProcessedQuestion as PQ

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # print(userText)
    res = ''
    #
    try:
        datasetFile = open("./dataset/basic.txt", "r")
    except FileNotFoundError:
        # print("Bot> Oops! I am unable to locate \"" + datasetName + "\"")
        # add email return
        exit()

    paragraphs = []
    for para in datasetFile.readlines():
        if (len(para.strip()) > 0):
            paragraphs.append(para.strip())

    drm = DRM(paragraphs, True, True)

    # greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$", re.IGNORECASE)

    userQuery = userText

    if (not len(userQuery) > 0):
        # print(len(userQuery))
        print("Bot> You need to ask something")
    # elif greetPattern.findall(userQuery):
    #     response = "Hello!"
    else:
        pq = PQ(userQuery, True, False, True)
        response = drm.query(pq)
        res = 'bot says ' + response
        return res


if __name__ == "__main__":
    app.run()

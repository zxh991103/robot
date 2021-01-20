
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/robot1")
def robotindex():


    return render_template("index.html")


@app.route("/ask/<question>")
def talk(question=None):

    global handler
    answer = handler.chat_main(question)


    return answer









if __name__ == '__main__':
    from chatbot_graph import ChatBotGraph
    handler = ChatBotGraph()
    app.run(host='127.0.0.1', debug=True)

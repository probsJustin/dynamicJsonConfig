from flask import *
import autodynatrace
import oneagent
import json

from oneagent.common import DYNATRACE_HTTP_HEADER_NAME
app = Flask("Dynatrace Support Lab Landing Page")

init_result = oneagent.initialize()
print('OneAgent SDK initialization result' + repr(init_result))
if init_result:
    print('SDK should work (but agent might be inactive).')
else:
    print('SDK will definitely not work (i.e. functions will be no-ops):', init_result)

sdk = oneagent.get_sdk()

@autodynatrace.trace
@app.route("/", methods=['GET'])
def index():
    with open('./configData.json') as json_configData:
        dict_configData = json.load(json_configData)
        print(dict_configData["test"])
    return render_template("index.html", dict_configData=dict_configData)

@app.route("/json", methods=['GET'])
def json_text():
    with open('./configData.json') as json_configData:
        return str(json_configData.read())


if __name__ == "__main__":
    app.run('0.0.0.0')
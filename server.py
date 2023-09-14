# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response, send_from_directory
from pywebpush import webpush, WebPushException
import json
import datetime as dt
import holidays
 
# (A2) FLASK SETTINGS + INIT - CHANGE TO YOUR OWN!
HOST_NAME = "localhost"
HOST_PORT = 80
VAPID_SUBJECT = "mailto:diegogomez81655@gmail.com"
VAPID_PRIVATE = "zkFGObQ51LPASmKbm5HyBV1NIZuygcM5536STxhtwzU"
app = Flask(__name__)
# app.debug = True

# (B) VIEWS
# (B1) "LANDING PAGE"
@app.route("/")
def index():
  return render_template("index.html")
 
# (B2) SERVICE WORKER
@app.route("/sw.js")
def sw():
  response = make_response(send_from_directory(app.static_folder, "sw.js"))
  return response
 
# (B3) PUSH DEMO
@app.route("/push", methods=["POST"])
def push():
  # (B3-1) GET SUBSCRIBER
  sub = json.loads(request.form["sub"])
 
  # (B3-2) TEST PUSH NOTIFICATION
  result = "OK"
  try:
    webpush(
      subscription_info = sub,
      data = json.dumps({
        "title" : "Absen!",
        "body"  : "Hey, don't forget to fill you attendance!",
        #"icon" : "static/ayase.png",
        "image" : "static/angryayase.png"
      }),
      vapid_private_key = VAPID_PRIVATE,
      vapid_claims = { "sub": VAPID_SUBJECT }
    )
  except WebPushException as ex:
    print(ex)
    result = "FAILED"
  return result

def attendance():
  x = dt.datetime.now()
  if x.strftime("%A") == "Thursday":
    app.run(HOST_NAME, HOST_PORT)
  else:
    return
  
# (C) START
if __name__ == "__main__":
  
  #app.run(HOST_NAME, HOST_PORT)
  attendance()

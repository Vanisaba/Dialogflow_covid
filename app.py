# doing necessary imports

from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import json
import os
from SendEmail.sendEmail import EmailSender
from logger import logger
from email_templates import template_reader
#import pymongo

app = Flask(__name__)  # initialising the flask app with the name 'app'




@app.route('/webhook',methods=['POST' ]) # route with allowed methods as POST
@cross_origin()
def webhook():
    req=request.get_json(silent=True,force=True)
    #req=json.dumps(req,indent=4)
    print(req)
    res=processRequest(req)
    res=json.dumps(req,indent=4)
    print(res)
    r=make_response(res)
    r.header['Content-Type']='application/json'
    return(r)

def processRequest(req):
    log=logger.Log()
    sessionID=req.get("responseId")
    user_says=req.get("queryText")
    result=reg.get("queryResult")
    log.writeLog(sessionID,"User Says : " +user_says)
    parameters=req.get("parameters")
    name=parameters.get("name")
    pin=parameters.get("pin")
    mailid=parameters.get("mailid")
    phone=parameters.get("phone")
    option_name=paramerers.get("option_name")
    intent = result.get("intent").get('displayName')
    if intent=="covid_intent":
        email_sender = EmailSender()
        template = template_reader.TemplateReader()
        email_message = template.select_info(option_name)
        email_sender.send_email_to_student(mailid, email_message)
        email_file_support = open("email_templates/preventive_Template.html", "r")
        email_message_support = email_file_support.read()
        email_sender.send_email_to_support(name=name, phone=phone, mailid=mailid,
                                           option_name=option_name, body=email_message_support)
        fulfillmentText = "We have sent the details to you via email. An email has been sent to the Support Team with your contact information, you'll be contacted soon. Do you have further queries?"
        log.write_log(sessionID, "Bot Says: " + fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
    else:
        log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)


if __name__ == "__main__":
    port = int(os.getenv('PORT',5000))
    print('Starting app on  port   %d' %port)
    app.run(port=port,debug=False,host='0.0.0.0') # running the app on the local machine on port 8000
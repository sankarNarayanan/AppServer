from flask import Flask
from flask import request, send_from_directory
from flask import json
from flask import Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# url="http://127.0.0.1:5000"

# ret =[ {"title":"Sales Enablement","values":[
#     {"Elevate":"Pending","img":url+"/images/Elevate.png","title":"Elevate","smallDesc":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news.", "version":"v2.0.2","description":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news."},
#     {"E-lab Navigator":"Pending","img":url+"/images/Elab.png","title":"E-lab Navigator","smallDesc":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place.", "version":"v1.0.2","description":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place."},
#     {"Tricorder":"Pending","img":url+"/images/Tricorder.png","title":"Tricorder","smallDesc":"sample Description", "version":"v1.0.0","description":"This is sample description"},
#     {"VxRail":"Pending","img":url+"/images/VxRail.png","title":"VxRail","smallDesc":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team.", "version":"v1.0.1","description":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team."}
#   ]},{"title":"Technical Practictioner","values":[
#     {"DellEMC":"Pending","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move."},
#     {"Help a Customer":"Pending","img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows."}
#   ]},{"title":"Employee Productivity","values":[
#     {"Engage":"Pending","img":url+"/images/Engage.png","title":"Engage","smallDesc":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile.", "version":"v1.0.0","description":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile."},
#     {"Spaces":"Pending","img":url+"/images/Spaces.png","title":"Spaces","smallDesc":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda.", "version":"v1.0.0","description":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda."},
#     {"Help":"Pending","img":url+"/images/Help.png","title":"Help","smallDesc":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone", "version":"v1.0.3","description":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone"}
#   ]},{"title":"Pipeline","values":[
#     {"Self Service Portal":"Pending","img":url+"/images/E2E.png","title":"Self Service Portal","smallDesc":"A portal for making mobile apps.", "version":"v1.0.0","description":"The Self Service portal is a website that enables"},
#     {"Sales Dashboard":"Pending","img":url+"/images/SD.png","title":"Sales Dashboard","smallDesc":"Provides the real time statistics of operations in Sales", "version":"v1.0.5","description":"Provides the real time statistics of operations in Sales"},
#     {"EZDialer":"Pending","img":url+"/images/EZDialer.png","title":"EZDialler","smallDesc":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code.", "version":"v2.1.0","description":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code."},
#     {"Burn Notification":"Pending","img":url+"/images/BN.png","title":"Burn Notification","smallDesc":"Burn Notification App send out notification status to the user’s smart watch.", "version":"v1.0.0","description":"Burn Notification App send out notification status to the user’s smart watch."},
#     {"E2E MRP":"Pending","img":url+"/images/E2E.png","title":"E2E MRP","smallDesc":"sample Description", "version":"v1.0.1","description":"This is sample description"}
#   ]}]

@app.route('/', methods=["GET","POST"])
def get_json():
    url="https://4539d8c7.ngrok.io";

    # ret =[ {"title":"Sales Enablement","values":[
    #     {"Elevate":"Pending","img":url+"/images/Elevate.png","title":"Elevate","smallDesc":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news.", "version":"v2.0.2","description":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news."},
    #     {"E-lab Navigator":"Pending","img":url+"/images/Elab.png","title":"E-lab Navigator","smallDesc":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place.", "version":"v1.0.2","description":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place."},
    #     {"Tricorder":"Pending","img":url+"/images/Tricorder.png","title":"Tricorder","smallDesc":"sample Description", "version":"v1.0.0","description":"This is sample description"},
    #     {"VxRail":"Pending","img":url+"/images/VxRail.png","title":"VxRail","smallDesc":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team.", "version":"v1.0.1","description":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team."}
    #   ]},{"title":"Technical Practictioner","values":[
    #     {"DellEMC":"Pending","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move."},
    #     {"Help a Customer":"Pending","img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows."}
    #   ]},{"title":"Employee Productivity","values":[
    #     {"Engage":"Pending","img":url+"/images/Engage.png","title":"Engage","smallDesc":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile.", "version":"v1.0.0","description":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile."},
    #     {"Spaces":"Pending","img":url+"/images/Spaces.png","title":"Spaces","smallDesc":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda.", "version":"v1.0.0","description":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda."},
    #     {"Help":"Pending","img":url+"/images/Help.png","title":"Help","smallDesc":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone", "version":"v1.0.3","description":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone"}
    #   ]},{"title":"Pipeline","values":[
    #     {"Self Service Portal":"Pending","img":url+"/images/E2E.png","title":"Self Service Portal","smallDesc":"A portal for making mobile apps.", "version":"v1.0.0","description":"The Self Service portal is a website that enables"},
    #     {"Sales Dashboard":"Pending","img":url+"/images/SD.png","title":"Sales Dashboard","smallDesc":"Provides the real time statistics of operations in Sales", "version":"v1.0.5","description":"Provides the real time statistics of operations in Sales"},
    #     {"EZDialer":"Pending","img":url+"/images/EZDialer.png","title":"EZDialler","smallDesc":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code.", "version":"v2.1.0","description":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code."},
    #     {"Burn Notification":"Pending","img":url+"/images/BN.png","title":"Burn Notification","smallDesc":"Burn Notification App send out notification status to the user’s smart watch.", "version":"v1.0.0","description":"Burn Notification App send out notification status to the user’s smart watch."},
    #     {"E2E MRP":"Pending","img":url+"/images/E2E.png","title":"E2E MRP","smallDesc":"sample Description", "version":"v1.0.1","description":"This is sample description"}
    #   ]}]
    ret =[ {"title":"Video","values":[
        {"desc_type":"video","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","version":"10.10.2018","smallDesc":"This is a sample video","url":"https://cf-e2.streamablevideo.com/video/mp4/4jguk.mp4?token=1522220711-bDlDne%2BuKjOP%2FQVsosf9%2BhxC47FHNwsSvjMX%2Bw6P1Z4%3D"},
        {"desc_type":"video","img":url+"/images/HaC.png","title":"Help a Customer","version":"10.10.2019","smallDesc":"This is a sample video","url":"https://cf-e2.streamablevideo.com/video/mp4/4jguk.mp4?token=1522220711-bDlDne%2BuKjOP%2FQVsosf9%2BhxC47FHNwsSvjMX%2Bw6P1Z4%3D"}
        ]},
        {"title":"Audio","values":[
        {"desc_type":"audio","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","version":"1.1.12","smallDesc":"This is a sample audio","url":"https://audio.clyp.it/of5issec.mp3?Expires=1522241732&Signature=j8PmHWUeuaQO25EEmAsbCnbYtqKMU4rF6Ml-Vckk2BQasxTOmXrtS5bqRn34kRrAxcZH7enFnstXRt~u2oC3Mdusnr~GBvcDCt-dSbfs1gecRa~wiNcIlQozWtBICezMqEbrXjBBt5jpIZOcL~RldS2b5tKYZ7SPGEY8tlsH-vE_&Key-Pair-Id=APKAJ4AMQB3XYIRCZ5PA"},
        {"desc_type":"audio","img":url+"/images/HaC.png","title":"Help a Customer","version":"12.2.04","smallDesc":"This is a sample audio","url":"https://audio.clyp.it/of5issec.mp3?Expires=1522241732&Signature=j8PmHWUeuaQO25EEmAsbCnbYtqKMU4rF6Ml-Vckk2BQasxTOmXrtS5bqRn34kRrAxcZH7enFnstXRt~u2oC3Mdusnr~GBvcDCt-dSbfs1gecRa~wiNcIlQozWtBICezMqEbrXjBBt5jpIZOcL~RldS2b5tKYZ7SPGEY8tlsH-vE_&Key-Pair-Id=APKAJ4AMQB3XYIRCZ5PA"}
        ]},
        {"title":"Normal Description","values":[
          {"desc_type":"description" ,"img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.","share":["https://i.imgur.com/qBnk1Bh.jpg","https://i.imgur.com/qBnk1Bh.jpg"],"message":"some message","subject":"some_subject","name":"sampleName.png","downloads":"https://i.imgur.com/qBnk1Bh.jpg"},
          {"desc_type":"description" ,"img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.","downloads":"https://i.imgur.com/qBnk1Bh.jpg","message":"some message","subject":"some_subject","name":"sampleName.png","share":"https://i.imgur.com/qBnk1Bh.jpg"},
          {"desc_type":"description" ,"img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows."}
        ]},
        {"title":"Graphs","values":[
          {"desc_type":"graph" ,"img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for ", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.","graphs":[{"type":"bar","title":"bar","url":url+"/get/data/bar"},{"type":"pie","title":"pie","url":url+"/get/data/pie"}]},
          {"desc_type":"graph" ,"img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all ", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.","graphs":[{"type":"bar","url":url+"/get/data/bar","title":"sampleTitle"}]}
        ]}
      ]
    
    try:
        ##print("inside here");
        if request.method=="GET":
            # if 'id' in request.args:
            #     ret['id'] = request.args['id']
            # if 'name' in request.args:
            #     ret['name'] = request.args['name']
            print(ret);
            print(request.headers);
            # if request.headers['Content-Type'] == 'application/json':
            #     print("headers work my lord")
            return Response(json.dumps(ret), status=200, mimetype='application/json')
        elif request.method=="POST":
            print(request.headers);
            print(request.get_json());
            if request.headers['Content-Type'] == 'application/json':
                content = request.get_json();
                if content['username'] == 'admin' and content['password']=='admin':
                    return '{"status":"success"}';

                elif content['username'] == 'sheenam.ohrie' and content['password']=='sheenam@123':
                    return '{"status":"success"}';

                elif content['username'] == 'akta.jain' and content['password']=='akta@123':
                    return '{"status":"success"}';
                
                elif content['username'] == 'mathew.basilthomas' and content['password']=='mathew@123':
                    return '{"status":"success"}';
                else:
                    return '{"status":"failure"}';
            else:
                return '{"status":"Inside post else"}';
    except Exception as e:
        ret = "error"
        return Response(json.dumps(ret),status=400,mimetype='application/json')

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('AppIcons',path);

# @app.route('/updateStatusApprove',methods=["POST"])
# def updateStatus():
#     print("inside here");
#     if request.method=="POST":
#         print("POST");
#         if request.headers['Content-Type'] == 'application/json':
#             print("inside headers");
#             content = request.get_json()
#             print(content);
#             for ele in ret:
#                 val=ele["values"]
#                 for row in val:
#                     print(row)
#                     if row[content['title']] == "Pending":
#                         row[content['title']] = "Approved";
#                         return '{"Success":"Approved"}'
#                     else:
#                         return '{"Success":"Already Approved"}'
#         else:
#             return '{"Failure":"failed"}'

@app.route('/get/data/bar',methods=['GET'])
def send_bar_data():
    ret = {
     "labels": ["Red", "Brown", "Blue", "Yellow", "Green", "Purple", "Orange"],
     "datasets": [{
       "label": '# of Votes',
       "data": [11, 15, 22, 4, 6, 2, 3],
       "backgroundColor": [
         'rgba(255, 99, 132, 0.2)',
         'rgba(244, 164, 96, 0.8)',
         'rgba(54, 162, 235, 0.2)',
         'rgba(255, 206, 86, 0.2)',
         'rgba(75, 192, 192, 0.2)',
         'rgba(153, 102, 255, 0.2)',
         'rgba(255, 159, 64, 0.2)'
       ],
       "borderColor": [
         'rgba(255,99,132,1)',
         'rgba(244, 164, 96, 1)',
         'rgba(54, 162, 235, 1)',
         'rgba(255, 206, 86, 1)',
         'rgba(75, 192, 192, 1)',
         'rgba(153, 102, 255, 1)',
         'rgba(255, 159, 64, 1)'
       ],
       "borderWidth": 1
     }]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json');

@app.route('/get/data/donut',methods=['GET'])
def send_donut_data():
    ret = {
     "labels": ["Red", "Brown", "Blue", "Yellow", "Green", "Purple", "Orange"],
     "datasets": [{
       "label": '# of Votes',
       "data": [12, 19, 3, 5, 2, 3,6],
       "backgroundColor": [
         'rgba(255, 99, 132, 0.2)',
         'rgba(244, 164, 96, 0.8)',
         'rgba(54, 162, 235, 0.2)',
         'rgba(255, 206, 86, 0.2)',
         'rgba(75, 192, 192, 0.2)',
         'rgba(153, 102, 255, 0.2)',
         'rgba(255, 159, 64, 0.2)'
       ],
       "hoverBackgroundColor": ["#FF6384", "#551a8b", "#36A2EB", "#FFCE56", "#FF6384", "#36A2EB", "#FFCE56"]
     }]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/line',methods=['GET'])
def send_line_data():
    ret = {
     "labels": ["January", "February", "March", "April", "May", "June", "July", "August"],
     "datasets": [
       {
         "label": "Initial Dataset",
         "fill": "false",
         "lineTension": 0.1,
         "backgroundColor": "rgba(75,192,192,0.4)",
         "borderColor": "rgba(75,192,192,1)",
         "borderCapStyle": 'butt',
         "borderDash": [],
         "borderDashOffset": 0.0,
         "borderJoinStyle": 'miter',
         "pointBorderColor": "rgba(75,192,192,1)",
         "pointBackgroundColor": "#fff",
         "pointBorderWidth": 1,
         "pointHoverRadius": 5,
         "pointHoverBackgroundColor": "rgba(75,192,192,1)",
         "pointHoverBorderColor": "rgba(220,220,220,1)",
         "pointHoverBorderWidth": 2,
         "pointRadius": 1,
         "pointHitRadius": 10,
         "data": [65, 59, 80, 81, 56, 55, 40, 32],
         "spanGaps": "false",
       },
       {
         "label": "Final Dataset",
         "fill": "false",
         "lineTension": 0.1,
         "backgroundColor": "rgba(175,92,192,0.4)",
         "borderColor": "rgba(31,156,156,1)",
         "borderCapStyle": 'butt',
         "borderDash": [5, 8],
         "borderDashOffset": 0.0,
         "borderJoinStyle": 'miter',
         "pointBorderColor": "rgba(31,156,156,1)",
         "pointBackgroundColor": "#fff",
         "pointBorderWidth": 1,
         "pointHoverRadius": 5,
         "pointHoverBackgroundColor": "rgba(31,156,156,1)",
         "pointHoverBorderColor": "rgba(220,220,220,1)",
         "pointHoverBorderWidth": 2,
         "pointRadius": 1,
         "pointHitRadius": 10,
         "data": [15, 39, 50, 81, 51, 55, 30, 70],
         "spanGaps": "false",
       }
     ]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/radar',methods=['GET'])
def send_radar_data():
    ret = {
     "labels": ["Eating", "Drinking", "Playing", "Designing", "Coding", "Dancing", "Running"],
     "datasets": [
       {
         "label": "Initial Dataset",
         "backgroundColor": "rgba(179,181,198,0.2)",
         "borderColor": "rgba(179,181,198,1)",
         "pointBackgroundColor": "rgba(179,181,198,1)",
         "pointBorderColor": "#fff",
         "pointHoverBackgroundColor": "#fff",
         "pointHoverBorderColor": "rgba(179,181,198,1)",
         "data": [65, 59, 90, 81, 56, 55, 40]
       },
       {
         "label": "Final Dataset",
         "backgroundColor": "rgba(255,99,132,0.2)",
         "borderColor": "rgba(255,99,132,1)",
         "pointBackgroundColor": "rgba(255,99,132,1)",
         "pointBorderColor": "#fff",
         "pointHoverBackgroundColor": "#fff",
         "pointHoverBorderColor": "rgba(255,99,132,1)",
         "data": [28, 48, 40, 19, 96, 27, 100]
       }
     ]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/polararea',methods=['GET'])
def send_polararea_data():
    ret = {
     "datasets": [{
       "data": [11, 16, 7, 3, 14],
       "backgroundColor": ["#FF6384", "#4BC0C0", "#FFCE56", "#E7E9ED", "#36A2EB"],
       "label": 'Current Dataset'
     }],
     "labels": ["Red", "Green", "Yellow", "Grey", "Blue"]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/pie',methods=['GET'])
def send_pie_data():
    ret = {
     "labels": ["Red", "Blue", "Yellow"],
     "datasets": [
       {
         "data": [300, 50, 100],
         "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56"],
         "hoverBackgroundColor": ["#FF6384", "#36A2EB", "#FFCE56"]
       }]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/bubble',methods=['GET'])
def send_bubble_data():
    ret = {
     "datasets": [
       {
         "label": 'Initial Dataset',
         "data": [
           { "x": 20, "y": 30, "r": 15 },
           { "x": 40, "y": 10, "r": 10 },
         ],
         "backgroundColor": "#FF6384",
         "hoverBackgroundColor": "#FF6384",
       }]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

@app.route('/get/data/mixed',methods=['GET'])
def send_mixed_data():
    ret = {
     "labels": ['Item 1', 'Item 2', 'Item 3'],
     "datasets": [
       {
         "type": 'bar',
         "label": 'Bar Component',
         "data": [10, 20, 30],
         "backgroundColor": "#F5DEB3"
       },
       {
         "type": 'line',
         "label": 'Line Component',
         "data": [30, 20, 10],
         "backgroundColor": "#F5DEB3"
       }
     ]
   };
    return Response(json.dumps(ret), status=200, mimetype='application/json')

if __name__  == '__main__':
    app.run(host='127.0.0.1', port=5001)
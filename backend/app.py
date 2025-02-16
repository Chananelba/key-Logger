from flask import Flask, request, jsonify
import os
import json
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return "server is run "
SAVE_FOLDER = os.path.join(os.getcwd(), 'data')

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json
    if data:
        folder_name = data["mac"]
        folder_path = os.path.join(SAVE_FOLDER,folder_name)

        if os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M") + ".json"
        file_path = os.path.join(SAVE_FOLDER,file_name)

        with open(file_path,"w") as json_file:
            json.dump(data,json_file,indent=4)

        return jsonify({"message": "Data saved", "file": file_name, "folder": folder_name}), 201



#טיפול בבקשת גט


#שליחת מידע לפרונט לפי מחשבים וזמנים

    #יצירת מילון לכל מחשב המפתח שם המחשב הערך מערך של כל התקיות של התאריכים




if __name__ == '__main__':
    app.run(debug=True)

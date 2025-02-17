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
    data = request.get_json()
    if data["data"]:
        folder_name = data["mac"]
        folder_path = os.path.join(SAVE_FOLDER,folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = datetime.strftime(datetime.now(),"%Y-%m-%d %H-%M") + ".json"
        print(file_name)
        file_path = os.path.join(folder_path,file_name)
        print(file_path)

        with open(file_path,"w") as json_file:
            json.dump(data["data"],json_file,indent=4)

        return jsonify({"message": "Data saved", "file": file_name, "folder": folder_name}), 201


@app.route('/add_user_details', methods=['POST'])
def add_user_details():
    pass



@app.route('/get_computer_list', methods=['GET'])
def get_computer_list():
    computers_list = []
    for item in Path(SAVE_FOLDER).iterdir():
        if item.is_dir():
            computers_list.append(item)
    return jsonify(computers_list),200


@app.route('/get_computer_files', methods=['GET'])
def get_computer_files():
    pass


@app.route('/get_users_details', methods=['GET'])
def get_users_details():
    pass


@app.route('/stop_tracking_computer', methods=['GET'])
def stop_tracking_computer():
    pass




#שליחת מידע לפרונט לפי מחשבים וזמנים

    #יצירת מילון לכל מחשב המפתח שם המחשב הערך מערך של כל התקיות של התאריכים




if __name__ == '__main__':
    app.run(debug=True)

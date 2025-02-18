from flask import Flask, request, jsonify, send_file
import os
import json
from datetime import datetime
from pathlib import Path
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

@app.route('/get_computer_list', methods=['GET'])
def get_computer_list():
    computers_list = []
    for item in Path(SAVE_FOLDER).iterdir():
        if item.is_dir():
            computers_list.append(item)
    return jsonify(computers_list),200

@app.route('/get_list_computer_files', methods=['GET'])
def get_list_computer_files():
    computer_name = request.args.get("computer_name")
    list_of_files = [item for item in Path(os.path.join(SAVE_FOLDER,computer_name)).iterdir()]
    return jsonify(list_of_files)

@app.route('/get_computer_file', methods=['GET'])
def get_computer_file():
    computer_name = request.args.get("computer_name")
    file_name = request.args.get("file_name")
    file_path = os.path.join(os.path.join(SAVE_FOLDER,computer_name),file_name)
    return send_file(file_path)


@app.route('/get_users_details', methods=['GET'])
def get_users_details():
    return send_file(os.path.join(os.getcwd(), 'users/user_details.json'))



@app.route('/stop_tracking_computer', methods=['GET'])
def stop_tracking_computer():
    pass


if __name__ == '__main__':
    app.run(debug=True)

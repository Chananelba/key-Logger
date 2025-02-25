## README: Keylogger Project

### Overview

This project involves building a basic cybersecurity tool: a keylogger. It is divided into three main parts:

1.  **KeyLogger Agent:** A program that runs on the target machine, collects keystrokes, encrypts them, and sends them to a server.
2.  **Backend (Flask Server):** A Flask server that receives the encrypted data, decrypts it, and stores it.
3.  **Frontend (User Interface):** A web page that displays the collected data.

**Warning:** This project is for educational purposes only. Do not use it for illegal or unethical activities.

### Part A: Keylogger Agent

#### Goal

Develop a system that simulates an advanced keylogger.

#### Steps

1.  **Design:** Plan the system architecture and divide responsibilities. Consider:

    *   How to separate keystroke collection (KeyLoggerService) from file writing management.
    *   How to manage the tool's memory.
    *   How to design the interface to easily add a NetworkWriter class in the future.
    *   Where encryption should be implemented.
2.  **Implement KeyLoggerService:** Create a KeyLoggerService class with the IKeyLogger interface to listen for and temporarily store keystrokes in memory.
3.  **Implement FileWriter:** Develop a FileWriter class responsible for writing data to a file.
4.  **Implement XOR Encryption:** Create an Encryptor class to perform basic XOR encryption on the data.
5.  **Implement KeyLoggerManager:** Develop a KeyLoggerManager class to manage the KeyLoggerService and FileWriter, handle data buffering, add timestamps, and perform encryption before sending data to the writer classes.
6.  **Keylogger Decryption:** Create a script (e.g., `decrypt_file.py`) that accepts the path to the encrypted file and the XOR key as command-line arguments, decrypts the file, and prints the decrypted content to the screen.
7.  **Implement NetworkWriter:** Implement a `NetworkWriter` class that implements the `IWriter` interface, using the `requests` library to send data to a server.

#### Additional Notes

*   Include a README file with instructions, a flow chart, and a description of the system architecture.
*   Consider error handling (Exceptions) and logging in each component.

### Part B: Backend (Flask)

#### Goal

Create a backend server to receive and store data from the keylogger and provide an API to retrieve the data.

#### Steps

1.  **Design:** Define the data architecture and how the information will be organized in the file system.
2.  **Setup:** Create a new directory called `backend` and create `app.py` (main server file) and `data/` (directory to store KeyLogger files).
3.  **Create Basic Flask Server:** Create a basic Flask server in `app.py`.
4.  **Create API to Receive Keylogger Data:** Create a Flask endpoint to listen for data submissions from the keylogger.
5.  **Create API to Return List of Machines:** Create an API endpoint to get a list of machines that the tool has been run on.
6.  **Create API to Retrieve Keystroke Data for a Specific Machine:** Create an API endpoint to retrieve keystroke data from a specific machine.

#### Additional Notes

*   Include a README file explaining how to run the server, the project directory structure, a description of each endpoint, and references to Flask documentation.
*   Consider adding advanced error handling and logs.

#### Deliverables

*   Source code in `app.py` with the following endpoints:

    *   `/` - Status message.
    *   `/api/upload` - Receives and stores Keylogger data.
    *   `/api/get_target_machines_list` - Returns a list of machines.
    *   `/api/get_keystrokes` - Retrieves log file content for a specific machine.
*   Directory structure emphasizing data organization under `data/`.
*   README file with instructions, flow chart, and system description.

### Part C: Frontend (HTML, CSS, JS)

#### Goal

Build a basic frontend interface to view the collected information.

#### Steps

1.  **Plan the interface:** Design a page to display a list of target machines and a display to show the keystrokes for each target machine.
2.  **Implement Target Machine Display Page:** Create an `index.html` file.
3.  **Write CSS File for Basic Styling:** Use CSS to style the page.
4.  **Pull the list of computers from the server:** Use the server API to get the list of target machines. Use JavaScript to do this, and update the table you designed in the previous step accordingly.
5.  **Pull Keystroke Data for a Specific Computer:** Use the server API from the previous step to get the list of keystrokes for a specific target machine.

async function get_computer_list() {
    let dropdown = document.getElementById("computer_list"); 
    dropdown.innerHTML = '';  

    let defaultOption = document.createElement("option");
    defaultOption.text = "Select a computer";
    defaultOption.value = ""; 
    dropdown.add(defaultOption);

    let computer_list = await get_computer_list_from_server();
    computer_list.forEach(function(computer_name) {
        let option = document.createElement("option");
        option.text = computer_name;
        dropdown.add(option);
    });


    clear_result();
}

async function get_computer_list_from_server() {
    const response = await fetch("http://127.0.0.1:5000/get_computer_list");
    const data = await response.json();
    return data;
}

async function on_computer_selected() {
    let dropdown = document.getElementById("computer_list");
    let selected_option = dropdown.options[dropdown.selectedIndex].text;

    if (selected_option) {
        const queryParams = new URLSearchParams({ computer_name: selected_option }).toString();
        const response = await fetch(`http://127.0.0.1:5000/get_list_computer_files?${queryParams}`);
        const data = await response.json();

        let filesSection = document.getElementById("files_section");
        filesSection.style.display = "block";
        get_files(data);

        clear_result();
    }
}

function get_files(data) {
    let fileDropdown = document.getElementById("computer_files");
    fileDropdown.innerHTML = ''; 

    data.forEach(function(fileName) {
        let option = document.createElement("option");
        option.value = fileName;
        option.text = fileName;
        fileDropdown.add(option);
    });
}

async function get_file_details() {
    let dropdown_file = document.getElementById("computer_files");
    let selected_file = dropdown_file.options[dropdown_file.selectedIndex].text;

    let dropdown_computer = document.getElementById("computer_list");
    let selected_computer = dropdown_computer.options[dropdown_computer.selectedIndex].text;

    const queryParams = new URLSearchParams({
        computer_name: selected_computer,
        file_name: selected_file
    }).toString();

    const response = await fetch(`http://127.0.0.1:5000/get_computer_file?${queryParams}`);
    const data = await response.json();

    let result = document.getElementById("result");
    result.textContent = JSON.stringify(data, null, 2); 
}


function clear_result() {
    let result = document.getElementById("result");
    result.textContent = '';
}

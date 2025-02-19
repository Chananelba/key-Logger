count = 0
font_size = 40

// computer_list = get_copmputer_list_from_server()
async function get_somthing(){

    let dropdown = document.getElementById("computer_options");
    dropdown.innerHTML = '';
    let computer_list = await get_copmputer_list_from_server();

    computer_list.forEach(function(computer_name) {
        let optins = document.createElement("option");
        optins.text = computer_name;
        dropdown.add(optins);


    })

}
async function get_copmputer_list_from_server(){
    const response = await fetch("http://127.0.0.1:5000/get_computer_list");
    const data = await response.json();
    return data;
    // fetch("http://127.0.0.1:5000/get_computer_list")
    // .then(response => response.json())
    // .then(data => {computer_list = data;
    //     console.log(computer_list);
    //      return computer_list;
    //     })    
}

async function getSelectedcomputer(){
    let dropdown = document.getElementById("computer_options")
    let select_option = dropdown.options[dropdown.selectedIndex].text
    const queryParams = new URLSearchParams({computer_name :select_option}).toString();
    const response = await fetch(`http://127.0.0.1:5000/get_list_computer_files?${queryParams}`);
    const data = await response.json();
    let undisplay = document.getElementById("computer_files_rpresent")
    undisplay.style.display = "block"
    // let result = document.getElementById("result")
    // result.textContent  = JSON.stringify(data,null,2)
    getfiles(data)
}

function getfiles(data){
    let fileDropdown  = document.getElementById("computer_files")
    fileDropdown .innerHTML = '';
    data.forEach(function(fileName) {
        let option = document.createElement("option");
        option.value = fileName;  
        option.text = fileName;  
        fileDropdown.add(option); 
    });
}

async function getSelectedfile(){
    let dropdown_file = document.getElementById("computer_files")
    let select_file = dropdown_file.options[dropdown_file.selectedIndex].text
    let dropdown_computer = document.getElementById("computer_options")
    let select_computer = dropdown_computer.options[dropdown_computer.selectedIndex].text
    const queryParams = new URLSearchParams({computer_name: select_computer, file_name: select_file}).toString();
    const response = await fetch(`http://127.0.0.1:5000/get_computer_file?${queryParams}`);
    const data = await response.json();
    let result = document.getElementById("result")
    result.textContent  = JSON.stringify(data,null,2)


}


// function get_somthing(){
//     document.getElementById("first_button").style.color = "green"
//     if (count == 0){
//         document.getElementById("list").innerHTML = new_line() 
//     }
//     else {
//         document.getElementById("list").style.fontSize = increas_font_size()
//         document.getElementById("list").innerHTML += new_line() 
//     }
// }
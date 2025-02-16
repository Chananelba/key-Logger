count = 0
font_size = 40

computer_list = ["A","B","C"]
function get_somthing(){

    let dropdown = document.getElementById("computer_options");
    //computer_list = get_copmputer_list_from_server()
    computer_list.forEach(function(computer_name) {
        let optins = document.createElement("option");
        optins.text = computer_name;
        dropdown.add(optins);


    })

}
function get_copmputer_list_from_server(){
    let computer_list = []
    return computer_list

}

function getSelectedOption(){
    let dropdown = document.getElementById("computer_options")
    let select_option = dropdown.options[dropdown.selectedIndex].text
    let result = document.getElementById("result")
    result.textContent  = select_option
    

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

function new_line(){
    count = count + 1 
    

    return "line" + String(count) + "\n"
}

function increas_font_size(){
    font_size++
    return String(font_size) + "px"
}
function add_computer_optins(){

}
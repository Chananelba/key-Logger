let users = {}

window.onload = async function(){
    users =  await load_users();
}
async function load_users(){
    fetch("http://127.0.0.1:5000/get_users_details")
    .then(response => response.json())
    .then(data => {users = data;
        console.log(users);
         return users;
        })  
        
}

function log_in(){
    let username = document.getElementById("Username_input").value
    let password = document.getElementById("Password_input").value
    if (username in users && password === users[username]){
        window.location.href = "../web_page/index.html";
    }
    else{
        alert("username or password are wrong")
    }
    
}
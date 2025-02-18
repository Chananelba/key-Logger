let users = {}

window.onload = function(){
    users = load_users();
}

function load_users(){
    fetch("users.json")
    .then(response => response.json())
    .then(data => {users = data;
        console.log(users);
         return users;
        })      
}

function sudmit(){
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    let verify_password = document.getElementById("verify_password")
    if (verify_password.style.display == "none" || verify_password.style.display == "" ){
        if (username in users && password == users[username]){
            window.location.href = "../learn.html"
        }
    }
    else{
        if(username in users ){

        }
        else{
            if(password == verify_password.value){
                users[username] = password
                
            }
            else{
            }
        }
    }
}

function new_user(){
    let verify_password = document.getElementById("verify_password")
    if (verify_password.style.display == "none" ||verify_password.style.display == "" ){
        verify_password.style.display = "block"
        document.getElementById("sign_up").textContent = "sign in"
    }
    else{
        verify_password.style.display = "none"
         document.getElementById("sign_up").textContent = "sign up"
    }
}
var my_user_name ="chananel"
var my_password = "1234"

function sudmit(){
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value

    if (username == my_user_name && password == my_password){
        window.location.href = "../learn.html"
    }
}
function new_user(){
    let verify_password = document.getElementById("verify_password")
    if (verify_password.style.display == "none"){
        verify_password.style.display = "block"
        document.getElementById("sign_up").textContent = "sign in"
    }
    else{
        verify_password.style.display = "none"
         document.getElementById("sign_up").textContent = "sign up"

    }

}

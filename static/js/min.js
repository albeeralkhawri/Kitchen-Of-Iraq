// this for password confirm Sign Up form
var password = document.getElementById("password"),
confirm_password = document.getElementById("confirm_password");
  
// This message appears when the password does not match
function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  }
  else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
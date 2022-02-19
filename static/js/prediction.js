function Login(){
    email = document.getElementById("inputLogin").value;
    password = document.getElementById("inputPassword").value;
    console.log("sucess")
    if(email=="zineb.oufqir@esith.net" && password=="1990" || email=="youssef.chamrah@esith.net" && password=="1990" ){
        
        alert("Login Succefully!")
        $("form").attr('action','form.html')
   }
   else{
       alert("Incorrect email or password!")
   }
}
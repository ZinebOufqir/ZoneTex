document.write(`
<nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
<div class="container-fluid">
  <a class="navbar-brand" href="#">ZoneTex</a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsExample02">
    <ul class="navbar-nav me-auto">
      <li class="nav-item">
        <a class="nav-link active"  href="form.html">Predict</a>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="another.html">another</a>
      </li>
    </ul>
    </div>
    <form >
      <button type="button" class="btn btn-light text-dark me-2">Save</button>
      <button   class="btn btn-primary" type="submit" onclick="Logout()" >Logout</button>
    </form>
  
</div>

</nav>
<script>
  function preventBack() { window.history.forward(); }  
setTimeout("preventBack()", 0);  
window.onunload = function () { null };
  function Logout(){
      
      if (confirm("You sure wanna lougout ?") == true) {
        $("form").attr('action','login.html');
     } 
      
  }
</script>`)
        
        
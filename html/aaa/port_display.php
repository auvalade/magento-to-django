<!doctype html>
<html>

<?php
$sys = strtoupper(PHP_OS);
 
if(substr($sys,0,3) == "WIN")
{
	error_reporting(E_ERROR);
	echo "Windows !<br/>";
        $ports = array(COM1, COM2, COM3, COM4, COM5, COM6, COM7);
}
elseif($sys == "LINUX")
{
	echo "Linux<br/>";
        $ports = array('/dev/ttyUSB0', '/dev/ttyACM0','/dev/tty0','/dev/tty1','/dev/tty2','/dev/tty3','/dev/tty4');
}
else
{
	echo "Other OS, using Windows COM names";
	$ports = array(COM1, COM2, COM3, COM4, COM5, COM6, COM7);

}


$available_ports;

foreach($ports as $port)
{
	$fp = fopen ($port, "r");
	
	if($fp)
	{
		$available_ports[] = $port;
		fclose($fp);
	}
}

if(count($available_ports)>0)
{
	echo '<select name="COM Select" >' ;
	echo '<option value="">Select your COM port...</option>';
	foreach($available_ports as $port)
	{
		echo '<option value="'.$port.'">'.$port.'</option>' ; 
	}
	echo'</select>';
}
else
{
	echo "No COM ports available !<br/>Check if your APM is connected or if your port is not already used !";
}
?>
</html>

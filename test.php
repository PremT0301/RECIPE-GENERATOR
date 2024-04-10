<?php

$server="localhost";
$username="root";
$password="";
$dbname="recipe";

$con=mysqli_connect($server,$username,$password,$dbname);

if(!$con)
{
    echo"not connected";
}

$Email=$_POST['email'];
$name=$_POST['Name'];
$password=$_POST['password'];
$cpassword=$_POST['cpassword'];

$sql="INSERT INTO `test`(`Email`, `Name`, `password`, `confirm password`) VALUES ('$Email','$name','$password','$cpassword')";

$result=mysqli_query($con,$sql);

if($result)
{
    echo "data submit";
}
else
{
    echo "faild";
}

?>
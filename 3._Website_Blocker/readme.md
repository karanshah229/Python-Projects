# Website Blocker

## Features

1. A python program that blocks a user from visiting certain  
websites within working hours
2. The user can enter all the websites that he thinks distract  
him during working hours and steal his focus
3. The way this works is by modifying the HOSTS file on the  
system. The program will redirect all the websites from the  
list to 127.0.0.1
4. The program will **automatically** detect the time and allow  
the user to visit the websites if working hours are over

### Technology Learnt and Used:
1. datetime Module - To check if it is working hours or not
2. pyw to make an executable python script

---

## Install Instructions

1. Git clone the repository or alternatively download all the files in this folder
2. Navigate to download location in explorer and double click on website_blocker.pyw  
Note: Make sure you are logged in as Administrator
3. This will add all the entries in the file and remove them automatically
4. Now if you try to visit these websites in working hours, you will be redirected

## Screenshots

![alt text](https://github.com/karanshah229/Python-Projects/blob/master/3._Website_Blocker/screenshots/website_blocker.jpg "Website Blocker")  

##### Note:
Make sure you are logged in as Administrator  
To run this on startup itself, create a task in task scheduler and schedule it to  
run on startup
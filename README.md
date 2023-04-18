# FITDownloader

## Python and selenium script used for automatic file tracking


The purpose of this project was to allow students of FIT Mostar to track their lecture files more easily. This script can do the following:

* Automatic login to the system based on your credinentials
* Checking if any files were uploaded on todays date
* Selection of all new files
* Downloading and sorting of new files

You can watch the showcase of this project here: <a href='https://youtu.be/duaW2D-OKh0'>Click me :D</a>
  

## How to setup FITDownloader
First of all for this project to work you need to have Python and Selenium package installed.
You can download python from the following link:
<a href='https://www.python.org/downloads/'>

After you download python you need to install Selenium, you can do that via pip commands
<img src='https://www.swtestacademy.com/wp-content/uploads/2017/04/python-selenium-4.png'>

<br/>  
After successfully installing both python and selenium, the only thing left is to enter your login credinentials in data.json file
<img src='https://i.imgur.com/63WEzwP.png'>
Once you do that the only thing left is to enter you download path, and path of directory where you want your folders to be created
<img src='https://i.imgur.com/WvOpSIU.png'>

## How to use FIT Downloader
After the initial setup for the script to work, you need to run folderSetup.py. The purpose of that file is to create
folders with names of your subjects based on the data you entered I data.json.
After that the only thing left is to run main.py and you are good to go.

# To do
Project is still in development due to my academic obligations, so some of the things i still need to implement are:
* moveToFolder function inside main
* code optimisation
* fix downloadsLog

# Kalahari LMS
### This is the repository for the Kalahari Experience Education Project's Learning Management System.

Demo: [lms.luke.net.za](http://lms.luke.net.za)

One of my main focuses as part of the Kalahari Education Experience Project has been developing the Learning Management System (LMS).  This allows students in the Kalahari to access important learning resources like videos, Wikipedia, Khan Academy, on their devices for free and without data costs.

Here are some screenshots of what it looks like

![1](https://github.com/user-attachments/assets/bd38d50f-558e-4b47-af4b-ce9478f197d0)

Landing Page

![2](https://github.com/user-attachments/assets/8f6efeca-f59c-40df-95e4-2f4dc3aa0481)
![3](https://github.com/user-attachments/assets/a2639f81-36cc-447e-ac3b-642432cabc18)


Student created content and past papers

![4](https://github.com/user-attachments/assets/ec103771-77d6-42b0-b943-b42f35f55907)

Student made videos explaining important content


## Getting started guide
This guide is for how to set up your computer to edit the code for the LMS and commit your changes to the repository.
This is assuming that you use VScode as your code editor.

1. Download the following programs if you don't have them already

[Python]([url](https://www.python.org/downloads/)) (If you are on Windows, make sure to allow it to add Python to your path in the installer when you are setting it up)
[VScode]([url](https://code.visualstudio.com/download))
[Git]([url](https://git-scm.com/downloads))
[Github for desktop]([url](https://desktop.github.com/download/))

And restart VScode if you have it open.

2. Open VScode and clone the LMS Repo
![image](https://github.com/user-attachments/assets/faf287e1-a7aa-440d-a4a0-e0a206796977)
File > New Window

![image](https://github.com/user-attachments/assets/f601336d-fb75-43c6-8cbc-0490a54b88a7)
Clone Git Repository

Copy paste this URL into the dialogue box that appears
https://github.com/luke-da-nuke/lms/

Select a folder to clone to
This downloads the code for the LMS to your computer so you can edit it.

3. Use pip to install requirements.txt
Open the terminal in VScode with Ctrl + ` or selecting View > Terminal from the menu bar
```
pip install -r requirements.txt
```
This installs all the libraries needed to run the program

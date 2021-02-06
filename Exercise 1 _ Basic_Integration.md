# Intern_Test
GIT repository for managing the codes and documents required to fulfill the proposed tasks

## Notes:
To open the presented pages, it is recommended to go through the following steps:

### 1.1. Python
Install the most recent Python version (https://www.python.org/downloads/). Choose between [32-bit] or [64-bit] according to your system's settings.

In the first installation window, select the option ** Add Python 3.x to PATH ** and continue the installation normally.

### 1.2. PIP
The pip already comes installed for Python versions 3.4 (or higher).
To find out if it is installed, open your terminal and enter the "pip" command.

If you have not installed it, go to the save [this file](https://bootstrap.pypa.io/get-pip.py) as ** git-pip.py ** and, in the terminal, type "python get-pip.py"

### 1.3. Modules
Before running the platform, you must have the following modules installed on your Python environment:

- "flask"

All of those modules can be downloaded through the "pip install" command for windows users, or through "sudo pip install" for mac/linux, inside the command prompt.

### 2. Run System
First, you have to enter the directory ("working directory") in which the shared files were saved to the user's computer through the following command inside the command prompt:
"cd (disk):\...\workingdirectory" ,  in which you should access the platform's folder ("workingdirectory") through its directory inside your computer.

Finally, to run the system, type the following command inside the command prompt:

"python open.py"

### 3. Open Cloudfront and Level3 HTML pages
After running the system in the command prompt, it is presented the localhost in which the webpages are being run. The server response should be equivalent to what is presented in the image below:

![Python Open](https://github.com/henriquewills/Intern_Test/tree/main/images/Python_Open.jpg)

In this example, the server is being run at the "(localhost) = 127.0.0.1:5000". For accessing the CloudFront and Level3 test pages, the user should input in the web browser the following URLs:

- CloudFront: http://(localhost)/video_CloudFront
- Level3: http://(localhost)/video_Level3

# Members Database Application

This is a web application powered by Django. It is used to create and manage the data of members of an organisation, group, institution or anywhere that requires the tracking of followers data. This application has the following functionalities:

*Add new member data* <br />
*View the data of a member* <br />
*Edit the data of a member* <br />
*Delete the data of a member* <br />

## :hammer_and_wrench: Tools and Technologies
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg" title="SQLite" alt="SQLite" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="PostgreSQL" alt="PostgreSQL" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-original.svg" title="CSS3" alt="CSS3" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JS" alt="JS" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original.svg" title="Bootstrap" alt="Bootstrap" width="40" height="40"/>&nbsp;

### Other Tools
<img src="https://github.com/devicons/devicon/blob/master/icons/vim/vim-original.svg" title="Vim" alt="Vim" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" title="VS Code" alt="VS Code" width="40" height="40"/>&nbsp;

## Application Development Timeline
This describes the process I used to create the application.

### Requirements Analysis
The project began with the analysis of requirements and specifications of the system. As a web application, it will be accessed mainly on mobile phones, tablets, laptops and desktop computers. 

**Usage Requirements**<br />
The application will require users to be authenticated anytime they want to access the platform. The user must therefore create an account with the system before proceeding with anything else.

**Typical Execution Process**<br />
For a user accessing the platform for the first time, the typical process follows the steps below:

- User accesses the main page with the platform's domain address
- User clicks on **here** link just below the login button to access the sign up page
- User provides *username, email address, password* and confirms *password*
- Login instructions are sent to the provided email address
- Using the link provided in the instructions, user accesses the platform’s **login** page
- User provides username and password to login
- If successful, user lands on the application’s **dashboard**

### System Design
At this stage, I converted the specifications and requirements into layout designs, showing where buttons, textboxes, textfields, and other widgets will be placed on the platform. Also, colours and how the platform's various parts can be accessed through navigation.

### Application Development
The next stage in the timeline is development of the platform. At this stage, I turned the design layouts, system requirements and specifications into source code using the specified tools and technologies for the project.

### Testing and Deployment
The final stage in the development timeline is testing the completed platform to ensure it produces the expected output. Finally, the platform was deployed to Heroku for the world to see.

*Note:*
**The link of the platform will be shared when development is complete**

---
## Application Domains
This section describes the various parts of the platform

### User Authentication
This is used to verify the identity of the user to grant access to the platform. There is no external authentication and the user will be required to either sign up or provide a username and password to login to the system.

### Dashboard
This is the main access point of the application. A successful login will bring the user to the dashboard. All features of the application can be accessed from here. The features include: *members, member details, new member, user profile and logout*

### Member Details
This section enables the user to access the details of a member. It can be accessed by either clicking on the **name**, or **photo** of a member

### New Member
This section has a form and enables a user to create a new object. It can be accessed from the navigation bar by clicking on the **New Member** button

### User Profile
This section permits a user to access and manage his or her information.

## Other Features

### Search
This widget enables a user to search for a particular member from a sea of  members. It is found on the navigation bar of the dashboard. Search for a member can be done by either **last name, first name, age, gender** or **status**

*Have fun exploring*

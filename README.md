DEVPIE - https://devpie.herokuapp.com/home

To create a microblog community and space for developers to gather and share about their development or issues they are facing or faced not just at work but throughout their journey. 

UX
This website will be aimed at users of similar communities (in this case Jr developers) to expand their network, to update on the latest news , discuss on emerging trends and share about their journey/problems/anything actually in a space where most of the people are going through similar situations. Users make use of the site to share and benefit from having convenient access to the information provided by all other members.
Features

The features of this application are as follows:
* Ability to Register, Sign into and Logout of an Account
* Ability to Create, Edit, Delete and View Posts
* Ability to upload photo for use as  profile picture
* Ability to update username and password.
* Ability to to scroll through older or current posts via pagination.

Features Left to Implement
* Searching / filtering of posts

Technologies Used

SQLALCHEMY
PYTHON
FLASK
JINJA2
HTML, CSS, SCSS

Testing

Manual Testing
For manual testing I have tested on the following browsers. Firefox, Chrome, Edge and IE11.
Scenarios
* Registering a user that already exists on the system
* Registering an email that already exists on the system
* Register a new user
* Login with incorrect details
* Login in with correct details
* Create a new post
* Edit a post
* Delete a post
* Update profile picture
* Updating username
* Logout
After running each possible scenario multiple times, going over each feature, user stories and client requirements I then validated my HTML and CSS using the following:
* HTML Validation
* CSS Validation
CONTRIBUTIONS
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Deployment

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base.
The development version of my application is on GitHub and I push this code using git push origin master and the code is run and tested on Cloud 9 before being updated to heroku
Create a remote Git repo for your app on Heroku

After you push your app to the repo, Heroku will serve the app from there.
1. If not already done, login to Heroku in your command-line interface:
$ heroku login
2. Run the following command:
$ heroku create your-app-name
Change "your-app-name" to whatever you want to name your app. You can expect that common names like “my-app” or “tutorial” will already be taken. You can omit the name and let Heroku generate a random name that you can change it later. Example:
$ heroku create
Example response:
Creating app... done
This is a one-time-only requirement. Heroku creates a remote git repository that you'll link to a local Git repo in the next section. This setup will let you use a simple git push command to deploy your app to the server.
1. Run the following 3 commands one after the other:
$ git init
$ git add .
$ git commit -m "my first commit"
This creates a local Git repository and adds you files to it. You'll connect this local repo to a remote repository on Heroku in the next step.
2. Make sure you're logged in to Heroku ($ heroku login), then run the following command to set your Heroku app repo as the remote repo of your local repo:
$ heroku git:remote -a your-app-name
Important: Change "your-app-name" to whatever is the name of your app. Example:
$ heroku git:remote -a devpie
3. To verify you set the remote repo, run:
$ git remote -v
Prepare the app files for deployment

When deploying, the following configuration files need to be included in the web app's root directory:
* Procfile
* runtime.txt
* requirements.txt
1. In a text editor, create a file named Procfile and make sure it contains the following line:
web: python sample_app.py
A Procfile lists the app's process types and the commands to start each process. The Bottle app runs a single web process, which is started by executing the python sample_app.py command.
2. Create requirements.txt 
3. pip freeze --local > requirement.txt
Add the new config files to your local repo:
4. 
$ git add .
$ git commit -a -m "Add config files"
Push the app to Heroku

In this step, you deploy the app to Heroku for the first time.
1. If not already done, login to Heroku and enter your Heroku email and password when prompted:
$ heroku login
2. Deploy the app:
$ git push heroku master

Credits

Would like to credit https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database for his tutorials and videos for this project to take place.
# Mama's Letterbox

<div align="center">
    <img src="#" alt="#"/>
</div>
<br>

[View deployed site here](#)

## Project Description
Many people try to reduce the presence of screens in their lives and go back to activities they used to enjoy before screens took over our lives. Writing letters is one of them. Being a parent of a young child during the pandemic has been a challenging and often isolating experience for many parents, especially moms. This website seeks to help parents, especially but not exclusively mothers of young childen, to make meaningful connections with other parents around the world through letters.

The current version of the application is an MVP designed to provide basic functionality. In the future, additional functionalily will be implemented to allow a hopefully growing number of users to search the website more effectively and create more appealing profiles.

Currently, the general goals of the application are:
* Provide visitors with a sense of the goals of the application
* Provide login, logout, and new user registration functionality
* Provide plan subscription functionality
* Allow registered users to create and update their personal profile
* Allow registered and subscribed users to view other users' profiles and contact them via email


## UX

### Core Target Audience
#### The core target audience of this application is:
* Parents, especially mothers, who are interested in establishing meaningful connections with other parents
* Parents, especially mothers, who are looking to spend less time in front of screens 
* Parents, especially mothers, who would like to send and receive more snail mail again


#### Users of this application are searching for:
* Other parents with similar interests and/or children of similar ages to connect
* A way to increase the amount of offline acctivities in their lives

#### Client Stories
Client Stories and the status of the features in response to those stories can be found in the User Stories Overview[https://docs.google.com/spreadsheets/d/1CRY7aYiLONmYjMFSnk4xuDKDCOrky4-98dOgRmqB0fU/edit?usp=sharing].

### Wireframe Mockups: 
- [Landing Page](media/mamasLetterboxHOME.png)
- [About Page](media/mamasLetterboxABOUT.png)
- [Login Page](media/mamasLetterboxHLOGIN.png)
- [Profile Page](media/mamasLetterboxPROFILE.png)
- [Profile Creation Page](media/mamasLetterboxCREATE.png)
- [Profile Editing Page](media/mamasLetterboxEDIT.png)
- [Subscription Page](media/mamasLetterboxSUBSCRIPTION.png)
- [Penpals Listing Page](media/mamasLetterboxLIST.png)


## Features
#### Across Pages
Every page features a responsive **navigation bar** with conventional placing of **logo** (top left).

Every page features a background appropriate to the theme of writing letters. 

Every pages features an **account icon** in the upper right corner to allow visitors to easily register or login and to allow logged-in users to log out.

#### Registration
The registration page allows new users to register. The **input fields** for username and password have input **validation** to ensure the new account is properly set up. Users who are already registered can get to the login page by clicking on the **account icon** in the upper right corner.

#### Login
The login page allows existing users to log in to their account. The **input fields** for username/e-mail address and password have input **validation** to ensure the input matches the requirements for each field. New users can get the registration page by clicking either on the **account icon** in the upper right corner..

#### Landing Page
The landing page tells visitors in a few simple words what the website is about. The **Start Here button** directs to the About page and thus provides a quick way to learn more.

#### About Page
The About page tells visitors more about the project, its goals, current fucntionality, and future features.

#### My Profile Page
This page is visible only to registered users. Newly registered users are directed to the **Create Profile page** to create their personal profile for other users to see. Existing users can see the information they have provided and use the **Edit Profile button** to update their profile.

##### Find a Penpal! Page
This page is visible only to subscripers. Users who have not purchased a subscription, are directed to the **Subscription page**. Subscribed users can see a list with the basic data of all registered users: name, age (if entered), and country of residence. By clicking the **View Profile button**, subscribers can see additional profile details and make initial contact with the profile owner if desired.

#### Subscription Page
The subscription page directs the user to Stripe, where they can purchase a subscription, currently available at the symbolic price of $0.50 to allow new users to test out the site without any risk while additional features are still being developed. This approach will hopefully make more users purchase a subscription and thus make the site more attractive for future users.

### Existing Features
- Header Navigation Bar - Exists on [every page](base.html) and allows all users to easily navigate all the website's pages and find what they are looking for quickly, including being led back to their profile page when cklicing on the **logo**. (When clicking on the logo while not logged in, the login page will reload.)
- [Registration Page](register.html) - Allows new users to open an account and leads existing users to the login page throughte embedded link or by clicking on the Log In item in the navbar.
- [Login Page](login.html) - Allows existing users to log in to their account and leads new users to the registration page throughte embedded link or by clicking on the Log In item in the navbar.
- [Add Client Page](addClient.html) - Displayed only to logged in users. Provides interface to enter and save new client information.
- [Manage Clients Page](clientInfo.html) - Displayed only to logged in users. Displays the organization names of all saved client information entries *in alphabetical order* and allows uers to view the complete entries, delete them, and access the edit page. 
- [Edit Client Page](editClient.html) - Displayed only to logged in users. Allows users to modify every line of the selected client information entry and either save or discard the changes. Automatically displays the current date in standard U.S. format at the top of the page.
- [New Invoice Page](invoice.html) - Displayed only to logged in users. Allows users to create an invoice by using the dropdown menus and textfields that are part of the form and converting the completed form into ready-to-share pdf document at the end.
- [Profile Page](profile.html) - Displayed only to logged in users. Provides quick explanations of and direct links to the different functionalities of the application.

### Features to Implement in the Future
- POST request-based functionality for users to submit additional personal information on the profile page, which will then be added to the invoice header via GET request.
- Functionality to add rates to the database the same way it is currently possible to add client information.
- A modal confirming a user's intent to delete a client information entry.
- Forgot password functionality.


## Technologies Used

### Workspace

- [Gitpod](https://www.gitpod.io/)

### Languages

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python3](https://www.python.org/)

### Frameworks, Libraries, Other

- [Heroku](https://dashboard.heroku.com/). The cloud platform used to deploy and run the code pushed to the associated GitHub repository.
- [Django](https://www.djangoproject.com/) - The project was built using Django's web framework.
- [SQLite](https://www.sqlite.org/index.html) - default Django's database used in development.
- [PostgreSQL](https://www.postgresql.org/) - production database through Heroku.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - CSS framework.
- [jQuery](https://jquery.com/)
- [Google Fonts](https://fonts.google.com/)
- [AWS Amazon S3](https://aws.amazon.com/s3/) - Amazon Simple Storage Service (Amazon S3) was used to store media and static files used in the project.
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/docs) - Stripe was used for the online payment authentication and processing system.

### Version Control

- [Git](https://git-scm.com/)
- [Github](https://github.com/)

### Wireframes

- [Balsamiq](https://balsamiq.com/)

## Testing 
Testing information can be found in a separate [TESTING.md file](TESTING.md).

## Deployment
This project was developed using the [Gitpod](https://gitpod.io) deveopment environment, committed to git, and pushed to GitHub using the Gitpod terminal. 

To deploy this page to [Heroku](https://heroku.com/) from its [GitHub repository](https://github.com/katjacodes/invoicingApp), the following process was completed: 
1. Log in to Heroku
2. Click **"]New** and select **Create New App** from the drop-down menu in the upper right half of the window. 
3. Enter a **Name** for your application. The name needs to be unique. Next, select the **Region** closest to your geographical location. When you're finished, click **Create App**.
4. In the navbar at the top of the page, click on **Settings**, scroll down to the **Reveal Config Vars** button, and click it.
5. Enter the following information:
    IP: 0.0.0.0
    MONGODB_NAME: [name of the MongoDB cluster you are using for your application]
    MONGO_URI: [the URI you created after setting up your collection in MongoDB found by logging in to MongoDB > navigating to the cluster that holds the collection you are using for your application > clicking on "Connect" > selecting "Connect your application" > selecting the correct driver & version > copying the generated string & replacing the placeholders in it with your own information]
    PORT: 5000
    SECRET_KEY: [copy from the [env.py](env.py) file
    Click **Add** after entering each variable.
6. Scroll down and click **Buildpacks** and select **Python**, then click **Save changes**.
7. In the navbar at the top of the page, click on **Deploy**, scroll down to **Deployment method**, and select **GitHub**.
8. **Authorize** the connection to GitHub.
9. Search for your **GitHub repository name** and select the repository holding the code for you application.
10. Make sure the **Main Branch** is selected for deployment and select **Enable Automatic Deploys** for Heroku to automatically re-build your application every time you push your code to GitHub.
11. Click the **Deploy Branch** button. Once Heroku has built the application, a pop-up message will confirm deployment
12. You can click the **View** button to be taken directly to the site.

At the moment of submitting this Milestone project the Development Branch and Main Branch are identical. 

### How to Clone the Repository
To clone this project into Gitpod you will need a Github account and an HTML 2 PDF Rocket account. You can [create a Github account here](https://github.com/), and you can [create an HTML 2 PDF Rocket account here.](https://www.html2pdfrocket.com/).

Then follow these steps:
1. Log into [Gitpod](https://gitpod.com) with your gitpod account.
2. Navigate to the [Project GitHub repository](https://github.com/katjacodes/invoicingApp)
3. Click the green "Gitpod" button in the top right corner of the respository
4. This will trigger a new gitpod workspace to be created based on the code in GitHub. There, you will be able to work locally.

To work on the project code within a local IDE such as VSCode, Sublime Text, etc.:
1. Navigate to the [Project GitHub repository](https://github.com/katjacodes/invoicingApp)
2. Click the "Code" download button next to the green "Gitpod" button.
3. In the Clone section, select HTTPs and copy the clone URL for the repository. 
4. Open your local terminal.
5. Change the current working directory to the location where you want the cloned directory to be located.
6. Type ```git clone```, and then paste the URL you copied in Step 4.
7. Press Enter for your local clon to be created.

You will need to create an HTML to PDF Rocket account to obtain an API key for the API that will allow you to create PDF a PDF version of your invoice. To do so, follow these steps.
1. Ater you [create your HTML 2 PDF Rocket account](https://www.html2pdfrocket.com/), you will be sent your API key to the email you registered with. At that time, you can also update your password.
2. Navigate to to the [Code Examples page](https://www.html2pdfrocket.com/Examples/javascript) and copy the HTML and JavaScript code to create a button that will allow you to create PDF documents.
3. Make sure to update the following information in the code:
    - Your API key
    - The URL of the page you want turn into a PDF document, i.e., the URL of your invoice page.


## Credits
### Content
- The background image was created by [Ramiro Menes for Unsplash](https://unsplash.com/photos/sMCBEI5zkqc) and made available under the [Do Whatever You Want License](https://unsplash.com/license).

### Code
- The [Code Institute Walk-Through project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching) for Milestone 3 was taken as a starting point for the set-up of the base, addClient, clientInfo, editClient, login, register, and logout templates and edited heavily.
- The [Code Institute Walk-Through project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching) for Milestone 3 was taken as a starting point for parts of the [app.py](app.py) file.
- HTML, CSS, and JS code for the scroll-to-top button originally taken from [W3 Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top) and edited slightly to fit project needs.
- The JavaScript code for the automatic date set function on the invoice page was taken from [W3 Schools](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_tolocaledatestrin) and edited to display the date in U.S. format.
- The JavaScript code for the addition of charges on the invoice page was taken from [Codegrepper](https://www.codegrepper.com/code-examples/javascript/calculate+two+number+and+diplay+next+field+without+reload+the+page+javascript) and edited to fit project needs.
- The HTML and JavaScript code for the integration of the PDF conversion API was taken from [HTML 2 PDF Rocket](https://www.html2pdfrocket.com/Examples/javascript) and edited to fit project needs.
- Joshua Ugba helped me understand how to connect Python and Javascript for the automatic address field population section of the invoice page.


### Acknowledgements
- The Code Institute Slack Community and my session with a tutor was really really helped me out by providing pointers when I got stuck and unable to see the forest for the trees.
- Joshua Ugba took the time to explain to me in depth how to integrate JavaScript and Python. I owe a better understanding of JSON files to him. 
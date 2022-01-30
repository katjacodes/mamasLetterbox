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
Client Stories and the status of the features in response to those stories can be found in the [User Stories Overview](https://docs.google.com/spreadsheets/d/1CRY7aYiLONmYjMFSnk4xuDKDCOrky4-98dOgRmqB0fU/edit?usp=sharing).

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
- Header Navigation Bar - Exists on [every page](templates/main-nav.html) and allows all users to easily navigate all the website's pages and find what they are looking for quickly, including being led back to their profile page when clicking on the **Account icon** and the on **My Profile**. (When clicking on the icon while not logged in, a visitor will be able to either register or log in.)
- [User Account Administration](templates/allauth) - This site uses the **Allauth** package to provide vistors with comprehensive user account management, including account creation and email verification, login, logout, and forgotten password recovery.
- [Profile Creation](penpals/templates/penpal_create) and [Profile Editing](penpals/teamplates/penpal_edit) allowys registered users to create and edit their [personal profile](penpals/templates/penpal_detail) tied to their user account and visible to users with subscriptions.
- [Penpal Listing](penpals/templates/penpal_list) allows **users** to see a list of other registered users, their age, language(s), and location. **Subscribers** can click on a button next to the profile and see more profile details including **contact information**.
- The [Subscription Feature](subscriptions/templates/home) allows users to purchase a monthly subscription, currently at a trial price of U.S. $0.50/month to be able to view complete profile details of other users registered in the penapl database and contact them. Existing subscribers have the option to cancel their subscription using the **contact link** provided in the [Subscribers' view of the page](subscriptions/templates/subscriber.html).

### Features to Implement in the Future
- Profile pictur feature as part of the penpal profile.
- Integrated chat option.
- Ability to manage subscription directly from the website. 
- A blog spotlighting existing members


## Technologies Used

### Workspace

- [Gitpod](https://www.gitpod.io/)

### Languages

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python3](https://www.python.org/)

### Frameworks, Libraries, Other

- [Heroku](https://dashboard.heroku.com/) - The cloud platform used to deploy and run the code pushed to the associated GitHub repository.
- [Django](https://www.djangoproject.com/) - The project was built using Django's web framework.
- [SQLite](https://www.sqlite.org/index.html) - Pefault Django's database used in development.
- [PostgreSQL](https://www.postgresql.org/) - Production database through Heroku.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - CSS framework.
- [jQuery](https://jquery.com/) - JavaScript framework.
- [Google Fonts](https://fonts.google.com/) - Additional fonts.
- [AWS Amazon S3](https://aws.amazon.com/s3/) - Amazon Simple Storage Service (Amazon S3) was used to store media and static files used in the project.
- [Font Awesome](https://fontawesome.com/) - Icons.
- [Stripe](https://stripe.com/docs) - Stripe was used for the subscription plan.

### Version Control

- [Git](https://git-scm.com/)
- [Github](https://github.com/)

### Wireframes

- [Balsamiq](https://balsamiq.com/)

## Testing 
Testing information can be found in a separate [TESTING.md file](TESTING.md).

## Deployment 
(Steps taken from and followed based on [Fraciska Du Toit's project Happybean](https://github.com/Franciskadtt/happybean))

#### Setup an enviroment for variables
You now need to set up the database with environment variables. Create a file titled env.py and make sure it is placed on top of the of file structure, on the same level as the app.py file. Alternatively, they can be added to the workspace variable section. 

Option 1: Env.py file:
```
 os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('DEVELOPMENT', 'True')
 os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your_variable_here>')
 ```
- In ` settings.py`  add:
```
if os.path.exists("env.py"):
    import env
```
-  Add your env.py file to `.gitignore`, before pushing your changes.


<br>Option 2: Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_CH', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_SUB', VALUE = '<your_variable_here>'
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

- In ` settings.py`  add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = 'DEVELOPMENT' in os.environ
```

### **Heroku Deployment**
- Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
- Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
- In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
- Search for your repo (or sign in and connect GitHub account) and select this.
- Then click "Hide Config Vars" in Heroku.
- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the `settings.py file`, you will need to comment out the 'SQLite and Postgres databases' section and uncomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet).
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
- Create a superuser with the following command, and fill in the required information.:
    ```
    python3 manage.py createsuperuser
    ```
- In the `settings.py` file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Install gunicorn and freeze that to the requirements file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
- Create a Procfile and inside, add the following:
    ```
    web: gunicorn mamasLetterbox.wsgi:application
- In `settings.py`, use an if statement so that when the app runs on Heroku, you will connect to Postgres, and otherwise, it will connect to sqlite3:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
- Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    ```
- Log in to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app happybean
    ```
- Add your Heroku app and local host to allowed hosts in `settings.py.`
- Push to Github, and then to Heroku master. 
- In Heroku, go to the 'Deploy' tab. In the section 'Deployment Method' click on 'Github - Connect to Github'. Make sure your Github profile is displayed. Add the repository name and click on 'Search'. After Heroku has found the repository, click on 'Connect'. This will connect your Heroku app to your GitHub repository. Click 'Enable automatic deploys'. Your code will automatically be deployed to Heroku as well. 

### **AWS (Amazon Web Services)**
Create an account with [AWS](www.aws.amazon.com), follow the steps and sign in. 
- Go to the AWS management console and go to the S3 service. There, create a new bucket. Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Go to the buckets properties, and turn on static website hosting. Select 'Use this bucket to host a website', and fill in index.html and error.html, then click 'save'.
- Go to the permissions tab, and go to CORS configuration. Paste in a CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Go to the Bucket policy tab and click 'policy generator', to create a policy. Choose 's3 bucket policy', allow all principals by typing a star. From the action dropdown menu select 'GetObject'. Copy the ARN and paste it into the ARN box. Then click 'add statment' and then click 'generate policy'. Copy the policy into the bucket policy editor. Add a slash star onto the end of the resource key. Click 'save'. 
- Go to access control list tab, under public access, click on 'Everyone', select 'List Objects'. Then click 'save'. 
- Go to IAM (from services menu), click on 'groups' and create a new user group. Give the group a group name (f.e. 'manage-happybean'). Then click 'create group'. 
- Click 'policies' in the dashboard, and then click 'create policy'. Go to the JSON tab. Click 'import managed policy'. Import 'AmazonS3FullAccess'. Get the bucket ARN from the bucket policy page in S3, and paste that in after 'Resource', as a list (first the ARN, then also the ARN with a slash and star). Click 'next tags' and then 'next review'. Give it a name and description. Click 'create policy'. 
- Go to 'groups'. Click the manage-happybean group. Go to 'permissions'. Click 'attach policy'. Select the policy you just created. Click 'add permissions' and then 'Attach policy'.
- Go to 'users'. Click 'add user'. As username write 'happybean-staticfiles-user. Give programmatic access. Click 'next'. Add the user to the group. Click through to the end. Download the .csv file. 

### **Connecting to DJANGO to S3**
- Go back to GitPod. Install boto3 and Django storages, and freeze them to the requirement file with the following commands:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
- Add 'storages' to the installed apps in the settings.py file.
- Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'happybean'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
- On Heroku, add the AWS keys to the Config Variables (they can be found in the csv file you downloaded earlier). Also, add USE_AWS and set it to True. 
- Remove the DISABLE_COLLECTSTATIC from the variables. 
- In GitPod, create a file called custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S#Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION 
    ```
- To the before mentioned if statement from above, in settings.py, also add:
    ```
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
- Add, commit and push these changes. If you now go to the bucket, you will see all the static files. 
- Go to your bucket and add a new folder called media. Inside it, click 'upload' and then 'add files'. Then select all the images you'd like to use. Click 'next'. Under 'manage public permissions', select 'grant public read access'.
- On Stripe, add a new webhook endpoint, with the URL of your Heroku app, followed by 
```/checkout/wh/```. Select 'receive all events' and click 'add endpoint'.

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

You will need to create a [Stripe account](https://stripe.com/) to integrate payment function for the subscription plan.


## Credits
### Content
- The background image was created by [Egor Myznik for Unsplash](https://unsplash.com/photos/goqv5ZsmjfY) and made available under the [free to use Unsplash License](https://unsplash.com/license).

### Code
The [Code Institute Boutique Ado project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) was used as a starting point for the HTML templates in the Home application and some of the HTML templates in the Penpals application.

The [Code Institute Hello Dango module](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/1e823874aa044d92aa949431864834e5/0b913e08a887468b9e5448274ff16372/) was used as a starting point for the views of the Penpals application.

[Nik Tomazic's tutorial on Django Stripe Subscriptions](https://testdriven.io/blog/django-stripe-subscriptions/) was used as a starting point for the subscription functionality.

Benoît Blanchon helped me fix a bug that caused issues with my loccal Gitpod environment, taught me how to write my own decorators to restrict access to certain parts of my site to paying subscribers, and helped me debug my Penpals model and the views in my Subscriptions application.


### Acknowledgements
- Benoît Blanchon took the time to explain decorators and sginals to me and helped me get a better understanding of the way Djano and Stripe work together.
- Dom Habersack is an invaluable help whenever I have JavaScript-related questions. (And I continue to have many.)
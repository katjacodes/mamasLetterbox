# Mama's Letterbox – Testing details

[Main README.md file](README.md)

[View website on Heroku](#)

## Testing
To check the validity of HTML, CSS, JavaScript, and Python code, I used **[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)**, **[W3C Markup Validation](https://validator.w3.org/)**, **[JSHint](https://jshint.com/)**, and **[PEP8 online](http://pep8online.com/)**.


### Client stories testing:

#### Testing client stories from UX section of the [READEME file](README.md)
Client stories were tested by going through the [User Stories Overview](https://docs.google.com/spreadsheets/d/1CRY7aYiLONmYjMFSnk4xuDKDCOrky4-98dOgRmqB0fU/edit?usp=sharing) and noting the results in the last column. The current version of the application works for all clients stories that are checked off. Stories that are not checked off require functionality that will be implemented in a future version. (See Features to Implement in the Future section of the [READEME file](README.md).)


#### Manual (logical) testing of all elements and functionality on every page on mobile, tablet, and desktop
##### User Account Management Features
Visitors are able to 
- create a new account.

Registered users
- are able to log in.
- receive an account verification email upon registration.
- are able to reset their password password should they forget theirs. 

###### Landing Page for the General Public
- Navbar item and Start Here! button both direct to the About page
- Account icon dropdown menu allows visitors to either register or log in

##### Navbar for Registered Users
- All navbar items direct to their respective pages
- Account icon dropdown menu allows registered users to access their penpal profile or log out

##### My Profile Navbar Item & Page for Registered Users
- For users who have already created a penpal profile: Profile page with buttons that allow to edit or delete the profile
- For users who have yet created a penpal profile: Redirection to the Profile Creation page

##### Find a Penpal! Navbar Item & Page for Registered Users
- For users who have purchased a subscription: List of other other registered users featuring name, age, location, and a button to view the full profile
- For users who do not have a subscription: List of other other registered users featuring name, age, and location. The button "View Profile" button redirects to the Subscriptions page

##### Subscription Navbar Item & Page for Registered Users
- For users who have purchased a subscription: a page reminding them that they have already purchased a subscription and a button to send an email to cancel it
- For users who do not have a subscription: a page providing subscription details and a button directing them to Stripe to purchase a subscription


## Bugs Discovered

### String Method not Working
```
def __string__(self):
        return self.name
```


#### Solution:
Changed to 

```
def __str__(self):
        return f'{self.name}'
```

based on information found in the documentation for [a flake8 plug-in](https://github.com/rocioar/flake8-django/wiki/%5BDJ08%5D-Model-does-not-define-__str__-method).

### ``` NOT NULL constraint failed ```

```
NOT NULL constraint failed: home_item.childAge2
```

#### Solution: 

```
"blank=True" "null=True" 

````

require an additional ``` default value ```.





#### JavaScript Date Shown in the Wrong Format
- Using the JavaScript ``Date()`` constructor, the date at the to of the invoice template did not appear in the desired format.

- Using a customized function that including a location setting allowed me to set the date to standard U.S. format, i.e., the format of the region where the app will be used:

<figure align="left">
    <img src="static/img/testing/jsDate.png" alt="JavaScript code of a customized date function used to display the current date in U.S. standard format"/>
    <figcaption>JavaScript code of a customized date function used to display the current date in U.S. standard format</figcaption>
</figure>


### List of Clients Disappared

- At one point, the list of clients on the manage clients page completely disappeared.

- Using Google Developer Tools, I discovered the following:

 ```list``` in ```clientInfo``` had been missing. Below the fixed code:\
```@app.route("/get_clientInfo")```\
```def get_clientInfo():```\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```clientInfo = list(mongo.db.clientInfo.find())```\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```return render_template("clientInfo.html", clientInfo=clientInfo)```\


### Failure to Display Multiple Dropdown Menus on the Same Page
- Initially, I did not magage to display several different dropdown menus on the invoice page. This is the code I was usinng:

<figure align="left">
    <img src="static/img/testing/severalDropdowns.png" alt="Python code that did not allow me to display more than one dropdown menu on the invoice page"/>
    <figcaption>Python code that did not allow me to display more than one dropdown menu on the invoice page</figcaption>
</figure>


### Buttons on Edit Client Page Not Centered on iPad
- During initial testing of responsiveness, the buttons on the editc client page were not centered on iPad screens.
- I solved the problem by writing my own CSS code instead of using the Materialize styling.


### JavaScript Function at the Bottom of Invoice Page not Adding Amounts
- Initially, the field for the total remained blank even after selecting amount from the dropdown menus.
- Through Google research I realized that I needed to save the rates in the Int64 format, not as strings, in MongoDB.
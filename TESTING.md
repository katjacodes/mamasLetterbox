# Mama's Letterbox – Testing details

[Main README.md file](README.md)

[View website on Heroku](#)

## Testing
To check the validity of HTML, CSS, JavaScript, and Python code, I used **[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)**, **[W3C Markup Validation](https://validator.w3.org/)**, **[JSHint](https://jshint.com/)**, and **[Pylint](https://pypi.org/project/pylint/)**.

Note on **PEP8 Testing**: Pylint throws errors regarding certain classes not having 'objects' members. After doing some research, I learned [that Django automatically creates classes, which Pylint does not recognize](https://forum.djangoproject.com/t/class-question-has-no-objects-member-pylint-no-member/4024) and have decided to leave the error message.


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


### URLs in Penpals App not Accessible

Despite creating all the urlpaths, the pages could not be found

#### Solution:
Based on on this [Stackoverflow solution](https://stackoverflow.com/questions/55429392/django-url-pattern-not-being-found), I was able to modify the urlpaths and get them to work.
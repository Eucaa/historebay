# Historebay

Welcome to Historebay, the safe haven for all favorite antiques and requisitions you'd never thought to see again!

[![Build Status](https://travis-ci.org/Eucaa/historebay.svg?branch=master)](https://travis-ci.org/Eucaa/historebay)

## Heroku
To see this application live with Heroku, click here: [_Historebay_](https://historebay.herokuapp.com/)

## UX 
This fictional application has been created to let people find antiques, collectables and reproductions of products whom where produced in the past. All items are bought by Historebay themselves and are put on sale for a certain fixed amount.
Visitors are able to see all available items of Historebay, they also check details of an item and add them to the cart.
However, only registered users will be able to buy the products. So creating an account will be necessity to be able to make a purchase. 
The user will be automatically revered to the login page to cover this. 

As we are dealing with an antiques oriented webite, I have tried to make it easy to use for people who have reached a higher age.

General User Stories:

* As a user type, I would like to be able to see what ware the website has to offer me without giving any personal data.
* As a user type, I would like an easily readable a accessible website.
* As a user type, I want to be able to create an account with my own username and password, and login with these credentials each time I want to access the application.
* As a user type, I would like to buy products from the website without having to make too many clicks.
* As a user type, I want to be able to add, adjust the quantity and delete products from my cart.
* As a user type, I would like to check this website on multiple devises so that I will be able to buy products and check what is new when I'm not using a pc.
* As a user type, when registering, I would like to create my own personal user name and password that is not restricted or automatically generated.
* As a user type, when registered, I would like to work with an easy to-use-payment system when buying my products.
 
Wireframes:

* The original wireframes have been created using Balsamiq Mockups 3. For view [_Wireframes_](https://github.com/Eucaa/historebay/blob/master/docs/Wire%20Frames%20CI.pdf).
* The original ERD has been created in the MySQL Workbench and can be fond here: [_ERD_](https://github.com/Eucaa/historebay/blob/master/docs/ERDCI%20DB.png).
* The original workflow has been thought the app Pencil and is show here: [_Workflow_](https://github.com/Eucaa/historebay/blob/master/docs/Workflow%20CI.pdf). 

# Existing Features
* A home-function thats will re-direct the user back to the home page from where ever else they are located at that time.
* Two dropdown features, so users will be able to find products based on their chosen Category or the Product Type.
* Login/Register form - this will allow the user to either log into an existing account or create a new account, inserting them into the database.
* Password reset - this will allow the user to choose a different password when its lost or for security reasons.
* Cart amount indication - this will show the quantity of items that are currently in the cart.
* Cart function - when clikcing on "cart" the user will be automatically redirected to the cart view and check their products in cart.
* Search bar option - the search will handle the search of a products by entering (a part of) the name or the description of a product that the user is searching for.
* Search bar drop-down - when using the search bar, this function will show the options of all available products that have the description in it.
* Details option - a button that allows the user to check the futher details of a product (e.g. the category).
* Quantity bar - to add a quantity to the product that a user wishes to purchase.
* Add option - a button to add a product to the cart.
* Adjust option - a button to adjust the amount of the product that a user currently has resevered in their cart or either add it to the cart, from the details view.
* Delete option - a button to delete an item from the cart.
* Checkout option - a button to refer to the payment view.
* Payment option - a button to confirm and proceed with purchase.
* Re-direct user to register - this function automatically redirects the unregistered user to the login screen where they can either log in to their account or continue further to create one to purchase products from Historebay.
* Profile - allows the user to see their profile which is registered in the database. 

## Features Left to Implement
* Favorite option - to let users favorite a product. 
* Broad description of product - on the details page only, a more broad description of a product it's whereabouts, origin and previous owners can be given.
* A suggestion option - if a registered user adds a product to their cart, a suggested and related product could be shown via related tags that the products might have.
* Newsletter Subscription - there could be a newsletter to inform registered user about newly arrived products on the page.
* Online chat with Historebay - an online chat with Historebay where registered users can contact historebay directly.
* Tracking system - to inform registered users on where their puchases are located at that moment.
* Futher expansion of the user's profile page. E.g. letting users see the current address they are registered under and adding a profile picture.

# Known Issues
A lot of issues have been solved and committed to GitHub on a very regular basis. However, there are stil some things that will need to get resolved.
* A feature I wanted to add was to actually send out an email to the registered user when they wanted to reset their password. The option will provide the user a standard email with instructions
  on how to proceed to dot so, including a temp password which could be changed when arriving in the correct view. This is a build-in function of Django. Since I needed to use Django version 
  1.11, there seem to have been a problem with generating the url to send the email. A communnication error between http and https usage. 
  I have tried to get around this problem by using an external email service called [_EmailJS_](https://www.emailjs.com/), which I had used before in my cv and have also been using the create the contact form in this project.
  However, since this is Django build-in function content, it could not correspond with eachother. The code that I used was a follow:
  ```
  $("#reset-password").submit(function(event) {
        email = $("input[name='email'").val();
        resetUrl = $("input[name='reset_url'").val();
        console.log(email);
        console.log(resetUrl);
        emailjs.send("gmail", "password_reset_request", {
            "from_email": email,
            "reset_url": resetUrl
        },"user_r7tdLbadZRBs7vClusXBr")
        .then(
            function(response) {
                $("#emailaddress").val("");
                $(".alert").removeClass('hide').addClass('show')
                document.location = "/"
                console.log("SUCCESS", response);
            },
            function(error) {
                console.log("FAILED", error);
            }
        );
        return false;
    });
    ```
    After deletion of the above code and on advise, since information was given that gmail was a problem causer why emails wehere not send, i tried to add the following code to tell gmail
    that Django is a save platform to use:
    ```
    EMAIL_USE_TLS = True
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    ```
    The above code however is an instruction related to a newer version of Django (django 2.1). It does generate the email but still not send the actual. Proof of this is generated
    inside the [_console_](https://github.com/Eucaa/historebay/blob/master/docs/blep5.PNG).
    These logs can also be checked by using the command `$ heroku logs -a historebay --tail` in the command terminal.
    So now, the user will see the message that "a new password has been sent by email", but the email itself does not arrive.

    The activation of SMTP can be done by activating a [_2-step-verification_](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome). However, this requires an additional access
    to a private gmail account, which I am not willing to give for this project.
    A solution for this could be that the educator provides a dummy email address there these kind of issues can be arranged upon, or perhaps make the lesson material more compatible with the current
    version of the programs and platforms you are required to work with.

    As I had to keep to true to my dealine, I will need to try and fix this issue some other time.
    This is the reason why `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` is stil set to console and not SMTP.

* To host images in your static files, I was instructed by the Institute to create a "S3 bucket" through AWS cloud services, as Heroku is not able to hold certain images that are added to the project.
  For, this I was required the make an account at AWS. I already had two previous ones (since I hade made a previous project by using the AWS platform. However, credits kept running low quickly so I
  had to make an extra account and thus and extra email address to be able to finish that project on the same platform or I would have lost the data), I chose one of these to start up the procedure.
  For this setup, it is necessary to give your private credit- or debit card details. This is a requirement that AWS needs to verify your account so you can open this cloud server bucket. AWS will 
  deduct a temporary amount of 0,01 cents from your private bank account and will deposit this back later.
  Since I do not own a credit card, I tried to use my debit card details. However, my bank card does not support Mastercard or Visa etc(a bank card and credit card are really two separate things),
  so I was not allowed to create a bucket for myself. I have contacted Code Institute for support and ask how to solve this. Unfortunately, they could not give me any solutions and advised me to
  contact AWS help desk myself, which I did. After explaining the situation to the AWS customer service, they informed me that a debit card must also have MasterCard or Visa option for it to be able to
  work. So they couldn't really help me out either. 
  To resolve this, an good option would be to let the Institue open a AWS account where students can apply for a bucket, or provide a credit card number that can be used specifically for this project part
  only. The most basal option would be to at least inform future students about this issue before they start this part of the project.

  All images can be viewed normally in the development area. 

# Technologies Used
* [HTML5](https://www.w3schools.com/html/html5_intro.asp)
    - This project uses HTML to build the foundation of the web application and includes links to [_Bootstrap_](https://getbootstrap.com/docs/4.4/getting-started/introduction/), Bootstrap JS, CSS, and Font Awesome.
* [CSS](https://www.w3schools.com/css/)
    - This project uses CSS to style the features of the web application, including the header, footer and each page of the application. It is also used to modify Bootstrap 4 styles.
* [Javascript](https://www.w3schools.com/js/)
    - This project uses JavaScript to provide the functionality for the Stripe API and for the functionality of the search field, the contact form and the carousel. The carousel JS is provided by Bootstrap 4.
* [Python](https://www.python.org/)
    - This project uses Python to provide the backend functionality, including functions to report bugs.
* [Django](https://www.djangoproject.com/)
    - This project uses Django, a Python Web framework for pragmatic design.
* [Stripe](https://stripe.com/en-nl)
    - This project uses the Stripe payment API, providing a secure payment form for the application.
* [JQuery](https://jquery.com/)
    - The project uses JQuery to simplify DOM manipulation.
* [Google Fonts](https://fonts.google.com/)
    - The project uses the font Domine as chosen letter type.
* [Font Awesome](https://fontawesome.com/)
    - This project uses Font Awesome to provide icons for the application.
* [WhiteNoise](http://whitenoise.evans.io/en/stable/)
    - This project uses WhiteNoise to host the staticfiles for Heroku.
* [Balsamiq Mockups](https://balsamiq.com/wireframes/desktop/)
    - This project used Balsamiq Mockups for the Skeleton and Surface Plan, providing views of the web application.
* [MySQL](https://www.mysql.com/products/workbench/)
    - This project used MySQL for the creation of the ERD to show entities (main tables) of the database and relationships between tables within that database.
* [Pencil](https://pencil.evolus.vn/)
    - This project used Pencil Project for the creation of the workflow, to show the the route that a user can experience when entering the website and making a purchase.

# Testing
_____
## Manual Testing
Below are scenarios which a user may experience while navigating the website. These have been used to manually test the application's features.

* Log in
    1. Click on 'Login' in navigation bar
    2. Fill in your username and password
    3. Be presented with the message 'login successful'
    4. When either not filling in the required input, user will receive a notification to complete this.
* Register
    1. Click on 'Register' button in the navigation bar.
    2. Fill in the required fields.
    3. Click on register button.
    4. User now has a profile.
    5. Be presented with the message 'successfully registered'.
    6. When either not filling in the required input, user will receive a notification to complete this.
* Log out
    1. When a user clicks on 'Log out' when logged in in the navigation bar.
    2. A message 'successfully logged out' will appear.
* Profile
    1. Click on 'Profile' button in the navigation bar.
    2. User can see his or her own Profile.
* Reset password
    1. When a user wants to change their password or dont remember theirs then they can click on the 'reset password' option.
    2. A new view to enter the users email address will appear.
    3. Fill in the emailaddress you have chosen for your account and click 'reset password'.
    4. The user will get a unique link in their emailaddress to change their password
* Category and Product Types dropdown
    1. Click on Category or Product Types in the navbar.
    2. User is presented with a dropdown which shows all available categories and product types.
    3. When a user clicks on a certain category or product type, he/she will be redirected to view with a available products of that specific tag.
* View product details
    1. Under the description of a product (which already can be viewed from the home page), user can click the 'details' button for more information about a product.
    2. When clicked, the user will be redirected to the details page.
    3. Products can be added via the product details view by filing in the quantity and clicking the 'adjust' button.
* Add product to cart
    1. Below the image and description of a product, an option is available to add a product by quantity.
    2. Fill in the quantity and click 'add' to add the product to the cart.
    3. Products can also be added via the product details view by filing in the quantity and clicking the 'adjust' button. 
* Viewing from cart
    1. Click on 'cart' in the navbar and get redirected to a view with an overview of all products available in cart.
    2. When clicking the 'details' button, the user will be redirected to the details page.
    3. The quantity of products can be adjusted by filing in the quantity and clicking the 'adjust' button.
    4. Product can also be deleted from the cart by using the 'delete item' button.
    5. A total price is provided at the bottom of the view.
    6. This view also contains a checkout button that, when clicked, will redirect the user to the payment view.
* Pruchasing products
    1. When arriving in the checkout view, a user will see a static overview of all products to be purchased together with a total price.
    2. The user will be presented with a payment to fill out personal data to be able to finalize the purchase.
    3. The user will receive an in-built notification if something required has not been filled in.
    4. The purchase will be finalized once the user has clicked the 'submit payment' button. 

## Responsive Testing
This website has been tested on different device screen sizes using Google Chrome Developer Tools so that this website functions responsively on all device screen sizes.

## Code Validation
HTML code has been passed through the official W3 Validator. Errors within the code have been corrected. CSS code has been passed through the official W3 Validator.

## Continuous Integration
The Continuous Integration was handeled by [_Travis_](https://travis-ci.org/) which constantly tested my app every time when the project got pushed to GitHub.

### Testpayment
In accordance with the instruction given by [_Stripe_](https://stripe.com/docs/payments/checkout), test payment can be done by inserting the following dummy card details:
* 4242 4242 4242 4242 (payment successful)
* 4000000000009995 (decline of insufficient_funds)
* 4000002500003155 (Requires authentication which, in this integration, will pop up a modal for the user to authenticate)
* CCV: 125 (but you can use anything really, as long as it's not any longer than 3 digits)
* Choose a month that lies in the future of the month you are currently testing in (e.g when it's June choose a month from July to December)

# Deployment
_____
To run this app locally:
1. Create a new repository in GitHub workspace name and description.
2. Create a virtual environment by choosing the Code Institue Repository Template (CI student required).
3. Click the button 'Gitpod' in your new environment to get automatically redirected to a workspace in Gitpod.
4. Install the correct version of Django for this project `$ pip3 install django==1.11.28`
5. Start the project itself `$ django-admin startproject *name of project*` followed by `$ django-admin startapp accounts`. 
6. Install requirements with pip3 install -r requirements.txt.
7. Create an env.py file with the following:
```
    - import os

        - os.environ.setdefault('STRIPE_PUBLISHABLE', "")
        - os.environ.setdefault('STRIPE_SECRET', "")
        - os.environ.setdefault('SECRET_KEY', '')
        - os.environ.setdefault('DATABASE_URL', '')
```

8. Make sure you uncomment `DATABASES ={}` for either Gitpod or Heroku in settings.py depending on where you want to view the app from.
9. You will need to generate your own SECRETKEY. You will need to set up a Stripe account and use their testing API keys. Once you have a database set up (you can use Postgres for database on Heroku) you can uncomment os.environ.setdefault('DATABASE_URL', '') and use the key that PostgreSQL generates for you in Heroku's Config Vars.
10. Make migrations with python3 manage.py makemigrations.
11. Migrate with python3 manage.py migrate.
12. Create a super user with python3 manage.py createsuperuser and follow instructions in your terminal.
13. To run the application locally, type in python3 manage.py runserver.

## Heroku
To see this application live with Heroku, click [here](https://historebay.herokuapp.com/)

1. Log into Heroku and Create New App. Create a unique name and region (USA or Europe, whichever is closest to you).
2. Navigate to Resources and search for 'PostgreSQL' - choose 'Hobby Dev - Free' and select 'Provision'. 
3. Go to Settings and Reveal Config Vars - copy and paste the following keys and its values (for this particular project) into the fields.
    - DATABASE_URL
    - EMAIL_HOST
    - EMAIL_HOST_PASSWORD
    - EMAIL_HOST_USER
    - SECRET_KEY
    - SITE_HOST
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
4. In Config Vars, also add `DISABLE_COLLECTSTATIC = 1` to instruct Heroku to ignore running the manage.py collecstatic command during the deployment process.
5. Run `$ python3 manage.py makemigrations` and `$ python3 manage.py migrate`.
6. Create a new super user for the production database with `$ python3 manage.py createsuperuser` and follow instructions in the terminal.
7. `$ pip3 freeze > requirements.txt` to make sure requirements.txt is up to date. 
8. Create a Procfile and add the text `web: gunicorn finalmilestone.wsgi:application` inside of it.
9. In settings.py, comment out import env and set DEBUG = False.
10. In Heroku, go to Deploy and select GitHub as a deployment method. Find your repository. Manually deploy the master branch. Activate automatic deploys.
11. Add the deployed Heroku link to ALLOWED_HOSTS in settings.py and git push origin master. The Heroku app should now be working.

## Development vs Deployed Version
In the development version, Debug is set to True and the env.py file is imported into settings.py. However, in the deployed version, Debug is set to False. 
The env.py file is not pushed to GitHub or Heroku as this contains keys which need to remain hidden from other users. 
The deployed version uses Heroku's PostgreSQL database whereas the development version uses SQLite.

# Credits
_____
## Content
The most basic setup for this app came from the lessons of Code Institue. The checkout of Stripe i used is from [_stripe checkout_](https://testdriven.io/blog/django-stripe-tutorial/).
All written content is finctional, parts of the terms & conditions where produced by the [_Privacy Policy Generator_](https://www.privacypolicies.com/blog/ecommerce-terms-conditions/) on privacypolicies.com
to give these a more realistic feel. 
The contact form sends emails via the external email service called [_EmailJS_](https://www.emailjs.com/).

## Media
The [_Historebay logo_](https://github.com/Eucaa/historebay/blob/master/static/css/img/heb_logo2.png) and [_brand/icon_](https://github.com/Eucaa/historebay/blob/master/static/css/img/heb_icon.png) 
where created by myself. The monocle used in these images comes from the free of use image source [_VHV_](https://www.vhv.rs/).

The images for the carousel where taken from:
- [Pixabay](https://pixabay.com/)\ 

The images for the products where taken from:
- [Momsforpennies](https://www.momspenniesfromheaven.com/store.php/momspennies/)
- [Deviantart](https://www.deviantart.com/)
- [F2HO](https://www.collectables-f2ho.com/en/)
- [Pinterest](https://nl.pinterest.com/)
- [Express](https://www.express.co.uk/)
- [Reddit](https://www.reddit.com/)
- [RPF](https://www.therpf.com/forums/whats-new/posts/285061/)
- [Trocadero](https://www.trocadero.com/directory/Antiques/Regional-Art/Asian/Japanese)
- [Worthpoint](https://www.worthpoint.com/)

### Credits
I would to credit the following sources for their inspiration:
Stack Overflow community
CodePen community

### Acknowledgement
I especially would like to thank my mentor Anthony Ngene, Arjan Speiard and some of the tutors of Code Institute for their support throughout this project.
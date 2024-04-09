# Otaku Blog

Otaku Blog is a blog style review site created using Django Frameworks and Libaries.
On the site, users can:
1. Register as a user of the site by creating an account and logging in.
2. Read reviews posted to the site.
3. Comment on the posted review.
4. Edit their comments once they have been posted to the site.
5. Delete their comments once they have been posted to the site.
6. Like and unlike posts.

On the site, admin can:
1. Write and post reviews to the site.
2. Save posts as drafts before publishing them.
3. Approve all comments before they are posted and become visible on the site.

This has been developed as my 4th Portfollio Project for my Full Stack Software Development Diploma with Code Institute.

The project can be viewed here: [Otaku Blog](https://otaku-blog-3f79f19c74fc.herokuapp.com/)


## Table Of Content
1. [User Experience](#user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colour Scheme](#colour-scheme)
2. [Planning](#planning)
    - [Methodology](#methodology)
    - [Models](#models)
3. [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [Post Detail Page](#post-detail-page)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
4. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
5. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Device Testing](#device-testing)
    - [Browser Testing](#browser-testing)
    - [Feature Testing](#feature-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credit](#credit)
    - [Content](#content)
    - [Code](#code)
8. [Acknowledgements](#acknowledgements)


## User Experience
### Project Goals
- Create a Django Blog site centered on reviews of Video Games, Movies, Anime and TV Shows.
- It will be created using the Django libaries and external database, storage and hosting sites.
- Ensure that all web pages are clean, fully responsive and provide feeback to the user when possible.
- Implement CRUD Functionality so that users can modify data and interact with the site.
- Implement authentication layers of that pages are robust and have security.

### Users Stories
1. As a Site User I can See A Paginated List Of Reviews so that I Can Find One To Read And Comment On.
2. As a Site User I can View A List Of Posts so that I Can Select One To Read.
3. As a Site User I can Click On A Review Post so that I Can Read The Full Review.
4. As a Site User/ Admin I can See The Number Of Likes On Each Post so that I Can See What Is Popular.
5. As a Site User/ Admin I can View Comments On Individual Posts so that See Others Opinions And Conversations On The Topic.
6. As a Site User I can Create/ Register An Account so that I Can Like And Comment On Post.
7. As a Site User I can Log Into My Account so that I Can Continue Liking And Commenting On Posts When I Return To The Site.
8. As a Site User I can Leave A Comment On A Post so that I Can Give My Opinion And Join The Conversation.
9. As a Site User I can Update My Comments so that I Can Change Or Add To My Comment.
10. As a Site User I can Delete My Comments so that I Can Remove My Comment From The Conversation.
11. As a Site User I can Like Or Unlike A Post so that I Can Interact With A Post And Show My Opinion.
12. As a Site Admin I can Create, Read, Update and Delete Posts so that I Can Manage My Blog's Content.
13. As a Site Admin I can Create Draft Posts so that I Can Finish The Posts At A Later Date When Required.
14. As a Site Admin I can Approve Or Reject Comments so that I Can Filter Out Inappropriate Comments.

### Colour Scheme
The website was designed to have a bright feel to it. This is because it fits in with the general themes assosiated with the content of the reviews (Video Games, Anime, ect)

<image src="assets/readme/otaku_blog_pallette.png" width="650px"></image>

## Planning
### Methodology

This project was planned and implemented with agile methodology and principles. This was managed and documented on GitHub Projects.

The GitHub project can be viewed here: [Otoku Blog Project](https://github.com/users/BenHowkins/projects/10)

The EPICS were defined using the GitHub Milestones feature and each User Story was given one of the following milestones:
- Core Functionality: A feature of the project that is part of the project's core functionality
- CRUD Functionality: A feature of the project that is part of the project's CRUD functionality
- Account Management: A feature of the project that is part of the project's account management functionality
- Site Admin: A function of the project that is part of the site's administrative uses

User Stories contained a list of Acceptance Criteria and Tasks to support the development of the project.
Following MoSCoW Priortisation principles, each User Story was assigned a tag from one of the following:
- Must Have
- Should Have
- Could Have
- Won't Have

### Models
The project uses created two models, Post and Comment. It also uses the Django allauth User model.
1. The Post model stores the blog post data:
- author is a foreign key connecting to the User model.
2. The Comment model stores the data regarding comments made on the blog posts:
- post is a foreign key connecting to the Post model.

The  entity relationship diagram below was created using [dbdigram](https://dbdiagram.io/home) and demonstrates the relationship between the models. <br>
<image src="assets/readme/fst_project_diagram.png" width="650px"></image>

## Features

### General
- The website incorporates a responsive design so it can be used across multiple device sizes.
- The website uses a consistent colour scheme across the site.
- Each page has a responsive navigation bar containing the logo and nav menu. The nav bar turns into a burger menu on mobile devices.
- Each page has a repsonsive footer with helpful links to associated sites. The site links open in a new browser window.

### Home Page
- Post List
  - The home page displays a list of cards of showing the post on the blog.
  - The cards contains:
    - The featured image
    - The author's name
    - The post's title
    - THe post excerpt
    - The published date
    - Number of likes
  - The page displays the 6 most recent posts in 2 row of 3 posts.
  - When more than 6 posts are avaiable the site pagination will cause the page navagtion bar to appear which allows the user to scroll to view older post.
  - On a mobile device, there will be a single post on each row.<br>
  <image src="assets/readme/home_page_top.png" width="650px"></image><br>
  <image src="assets/readme/home_page_bottom.png" width="650px"></image>

### Add Post Page
- This page displays a form which allows users to submit their own posts/ reviews.
- The form includes the following fields for input:
    - The post's title
    - The post's slug
    - The author's name
    - A selector for the featured image
    - The post's excerpt
    - The post's content
- The Title, Slug, Author and Content fields are labeled with a * to indicate they are required.
- The bootom of the form has a Submit button which when pushed with a correctly filled out form will submit the post for approval and  sends the user back to the home screen.<br>
<image src="assets/readme/add_post_page_top.png" width="650px"></image>
<image src="assets/readme/add_post_page_bottom.png" width="650px"></image>

### Post Detail Page
- The following data displays at the top of the page:
    - The featured image
    - The author's name
    - The post's title
    - The post excerpt
    - The published date
- On a mobile device the featured image doesn't appear on the page.
- The page displays the review/ post left. 
- If the user is logged in the 'Leave a comment' box appears and allows user to add a comment on the post. 
- Users can also like others peoples comments if they are logged in.
- If the user has made a comment then buttons allowing them to Edit or Delete their comment will be seen.<br>
<image src="assets/readme/post_detail_page_top.png" width="650px"></image><br>
<image src="assets/readme/post_detail_page_bottom.png" width="650px"></image>

### Register Page
- This page displays a form which allows the user to register for an account on Otaku Blog.<br>
<image src="assets/readme/register_page.png" width="650px"></image>

### Login Page
- This page displays a form which allows the user to log into their Otaku Blog account.<br>
<image src="assets/readme/sign_in_page.png" width="650px"></image>

### Logout Page
- This page displays a form which allows the user to log out of their account on Otaku Blog account.<br>
<image src="assets/readme/sign_out_page.png" width="650px"></image>

### Edit Comment Page
- This page displays a text box showing the user's current comment which they have wish to edit and allows them to make the alterations before clicking the submit button, editing the comment and sending the user back to the home screen.<br>
<image src="assets/readme/edit_comment_page.png" width="650px"></image>

### Delete Comment Page
- This page displays a message tellinging the user that the comment which they have wish to delete will be gone for good and are they wish to continue. If so they click the submit button, deleteing the comment and sending the user back to the home screen.<br>
<image src="assets/readme/delete_comment_page.png" width="650px"></image>

## Technologies Used
### Languages
- HTML
- CSS
- Javascript
- Python
- [Jinja Templating Langugage](https://jinja.palletsprojects.com/en/3.1.x/)

### Frameworks, Libraries and Programmes
- [Font Awesome](https://fontawesome.com/): this was used to add likes and comments icons to the post detail and home pages to enhance user experience
- [Coolers](https://coolors.co/): this was used to create a colour pallete for the website. 
- [Django](https://www.djangoproject.com/): this was the MVC web framework used.
- [Bootstrap 5](https://getbootstrap.com/): this was the CSS framework used to make the site responsive. 
- [Cloudinary](https://cloudinary.com/): this was used to store static and media files.
- [Codeanywhere](https://app.codeanywhere.com/): this was used to write, commit and to push the code to Github. 
- [Github](https://github.com/): this was used for version control. 
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.
- [ElephantSQL](https://www.elephantsql.com/): this is the SQL database used in production.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): this was used throughout the project to check responsiveness and debug.
- [W3C Markup Validator](https://validator.w3.org/): this was used throughout the project to validate HTML code. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): this was used throughout the project to validate CSS code. 
- [CI Python Linter](https://pep8ci.herokuapp.com/): this was used to validate python code. 

A list of packages and dependencies can be found in the requirements.txt file.

## Testing

### User Stories Testing
1. As a Site User I can See A Paginated List Of Reviews so that I Can Find One To Read And Comment On.
  - The home page displays reviews in an ordered, paginated view.
  - The reviews are displayed in descending date order with the newest reviews on the top of the page.
  - There should be no more than 6 reviews on the page before the scroll bar appears to prevent the page from being too crowded.
2. As a Site User I can View A List Of Posts so that I Can Select One To Read.
  - On the main page there should be a visible list of all available posts to read.
  - The posts should be in descending date order with the newest post at the top of the page.
  - The page should only have a maximum of 6 posts showing at once before it allows older posts to be visible through screen navigation.
3. As a Site User I can Click On A Review Post so that I Can Read The Full Review.
  - When The user clicks on a post they are taken to a new page showing the review.
  - The page shows the review as well as the feature image and any comments that may have already been posted.
4. As a Site User/ Admin I can See The Number Of Likes On Each Post so that I Can See What Is Popular.
  - Have an icon (either a heart or thumbs up) below the review post on both the home page and the review's main page.
  - The icon has a numerical counter displaying the number of likes the review has received.
5. As a Site User/ Admin I can View Comments On Individual Posts so that See Others Opinions And Conversations On The Topic.
  - An icon (a speech bubble) is displayed below the post on the post page to say if/ how many comments it currently has.
  - Upon clicking on the post on the home page and being taken to the post's full page, any comments made by registered users should be visible below the post in descending order with the oldest comments at the top.
  - The comments should be in descending order with the oldest comments at the top.
6. As a Site User I can Create/ Register An Account so that I Can Like And Comment On Post.
  - The user must create a unique username with an email address.
  - The user must create and confirm a password.
  - The user is informed by a message they are successfully registered.
7. As a Site User I can Log Into My Account so that I Can Continue Liking And Commenting On Posts When I Return To The Site.
  - The user must input the username/ email address and password used upon creating the account.
  - If the credentials are correct, they're notified they are logged in and taken to the home page.
  - If the credentials are wrong, they inform the information is incorrect and are asked to try again.
8. As a Site User I can Leave A Comment On A Post so that I Can Give My Opinion And Join The Conversation.
  - When on the main page of a post, a registered user can leave a comment on that post.
  - The comment area should only appear if the user is logged in
  - When the comment is made a message will inform the user it's waiting for approval from the site admin.
  - The comment should only appear once the site admin has approved it.
9. As a Site User I can Update My Comments so that I Can Change Or Add To My Comment.
  - Below each comment a registered user has made there will be a button labelled 'Update'.
  - If the user clicks the button, they are able to make alterations to/ update their comment.
  - When the user has changed the comment, they click the submit button to confirm the alterations.
  - When the user pushes the submit button, they are taken to the home page.
10. As a Site User I can Delete My Comments so that I Can Remove My Comment From The Conversation.
  - Below each comment a registered user has made there will be a button labelled 'Delete'.
  - If the user clicks the button, they will be taken to a page asking if they want to delete the message
  - If the user clicks 'Delete Comment', the comment will be deleted and the user will be taken back to the homepage.
11. As a Site User I can Like Or Unlike A Post so that I Can Interact With A Post And Show My Opinion.
  - Have an icon (either a heart or thumbs up) below the review post on the post page.
  - If the user is logged in then the icon should become clickable.
  - If the user clicks on the icon it will change (go from empty to solid or coloured) to indicate they like the post, this also increases the number next to the icon indicating the number of likes.
  - If the user clicks the icon again it will change back to its original state (solid or coloured to an empty icon) to indicate a dislike, this also decreases the number next to the icon.
12. As a Site Admin I can Create, Read, Update and Delete Posts so that I Can Manage My Blog's Content.
  - The admin/ superuser will be able to write posts that appear on the main site.
  - The post panel should only be visible on the admin page of the site when logged in as a superuser.
  - Once a post is created, the superuser can edit and/or delete the post by clicking the corresponding button.
13. As a Site Admin I can Create Draft Posts so that I Can Finish The Posts At A Later Date When Required.
  - The admin/ superuser will be able to save posts they are writing by saving the post under the status 'Draft'.
  - The draft posts should be saved on the admin page and not visible on the main site until the status is changed to 'Published'.
  - Once a draft post is published, it should appear on the main page.
14. As a Site Admin I can Approve Or Reject Comments so that I Can Filter Out Inappropriate Comments.
  - When a user makes a comment on a post, it doesn't appear automatically under the post.
  - A message appears when a comment is entered stating 'comment awaiting approval by admin'.
  - On the admin page the comment is visible for the admin to read.
  - If the comment is approved, it appears on the site under the post it was made on.
  - If it isn't approved, it will not appear on the site and will be deleted.

### Code Validation
The following validators were used to test the code:
- [W3C Markup Validator](https://validator.w3.org/): No errors were reported when passing the final HTML code through the validator. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): No errors were reported when passing the final CSS code through the validator. <br>
- [CI Python Linter](https://pep8ci.herokuapp.com//): No errors were reported when passing the final python code through the validator.  <br>

#### Unresolved HTML Error
- Upon passing through the validator, no error were shown.
#### Unresolved Python Error
- When passing the py files through the validator, it stated that the env.py and settings.py had a total of 7 lines deemed 'too long', however these lines were either names of password validators or names of keys, so were all left as they were.

### Device Testing
- The website was manually tested on a:
  - Jumper EZbook S5 Max
  - OPPO A54
  - Amazon Kindle Fire

### Browser Testing
The website was tested on the following browsers with no issues:
- Google Chrome
- Avast Secure Browser
- Mozilla Firefox
- Microsoft Edge

### Feature Testing
The following manual tests were carried out:
#### General: base.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logo | When the logo is clicked, the user is brought back to the home page | PASS
Mobile menu | On mobile devices, a burger menu is used to display nav links | PASS
Register nav link | Brings the user to the signup page | PASS
Login nav link | Brings the user to the login page | PASS
Logout nav link | Brings the user to the logout page | PASS
Footer links | When clicked, footer links open in a new browser window | PASS

#### Home Page: index.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Post Card | A card for each post is visible containing: Feature image, Author's Name, Post's Title, Post Excerpt, Published Date, Number Of LIkes | PASS
Post Card Link | When the title of the card is clicked, the user is brought to the post detail page for the post | PASS
Number Of Likes | The number of likes on the card should be the same as that on the post detail page | PASS
Page Pagination | The post cards should be in rows of 3 posts per row and should have page navigation appear when more than 6 posts are visable | PASS

#### Add Post Page: add_post.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Register Message | The user should be welcomed with a message saying welcome back to the page and told to fill out the form below if they wish to leavee a post of their own | PASS
Input Form | There should be a labeled form for the user to input a Title for the post, a Slug name, select the Author of the post, select an Image, create an Exerpt decription and the post Content itself with the Title, Slug, Author and Content all being starred to indicate they are authorised fields  | PASS
Confirmation Button | A button should be visable below the message labelled "Submit" which confirms submission of the review | PASS
Data Input Autherisation | After the submit button is pushed the site will check all the required fields have data entered in them and also check the data input against the database to see there is no repeated Titles or Slugs being used. If either of these things happen a error message will appear under the offending field saying either that this field is required or this Title or Slug has been used and to select another one  | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page | PASS

#### Post Detail Page: post_detail.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Post Details | The top of the page should display: Author's Name, Post Title, Excerpt and Date Published on the left side of the screen and the Featured Image on the right | PASS
Post Body | The post itself should be displayed directly below the details card | PASS
Likes And Comments Counter | Icons and counters displaying the current number of likes and comment the post has should be visible below the post | PASS
Like And Unlike |  When a user has an account and is logged in they are able to click on the like icon and like the post or click it again and unlike the post | PASS
Leave A Comment Section | If the user has an account and is logged in then there will be a box visable for them to leave a comment. If they aren't logged in the box won't appear | PASS
Comment Authorisation | All comments when left shouldn't display automatically but should show a message stating they are "Await Approval". Once approval is given they should then appear on the page | PASS
Comment List | All approved comment should appear down the left side of the screen in order of creation with the oldest comment at the top and getting newer as you go down, to easily follow the conversation | PASS
Comment Edit Button | A button should appear below any comment a logged in user has made named "Edit". This should take them to the comment edit page. This button should only appear on comments they have made | PASS
Delete Comment Button | A button should appear below any comment a logged in user has made "Delete". This should take them to the comment delete page. This button should only appear on comments they have made | PASS

#### Comment Edit Page: comment_edit.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Edit Comment Message | The user should be welcomed with a personalised message containing their username stating that they can change their comment | PASS
Comment Edit Box | A textbox should be visable, displaying the original message and allowing the user to make alterations | PASS
Confirmation Button | A button should be visable below the textbox labelled "Update Comment" which confirms any changes made | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page | PASS

#### Comment Delete Page: comment_delete.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Edit Comment Message | The user should be welcomed with a personalised message containing their username stating that they are deleting their comment and this is unreversable | PASS
Confirmation Button | A button should be visable below the message labelled "Delete Comment" which confirms deletion of the comment | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page | PASS

#### Register Page: signup.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Register Message | The user should be welcomed with a message saying welcome back to the page and told if they already have an account to log in with a link to the log in page or sign up below if they don't have an account | PASS
Input Details | There should be labeled boxes for the user to input a username, an email address if they wish too and to input a password and another password field to confirm the password match. There is also a submit button to confirm entry of the details | PASS
Input Autherisation | After the submit button is pushed the site will check the data input against the database. If the passwords match and the username is unique the user will be redirected to the home page. If the username is taken the user will be informed it has been taken and asked to pick another one. If the passwords don't match the user will be told they didn't match and asked to try again | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page and a message should display stating they have signed in with their username | PASS

#### Login Page: login.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Login Message | The user should be welcomed with a message saying welcome back and log in or sign up with a link to the register page if they don't have an account | PASS
Input Details | There should be labeled boxes for the user's username and password and a submit button to confirm entry of the details | PASS
Input Autherisation | After the submit button is pushed the site will check the data input against the database. If the data is correct the user is redirected back to the home page, if it is incorrect a message will appear stating that either the username and/ or password are incorrect and allow the user to try again | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page and a message should display stating they have signed in with their username | PASS

#### Logout Page: logout.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logout Message | The user should be welcomed with a message stating that they are logging out of their account and see if they are sure | PASS
Confirmation Button | A button should be visable below the message labelled "Log Out" which logs the user out of their account | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page and a message should display stating they have signed out | PASS

### Bugs
#### Resolved Bugs
1. Authorised Comment User Bug- When creating the buttons for the "Edit" and "Delete" comment functionality I was unable to correctly have it so that only the user who created the comment could edit or delete it. I realised that I had: 
  1. I only used a single "=" sign in the equalty check.
  2. I had not used the correct wording in the if statement. I had put "user.name == comment.name" instead of "user.username == comment.name"
once I corrected both these issue both buttons appeared correctly.
2. Edit Comments Bug- Whilst trying to create this functionality I was unable to get it to correctly function without giving me a "No Reverese" or a "Page Not Found" error. After speaking to several Code Institute Tutor I found that I was trying to override the Post and Get methods and instead I should be updating the view. And after reading through and article on [GeeksForGeeks](https://www.geeksforgeeks.org/) I was able to write the correct code.

#### Unresolved Bugs
- Through testing and validations I don't believe that there is any unresolved bugs on the site.

## Deployment
The program was developed in Codeanywhere. It was then commited and pushed to GitHub periodically.
The finished project was then deployed to Heroku. 
Deployment to Heroku was completed using the following steps: 
1. Open and login to [Heroku](https://id.heroku.com/login).
2. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu. 
3. Enter the App name, choose a region, then click 'Create app'.
4. Navigate to the 'Settings' tab.
5. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
6. Add config vars using the 'KEY' and 'VALUE' pairs from env.py.
7. Navigate to the 'Deploy' tab. 
8. Within 'Deploy', navigate to 'Deployment method'. 
9. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub' 
10. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
11. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
12. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method. 
13. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
14. Click 'View' to see the deployed app. 

## Credit
### Content
- All other content was written by the developer.

### Code
- [GeeksForGeeks](https://www.geeksforgeeks.org/):
  - The information on this site was used in the creating the comment "Edit" and "Delete" functionality.
- [Code Institute](https://codeinstitute.net/):
  - Code Insitute full stack walkthrough projects were referred to when setting up the project. Elements of these projects were used and adapted to suit this project.
- [Bootstrap5](https://getbootstrap.com/): was used to add elements including cards for the posts and the navigation bar. 
- [Django](https://www.djangoproject.com/): documentation was referred to throughout development. 

## Acknowledgements
- Thank you to Oisin, Holly, Roo and Joanne from Code Institute Tutor Support for helping me along the way. 
- Thank you to Code Institute for providing me with the tools and skills to complete this project. 
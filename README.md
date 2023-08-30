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

The project can be viewed here: [Otaku Blog]()


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
  - On a mobile device, there will be a single post on each row
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
- Users can also like others peoples reviews if they are logged in.
- If the user has made a comment then a buttons allowing them to Edit or Delete their comment will be seen.
### Register Page
- This page displays a form which allows the user to register for an account on Otaku Blog.
### Login Page
- This page displays a form which allows the user to log into their Otaku Blog account.
### Logout Page
- This page displays a form which allows the user to log out of their account on Otaku Blog account.
### Edit Comment Page
- This page displays a text box showing the user's current comment which they have wish to edit and allows them to make the alterations before clicking the submit button, editing the comment and sending the user back to the home screen.
### Delete Comment Page
- This page displays a message tellinging the user that the comment which they have wish to delete will be gone for good and are they wish to continue. If so they click the submit button, deleteing the comment and sending the user back to the home screen.
## Technologies Used
### Languages
- HTML
- CSS
- Javascript
- Python
- [Jinja Templating Langugage](https://jinja.palletsprojects.com/en/3.1.x/)

### Frameworks, Libraries and Programmes
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
- [W3C Markup Validator](https://validator.w3.org/): Apart from o errors were reported when passing the final HTML code through the validator. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): No errors were reported when passing the final CSS code through the validator. <br>
- [CI Python Linter](https://pep8ci.herokuapp.com//): No errors were reported when passing the final python code through the validator.  <br>

#### Unresolved HTML Error
- When passing the final HTML code through the validator, an error appeared stating that there was no alt tags in any of the images on the site. However, the code was written with an if/ else statement. This stated that if there wasn't a set featured image then the placeholder image is used instead, so an alterenative is given to all images just in a different part of the code.
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
### Bugs
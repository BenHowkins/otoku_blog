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
12.<> As a Site Admin I can Create, Read, Update and Delete Posts so that I Can Manage My Blog's Content.
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
### Register Page
- This page displays a form which allows the user to register for an account on Otaku Blog.
### Login Page
- This page displays a form which allows the user to log into their Otaku Blog account.
### Logout Page
- This page displays a form which allows the user to log out of their account on Otaku Blog account.

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

A complete list of packages and dependencies can be viewed in the requirements.txt file. 
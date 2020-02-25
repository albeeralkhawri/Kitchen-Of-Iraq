![picture](https://www.up-00.com/i/00146/eft20qbwcohv.png)
***


##### *The third project : Data Centric Development Milestone Project / cookbook*

###### This site is designed in a way that is understood by all users. The project logo was chosen in the form of a tea kettle To symbolize the Iraqi Kitchen because Iraqi tea a Famous in the Middle East.
***

# UX

##### My goal in this project is to enable users to get to know the Iraqi recipes and also the user can add the recipes that I like and savor before and they can also see the recipe details and learn more about them. There is a simple description of each recipe, what its contents are, how long they are prepared and cooked, and each description includes the category you belong to according to the Iraqi cuisine and also some recipes that I recommend trying. The user can delete and edit in each recipe to add something or remove something to make the recipe good as desired by the user.

###### This project is designed in a very easy way so that the site can be used by all different ages.

#### <p align="center">This is the sitemap</p>
<p align="center">
<img src="https://www.up-00.com/i/00160/zrfhfm59zzf7.png"></p>

***

#### <p align="center">These are three of the project designs, you can see the rest of the designs in <a href="https://github.com/albeeralkhawri/Kitchen-Of-Iraq/tree/master/Project%20Design">Project Design</a></p>

 # <p align="center">Home Page</p>
  <p align="center">
   <img src="https://www.up-00.com/i/00160/rb4cfi3zd5io.png"></p>

# <p align="center">Recipes Page</p>
<p align="center">
  <img src="https://www.up-00.com/i/00160/t8pe5utpupjf.png"></p>

# <p align="center">Add recipe Page</p>
<p align="center">
  <img src="https://www.up-00.com/i/00160/d3rn97fx5jq9.png"></p>

***

# <p align="center">  Database Schema Design </p>

 <p align="center"> <img src="https://www.up-00.com/i/00160/x4ktezabtn4i.png"></p>
 
###### <p align="center">You can see the Database Schema more clearly in <a href="https://github.com/albeeralkhawri/Kitchen-Of-Iraq/blob/master/Database%20Scheme/Data%20Scheme.png">Database Scheme</a></p>

***

# Demo

##### You can view the site directly <a href="https://kitchen-of-iraq.herokuapp.com/">Kitchen Of Iraq</a>
<p align="center" href="https://imgflip.com/gif/34viqn"><img src="https://www.up-00.com/i/00160/mamdwe8wqzh9.gif" title="made at imgflip.com"/></p>

***

## What does it do?

###### This is a web application that allows a user to store recipes and easily access them as a web application (create, read, update, delete) of a database hosted by the presentation link by Heroku

***

# Features

##### This site is characterized by ease of use, registration, logging in, adding, editing and deleting recipes and categories also includes every recipe, including a picture and details for each recipe, and also responds to all types of large and small screens designed for all

### Users can:

- Registration and Login
- Add, edit and delete recipes
- View details for each recipe
- Add photos for each recipe
- Add, edit and delete categories
- Search for the name of recipes in the list of recipes
- Watch recipes with a picture of each recipe
- Display categories and navigate between sections of the site easily
- Log out

***

# Technologies Used

1. <a href="https://en.wikipedia.org/wiki/HTML5">HTML5</a>
2. <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3">CSS3</a>
3. <a href="https://www.javascript.com/">JavaScript</a>
4. <a href="https://www.python.org/">Python3</a>
5. <a href="https://en.wikipedia.org/wiki/Flask_%28web_framework%29">Flask</a>
6. <a href="https://cloud.mongodb.com/user#/login/login?nds=true&_ga=2.185312873.1385114917.1506971088-288232041.1493043934&nds=true">MongoDB</a>
6. <a href="https://materializecss.com/">Materialize</a>
7. <a href="https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/">jQuery(3.2.1)</a>
8. <a href="https://fonts.google.com/">Google Fonts</a>
***

# Testing

- The project was checked that it works on all screen sizes
<p align="center" href="https://imgflip.com/gif/34viqn"><img src="https://www.up-00.com/i/00160/mamdwe8wqzh9.gif" title="made at imgflip.com"/></p>

- The html code was checked manually I tried to search for a special validator html template but I did not find the natural validator does not work on the html template but when i was check manually the html template didn't found any error or problem
- I checked the CSS code manually and through the CSS checker I did not get any errors or problems and the picture below shows that
<img src="https://www.up-00.com/i/00160/f0ggm608a3d9.png">

- The Python code was manually verified by Inspection, Console and I didn't see any errors and also I ran the code line by line and I didn't see any errors and the project works perfectly.
- I manually checked JavaScript min.js and jquery.js via Inspection, Consol and I also ran the code line by line and didn't see any errors and the project works perfectly.
- The site has been tested with different devices to ensure the site works perfectly and is compatible with all devices for devices that  have been tested below.
   - My laptop dell 
   - My phone iphone 8 plus
   - My tablet Samsung Tab E
   - my friends Phones Samsung Note 8 and samsung Note 9 and iphone 11

- The register was test in this way below
  - I tried to submit an empty form but did not send it and say please fill in the fields
  - I tried to submit an incomplete form but did not send it and say please fill in the fields
  - I tried to submit a form with a mismatched password that did not send and say the password did not match
  - I tried to send a form with a password of less than 8 letters or numbers but it was not sent and says please write it at least 8 or more characters
  - Then I tried to submit a completed form with complete requirements and it succeeded

- The Log in was test in this way below
  - I tried to submit an empty form but did not send it and say please fill in the fields
  - I tried to login with a wrong username, took me to a page with instructions that says Registration or verification of the password and username
  - I tried to login as an error password, took me to a page with instructions that says Registration or verification of the password and username
  - Then I logged in with a valid username and password and succeeded

- When Log out was test in this way below
  - When you click Log Out, you will return to the home page

- The Add Recipe was test in this way below
  -  tried to submit an empty form but did not send it and say please fill in the fields
  <img src="https://www.up-00.com/i/00160/8buxp2wbrein.png">

  - I tried to submit an incomplete form but did not send it and say please fill in the fields
  <img src="https://www.up-00.com/i/00160/3cn9jp8tbvxw.png">
  
  - I have checked all the entries and confirmed that the user cannot send any empty fields
  - I tried to enter all the details and successfully added the recipe

- The Edit Recipe was test in this way below
  - It is check when the recipe is edited, the contents of the recipe are changed and in the database as well
  - It has been verified that you can modify only one thing that does not need to re-enter the data again. You can amend the name of the category, the picture or anything else.
  - It has been confirmed if you entered edit the recipe and do not want to change anything. You can press the cancel button or choose any part of Navbar
  - I tried it when the name, image or something else in the recipe was changed, and it was actually changed on the recipe itself or in the recipe details

- Tried when deleting the recipe is deleted successfully

- The categories was test in this way below
  - Checked, added, edited, deleted, was working perfectly
  - It was confirmed that the user could not submit an empty form

The add category was test in this way below
  - I tried to submit an empty form but did not send it and say please fill in the fields
  - I tried to write the name of the category, pressed Add, and I successfully added a new category

- The edit category was test in this way below
  - I tried to remove the category name. Resend it. The form is blank, but this is not allowed. It says this field is being filled in
  - I tried to change the category name to another name and it succeeded in this

- Tried when deleting the category is deleted successfully

- The buttons was test in this way below
  - I checked the login button and it works
  - I checked the signup button and it worked
  - I checked the navbar buttons, they all work
  - I checked the button for adding the recipe it was working
  - When you press the Delete Recipe button, it is deleted
  - When you click on the "Edit Recipe" button, it will be moved to the "Edit Recipe" page
  - When you press the Delete category button, it is deleted
  - When you click on the "Edit category" button, it will be moved to the "Edit category" page
  - When you press the Back button in the recipe detail, you will return to the recipes page
  - The search button has been checked and it is working
  - All buttons were checked in all sections of the project as they are working perfectly

- The Search was test in this way below
  - I tried to click on the search button and enter the name of his description, I did not search for the recipe and he says the field is being filled in
  - When typing the name of the recipe in the search box, the recipe whose name was written will appear

- It was confirmed that there is no code that I do not need
- The project was generally checked by Inspection, Console and I didn't get any errors and the project works very well
***

# Deployment

###### Project files were hosted by <a href="https://github.com/">Github</a> and the project was presented by <a href="https://www.heroku.com">Heroku</a>

- The site was posted by Github and hosted in the repository on Github (https://github.com/albeeralkhawri)
- Repository site link (https://github.com/albeeralkhawri/Kitchen-Of-Iraq)
- The live display link (https://kitchen-of-iraq.herokuapp.com/)

### Take the next steps for publication:
 - Create file requirements.text has the necessary dependencies to run the project
 - Create env.py file containing security variants and add it to .gitignore to avoid posting it in github
 - Create a new repository in github
 - Created a Heroku app with a kitchen-of-iraq name
 - Connected Heroku app with github repository and enabled automatic deploys
 - I stored the variables in env.py and put them in Reveal Config Vars to enable heroku to read the variables
   - Variables include IP, MONGO_URI, PORT, and SECRET_KEY
 - Add the Procfile required by Heroku
***

# Credits

### Content
- I designed the site by <a href="https://balsamiq.com/wireframes/desktop/">Balsamiq Mockups 3</a>
- The site map by <a href="https://www.gloomaps.com/">GlooMaps</a>
- The chart database <a href="https://www.lucidchart.com/pages/">Lucidchart</a>
- Use to confirm the password in the home page <a href="https://codepen.io/">CodePen</a>

### Media

- Photos have been obtained from <a href="https://www.google.ie/imghp?hl=ar&tab=wi&authuser=0&ogbl">Google Images</a>
- The videos used in Gif Image are recorded through this program <a href="https://icecreamapps.com/Screen-Recorder/">Icecream Screen Recorder</a>
- Some images have been uploaded with a link through this site <a href="https://www.up-00.com/">UP00</a>
###### *<p align="center"> This is all that was used to make this project. I hope I do not forget anything </p>*
***

# Acknowledgements

- My thanks and appreciation for all that helped me and support me in order to complete this project and thank also the support of teachers at the Code Institute
- I also thanked the Code Institute, from which I learned a lot, and this is the product of my work and Thanks Mentor helped me a lot

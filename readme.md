# DRF Crowdfunding API Project


**Contributi** is a local government area community fundraising platform for members of the community to fundraise for projects specifically for their local community. During COVID lockdowns we discovered that a strong local community is what helped to keep people happy and engaged. Contributi enables community members to connect and fund the local projects most important to them.

## Links
**GitHub**

https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-AngelaClarke5678


**Projects**

https://peaceful-wildwood-53690.herokuapp.com/projects/

**Users**

https://peaceful-wildwood-53690.herokuapp.com/users/

## Login

**Username:** SuperAdmin

**Password:** SuperAdmin

## Screenshots
### Get ###
![get request](/screenshots/Get%20Projects.png)

### Post ###
![post request](/screenshots/Post%20Project.png)

### Auth Token ###
![auth token](/screenshots/Token%20Auth.png)

## How to Register a new user
1. In Insomnia create a POST request on the URL http://peaceful-wildwood-53690.herokuapp.com/users/
2. In the body of the POST request select JSON 
3. Enter your preferred username, password, email, bio & profile image using the JSON structure below.
4. select SEND
5. If the JSON parameters are correct and the username is not a duplicate you will receive a 201 created success message and your account will be created. If the parameters are not correct you will receive a 400 bad request error.
**JSON code**

```
{
        "username": "Username",
		"password": "Password",
        "email": "email@email.com.au",
        "bio": "I am passionate about supporting access to fresh food",
        "profile_image": "https://via.placeholder.com/300.jpg"
    }
```
## How to Create a new project
1. First you will need to have registered an account already in the steps above.
2. Create a POST request on the URL http://peaceful-wildwood-53690.herokuapp.com/api-token-auth/ to generate your authentication token. Input the username and password you have just created in the BODY selecting JSON using the following JSON structure and press send.

```
{
	"username": "replace with your username",
 	"password": "replace with your password"
}
```

3. Copy the Token that has been created
4. Create another POST request this time on the URL https://peaceful-wildwood-53690.herokuapp.com/projects/
5. In the body of the POST request select JSON 
6. Enter your project title, description, goal, image URL & is_open & date created using the JSON structure below.
7. select SEND
8. If the JSON parameters are correct you will receive a 201 created success message and your account will be created. If the parameters are not correct you will receive a 400 bad request error.

**JSON code** 

```
{
	"title": "Fund a community garden on Smith Street",
	"description": "Access to Healthy food is important for a growing community",
	"goal": 1550,
	"image": "https://via.placeholder.com/300.jpg",
	"is_open": true,
	"date_created": "2022-04-20T14:28:23.382748Z"
}
```

## API Specification
|      HTTP Method     |      URL              |      Purpose                                    |      Request Body       |      Successful Response    Code     |      Authentication/Authorisation                         |
|----------------------|-----------------------|-------------------------------------------------|-------------------------|--------------------------------------|-----------------------------------------------------------|
|      GET             |      /projects/       |      Returns all projects                       |                         |      200                             |      n/a                                                  |
|      POST            |      /projects/       |      Create a new project                       |      Project object     |      201                             |      Must be logged in                                    |
|      GET             |      /users/1         |      View user profiles with an ID of ‘1’       |      User Object        |      200                             |      n/a                                                  |
|      POST            |      /users/          |      Create a new user                          |      User object        |      201                             |      n/a                                                  |
|      PUT             |      /projects/1/     |      Update the projects with an ID of ‘1’      |      N/A                |      200                             |      Must be logged in     Must be project owner          |
|      PUT             |      /pledges/1/      |      Update the projects with an ID of ‘1’      |      N/A                |      200                             |      Must be logged in     Must be the pledge owner       |
|      POST            |      /pledges/        |      Create a new pledge                        |      Pledge object      |      200                             |      N/A                                                  |
|      DELETE          |      /projects/1      |      Deletes the projects with an ID of ‘1’     |      n/a                |      200                             |      Must be logged in      Must be the project owner     |
|      DELETE          |      /pledges/1/      |      Deletes the pledge with an ID of’1”        |      n/a                |      200                             |      Must be logged in      Must be the pledge owner      |
## Database Schema 
![database schema](/screenshots/database%20schema.png)
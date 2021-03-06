# Template Generate System


## Table Of Contents

1. [How to use the project and prerequisite for running the project in the local machine.](#desc1)
2. [About project](#desc)


<a name="desc1"></a>
## How to use the project and prerequisite for running the project in the local machine.
1. Open command promt.
2. Go to your project clone directory.
3. Run the command -``` docker-composer build ```.
4. After sucessfully running without any error. run one more command that is  ``` docker-composer up```.
5. Then open your brower and go to the given link - ``` localhost:8000 ```.
6. Congratulations that your project has been ready to use.
<a name="desc"></a>

## About The Project.
* The project is to generate the template at runtime using the django framework.
* There are two users 1.Admin 2.Normal user 
1. Admin- Admin can upload and generate the templates.
2. Normal - The normal login user only generates templates that are uploaded by the administrator.


* How to create an account as an administrator?
1. Go to the project folder and open the command prompt, make sure that you are running the command given in the project directory  run the given command -``` python manage.py createsuperuser ```
2. Then enter the Username of your choice and press enter.
3. Then enter the Email address and press enter.(It can be left blank)
4. Enter password and confirm password then hit enter.
5. Now we can login into our Django Admin page by running the command python manage.py runserver . Then, open a Web browser and go to        “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/ and then enter the same Username and Password.
  
 * How to upload new template by admin?
  1. After login as an administrator.
  2. Click the uploadfile button on the left hand side on the admin deskboard.
  3. Click the add button, then add the file.
  
 Note - This system always takes the latest uploaded file by the admin. This is the first and must step otherwise the application will generate an error.Make sure that the file uploded by the administrator is only the docx file.
  
* Login and User Registration.
The user must first login before creating a template.
* How to sign up a normal user?
 1. Go to home page.
 2. Click on registeration button and fill the form.
 3. After register Successfully You are redirected to the login page.
 
Note - All generated files will be saved in the media folder of your project directory.
### Important Note- pdf option disable due to some reason. please test the application on docx file mode.










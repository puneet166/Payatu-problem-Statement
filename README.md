# Template Generate System


## Table Of Contents

1. [How to use the project and prerequisite for running the project in the local machine.](#desc1)
2. [About project](#desc)


<a name="desc1"></a>
## How to use the project and prerequisite for running the project in the local machine.
1. Open command promt.
2. Go to your project clone directory.
3. Run the command is-``` docker-composer build ```.
4. After run sucessfully without error run one more command of docker-composer that is ``` docker-composer up```.
5. Then open your brower and go to on this link - localhost:8000.
6. Congrate your project is read to use .
<a name="desc"></a>

## About The Project.
* This project for generate templates at runtime using django framework. 
* There are two user 1.Admin 2.Normal user 
1. Admin- Admin can upload and generate the templates.
2. Normal- Normal login user only generate the templates which uploaded by the admin.


* How to create account as a admin?
1. Go to project folder and open command prompt make sure you are in project directory run the given command -``` python manage.py createsuperuser ```
2. Then enter the Username of your choice and press enter.
3. Then enter the Email address and press enter.(It can be left blank)
4. Enter password and confirm password then hit enter.
5. Now we can login into our Django Admin page by running the command python manage.py runserver . Then, open a Web browser and go to        “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/ and then enter the same Username and Password.
  
 * How to upload new template by the admin?
  1. After login as a admin 
  2. Click uploadfile button in left hand side on admin deskboard.
  3. Click on add button then add file.
  
 Note- This system always take latest uploded file by the admin.This is first and must step otherwise application generate error.
  Make sure uploded file by the admin is docx file only.
  
* Login and registeration of User.
Before generate the template user must be login first.
* How to signup normal user?
 1. Go to home page
 2. Click on registeration button and fill the form.
 3. After sucessfully register you redirect on login page and login by username or password.
 
Note- All generated file save into media folder of your project directory.











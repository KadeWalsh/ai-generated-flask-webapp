# Prompts used to generate code
### Create basic flask app
>inside aiGenerated.py create the basic framework for a simple flask web app
>![Screenshot from 2024-02-05 16-06-35](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/63a27720-efa4-494c-862e-c4ac8cd2cd53)
>![Screenshot from 2024-02-05 16-07-04](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/753e14de-5adb-4588-b6e5-8a1abaa29ac3)

### Modify code to seperate routes in blueprint file instead of inside main app file
>modify the code from aiGenerated.py so that it imports blueprints from a seperate file, named myBlueprints.py, and generated the code needed for myBlueprints.py to replicate the current routes from aiGenerated.py
>![Screenshot from 2024-02-05 16-07-39](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/c07729ef-0e6d-4186-9150-13119157492a)
>![Screenshot from 2024-02-05 16-07-50](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/e4bec607-c1a7-4c97-adc3-57821794470d)

### Create layout file
>create a layout.html file which will be used as a jinja template, with a title block, and a body block, that will be replaced in each file that extends this base template
>![Screenshot from 2024-02-05 16-08-11](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/23e6d149-f029-4f9d-818a-4f7947eb420a)

### Create base layout.html file
>generate the code need for index.html, which will extend from the template layout.html
>![Screenshot from 2024-02-05 16-08-27](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/2c58e759-096c-40d0-9e73-aa8e80dd6c01)


### Create contact.html file
>generate the html code neded to handle the route 'contact' and display the message passed in the return statement
>![Screenshot from 2024-02-05 16-08-49](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/c83d4a6c-4b54-4f0c-b0a6-da92241fcd2f)

### Add navbar to layout template (layout.html)
>modify the code in 'layout.html' and add a navbar element across the top of the screen. The navbar needs to contain three links, one for home, the second for profile, and the third for contact. For now these links can have href='#'
>![image](https://github.com/KadeWalsh/ai-generated-flask-webapp/assets/107522159/8a543bb9-2bcb-47bb-9cbe-3eeeb3717b12)


## NOTE:
### The ONLY CHANGES made to AI generated code were to import render_template and requests inside of myBlueprints.py instead of aiGenerated.py

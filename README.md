=============================================================
        step - 1
=============================================================
Make a folder -->terminal(cntr + `)

•⁠  ⁠create a project -->django-admin startproject project_name
•⁠  ⁠cd project_name
•⁠  ⁠create app -->python manage.py startapp app_name

-- register the app 
project -->settings.py -->

INSTALLED_APP =[
    .....,
    "app_name"
]

================================================================
                        Step - 2
================================================================

python manage.py migrate -->it migrate already existing app to database
python manage.py runserver -->to develop a server

================================================================
                        Step - 3
================================================================

Folder Structure 

Base_Dir(Daraz)
            -->app 
                -->templates -->home.html
                -->static 
                       -->css
                       -->js
                       -->images
            -->daraz(project)
            -->manage.py
            -->database   

views.py

def function_name(request):
    return render(request,'file.html')

urls.py

from app_name import views

path("",views.function_name)

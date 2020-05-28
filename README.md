# Youtube-Video-Playslist
Collaborative youtube video playlist

![Screenshot](/animusicpark.jpg?raw=true "Phil Serme, More translate App")



* **Purpose of this app**

Save videos organize them and categorize them. Make it easier to have a collaborative youtube video playlist. 

* **Goal**

It is a simple full-stack application to teach about full-stack development. This is application is part of a series of applications to teach code.

* Frontend: w3.css library
* Backend: Django


* **How to use the app**

simply copy the link of any youtube video in the form, also add a video, select a ranking and type and publish the video.


* **Quickstart** 

git clone https://github.com/QbasicFan/Youtube-Video-Playslist


root setting.py
```
INSTALLED_APPS = (
    ...
    'Youtube-Video-Playslist',#project1
    ...
)
```

root url.py
```
urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url("^admin/", include(admin.site.urls)),
	...

    #url(r'project1/', include('Youtube-Video-Playslist.urls', namespace ="home")),#project1

	...
)
```

* **Test** 
```
python manage.py test book.tests
python manage.py test bookId.tests
python manage.py test user.tests
...
```

* **Todo**

* [ ] Add user account
* [ ] Add comments
* [ ] Add likes
* [ ] Add social auth
* [ ] Add test cases
* [ ] Better filter system

* **Credits** 

https://www.philserme.com


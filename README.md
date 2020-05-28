# Youtube-Video-Playslist
Collaborative youtube video playlist

![Screenshot](/animusicpark.jpg?raw=true "Phil Serme, More translate App")



* **Purpose of this app**

Save videos organize them and categorize them. Make it easier to have a collaborative youtube video playlist. 

* **Goal**

It is a simple full-stack application to teach about full-stack development. This is application is part of a series of applications to teach code.


* **How to use the app**

simply copy the link of any youtube video in the form, also add a video, select a ranking and type and publish the video.


* **Quickstart** 

git clone 


root setting.py
```
INSTALLED_APPS = (
    ...
    'project1',
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

    #url(r'project1/', include('project1.urls', namespace ="home")),

	...
)
```


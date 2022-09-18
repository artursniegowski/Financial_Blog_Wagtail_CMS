# Financial_Blog_Wagtail_CMS

This is a responsive website that represents a financial blog where the owner can easily manage the content with the wagtail framework. Wagtail is an open source CMS written in Python and built on the Django framework.
It offers a fast and attractive interface for editors where content can be created and structured intuitively.
The websites consist of a homepage where the user can enter the blog.
On the main page of the blog, the user has an overview of all the posts listed chronologically.
Each post also has a detailed view where the whole content is shown with additional information like categories, tags, author, date posted, main content of the post, and gallery.
For every post, the user can add tags and customise categories.
The user also has the option of choosing a specific tag and displaying all the posts on the blog related to that specific tag. Categories and profiles need to be edited or created before they can be connected to a specific post or article.
On the settings site there is also configuration prepared for linking the blog website with other social media websites. Currently active are Facebook, Twitter, and Instagram, but this can be easily added with the use of the added app_site_settings where all the social media links are configured.
The focus of this website is on the content management of a financial blog, which can be easily edited from the admin site provided by Wagtail.</br>

---


<br>
In order to run the website: <br>
1. Change the name of .env.example to .env and add your DJANGO_SECRET_KEY for your website. </br>
2. navigate to the main directory, which contains the entire project. </br>
3. python -m venv ENV - create a virtula enviromet. </br>
4. pip install -r requirements.txt - install all the required Python libraries. </br>
5. python manage.py migrate - execute your first migration command. </br>
6. python manage.py createsuperuser - create a super user for your project. </br>
7. python manage.py runserver - start your server, which will allow you to access your website via a web browser at localhost: 8000. </br>
</br>

---

</br>

**Created with  Wagtail 4.0, Django 4.1, Python 3.10.6, Flowbite, Tailwind CSS, CSS, HTML.**
</br>

</br>
Wagtail 4.0</br>
https://wagtail.org/ </br>

Django 4.1 </br>
https://www.djangoproject.com/ </br>

Flowbite</br>
https://flowbite.com/ </br>

Tailwind CSS </br>
https://tailwindcss.com/ </br>


---

### Website views:
</br>

1. Home page</br>
http://localhost:8000/</br>
2. Main blog view </br>
http://localhost:8000/blog/</br>
3. Detail post view</br>
http://localhost:8000/blog/house-as-investment/</br>
4. Tag specific view</br>
http://localhost:8000/tags/?tag=invest</br>



</br>
1. Home page:
</br>

![Screenshot](docs/img/Home.png)
</br>

---

2. Main blog view:
</br>

![Screenshot](docs/img/Blog_main_view.png)
</br>

---

3. Detail post view:
</br>


![Screenshot](docs/img/Post_detail_view.png)
</br>

---

4. Tag specific view:
</br>

![Screenshot](docs/img/Tag_related_posts.png)


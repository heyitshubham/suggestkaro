# suggestkaro
This project will give the suggestion for purchasing the product based on star ratings of the product available on the marketplace website/application. Star ratings will get analyzed and the suggestion will be made that this product is worth to purchase or not. Future Module : Fake ratings and reviews will be removed and original ratings will be analyzed. - It reduces the confusion for the customer in making final purchase. - Customer have to paste the link of the product and ratings will get fetched and it will be passed through an algorithm and it will return an output to help the customer for making decision of purchasing the product.

Setup
The first thing to do is to clone the repository:

```
$ git clone https://github.com/heyitshubham/suggestkaro.git
$ cd sample-django-app
```
Create a virtual environment to install dependencies in and activate it:
```
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:
```
(env)$ cd project
(env)$ python manage.py runserver
```

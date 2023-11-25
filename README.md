# Final Project Template From Rod - VERSION LOCAL

URLS Requested data

https://rvicenciow-8000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp/about/
https://rvicenciow-8000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp/contact/

IBM ENDPOINTS

GET DEALERSHIP
Cognitive Cloud: https://rvicenciow-3000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get
LOCAL Node: http://localhost:3000/dealerships/get
Local Django: http://127.0.0.1:8000/djangoapp/api/dealership

GET REVIEW
https://us-south.functions.appdomain.cloud/api/v1/web/c89f82e3-78ef-4147-992d-c5967e2a4256/dealership-package/get-review
v2 https://rvicenciow-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/get_reviews?id=15

POST REVIEW
https://us-south.functions.appdomain.cloud/api/v1/web/c89f82e3-78ef-4147-992d-c5967e2a4256/dealership-package/post-review
https://rvicenciow-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/post_review

------------ rest of the summary --------------------------

The final project for this course has several steps that you must complete.
To give you an overview of the whole project, all the high-level steps are listed below.
The project is then divided into several smaller labs that give the detailed instructions for each step.
You must complete all the labs to successfully complete the project.

## Project Breakdown

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**

1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**

1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**

1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**

1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together

**Add dynamic pages with Django templates**

1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**

1. Add deployment artifacts to your application
2. Deploy your application

# FAST-API
# Simple Project to Fetch Data Of DummyRESTAPI Example Site


# First Step:hypercorn main:app --reload
When we execute First step we will get http://127.0.0.1:8000
# Second Step: For Swagger UI  add /docs for  http://127.0.0.1:8000 i.e  http://127.0.0.1:8000/docs



# In GET:employee: It will give data of DummyRESTAPIexample site user data
# In POST:employee: It will allow us to create new user data


# Steps to Use Data Related to Cities Model
# In POST:cities: It is for to post(Add) User name with time
Example: User Name: 'Rahul', time:'America/Los_angeles'
# When we execute this we will get exact time of Los_angeles
# I have used worldtimeapi for this

# In GET:cities: Here I will get data of Cities which i have created using POST
# In GET:/cities/{city_id}: We will get data based on ID.

# Defining Restriction Rules through Postman

## Introduction

For this exercise, I am using Postman v.8.0.4 to create the proposed restriction rule in the underlying API.  

## Getting access to the API 
Before being able to post the new restriction rules in the API, it is required to input the authorization key in the postman "headers" tab. When working with the Key-Value edit type given by the application, the value of the new key should be inputted in the following format: "'Key name' 'Key Value'". Both are obtained through the user's login in the dashboard of the API provider, at the "Api Keys" menu inside the user's profile page. 

![Api Keys menu](https://github.com/henriquewills/Intern_Test/tree/main/images/Api_keys.jpg)
![Postman Key Auth](https://github.com/henriquewills/Intern_Test/tree/main/images/API_Key_Auth.jpg)

Moreover, it was required to input the customer ID as a path variable in the postman "params" tab, in order to fetch the web address linked to the user's profile. The customer ID value can be found at the "Company" menu inside the user's profile page.

![Company menu](https://github.com/henriquewills/Intern_Test/tree/main/images/Customer_ID_Dashboard.jpg)
![Postman Customer ID](https://github.com/henriquewills/Intern_Test/tree/main/images/Customer_ID.jpg)


## Restriction Rule
The following restriction rule was applied for the selected countries and ISPs. It was chosen the "blacklist" restriction type, which excludes from the Orchestrator and/or mesh network users who belong to the list of Countries OR the list of ISPs.
```
{
 "name":"Rule_Wills",
    "type":"blacklist",
    "countries":["France", "Italy"],
    "isps":["Orange France Mobile", "Wind Tre"]
} 
```
After sending the postman request, it was given the following response:
``` 
{
    "data": {
        "countries": [
            "France",
            "Italy"
        ],
        "customerId": "2aadc4f9-41b6-493f-9cd8-8bf1ef3e735f",
        "id": "3da41df4-33e9-4737-ab0a-b24f32802f96",
        "isps": [
            "Orange France Mobile",
            "Wind Tre"
        ],
        "name": "Rule_Wills",
        "type": "blacklist"
    }
}
``` 
## Postman JSON collection
The resulting postman collection in JSON format can be seen in the shared "Exercise 3 _ postman_collection.json" file in the Github repository. 

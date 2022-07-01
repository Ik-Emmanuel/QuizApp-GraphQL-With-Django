# Quiz App GraphQL API With Django and Graphene
-----

### Introduction 
This Graphql API was built with python django to serve graphl endpoints. It works with graphene and graphen_django library. 


# Description and Overview
The API exposes Quiz App data from sqlite database tables that contains:
 - Quiz categories
 - Quiz questions
 - Quiz answers 


## Versions and Dependencies
- Python 3.9.9
- Django 4.0.4
- graphene==2.1.9
- graphene-django==2.15.0

> **Note** - If you get error: cannot import force_text from venv/Lib/graphene_django/utils/utils. 
> simply edit the `force_text` import to `force_str`. 


## Set Up and Run
- create a virtual enviroment with the python version
- Install dependencies from requirements.txt `pip install requirements.txt`
- Run: `python manage.py runserver`


> **Note** App administration already set up. to sign in to admin portal for data management:
> - visit `"/admin"`  when app is run in 
> - Sign in with:   `username: admin` and `password:password123`


## ENDPOINTS
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/graphql``` | _Single Graphql endpoint_| _All users_|


## GraphQL Example Test Queries
```
### Queries examples

*  query {allQuestions{ quiz {id} title difficulty } } - used to fetch all questions 
*  query {allCategories{id name}}  - used to fetch all quiz categories
*  query { allQuizzes{id title } }  - used to fetch all available quizzes
*  query {allAnswers{ question {quiz{id}  title} answerText isRight}}  -  used to view questions and answers
*  query {specificQuestion(id:2){ id title difficulty}} - fetch a specific question
*  query { specificAnswers(id:2){  question {title} answerText isRight}} - fetch a specific question answer

-----

### Mutations examples

* mutation { createCategory(name:"Test"){category{name}} } - creates a new category and return the category
* mutation{createQuizzes (title:"Blockchain", categoryName:"Technology" ){quiz{title category{ id name }  }}} - create new quiz entry
* mutation{ updateCategory(id: 2, name: "Arts & Music"){ category{name }}}  - update a quiz category
* mutation { deleteCategory(id:6) { category }}  -  deletes a category


```


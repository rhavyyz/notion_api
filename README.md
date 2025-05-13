# Summary
- Setup

- Extra datatypes and endpoints
    - Comment of a Post
    - Comment of a Comment
    - Deleting a comment
    - Like of a Post
    - Like of a Comment   

- Decisions [ Important! ]

## Setup

Inside your python [virtual environment](https://docs.python.org/3/library/venv.html) install de dependencies with:

```
pip install -r requirements.txt
```
Now, setup the database with
```
python manage.py migrate
```

At the end, to run the api:
```
python manage.py runserver
```


## Extra datatypes and endpoints

Other than the mandatory datatypes, the api supports comments and likes, both of them for Posts and Comments.

Comments and likes can only be created and deleted.


- Comment of a Post


List of Comments of a Post with $id=id$.


```json
GET careers/<int:id>/comments/
Response:
[
    {
        "id": 1,
        "content": "text",
        "created_datetime": "2025-05-12T13:09:45.547563Z",
        "username": "silva",
        "post": 9,
        "like_qtd": 15
    },
    {...}
]
```

Create comment for post of $id=id$.

```json
POST careers/<int:id>/comments/ 

Body:
{
    "username": "silva",
    "content": "bunch of texts"
}

Response:
{
    "id": 1,
    "content": "text",
    "created_datetime": "2025-05-12T13:09:45.547563Z",
    "username": "silva",
    "post": 9,
    "like_qtd": 15
}

```

- Comment of a Comment

List of Comments of a Comment with $id=id$.


```json    
GET comments/<int:id>/comments/ 
 
Response:
[
    {
        "id": 1,
        "content": "text",
        "created_datetime": "2025-05-12T13:09:45.547563Z",
        "username": "silva",
        "comment": 9,
        "like_qtd": 15
    },
    {...}
]
```

Create comment for post of $id=id$.

```json
POST comments/<int:id>/comments/ 

Body:
{
    "username": "silva",
    "content": "bunch of texts"
}

Response:
{
    "id": 1,
    "content": "text",
    "created_datetime": "2025-05-12T13:09:45.547563Z",
    "username": "silva",
    "comment": 9,
    "like_qtd": 15
}
```

- Deleteing Comments

Delete Comment with $id=id$. Works for Comments of Posts and for Comments of Comments. 

```
DELETE comments/<int:id>/
```

- Likes of a post

Creates a like for Post with $id=id$ in the name of $username$

```json
POST careers/<int:id>/likes/<str:username>/
```

Deletes a like from Post with $id=id$ in the name of $username$

```json
DELETE careers/<int:id>/likes/<str:username>/
```


- Likes of a post

Creates a like for Comment with $id=id$ in the name of $username$

```json
POST comments/<int:id>/likes/<str:username>/
```

Deletes a like from Comment with $id=id$ in the name of $username$

```json
DELETE comments/<int:id>/likes/<str:username>/
```


## Decisions
The default features are really straight forward CRUD operations of a simple model, but, even in this context I've set the behavior of the serializers to strictly follow their intent.


Ex: A serializer that represents the data format of a model for select operations cannot perform update or create actions.


The separation between Comment and Post Comment/Like doesn't occur at model level. This decision was made aiming to provide a simple way of maintaining data consistency between the two "types" of Comments/Likes. The alternative to this unified approach is to maintain two models for each, making the process of changing these models prone to data inconsistency and more onerous.


The way of counting likes of a post and comment may lead to scalability issues due to the same situation as the [Justin Beiber Problem](https://medium.com/@AVTUNEY/how-instagram-solved-the-justin-bieber-problem-using-postgresql-denormalization-86b0fdbad94b). The decision of not using the same denormalization trick comes from the following way of thinking:


Prioritizing the first in the tradeoff of transaction simplicity in like creation/deletion or Performance. Since the performance optimization is not a must in the current context, writing in a simpler, with less inconsistency chances and more readable way seems reasonable. Because of the simplicity it is also easier to modify and evolve, so, in case the context changes and the performance emerges as a priority the code can be updated.



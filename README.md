# Pokemon Cards!

### Gotta Catch 'Em All

# Introduction
Pokemon cards RESTFUL API where users can create a variety of fantasy decks and wishlists of specified Pokemon cards. Users also have filtering capabilities when searching for cards and can return an overview of their deck and wishlists listing their statistics. Users are also able to add and remove individual cards from both decks and wishlist. 
# API Documentation
## Health Check

Health check API, used for checking if the server is up and working.

```http
GET /v1/health_check
```

Response

```javascript
{
    "Status": "Success"
}
```
-------------------------------------------
## Cards
```http
GET /v1/cards
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `current_page` | `int` | **Required**. The current page you are viewing |
| `limit` | `int` | **Not Required**.The limit per page of how many cards t display. |
| `short` | `bool` | **Not Required**. There are two version to display a card, briefly (short=True) or the longer version.|
| `supertype` | `string` | **Not Required**. The supertype of your pokémon card.|
| `set` | `string` | **Not Required**. The set of your pokémon card. |
| `name` | `string` | **Not Required**. The name of your pokémon card. |


Responses

Returns a list of pokémon cards

```javascript
{
    "Cards": [
       {
            "evolves_from": "Combee",
            "id": "xy7-10",
            "name": "Vespiquen",
            "rarity": "Uncommon",
            "set": "Ancient Origins",
            "subtype": "Stage 1",
            "supertype": "Pokémon"
        },
        {
            "evolves_from": null,
            "id": "dp6-90",
            "name": "Cubone",
            "rarity": "Common",
            "set": "Legends Awakened",
            "subtype": "Basic",
            "supertype": "Pokémon"
        }
    ],
    "Total": 2,
    "next_page": 2
}
```


```http
GET /v1/cards/{id}
```

Responses

Returns a pokémon card respective to the passed id

```javascript
{
    "Card": {
        "ability": null,
        "ancient_trait": null,
        "attacks": [
            {
                "convertedEnergyCost": 1,
                "cost": [
                    "Colorless"
                ],
                "damage": "10",
                "name": "Intelligence Gathering",
                "text": "You may draw cards until you have 6 cards in your hand."
            },
            {
                "convertedEnergyCost": 2,
                "cost": [
                    "Colorless",
                    "Colorless"
                ],
                "damage": "20+",
                "name": "Bee Revenge",
                "text": "This attack does 10 more damage for each Pokémon in your discard pile."
            }
        ],
        "evolves_from": "Combee",
        "hp": "90",
        "id": "xy7-10",
        "name": "Vespiquen",
        "rarity": "Uncommon",
        "series": "XY",
        "set": "Ancient Origins",
        "set_code": "xy7",
        "subtype": "Stage 1",
        "supertype": "Pokémon",
        "text": null,
        "types": [
            "Grass"
        ],
        "weaknesses": [
            {
                "type": "Fire",
                "value": "×2"
            }
        ]
    }
}
```

-------------------------------------------
## Users
```http
GET /v1/users/name
```
Get all users, you can filter by name

Response
```javascript
{
    "users": []
}
```
```http
GET /v1/users/{id}
```
Get users according to passed id

Response
```javascript
{
    "user": {
        "bio": "Adulting is soup and I am a fork, that's why I play Pokémon Cards.",
        "created_at": "2021-03-24T00:00:00",
        "email": "mistyk@gmail.com",
        "id": 1,
        "name": "Misty Kasumi",
        "updated_at": "2021-03-31T13:19:23"
    }
}
```


```http
POST /v1/users
```
Create a new user

Request Body:
```javascript
{
    "bio": "Adulting is soup and I am a fork, that's why I play Pokémon Cards.",
    "name": "Misty Kasumi",
    "email" : "mistyk@outlook.com"
}
```
Response
```javascript
{  
    "user": {
        "bio": "Adulting is soup and I am a fork, that's why I play Pokémon Cards.",
        "created_at": "2021-04-01T17:50:42",
        "email": "mistyk@outlook.com",
        "id": 1,
        "name": "Misty Kasumi",
        "updated_at": "2021-04-01T17:50:42"
    }
}
```
```http
PUT /v1/users/{id}
```
Update user's info

Request Body:
```javascript
{
    "bio": "An updated bio",
    "name": "An updated name"
}
```
Response
```javascript
{
    "count": 1,
    "message": "Success"
}
```
```http
DELETE /v1/users/{id}
```
Delete a user.

Response
```javascript
{
    "count": 1,
    "message": "Success"
}
```
-------------------------------------------
## Decks
```http
POST /v1/decks/{id}/cards
```
Adds a card to deck respective of the id passed

Request body
```javascript
{
    "cards": [
      card id 
    ]
}
```
Response
```javascript
{
    "count": 1,
    "message": "Success"
}
```
```http
DELETE /v1/decks/{id}/cards
```
Delete card respective to passed id 

Response
```javascript
{
    "deck": {
        "cards": [
            {
                "card": {
                    "created_at": "2021-03-21T02:49:14",
                    "id": "xy7-10",
                    "name": "Vespiquen",
                    "subtype": "Stage 1",
                    "supertype": "Pokémon",
                    "updated_at": "2021-03-21T02:49:14"
                }
```
```http
GET /v1/decks
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `email` | `string` | **Required**. Users email address. |


Returns deck collection containing all the cards 

Responses
```javascript
{
    "Decks": [
        {
            "cards": [
                {
                    "card": {
                        "created_at": "2021-03-21T02:49:15",
                        "id": "base1-16",
                        "name": "Zapdos",
                        "subtype": "Basic",
                        "supertype": "Pokémon",
                        "updated_at": "2021-03-21T02:49:15"
                    }
                },
                {
                    "card": {
                        "created_at": "2021-03-21T02:49:15",
                        "id": "base1-17",
                        "name": "Beedrill",
                        "subtype": "Stage 2",
                        "supertype": "Pokémon",
                        "updated_at": "2021-03-21T02:49:15"
                    }
                },
                {
                    "card": {
                        "created_at": "2021-03-21T02:49:15",
                        "id": "base1-18",
                        "name": "Dragonair",
                        "subtype": "Stage 1",
                        "supertype": "Pokémon",
                        "updated_at": "2021-03-21T02:49:15"
                    }
               ]   }
        }
}

       
```
```http
POST /v1/decks
```
Create a new deck for a user

Request Body
```javascript
{
    "email": "mistyk@gmail.com",
    "description": "My rare collection."
}
```
Response
```javascript
{
    "Deck": {
        "cards": [],
        "created_at": "2021-04-02T10:26:14",
        "description": "My rare collection.",
        "id": 6,
        "updated_at": "2021-04-02T10:26:14"
    }
}
```
```http
PUT /v1/decks/{id}
```
Update deck

Request Body:
```javascript
{
    "description" : "update description"
}
```
Respone
```javascript
{
    "count": 1,
    "message": "Success"
}
```
```http
GET /v1/decks/{id}
```
Returns a deck respective to the passed id

Response
```javascript
{
    "Deck": {
        "cards": [],
        "created_at": "2021-04-02T10:36:22",
        "description": "My rare collection.",
        "id": 7,
        "updated_at": "2021-04-02T10:36:22"
    }
}
```
```http
DELETE /v1/decks/{id}
```
Delete deck according to ID passed 

Response

```javascript
{
    "count": 1,
    "message": "Success"
}
```
```http
GET /v1/decks/{id}/cards/stats
```
Get deck statistics in respect to deck id

Response 

```javascript
{
    "Deck Statistics": {
        "Energy cards count": 0,
        "Pokemon cards count": 15,
        "Trainer cards count": 0
    }
}
```
-------------------------------------------
## Wishlists
```http
GET /v1/wishlist
```
Response 
```javascript
{
    "Wishlist": {
        "cards": [
            {
                "card": {
                    "created_at": "2021-03-21T02:49:15",
                    "id": "base1-1",
                    "name": "Alakazam",
                    "subtype": "Stage 2",
                    "supertype": "Pokémon",
                    "updated_at": "2021-03-21T02:49:15"
                },
                "threshold": null
            },
            {
                "card": {
                    "created_at": "2021-03-21T02:49:15",
                    "id": "base1-10",
                    "name": "Mewtwo",
                    "subtype": "Basic",
                    "supertype": "Pokémon",
                    "updated_at": "2021-03-21T02:49:15"
                },
                "threshold": null
            },
            {
                "card": {
                    "created_at": "2021-03-21T02:49:14",
                    "id": "base1-100",
                    "name": "Lightning Energy",
                    "subtype": "Basic",
                    "supertype": "Energy",
                    "updated_at": "2021-03-21T02:49:14"
                },
                "threshold": null
            },
            {
                "card": {
                    "created_at": "2021-03-21T02:49:15",
                    "id": "base1-2",
                    "name": "Blastoise",
                    "subtype": "Stage 2",
                    "supertype": "Pokémon",
                    "updated_at": "2021-03-21T02:49:15"
                },
                "threshold": null
            },
            {
                "card": {
                    "created_at": "2021-03-21T02:49:14",
                    "id": "base1-70",
                    "name": "Clefairy Doll",
                    "subtype": "",
                    "supertype": "Trainer",
                    "updated_at": "2021-03-21T02:49:14"
                },
                "threshold": null
            },
            {
                "card": {
                    "created_at": "2021-03-21T02:49:15",
                    "id": "base1-90",
                    "name": "Super Potion",
                    "subtype": "",
                    "supertype": "Trainer",
                    "updated_at": "2021-03-21T02:49:15"
                },
                "threshold": null
            }
        ],
        "created_at": "2021-03-24T00:00:00",
        "updated_at": "2021-03-24T00:00:00"
    }
}
```
```http
POST /v1/wishlist/{id}
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Cards` | `string` | **Not Required**. The card you are posting |
| `user_/id/cards` | `string` | **Not Required**. The wishlist id.|
Request 
```javascript
{

    "cards" :   ["base1-2",
                 "base1-70",
                 "base1-100",
                 "base1-90",
                 "base1-10"]

}
```
Response
```javascript
{
    "wishlist": {
        "cards": [
            {
                "card": {
                    "created_at": "2021-03-21T02:49:15",
                    "id": "base1-1",
                    "name": "Alakazam",
                    "subtype": "Stage 2",
                    "supertype": "Pokémon",
                    "updated_at": "2021-03-21T02:49:15"
                },
                "threshold": null
```
-------------------------------------------
```http
DELETE /v1/wishlist/{id}
```
Delete a wishlist respective of the id passed
Response

```javascript

{
    "count": 1,
    "message": "Success"
}
```
```http
GET /v1/wishlist/{id}/stats
```
Response
```javascript

{
    "Wishlist Statistics": {
        "Energy cards count": 1,
        "Pokemon cards count": 2,
        "Trainer cards count": 2
    }
}
```
# Status Codes

Pokémon App returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 409 | `CONFLICT` |
| 422 | `UNPROCESSABLE ENTITY` |
| 500 | `INTERNAL SERVER ERROR` |
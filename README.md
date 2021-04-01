# Pokemon Cards!

### Gotta Catch 'Em All

# Introduction
@Jack type here an intro about our app what it does briefly 

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

@jack add here APIs for decks

-------------------------------------------
## Wishlists
@jack add here APIs for wishlists

-------------------------------------------


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
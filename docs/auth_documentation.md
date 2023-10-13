# Auth API Documentation

## Register an account to Zealier
### POST `/register`

Request body sample:
```Json
{
    "username": "Redzyx",
    "email": "redzyx@epitech.eu",
    "password": "RedisisnotRedzyx"
}
```

![](https://img.shields.io/static/v1?label=&message=201&color) Response body sample: 
```Json
{
    "message": "Account Created !"
}
```
![](https://img.shields.io/static/v1?label=&message=400&color=red) Response body sample: 
```Json
{
    "message": "Account Created !"
}
```


## Sign in into your account
### POST `/login`

Request body sample:
```Json
{
    "email": "redzyx@epitech.eu",
    "password": "RedisisnotRedzyx"
}
```


<!-- |Query Parameters|Required|Sample| -->
<!-- | ------|-----|-----| -->
<!-- |id_zealier|`YES`|61cfdc7df54b4df7859b2e0b| -->

 ![](https://img.shields.io/static/v1?label=&message=200&color=green) Response body sample:
```Json
{
    "message": "Sucessfully Logged In",
    "user_id": "61cfdc7df54b4df7859b2e0b"
}
```
 ![](https://img.shields.io/static/v1?label=&message=400&color=red) Response body sample:
```Json
{
    "message": "Invalid credentials"
}
```


## Log out from your account
Clear the `user_id` cache in the front, the BackEnd has nothing to do with that !


## Delete your account
### DELETE `/delete`

Request body sample:
```Json
{
    "user_id": "61cfdc7df54b4df7859b2e0b"
}
```

----------------



![](https://img.shields.io/static/v1?label=&message=200&color=green) Response body sample:
```Json
{
    "message": "Account deleted"
}
```

![](https://img.shields.io/static/v1?label=&message=400&color=red) Response body sample:
```Json
{
    "message": "Can't delete this account"
}
```
# BackEnd Documentations

## Subject Mandatory Routes


## About
### GET /about.json
Response Sample:
```Json
{
    "client": {
        "host": "10.101.53.35"
    },
    "server": {
        "current_time": 1531680780,
        "services": [
            {
                "name": "Weather",
                "widgets": [
                    {
                        "name": "city temperature",
                        "description": "Display temperature for a city",
                        "params": [
                            {
                                "name": "city",
                                "type": "string",
                                "example": "paris"
                            }
                        ],
                        "endpoint": "/weather/refresh",
                    },
                ],
            },
            {
                "name": "Binance",
                "widgets": [
                    {
                        "name": "crypto price on the spot market",
                        "description": "Display the price in USD for a specific crypto in the spot market",
                        "params": [
                            {
                                "name": "crypto",
                                "type": "string",
                                "example": "BTCUSDT",
                            }
                        ],
                        "endpoint": "/crypto_spot/refresh",
                    },
                    {
                        "name": "crypto price on future market",
                        "description": "Display the price in USD for a specific crypto in the future market",
                        "params": [
                            {
                                "name": "crypto",
                                "type": "string",
                                "example": "BTCUSDT",
                            }
                        ],
                        "endpoint": "/crypto_future/refresh",
                    },
                ],
            },
        ],
    }
}
```
## Our Routes:

## POST `/zeal/create_zeal` Create a widget
Request sample:
```Json
{
    "user_id": "642061cf12852c8e4b16570c",
    "service": "Weather",
    "endpoint": "/weather/refresh",
    "body_params": {
        "city": "lille"
    }
}
```
Response sample:
```Json
{
    "message": "OK widget created !"
}
```

## GET `/zeal/get_zeals`   List all widget of an user
Request sample:
```Json
{
    "user_id" : "642061cf12852c8e4b16570c"
}
```
Response sample:
```Json
[
    {
        "name": "Weather",
        "posX": 5,
        "value": 15,
        "body_parans": {
            "city": "paris"
        }
    },
        {
        "name": "Crypto",
        "posX": 0,
        "value": 30000,
        "body_parans": {
            "crypto": "BTCUSDT"
        }
    }
]
```

## POST `/zeal/edit_zeal`     Edit a widget
Request sample:
```Json
{
    "_id": "642062b8e568f04bb0ab6e30",
    "body_params": {
        "city": "lausanne"
    },
    "posX": "-8"
}
```
Response sample:
```Json
{
    "message": "OK widget updated !"
}
```

## POST `/zeal/delete_zeal` Delete a widget
Request sample:
```Json
{
    "_id" : "642061cf12852c8e4b16570c"
}
```
Response sample:
```Json
{
    "message": "OK widget deleted !"
}
```
# Home Django Project
### Controls your SmartThings connected home using a REST API.



| Endpoint | Description |
| ---- | --------------- |
| [GET /api/v1/fan_status]() | Get boolean of current fan status |
| [POST /api/v1/twitter_status]() | Get boolean to turn on/off fan from POST with twitter username |
| [POST /api/v1/github_status]() | Get boolean to turn on/off fan from POST with github username |


#### Twitter POST Params
```json
{
    "username": "_paul____"
}
```

#### Github POST Params
```json
{
    "username": "pmoulton",
    "delta": "<seconds> since last event"
}
```

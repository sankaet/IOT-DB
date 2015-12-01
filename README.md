# IOT-DB
Sample application that allows IOTs to store/view data.

This version of the API is architected around REST using standard HTTP verbs to communicate and HTTP response codes to indicate status and errors. All responses come in standard JSON.

# Clients

Standard client object is used for authentication. Every client object has a `client_id` & `client_secret`.

Currently admin needed to log into shell to create a client.

Every request needes to contain `X-IOT-CLIENT` in the header.

`X-IOT-CLIENT` contains `client_id|client_secret` of the developer accessing the API.

Eg: `X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a`

# Schemas(Client)

Every client can add multiple DB schemas via the API. Schema is meant to protect the structural integrity of data posted to the API.

# GET Schemas

Request

```
curl -X GET -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" 'http://162.243.3.84/v1/schemas'

```

Response

```
[
  {
    "y": [
      1,
      2,
      3,
      4
    ],
    "x": [
      1,
      2,
      3,
      4
    ],
    "_id": "565be18dc6f0c01c0967292d",
    "client": 1
  },
  {
    "temps_in_c": [
      10,
      15
    ],
    "_id": "565be171c6f0c01c08919072",
    "name": "Name of Data",
    "time_in_sec": [
      1234345,
      1234349
    ],
    "client": 1
  }
]
```
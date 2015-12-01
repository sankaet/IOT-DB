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
    "temps_in_c": [10,15],
    "_id": "565be171c6f0c01c08919072",
    "name": "Name of Data",
    "time_in_sec": [1234345,1234349],
    "client": 1
  },
  {
  	...
  },
  {
  	...
  }
]
```

# POST Schemas

Request

```
curl -X POST -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" -d '{
    "x":[1,2,3,4],
    "y":[1,2,3,4]
}' 'http://162.243.3.84/v1/schemas'
```

Response

```
{
  "y": [1,2,3,4],
  "x": [1,2,3,4],
  "client": 1,
  "_id": "565d0140c6f0c02cd5560ccb"
}
```

# GET Schema

Request

```
curl -X GET -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072'
```

Response

```
{
  "temps_in_c": [10,15],
  "_id": "565be171c6f0c01c08919072",
  "name": "Name of Data",
  "time_in_sec": [1234345,1234349],
  "client": 1
}
```

# PUT Schema

Request

```
curl -X PUT -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" -d '{
    "name":"Smart Thermo 1",
    "temps_in_c":[10,15],
    "time_in_sec":[1234345,1234349]
}' 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072'
```

Response

```
{
  "temps_in_c": [10,15],
  "_id": "565be171c6f0c01c08919072",
  "name": "Smart Thermo 1",
  "time_in_sec": [1234345,1234349],
  "client": 1
}
```

# GET Data

Request

```
curl -X GET -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072/data'
```

Response

```
[
  {
    "name": "Name of Data",
    "time_in_sec": [1234345,1234329],
    "temps_in_c": [10,15],
    "schema_id": "565be171c6f0c01c08919072",
    "client": 1,
    "_id": "565cfd8ec6f0c02cd41a836a"
  },
  {
    ...
  },
  {
    ...
  }
]
```

# POST Data

Request

```
curl -X POST -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" -d '{
    "name":"Some new data",
    "temps_in_c":[10,15],
    "time_in_sec":[1234345,1234349]
}' 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072/data'
```

Response

```
{
  "name": "Some new data",
  "time_in_sec": [1234345,1234349],
  "temps_in_c": [10,15],
  "schema_id": "565be171c6f0c01c08919072",
  "client": 1,
  "_id": "565d039ac6f0c02cd6e208c8"
}
```

# GET (1)Data

Request

```
curl -X GET -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072/data/565cfd8ec6f0c02cd41a836a'
```

Response

```
{
  "name": "Name of Data",
  "time_in_sec": [1234345,1234329],
  "temps_in_c": [10,15],
  "schema_id": "565be171c6f0c01c08919072",
  "client": 1,
  "_id": "565cfd8ec6f0c02cd41a836a"
}
```

# PUT Data

Request

```
curl -X PUT -H "Content-Type: application/json" -H "X-IOT-CLIENT: id-a6603153-293c-4d3e-8d60-d189615c814f|secret-a41654b2-dac7-448f-8456-c7082dee439a" -d '{
    "name":"Name of Data",
    "temps_in_c":[10,15],
    "time_in_sec":[1234345,1234329]
}' 'http://162.243.3.84/v1/schemas/565be171c6f0c01c08919072/data/565cfd8ec6f0c02cd41a836a'
```

Response

```
{
  "name": "Name of Data",
  "time_in_sec": [1234345,1234329],
  "temps_in_c": [10,15],
  "schema_id": "565be171c6f0c01c08919072",
  "client": 1,
  "_id": "565cfd8ec6f0c02cd41a836a"
}
```

# Postman

All the API call examples have been added to a postman collection as well. Here is the link: https://www.getpostman.com/collections/d2f68e6a1fe8b182180a

# License

The MIT License (MIT)

Copyright (c) 2015 Sankaet Pathak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
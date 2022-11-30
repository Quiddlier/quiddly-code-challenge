#!/bin/bash

curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Beta",
  "total_amount": 100,
  "outstanding_amount": 100
}'


curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Beta",
  "total_amount": 200,
  "outstanding_amount": 200
}'

curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Gamma",
  "total_amount": 111,
  "outstanding_amount": 111
}'

curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Gamma",
  "total_amount": 222,
  "outstanding_amount": 222
}'

curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Beta",
  "total_amount": 200,
  "outstanding_amount": 200
}'

curl -X 'POST' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sender": "Company Alpha",
  "receiver": "Company Beta",
  "total_amount": 200,
  "outstanding_amount": 200
}'

curl -X 'GET' \
  'http://127.0.0.1:5000/invoice' \
  -H 'accept: application/json'

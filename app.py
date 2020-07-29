#!/usr/bin/env python

import requests
import os
import json
from flask import Flask, Response, request
from twilio.rest import Client
from dotenv import load_dotenv
from postal.expand import expand_address
load_dotenv()

ACCESS_KEY = os.getenv('POSTITION_STACK_API_KEY')

def get_address_set(input):
  # use set to ensure the values are unique
  address = expand_address(input)
  uniq = set(address)
  return list(uniq)

def check_remote_api(address_set):
  results = []
  for address in address_set:
    try:
      response = requests.get(f'http://api.positionstack.com/v1/forward?access_key={ACCESS_KEY}&query={address}')
    except HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    else:
       response = response.json()
       for data in response['data']:
         results.append(data)
       return (results)

# Create a Flask web app
app = Flask(__name__)

# Handle a POST request to validate address
@app.route('/check_input', methods=['POST'])
def check_input():
  input = request.form['input']
  address_list = get_address_set(input)
  return Response(json.dumps(address_list), mimetype='application/json')

# Handle a POST request to lookup address via API
@app.route('/api_lookup', methods=['POST'])
def api_lookup():
  input = request.form['input']
  addresslist = []
  addresslist.append(input)
  address_lookup = check_remote_api(addresslist)
  return Response(json.dumps(address_lookup), mimetype='application/json')

# Handle a POST Request, Store Address in Autopilot Memory
@app.route('/address_memory', methods=['POST'])
def address_memory():
  # Request Fields: https://www.twilio.com/docs/autopilot/actions/autopilot-request
  input = request.form['CurrentInput']
  address_list = get_address_set(input)
  print(address_list)

  if len(address_list)>=1:
    my_actions = {
      "actions": [
        {
          "say": {
            "speech": f"I heard {address_list[0]}. Is that correct?"
          }
        },
        {
			    "remember": {
				    "address": f"{address_list[0]}"
			    }
	      },
        {
          "listen": {
            "tasks": [
              "confirm-address",
              "reject-address"
            ]
          }
        }
      ]
    }

  else:
    my_actions = {
      "actions": [
        {
          "say": {
            "speech": "I didn't get that?"
          }
        },
        {
          "listen": {
            "tasks": [
              "address"
            ]
          }
        }
      ]
    }    

  return Response(json.dumps(my_actions), mimetype='application/json')

if __name__ == '__main__':
    # Note that in production, you would want to disable debugging
    app.run()
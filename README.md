# autopilot-address-validation

![Screenshot](/images/ActionsJSON.png)

Environment variables must be configured in your .env file.

POSTITION_STACK_API_KEY= (optional)

Installation
------------
I found multiple issues when trying to install libpostal while using chefdk. I recommend uninstalling chefdk, installing libpost, and then reinstalling chefdk if you run into similar errors.

Make sure you have the following prerequisites:

## Libpostal (MacOS). For Linux see [Libpostal Github](https://github.com/openvenues/libpostal)
brew remove chefdk
brew install curl autoconf automake libtool pkg-config

git clone https://github.com/openvenues/libpostal

cd libpostal

./bootstrap.sh

./configure --datadir=/tmp

make -j4

sudo make install

## To Switch from LibPostal Python Binding to Postion Stack API

You can either do validation based on address parsing rules in LibPostal, or you can point to an external API.

To switch to the API set the optional environment variable, update the "address_memory" flask endpoint to use the "check_remote_api" method instead of the "get_address_set" method.

## Local Setup

cd autopilot-address-validation

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Run 

./start.sh

## Ngrok Forwarding

ngrok http 5000
# autopilot-api-create

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


## Local Setup

cd autopilot-address-validation

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


## Ngrok Forwarding

ngrok http 5000

## Run 

./start.sh

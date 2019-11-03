#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

SECRET_URL = "https://koodihaaste-api.solidabis.com/secret"

secret_r = requests.get(url = SECRET_URL)

secret_data = secret_r.json()

BULLSHIT_URL = secret_data["bullshitUrl"]
JWT_TOKEN = secret_data["jwtToken"]

bullshit_r = requests.get(url = BULLSHIT_URL, headers={"Authorization": JWT_TOKEN})

bullshit_data = bullshit_r.json()
messages = bullshit_data["bullshits"]

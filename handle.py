#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import bullshits from the API
import get_bullshits

# We use static messages for dev so API doesn't get unnecessary load
# import bullshits 

# Import classification module
import classify

# Iterate through messages and calcuklate all relevant scores
output = []
for item in get_bullshits.messages:
    output.append(vars(classify.Message(item["message"])))

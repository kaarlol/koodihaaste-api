#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import get_bullshits
import bullshits
import classify

output = []
for item in bullshits.messages:
    output.append(vars(classify.Message(item["message"])))

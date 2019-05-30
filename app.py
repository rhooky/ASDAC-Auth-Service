##########################################################
## Let's run our first API call ... to an unexpected API !
## What sort of ouput is that?
## Any comments on the response status?

from flask import Flask, jsonify, request
import os
import controller

response = controller.role("admin")
print response

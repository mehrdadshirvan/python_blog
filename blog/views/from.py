import mysql.connector.connection
from MySQLdb import OperationalError
from django.shortcuts import render, redirect, get_object_or_404
import requests
import json
from django.db import connections
from django.http import HttpResponse



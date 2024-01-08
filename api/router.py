from flask import Blueprint, jsonify
from bs4 import BeautifulSoup  # 获取数据
import re  # 正则表达式，文字匹配
import urllib.request
import urllib.error  # 定制url
import xlwt  # excel操作
import os

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})



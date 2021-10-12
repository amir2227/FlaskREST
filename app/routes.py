from flask import Flask, Response, jsonify, request
from app import app
from app import mongo


@app.route('/test')
def test():
    return 'test'



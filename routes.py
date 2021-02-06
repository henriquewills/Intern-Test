import os
import secrets
import operator
from flask import render_template
from __init__ import app

## The standard route, which is seen when directly opening the localhost, should be addressed to the Test#2 code, related to the
## debugging of the page that is presenting some issues with the code

## The Level3 video of the Test#1 is linked to the '.../video_Level3' webpage extension, whereas the The CloudFront video
## should be accessed through the '.../video_CloudFront' Url


@app.route("/", methods=['GET', 'POST'])
@app.route("/debug", methods=['GET', 'POST'])
def video():
    return render_template('videojs2.html', title='debug')

@app.route("/video_Level3")
def video_LVL3():
    return render_template('Video_Level3.html', title='video_Level3')

@app.route("/video_CloudFront")
def video_CF():
    return render_template('Video_CloudFront.html', title='video_CloudFront')

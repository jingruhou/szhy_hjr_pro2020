import insightface
import urllib
import urllib.request
import cv2
import numpy as np


def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


url = 'https://github.com/deepinsight/insightface/blob/master/sample-images/t1.jpg?raw=true'
img = url_to_image(url)

model = insightface.app.FaceAnalysis()

ctx_id = -1

model.prepare(ctx_id = ctx_id, nms=0.4)
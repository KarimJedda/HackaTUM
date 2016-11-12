import os
from subprocess import Popen, PIPE
import shlex

bse_path = '/workspace/open_nsfw/frames/narcos1_output'
name = 'narcos'

def get_score_for_frame(image_path):
    query = "python ./classify_nsfw.py \
             --model_def nsfw_model/deploy.prototxt \
             --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel \
             {image_path}".format(image_path=image_path)

    process = Popen(shlex.split(query), stdout=PIPE)
    (output, err) = process.communicate()

    for line in output.splitlines():
        if line.startswith('NSFW'):
            return image_path.replace(bse_path+'/', '').replace('-frame.jpeg', '') + ', ' + line.split('NSFW score: ')[1].strip()

with open(name + '.csv', 'wb') as zbla:
    for file in os.listdir(bse_path):
        if file.endswith(".jpeg"):
            zbla.write(get_score_for_frame(bse_path + '/'+ file) + '\n')

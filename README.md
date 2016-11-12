# Computing FSK using Python and OpenNSFW 

Courtesy of Yahoo engineering: 

[https://github.com/yahoo/open_nsfw](https://github.com/yahoo/open_nsfw)

Detailed explanation: [https://yahooeng.tumblr.com/post/151148689421/open-sourcing-a-deep-learning-solution-for](https://yahooeng.tumblr.com/post/151148689421/open-sourcing-a-deep-learning-solution-for)

## Installing the stuff we need

1. Start docker-machine (if Mac)
2. docker build -t caffe:cpu [https://raw.githubusercontent.com/BVLC/caffe/master/docker/standalone/cpu/Dockerfile](https://raw.githubusercontent.com/BVLC/caffe/master/docker/standalone/cpu/Dockerfile)
3. docker run caffe:cpu caffe --version
4. git clone [https://github.com/yahoo/open_nsfw.git](https://github.com/yahoo/open_nsfw.git)
5. cd open_nsfw
6. docker run --volume=$(pwd):/workspace caffe:cpu 
7. python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel test_image.jpg

You will get a result: NSFW score:   0.14057905972

## Python Libraries

1. virtualenv venv
2. source venv/bin/activate
3. pip install moviepy
4. pip install youtube_dl
5. pip install shlex

Now we are all set

## Get a test video using youtube_dl

1. youtube-dl --merge-output-format mp4 [https://www.youtube.com/watch?v=P8IhIPq42Wg](https://www.youtube.com/watch?v=P8IhIPq42Wg)

## Work on the video and split it into frames

1. See splitandtest.py

## Send every frame into classification

1. See classify.py

Now automate it and plot and do more  

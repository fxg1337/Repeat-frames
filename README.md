# Repeat-frames
This scrip will look at a folder of image and copy each n image. 

~ How too~ 

If a video file is missing frames then what to do is: 

1> extract all frames of the video to a folder
2> Work out how many frames you need to add
3> start script and type in the N frame to copy 
4> browes to folder with images 
5. once done run ffmpeg -r 30 -f image2 -s 1920x1080 -i zimg%09d.jpg -c:v libx264 -crf 15 -pix_fmt yuv420p zzNewVid.mp4 to create the new video 

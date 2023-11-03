# Repeat-frames
This scrip will look at a folder of image and copy each n image. 

~ How too~ 

If a video file is missing frames then what to do is: 

1. Extract all frames of the video to a folder (fmpeg -i 20231027063325521@DVR-44573_Ch1.mp4 pic%09d.jpg) 

2. Work out how many frames you need to add

3. Start script and type in the N frame to copy 

4. Browes to folder with images 

5. Once done run ffmpeg -r 30 -f image2 -s 1920x1080 -i zimg%09d.jpg -c:v libx264 -crf 15 -pix_fmt yuv420p zzNewVid.mp4 to create the new video 

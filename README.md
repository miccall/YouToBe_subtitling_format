# YouToBe_subtitling_format

base on python 3.5

The code can formatted the readable articles from rich text and time subtitles
该代码可以把包含富文本和时间的字幕文件，格式化成可以阅读的文章

When we download the subtitles, he is like this
当我们下载字幕后 ，他是这样子的
``` html
  1
  00:00:00,000 --> 00:00:01,380
  <font color="#E5E5E5">this video</font><font color="#CCCCCC"> will go</font><font color="#E5E5E5"> through</font><font color="#CCCCCC"> all the</font>

  2
  00:00:01,380 --> 00:00:02,790
  different image effects in the new

  3
  00:00:02,790 --> 00:00:04,500
  <font color="#CCCCCC">post-processing stack</font><font color="#E5E5E5"> we'll talk about</font>

  4
  00:00:04,500 --> 00:00:06,299
  what they do and how we<font color="#E5E5E5"> can use them</font>

  5
  00:00:06,299 --> 00:00:07,919
  this<font color="#E5E5E5"> video</font><font color="#CCCCCC"> is also the first sponsored</font>

  6
  00:00:07,919 --> 00:00:09,929
  video on this<font color="#CCCCCC"> channel however</font><font color="#E5E5E5"> today's</font>

  7
  00:00:09,929 --> 00:00:11,219
  <font color="#CCCCCC">sponsor is actually something</font><font color="#E5E5E5"> that I</font>
```

After running this script， he is like this
运行脚本之后 他是这样子的
``` txt
    this video will go through all the

    different image effects in the new

    post-processing stack we'll talk about

    what they do and how we can use them

    this video is also the first sponsored

    video on this channel however today's

    sponsor is actually something that I
```





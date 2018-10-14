#Data processing
<p>When we did the category count MapReduce, it prompted the out of index error. <br>
After we diagonsed our program, we found that it was not our program's error but some lines of data missed the columns. <br>
It could be existed in Youtube videos because some videos might be deleted and cannot hold any other properties but their video IDs.<br>
So it is very important to make sure your dataset fits your MapReduce program well at very first.</p>


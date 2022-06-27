# Simple digint classifier

You are provided with a simple paint app that allows<br> 
you to reset it's state, earse stuff and change brush<br>
collors. After pressing "Scan" it will pop up a window<br>
with model's guess on the drawn digit. For it to work<br>
propertly, the following conditions must be meet:<br>
<ul>
    <li>Digit must be the only drawn object on the board</li>
    <li>The smaller the digit is - the thicker it's 28x28 version<br>
        would be - the more accurate the prediction would be<br></li>
</ul>        
To increase it's performance you can change paint_size in settings.py.<br>
<hr>
Having commited couple of tested models, even though all of them outscore<br>
default used model 1 (on small 100-samples test dataset), model 1 seems<br>
to be the only one that generizes well.<br>
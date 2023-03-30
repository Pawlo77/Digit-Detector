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

<hr>
Technical talk:
<ul>
    <li>All 5 models were trained on MNIST or datasets like it (ex MNIST extended etc were checked for better performance, however failed against original one)</li>
    <li>Precise models descriptions:
        <ul>
            <li>final_model2 - Sequential Neural Network trained in Tensorflow (keras) with around 700k params, used normal MNIST for 11 epochs</li>
            <li>final_model1 - Sequential Neural Network trained in Tensorflow (keras) with around 2.700k params, used normal MNIST for 18 epochs</li>
            <li>final_model2 - Sequential Neural Network trained in Tensorflow (keras) with around 700k params, used normal MNIST</li>
            <li>final_model1 - Sequential Neural Network trained in Tensorflow (keras) with around 2.700 params, used normal MNIST for 22 epochs</li>
            <li>final_model1 - Sequential Neural Network trained in Tensorflow (keras) with around 2.700k params, used normal MNIST for 12 epochs</li>
        </ul>
        Models 2-4 are a little bit different, but all of them are much deeper than first one, therefore the lag before prediction in the kivy app is larger <br><i>(their scores on paper tend to be a little bit higher than first one, however in practice first one is the best choice performance and accuracy - wise)</i>
    </li>
 </ul>

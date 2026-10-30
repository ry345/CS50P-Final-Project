# <span style="color:blue">AVOID THE SPIKES</span>
# <span style="color:green">Hello! I'm ryan, and this is my [project](./project.py).</span>  
- ***This is a fun 2d game in which the player has to avoid the spike by jumping. It's a bit like dino game!***<br/>
- ***all spikes are actually the same one! It resets position after going past the spike(x coordinate < 230).***<br/>
- ***The background gets assigned a random speed at first, and then the ground gets assigned $\frac{3}{10}$ of the random speed.***<br/>
- ***Since it is a parallax scrolling background, so the ground and background will scroll infinitely with different speeds!***
# <span style="color:green">video demo</span>:
### <https://youtu.be/Vd0JUdDB6lk>
## <span style="color:green">usage:</span>
- **run _`pip install pygame`_ to install the library required, as defined in _[requirements.txt](./requirements.txt)_,**<br/>
- **and if you don't have _`pip`_, go to bootstrap's _[get-pip.py](https://bootstrap.pypa.io/get-pip.py)_ and run the file. Now you can run _`pip install pygame`_,**<br/>
- **and run _`python project.py`_ to run the game.**<br/>
- **to run the test, run _`pytest test_project.py`_ or _`python -m pytest test_project.py`_ if the former does not work.**<br/>
- **you may see a warning, called _`DeprecationWarning`_ saying that `pkg_resources is deprecated as an API.`**<br/>
- **If so, ignore the warning as _`pkg_resources`_ is one of _`pygame`_'s modules. It does not affect the game itself.**<br/>
- **all six tests should work.**
# <span style="color:green">Challenges and processes:</span>
__One of the biggest problems i had was a play button. It was not working and took up a lot of time, so i ditched the idea.__
__I also spent a lot of time looking at inrelated websites, etc. So i wasted quite some time__
__I also spend too much time adjusting backgrounds__
__Another challenge i had was the jumping sound.__
__At first i put it at the top of `Player` class's `if self.jump`:__  
__so it played a lagging sound__
__but i then found that a process of `self.jump` takes several frames so i put it at the end__
__I also planned to do flappy bird at first__
__but I found that coming up with my own game was better__
__and that flappy bird was a bit more complex__
__Another challenge was creating a high score__
__but it had problems writing to the file__ 
__and i did not want to append to a list__
__so i ditched the idea__
__I created `pythagoras` for flappy bird, `fibonacci` as a challenge and `biggest_value` for high score__
__so i struggled to find a usage for them__
__and i decided to put them into the `randomness` function__
# <span style="color:green">Credits</span>
## <span style="color:red">***Thanks to my friend who learnt cs50 for giving me good advice,***</span> 
## <span style="color:green">***Thanks to my parents who gave me constant support,***</span>
## <span style="color:orange">***and thanks for my brother who tested the game and gave me advice on how to improve!***</span>
# <span style="color:blue">Thank you!</span>
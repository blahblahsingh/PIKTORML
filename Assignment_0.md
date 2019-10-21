### What is the definition of Machine Learning according to Arthur Samuel?
A popular definition is __" Field of study that gives computers the ability to learn without being explicitly programmed"__, But this definition does not exist in the papers written by Arthus Samuel in 1959 or 1967.
The closest statements to the above definition are:
__"A computer can be programmed so that it will learn to play a better game of checkers than can be played by the person who wrote the program."__
 
__" Programming computers to learn from experience should eventually eliminate the need for much of this detailed programming effort."__
 
ref: [Source of Arthur Samuel's definition of ML](https://datascience.stackexchange.com/questions/37078/source-of-arthur-samuels-definition-of-machine-learning)
 
### What is the definition of Machine Learning according to Tom Mitchell?
A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.
ref: [Machine Learning by Tom M Mitchell](http://profsite.um.ac.ir/~monsefi/machine-learning/pdf/Machine-Learning-Tom-Mitchell.pdf)
 
### Using an example of a machine learning problem (Anything that you can pose) explain it using the terms in Question 2 in your own words
 
Consider a robot that is meant to simulate a Table Tennis player. It has a certain program running in its CPU that helps it make decisions in terms of returning the ball in a certain fashion depending on the angle, speed, bounce and spin of the incoming tt ball. With respect to Tom Mitchell's definition, we have the following:
 
* **E:** Attempting to return the incoming TT ball
* **T:** To successfully return the incoming TT ball
* **P:** Number of successful returns per hundred attempts
 
The bot will improve its performance by re-adjusting the attack angle and speed for a particular incoming shot (i.e, set speed, spin, height etc) for every unsuccessful return. This will keep happening until the most desirable return is established.

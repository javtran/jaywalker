Speed Model Making
===

# Speed Models

## Table of Contents
1. [Paper Speed Model](Paper-Speed-Model)
2. [Dangerous Speed Model](Dangerous-Speed-Model)
3. [Suicides Speed Model](Suicide-Speed-Model)
4. [Question Reflection](Question-Reflection)

## Paper Speed Model

### Description
This speed model bases off on 3 data parameter given by the paper ["Application of social force model to pedestrian behavior analysis at signalized crosswalk"](). The 3 parameters we changed were relaxation time, desired speed, and maximum crossing speed. We set a minimum speed to set bounds of the range of speed.

| Parameters      | unit    |
| --------------- | ------- |
| min speed       | 1 m/s   |
| max speed       | 1.8 m/s |
| desired speed   | 1.6 m/s |
| relaxation time | 1 s     |

### Gif Demonstration

<img src='https://media4.giphy.com/media/naMqau6aXClhZ3wnuI/giphy.gif' title ='' alt=''/>

<img src='https://media2.giphy.com/media/ZUfOqlyajAh9FZVRaG/giphy.gif?cid=790b761171b7626ab052ce3f0a5411ef4fd9918b433f582e&rid=giphy.gif&ct=g' title ='' alt=''/>

<img src='https://media2.giphy.com/media/8nZNHTLgo7Qahg4LXl/giphy.gif?cid=790b7611f35ddf221d12c1ad2984fe58f0498f8424afbb3e&rid=giphy.gif&ct=g' title =''
alt=''/>

## Dangerous Speed Model

### Description
This speed model is experimental with 4 data parameters: relaxation time, desired speed, minimum crossing speed, and maximum crossing speed. The goal for this model is to model a faster speed model to make the pedestrian act in a dangerous way.


| Parameters      | unit    |
| --------------- | ------- |
| min speed       | 10 m/s  |
| max speed       | 20 m/s  |
| desired speed   | 15 m/s  |
| relaxation time | 1 s     |

### Gif Demonstration

## Suicide Speed Model

### Description
This speed model is experimental with 4 data parameters: relaxation time, desired speed, minimum crossing speed, and maximum crossing speed. The goal for this model is make a sort of unrealistic simulation to experiment around with the 4 parameters.

| Parameters      | unit    |
| --------------- | ------- |
| min speed       | 50 m/s  |
| max speed       | 100 m/s |
| desired speed   | 75 m/s  |
| relaxation time | 1 s     |

### Gif Demonstration

<img src='https://media0.giphy.com/media/40y86FAC82Wp1aAxMF/giphy.gif?cid=790b761184244985e8c4f2ed747c15e13ae232ca7a899344&rid=giphy.gif&ct=g' />


## Question Reflection
1. What changes can you observe in the simulation if the relaxation time is changed? Describe the effects of having a long relaxation time which are not easily observable.

Relaxation determines the acceleration or deceleration from current speed to desired speed. While messing around with the speed models, changing the 4 parameters, a short relaxation time definitely shows a fast change of speed. With long relaxation time, we saw the changes from current speed to desired speed to take longer. Though Long relaxation time are hard to observe, if we put a bigger range for current speed to desired speed, the changes can visually be seen.

2. How is your speed model different from the StaticSpeedModel? Could you detect any chagnes visually? If not, why?

The speed model that models after the reading is definitely slower to mimic realistic pedestrian speed.There is definitely a faster reaction time in static speed model than in the Paper Speed Model, but that's because the paper speed model has a longer relaxation time. For the other two models that we created, the obvious difference is in speed. Since the relaxation time is set to 1, the changes could be detected in the simulation. But these two models definitely acted more dangerously.

## Paper Review 2 Question (Jackson Tran)
1. Why speed model is needed?

In order to produce a more realistic vehicle-pedestrian jaywalking situations, we need to create speed models that best capture human walking behaviors. Our technology is not advanced enough to copy 100% of human behaviors and so we create many speed models to mimic such behaviors.

2. How does the papers capture speed variation while a pedestrian is crossing?

The paper uses different variables/parameters to capture any effects they have on speed and also to see correlations within the variables. Examples of such variables/parameters are group-crossing, age groups, gender, technological distraction, and carrying items.

3. Make a list of factors that determines the speed of a pedestrian.

Group-crossing, alone-crossing, age groups, gender, technological distraction, situational awareness models(looking left-right/right-left/front/ground), conflict models(conflict experience/collision avoidance)

4. When amy a drastic change in speed take place?

Evasive behavior causes drastic change in pedestrian speed. As they avoid conflict and collision, they make actions such as accelarating at an angle or  deccelerating (which can also mean deccelerating to stop).

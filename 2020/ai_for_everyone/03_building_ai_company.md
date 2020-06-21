# Building AI in your Company

Table of contents:

- [Building AI in your Company](#building-ai-in-your-company)
  - [Case Study: Smart Speaker](#case-study-smart-speaker)
  - [Case study: Self-driving car](#case-study-self-driving-car)
  - [Roles of an AI team.](#roles-of-an-ai-team)

## Case Study: Smart Speaker

command:

`Hey Device, tell me a joke`

__Step to process the command__
1. Trigger word/wakeword detection 
      -  (audio) "Hey Device?" 
2. Speech recognition
      
      - Audio -> "tell me a joke"
3. Intent recognition

    - tell me a "joke" (intent)
    - you can mapping list of intent
      - joke?
      - time?
      - music?
      - call?
      - wheater?

4. Execute joke


command:

`Hey device, set timer for 10 minutes`

__Step to process the command__
1. Trigger word/wakeword detection 
      -  (audio) "Hey Device?" 

2. Speech recognition
      
      - Audio -> "set timer for 10 minutes"

3. Intent Recognition

    -   set timer for 10 minutes -> timer

4. Extract duration

    - "set timer for `10 minutes`"
    - "let me know wen `10 minutes` is up"
5. Start Timer with set duration


other function:

1. play music
2. volume up/down
3. make a call
4. current time
5. unit conversion
6. simple question

-----------

## Case study: Self-driving car

[Video](https://www.coursera.org/learn/ai-for-everyone/lecture/lekja/case-study-self-driving-car)

Step for deciding how to drive

Image/Radar/Lidar -> Car Detection & Pedestrian detection -> `Motion planning` -> Steer/Accelerate/Break

<img src="./step_for_deciding_how_to_drive.png" />


Key steps:

1. Car detection - check camera in front, left and other side 
2. Pedestrian detection 
3. Motion planning: this is a piece of software tell you what is the path, shown here in red, you should drive in order to follow the road and not have an accident.  So the motion planning software's job is to output the path as well as speed at which you should drive your car in order to follow the road, and the speed should be set so that you don't run into the other car, but you also drive at a reasonable speed on this road.


Complete step for deciding how to drive

<img src="./step_for_deciding_how%20to_drive_complete.png">

---------------

## Roles of an AI team.

[Video](https://www.coursera.org/learn/ai-for-everyone/lecture/FlPw6/example-roles-of-an-ai-team)
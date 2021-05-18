#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on May 18, 2021, at 14:18
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'InterleavedStaircase'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\m01578dp\\InterleavedStaircase_2IFC_newer\\InterleavedStaircase_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please evaluate the differences in realism between the two scenes. You will be presented with 2 images describing the same scene with a short interval between them.\n\nA reference image will also be provided for each scene.\n\nPress the  ‘left’ arrow key if you think the first stimulus was more realistic.\n\nPress the  ‘right’ arrow key if you think the second stimulus was more realistic.\n\nPress any key to start',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "set_condition"
set_conditionClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Reference Image ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
leftImagePortrait = visual.ImageStim(
    win=win,
    name='leftImagePortrait', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
rightImagePortrait = visual.ImageStim(
    win=win,
    name='rightImagePortrait', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please record your answer. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
resp = keyboard.Keyboard()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "end"
endClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Thank you for participating in this trial. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('imageCondsNewest.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "set_condition"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    imageSet = imageSetLvl
    imageSetStr = str(imageSet)
    setName = imageSetName
    nRefImage = refSetNumber
    
    initStep = (nRefImage)
    
    #noOfMiniScenes  = 3
    noOfMiniScenes = 2
    
    reversals = 0
    trialCounter = 1
    
    reversalsSharp = 0
    reversalsFlat =  0
    
    
    
    levList = [0] * 2
    respList = [0] * 2
    kestList = [0] * 2
    reverseList = [0] * 2
    localTrialNo = [0] * 2
    staircaseTrialNo = [1] * 2
    
    for i in range(2):
        levList[i] = [0] * (noOfMiniScenes + 2)
        respList[i] = [0] * (noOfMiniScenes + 2)
        kestList[i] = [0] * (noOfMiniScenes + 2)
        reverseList[i] = [0] * (noOfMiniScenes + 2)
        localTrialNo[i] = [0] * (noOfMiniScenes + 2)
        for j in range(noOfMiniScenes + 2):
            levList[i][j] = [0] * 100
            respList[i][j] = [0] * 100
            kestList[i][j] = [0] * 100
            reverseList[i][j] = [0] * 100
            localTrialNo[i][j] = 1
            
            
    
    
    #globalTrialNo = 60
    globalTrialNo = 64
    
    maxNoFlat = globalTrialNo/(noOfMiniScenes * 2)
    
    referenceImage = f'stimuli/{imageSetStr}/ref.png'
    
    
    #image = visual.ImageStim(win, image='stimuli/studio/21_studio.png')
    #imageRatio = image.size[1] / image.size[0]
    #print("Aspect ratio is: " + str(imageRatio)) 
    #newScale = 1 # new horizontal size. vertical size will scale appropriately.
    #image.setSize((newScale, newScale * imageRatio)) #
    
    
    image.setImage(referenceImage)
    # keep track of which components have finished
    set_conditionComponents = [text_3, image]
    for thisComponent in set_conditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    set_conditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "set_condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = set_conditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=set_conditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "set_condition"-------
    for thisComponent in set_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_3.started', text_3.tStartRefresh)
    trials_2.addData('text_3.stopped', text_3.tStopRefresh)
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=64, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        
        images1 = [f'stimuli/{imageSetStr}/1/{i}.png' for i in range(22)]
        images2 = [f'stimuli/{imageSetStr}/2/{i}.png' for i in range(22)]
        images3 = [f'stimuli/{imageSetStr}/3/{i}.png' for i in range(22)]
        
        
        
        currentScene = int(random() * noOfMiniScenes) + 1
        staircase = round(random()) 
        
        if staircase == 0 and staircaseTrialNo[staircase] > globalTrialNo/2:
            staircase = 1
        if staircase == 1 and staircaseTrialNo[staircase] > globalTrialNo/2:
            staircase = 0
        
        if trialCounter <= globalTrialNo:
            if staircase == 0:
                    phi = 0.25
                    initN = nRefImage * 3
                    staircaseTrialNo[staircase] += 1
                    if localTrialNo[staircase][currentScene] > maxNoFlat:
                        i = 1 
                        while (i <= noOfMiniScenes): 
                            if localTrialNo[staircase][i] <= maxNoFlat:
                                currentScene = i
                            i = i + 1
            else:
                    phi = 0.75
                    initN = 0
                    staircaseTrialNo[staircase] += 1
                    if localTrialNo[staircase][currentScene] > maxNoFlat:
                        i = 1 
                        while (i <= noOfMiniScenes):  
                            if localTrialNo[staircase][i] <= maxNoFlat:              
                                currentScene = i
                            i = i + 1
        
        if currentScene == 1:
            images = images1
        elif currentScene == 2:
            images = images2
        elif currentScene == 3:
            images = images3
        print("Current local scene no is: " + str(currentScene))
        trial = localTrialNo[staircase][currentScene]
        print("Trial is: " + str(trial) + " " + str(staircase))
        
        if random() > 0.5:
            refSide = 1
        else:
            refSide = -1
            
        compSide = refSide * -1 
        
        if trial == 1:
           levList[staircase][currentScene][trial] = initN
        elif trial == 2:
            levList[staircase][currentScene][trial] = initN-(initStep/2)*(kestList[staircase][currentScene][trial-1]-phi)
        else:
            levList[staircase][currentScene][trial] = levList[staircase][currentScene][trial-1]-(initStep/(reversals+2))*(kestList[staircase][currentScene][trial-1]-phi)
        
        print("Before quality level is: " + str(levList[staircase][currentScene][trial]))
        # bound range
        if staircase ==  0:
            if levList[staircase][currentScene][trial] > initN:
                levList[staircase][currentScene][trial] = initN
            if levList[staircase][currentScene][trial] < 0:
                levList[staircase][currentScene][trial] = 0
        elif staircase == 1:
            if levList[staircase][currentScene][trial] < initN:
                levList[staircase][currentScene][trial] = initN
            if levList[staircase][currentScene][trial] < 0:
                levList[staircase][currentScene][trial] = 0
        
        
        print("Current quality level is: " + str(levList[staircase][currentScene][trial]))
        
        nCompQuality = int(round(levList[staircase][currentScene][trial]))
        
        comp_num = nCompQuality 
        
        
        #winAspectRatio = win.size[1]/win.size[0]
        #print("Window aspect ratio is: " + str(winAspectRatio))
        #leftImagePortrait.size = (1, 1*winAspectRatio)
        #rightImagePortrait.size = (1, 1*winAspectRatio)
        
        if refSide == -1:
            leftImage = images[nRefImage]
            rightImage = images[comp_num]
            
        else:
            leftImage = images[comp_num]
            rightImage = images[nRefImage]
        
        
        leftImagePortrait.setImage(leftImage)
        rightImagePortrait.setImage(rightImage)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [leftImagePortrait, ISI, rightImagePortrait, text_2, resp, ISI_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImagePortrait* updates
            if leftImagePortrait.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftImagePortrait.frameNStart = frameN  # exact frame index
                leftImagePortrait.tStart = t  # local t and not account for scr refresh
                leftImagePortrait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImagePortrait, 'tStartRefresh')  # time at next scr refresh
                leftImagePortrait.setAutoDraw(True)
            if leftImagePortrait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImagePortrait.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImagePortrait.tStop = t  # not accounting for scr refresh
                    leftImagePortrait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImagePortrait, 'tStopRefresh')  # time at next scr refresh
                    leftImagePortrait.setAutoDraw(False)
            
            # *rightImagePortrait* updates
            if rightImagePortrait.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                rightImagePortrait.frameNStart = frameN  # exact frame index
                rightImagePortrait.tStart = t  # local t and not account for scr refresh
                rightImagePortrait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImagePortrait, 'tStartRefresh')  # time at next scr refresh
                rightImagePortrait.setAutoDraw(True)
            if rightImagePortrait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImagePortrait.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImagePortrait.tStop = t  # not accounting for scr refresh
                    rightImagePortrait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImagePortrait, 'tStopRefresh')  # time at next scr refresh
                    rightImagePortrait.setAutoDraw(False)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 5.7-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *ISI* period
            if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                ISI.start(0.5)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
                ISI.tStop = ISI.tStart + 0.5  # record stop time
            # *ISI_2* period
            if ISI_2.status == NOT_STARTED and t >= 3-frameTolerance:
                # keep track of start time/frame for later
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.tStart = t  # local t and not account for scr refresh
                ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                ISI_2.start(0.2)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
                ISI_2.tStop = ISI_2.tStart + 0.2  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store level and response
        #respList.append(response)
        thisExp.addData('Trial No.', localTrialNo[staircase][currentScene])
        thisExp.addData('Comp Side', refSide * -1)
        thisExp.addData('Ref Num', nRefImage)
        thisExp.addData('Level List', levList[staircase][currentScene][trial])
        thisExp.addData('Bounce Num', comp_num)
        thisExp.addData('Staircase', staircase)
        thisExp.addData('Scene No', currentScene)
        
        kestResp = 0
        if compSide < 0 and resp.keys == 'left':
            kestResp = 1 # comp more realistic 
        elif compSide > 0 and resp.keys == 'right':
            kestResp = 1 # comp more realisitic
        
        
        kestList[staircase][currentScene][trial] = kestResp
        thisExp.addData('comp>ref?', kestResp)
        
        # count reversals
        if localTrialNo[staircase][currentScene] > 1:
            if kestList[staircase][currentScene][trial] != kestList[staircase][currentScene][trial-1]:
                reversals += 1
                reverseList[staircase][currentScene][reversals] = levList[staircase][currentScene][trial-1]
        
        # increment trials
        localTrialNo[staircase][currentScene] += 1
        trialCounter = trialCounter + 1 
        
        
        trials.addData('leftImagePortrait.started', leftImagePortrait.tStartRefresh)
        trials.addData('leftImagePortrait.stopped', leftImagePortrait.tStopRefresh)
        trials.addData('ISI.started', ISI.tStart)
        trials.addData('ISI.stopped', ISI.tStop)
        trials.addData('rightImagePortrait.started', rightImagePortrait.tStartRefresh)
        trials.addData('rightImagePortrait.stopped', rightImagePortrait.tStopRefresh)
        trials.addData('text_2.started', text_2.tStartRefresh)
        trials.addData('text_2.stopped', text_2.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
        trials.addData('resp.keys',resp.keys)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        trials.addData('resp.started', resp.tStartRefresh)
        trials.addData('resp.stopped', resp.tStopRefresh)
        trials.addData('ISI_2.started', ISI_2.tStart)
        trials.addData('ISI_2.stopped', ISI_2.tStop)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 64 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_4]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

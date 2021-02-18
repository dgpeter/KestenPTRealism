/***************************** 
 * Interleavedstaircase Test *
 *****************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'InterleavedStaircase';  // from the Builder filename that created this script
let expInfo = {'Participant:': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'imageConds3.xlsx', 'path': 'imageConds3.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var text;
var key_resp;
var set_conditionClock;
var trialClock;
var leftImagePortrait;
var rightImagePortrait;
var text_2;
var resp;
var endClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Please evaluate the quality differences between the two scenes.\n\nPress  ‘left’  if you think the stimulus on the left is of higher quality\n\nPress  ‘right’ if you think the stimulus on the right is of higer quality\n\nPress any key to start',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "set_condition"
  set_conditionClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  leftImagePortrait = new visual.ImageStim({
    win : psychoJS.window,
    name : 'leftImagePortrait', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.5), 0], size : [0.99, 0.99],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rightImagePortrait = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rightImagePortrait', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.5, 0], size : [0.99, 0.99],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Please record your answer. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(text);
    InstructionsComponents.push(key_resp);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instructions'-------
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_2;
var currentLoop;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'imageConds3.xlsx',
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(set_conditionRoutineBegin(snapshot));
    trials_2LoopScheduler.add(set_conditionRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(set_conditionRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    trials_2LoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    trials_2LoopScheduler.add(trialsLoopScheduler);
    trials_2LoopScheduler.add(trialsLoopEnd);
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 18, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var imageSet;
var imageSetStr;
var setName;
var nRefImage;
var initStep;
var noOfMiniScenes;
var reversals;
var trialCounter;
var reversalsSharp;
var reversalsFlat;
var levList;
var respList;
var kestList;
var reverseList;
var localTrialNo;
var globalTrialNo;
var maxNoFlat;
var set_conditionComponents;
function set_conditionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'set_condition'-------
    t = 0;
    set_conditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    imageSet = imageSetLvl;
    imageSetStr = imageSet.toString();
    setName = imageSetName;
    nRefImage = refSetNumber; 
    
    initStep = (nRefImage * 2);
    
    noOfMiniScenes  = 3;
    
    reversals = 0;
    trialCounter = 1;
    
    reversalsSharp = 0;
    reversalsFlat =  0;
    
    
    
    levList = new Array(2);
    respList = new Array(2);
    kestList = new Array(2);
    reverseList = new Array(2);
    localTrialNo = new Array(2);
    
    
    globalTrialNo = 18;
    maxNoFlat = globalTrialNo/(noOfMiniScenes * 2);
    
    
    for(var i = 0; i < levList.length; i++)
    {
        levList[i]= new Array(noOfMiniScenes + 2);
        respList[i] = new Array(noOfMiniScenes + 2);
        kestList[i] = new Array(noOfMiniScenes + 2);
        reverseList[i] = new Array(noOfMiniScenes + 2);
        localTrialNo[i] = new Array(noOfMiniScenes + 2);
        for(var j = 1; j <= noOfMiniScenes + 2; j++)
        {
            levList[i][j]= new Array(100).fill(0);
            respList[i][j] = new Array(100).fill(0);
            kestList[i][j] = new Array(100).fill(0);
            reverseList[i][j] = new Array(100).fill(0);
            localTrialNo[i][j] = 1;
        }
        
    }
    
    
    
    // keep track of which components have finished
    set_conditionComponents = [];
    
    set_conditionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function set_conditionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'set_condition'-------
    // get current time
    t = set_conditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    set_conditionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function set_conditionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'set_condition'-------
    set_conditionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "set_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var leftImage;
var rightImage;
var images1;
var images2;
var images3;
var staircase;
var currentScene;
var currentStaircase;
var phi;
var initN;
var images;
var trial;
var refSide;
var compSide;
var stairFactor;
var nCompQuality;
var comp_num;
var _resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    leftImage = new Image();
    rightImage = new Image();
    
    images1 = new Array();
    images2 = new Array();
    images3 = new Array();
    
    function preload(images, set) {
        for (var i = 0; i < 22; i++) {
            images[i] = new Image();
            images[i].src = `stimuli/${imageSetStr}/${set}/${i}_${setName}.png`;
        }
    }
    
    preload(images1, 1);
    preload(images2, 2);
    preload(images3, 3);
    
    
    staircase = 0;
    
    currentScene = Math.floor(Math.random() * noOfMiniScenes) + 1;
    currentStaircase = Math.random();
    
    
    
    if(trialCounter <= globalTrialNo/2)
    {
    //if ((Math.random() > 0.5)) {
        phi = 0.25;
        initN = (nRefImage * 3);
        staircase = 0;
        if(localTrialNo[staircase][currentScene] > maxNoFlat){
            for(var i = 1; i <= noOfMiniScenes; i++){
                if(localTrialNo[staircase][i] <= maxNoFlat){
                    currentScene = i;}
                   }
             }
                    
    }
    else {
    //if  ((Math.random() <= 0.5)){
        phi = 0.75;
        initN = 0;
        staircase = 1;
        if(localTrialNo[staircase][currentScene] > maxNoFlat){
            for(var i = 1; i <= noOfMiniScenes; i++){
                if(localTrialNo[staircase][i] <= maxNoFlat){
                    currentScene = i;}
                    }
                 }
    }
    
    
    images = []
    if (currentScene == 1)
    {
        images = images1;
    }
    else if (currentScene == 2)
    {
        images = images2;
    }
    else if (currentScene == 3)
    {
        images = images3;
    }
    
    
    
    trial = localTrialNo[staircase][currentScene];   
    
    if ((Math.random() > 0.5)) {
        refSide = 1;
    } else {
        refSide = (- 1);
    }
    compSide = (refSide * (- 1));
    stairFactor = true;
    //if(staircase == 1){
    //    stairFactor = -1;}
    if ((trial === 1)) {
        levList[staircase][currentScene][trial] = initN;
    } else
    {
        if ((trial === 2)) 
        {
            levList[staircase][currentScene][trial] = initN - ((initStep / 2) * (kestList[staircase][currentScene][(trial - 1)] - phi));
        } 
        else
        {
            levList[staircase][currentScene][trial] = levList[staircase][currentScene][(trial - 1)] - ((initStep / (reversals + 2)) * (kestList[staircase][currentScene][(trial - 1)] - phi));
        }
    }
    console.log("Trial is: " + trial);
    console.log("Level before is: " + levList[staircase][currentScene][trial]);
    if(staircase == 0)
    {
        if ((levList[staircase][currentScene][trial] > initN)) {
            levList[staircase][currentScene][trial] = initN;
        }
    
        if ((levList[staircase][currentScene][trial] < 0)) {
            levList[staircase][currentScene][trial] = 0;
        }
    }
    else
    {
        if ((levList[staircase][currentScene][trial] < initN)) {
            levList[staircase][currentScene][trial] = initN;
        }
        if ((levList[staircase][currentScene][trial] < 0)) {
            levList[staircase][currentScene][trial] = 0;
        } 
    }
    console.log("Level after is: " + levList[staircase][currentScene][trial]);
    
    nCompQuality = Number.parseInt(round(levList[staircase][currentScene][trial]));
    comp_num = nCompQuality;
    
    
    if ((refSide === (- 1))) {
        leftImage = images[nRefImage];
        rightImage = images[comp_num];
    } else {
        leftImage = images[comp_num];
        rightImage = images[nRefImage];
    }
    
    leftImagePortrait.setImage(leftImage);
    rightImagePortrait.setImage(rightImage);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(leftImagePortrait);
    trialComponents.push(rightImagePortrait);
    trialComponents.push(text_2);
    trialComponents.push(resp);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *leftImagePortrait* updates
    if (t >= 0.5 && leftImagePortrait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leftImagePortrait.tStart = t;  // (not accounting for frame time here)
      leftImagePortrait.frameNStart = frameN;  // exact frame index
      
      leftImagePortrait.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((leftImagePortrait.status === PsychoJS.Status.STARTED || leftImagePortrait.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      leftImagePortrait.setAutoDraw(false);
    }
    
    // *rightImagePortrait* updates
    if (t >= 0.5 && rightImagePortrait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightImagePortrait.tStart = t;  // (not accounting for frame time here)
      rightImagePortrait.frameNStart = frameN;  // exact frame index
      
      rightImagePortrait.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rightImagePortrait.status === PsychoJS.Status.STARTED || rightImagePortrait.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rightImagePortrait.setAutoDraw(false);
    }
    
    // *text_2* updates
    if (t >= 5.5 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *resp* updates
    if (t >= 5.5 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var kestResp;
function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("Trial No.", trial);
    psychoJS.experiment.addData("Comp Side", (refSide * (- 1)));
    psychoJS.experiment.addData("Ref Num", nRefImage);
    psychoJS.experiment.addData("Level List", levList[staircase][currentScene][trial]);
    psychoJS.experiment.addData("Bounce Num", comp_num);
    psychoJS.experiment.addData("Staircase", staircase);
    psychoJS.experiment.addData("Scene No", currentScene);
    
    kestResp = 0;
    if (((compSide < 0) && (resp.keys === "left"))) {
        kestResp = 1;
    }
    else {
            if (((compSide > 0) && (resp.keys === "right"))) 
            {
                kestResp = 1;
            }
        }
    
    //if(staircase == 0)
    //{
    //    if (((compSide < 0) && (resp.keys === "left"))) {
    //    kestResp = 1;
    //}
    //else {
    //        if (((compSide > 0) && (resp.keys === "right"))) 
    //        {
    //            kestResp = 1;
    //        }
    //    }
    //}
    //else
    //{
    //    if (((compSide > 0) && (resp.keys === "left"))) {
    //    kestResp = 1;
    //} else {
    //    if (((compSide < 0) && (resp.keys === "right"))) {
    //        kestResp = 1;
    //    }
    //}
    //}
    
    kestList[staircase][currentScene][trial] = kestResp;
     
    psychoJS.experiment.addData("comp>ref?", kestResp);
    if ((localTrialNo[staircase][currentScene] > 1)) {
        if ((kestList[staircase][currentScene][trial] !== kestList[staircase][currentScene][(trial - 1)])) {
            reversals += 1;
            reverseList[staircase][currentScene][reversals] = levList[staircase][currentScene][(trial - 1)];
        }
    }
    
    localTrialNo[staircase][currentScene] = (localTrialNo[staircase][currentScene] + 1);
    trialCounter = (trialCounter + 1);
    
    psychoJS.experiment.addData('resp.keys', resp.keys);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

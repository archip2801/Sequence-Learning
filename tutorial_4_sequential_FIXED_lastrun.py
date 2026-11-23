#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.3),
    on November 22, 2026, at 16:10
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
# conditions file: 200 rows = the sequence X-V-C-Z repeated 50 times.
# Sequential block uses it in order; random block shuffles the same 200 rows.
_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sequence_con.csv')
with open(_csv_path, 'w') as _f:
    _f.write('pos,corr_resp\n')
    for _i in range(50):
        _f.write('-50,x\n150,v\n50,c\n-150,z\n')
# Run 'Before Experiment' code from code
# conditions file: 200 rows = the sequence X-V-C-Z repeated 50 times.
# Sequential block uses it in order; random block shuffles the same 200 rows.
_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sequence_con.csv')
with open(_csv_path, 'w') as _f:
    _f.write('pos,corr_resp\n')
    for _i in range(50):
        _f.write('-50,x\n150,v\n50,c\n-150,z\n')
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.3'
expName = 'Sequence Learning'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data/' + expInfo['participant'] + '_' + expName + '_' + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\mihir\\Desktop\\final Lab exp\\t4\\tutorial_4_sequential_FIXED_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions" ---
    instr_text = visual.TextStim(win=win, name='instr_text',
        text='Sequence Learning Task\n\nFour vertical lines are shown on the screen. After a short pause a small triangle\nappears above ONE of the lines.\n\nPress the key that matches that line, as quickly and accurately as you can:\n\nZ = leftmost line     X = second line     C = third line     V = rightmost line\n\nRest your fingers on Z X C V. There are 400 trials with one short break.\n\nPress SPACE to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instr = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "trial" ---
    fixation = visual.ShapeStim(
        win=win, name='fixation', vertices='cross',units='pix', 
        size=(10, 10),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(-0.2549, 0.2392, 0.2549),
        opacity=None, depth=0.0, interpolate=True)
    line1 = visual.Rect(
        win=win, name='line1',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(-150, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    line2 = visual.Rect(
        win=win, name='line2',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(-50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    line3 = visual.Rect(
        win=win, name='line3',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    line4 = visual.Rect(
        win=win, name='line4',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(150, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    probe = visual.ShapeStim(
        win=win, name='probe',units='pix', 
        size=(10, 10), vertices='triangle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    # Run 'Begin Experiment' code from code
    trial_num = 0   # running trial counter across both blocks
    
    # --- Initialize components for Routine "block_break" ---
    break_text = visual.TextStim(win=win, name='break_text',
        text='Short break\n\nRest your hands and eyes for a moment.\n\nPress SPACE when you are ready to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_break = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "trial" ---
    fixation = visual.ShapeStim(
        win=win, name='fixation', vertices='cross',units='pix', 
        size=(10, 10),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(-0.2549, 0.2392, 0.2549),
        opacity=None, depth=0.0, interpolate=True)
    line1 = visual.Rect(
        win=win, name='line1',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(-150, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    line2 = visual.Rect(
        win=win, name='line2',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(-50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    line3 = visual.Rect(
        win=win, name='line3',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    line4 = visual.Rect(
        win=win, name='line4',units='pix', 
        width=(100, 10)[0], height=(100, 10)[1],
        ori=90.0, pos=(150, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    probe = visual.ShapeStim(
        win=win, name='probe',units='pix', 
        size=(10, 10), vertices='triangle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    # Run 'Begin Experiment' code from code
    trial_num = 0   # running trial counter across both blocks
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[instr_text, key_instr],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_instr
    key_instr.keys = []
    key_instr.rt = []
    _key_instr_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    thisExp.currentRoutine = instructions
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        
        # if instr_text is starting this frame...
        if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.tStart = t  # local t and not account for scr refresh
            instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_text.started')
            # update status
            instr_text.status = STARTED
            instr_text.setAutoDraw(True)
        
        # if instr_text is active this frame...
        if instr_text.status == STARTED:
            # update params
            pass
        
        # *key_instr* updates
        waitOnFlip = False
        
        # if key_instr is starting this frame...
        if key_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instr.frameNStart = frameN  # exact frame index
            key_instr.tStart = t  # local t and not account for scr refresh
            key_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instr.started')
            # update status
            key_instr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instr.status == STARTED and not waitOnFlip:
            theseKeys = key_instr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instr_allKeys.extend(theseKeys)
            if len(_key_instr_allKeys):
                key_instr.keys = _key_instr_allKeys[-1].name  # just the last key pressed
                key_instr.rt = _key_instr_allKeys[-1].rt
                key_instr.duration = _key_instr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if key_instr.keys in ['', [], None]:  # No response was made
        key_instr.keys = None
    thisExp.addData('key_instr.keys',key_instr.keys)
    if key_instr.keys != None:  # we had a response
        thisExp.addData('key_instr.rt', key_instr.rt)
        thisExp.addData('key_instr.duration', key_instr.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    sequential_block = data.TrialHandler2(
        name='sequential_block',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequence_con.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(sequential_block)  # add the loop to the experiment
    thisSequential_block = sequential_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSequential_block.rgb)
    if thisSequential_block != None:
        for paramName in thisSequential_block:
            globals()[paramName] = thisSequential_block[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisSequential_block in sequential_block:
        sequential_block.status = STARTED
        if hasattr(thisSequential_block, 'status'):
            thisSequential_block.status = STARTED
        currentLoop = sequential_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisSequential_block.rgb)
        if thisSequential_block != None:
            for paramName in thisSequential_block:
                globals()[paramName] = thisSequential_block[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[fixation, line1, line2, line3, line4, probe, key_resp],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        probe.setPos((pos, 60))
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code
        trial_num += 1
        cond = 'sequential' if currentLoop.name == 'sequential_block' else 'random'
        thisExp.addData('condition', cond)
        thisExp.addData('trial_num', trial_num)
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        thisExp.currentRoutine = trial
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisSequential_block, 'status') and thisSequential_block.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *line1* updates
            
            # if line1 is starting this frame...
            if line1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line1.frameNStart = frameN  # exact frame index
                line1.tStart = t  # local t and not account for scr refresh
                line1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line1.started')
                # update status
                line1.status = STARTED
                line1.setAutoDraw(True)
            
            # if line1 is active this frame...
            if line1.status == STARTED:
                # update params
                pass
            
            # *line2* updates
            
            # if line2 is starting this frame...
            if line2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line2.frameNStart = frameN  # exact frame index
                line2.tStart = t  # local t and not account for scr refresh
                line2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line2.started')
                # update status
                line2.status = STARTED
                line2.setAutoDraw(True)
            
            # if line2 is active this frame...
            if line2.status == STARTED:
                # update params
                pass
            
            # *line3* updates
            
            # if line3 is starting this frame...
            if line3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line3.frameNStart = frameN  # exact frame index
                line3.tStart = t  # local t and not account for scr refresh
                line3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line3.started')
                # update status
                line3.status = STARTED
                line3.setAutoDraw(True)
            
            # if line3 is active this frame...
            if line3.status == STARTED:
                # update params
                pass
            
            # *line4* updates
            
            # if line4 is starting this frame...
            if line4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line4.frameNStart = frameN  # exact frame index
                line4.tStart = t  # local t and not account for scr refresh
                line4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line4.started')
                # update status
                line4.status = STARTED
                line4.setAutoDraw(True)
            
            # if line4 is active this frame...
            if line4.status == STARTED:
                # update params
                pass
            
            # *probe* updates
            
            # if probe is starting this frame...
            if probe.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                probe.frameNStart = frameN  # exact frame index
                probe.tStart = t  # local t and not account for scr refresh
                probe.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe.started')
                # update status
                probe.status = STARTED
                probe.setAutoDraw(True)
            
            # if probe is active this frame...
            if probe.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['z','x','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(corr_resp)) or (key_resp.keys == corr_resp):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for sequential_block (TrialHandler)
        sequential_block.addData('key_resp.keys',key_resp.keys)
        sequential_block.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            sequential_block.addData('key_resp.rt', key_resp.rt)
            sequential_block.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from code
        # autosave every 50 trials so data are never lost if the run is interrupted
        try:
            if trial_num % 50 == 0:
                thisExp.saveAsWideText(thisExp.dataFileName + '_autosave.csv', delim='auto', fileCollisionMethod='overwrite')
        except Exception as err:
            print('autosave skipped:', err)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisSequential_block as finished
        if hasattr(thisSequential_block, 'status'):
            thisSequential_block.status = FINISHED
        # if awaiting a pause, pause now
        if sequential_block.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            sequential_block.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sequential_block'
    sequential_block.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if sequential_block.trialList in ([], [None], None):
        params = []
    else:
        params = sequential_block.trialList[0].keys()
    # save data for this loop
    sequential_block.saveAsText(filename + '_sequential_block.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "block_break" ---
    # create an object to store info about Routine block_break
    block_break = data.Routine(
        name='block_break',
        components=[break_text, key_break],
    )
    block_break.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_break
    key_break.keys = []
    key_break.rt = []
    _key_break_allKeys = []
    # store start times for block_break
    block_break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    block_break.tStart = globalClock.getTime(format='float')
    block_break.status = STARTED
    thisExp.addData('block_break.started', block_break.tStart)
    block_break.maxDuration = None
    # keep track of which components have finished
    block_breakComponents = block_break.components
    for thisComponent in block_break.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_break" ---
    thisExp.currentRoutine = block_break
    block_break.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        
        # if break_text is starting this frame...
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_text.started')
            # update status
            break_text.status = STARTED
            break_text.setAutoDraw(True)
        
        # if break_text is active this frame...
        if break_text.status == STARTED:
            # update params
            pass
        
        # *key_break* updates
        waitOnFlip = False
        
        # if key_break is starting this frame...
        if key_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_break.frameNStart = frameN  # exact frame index
            key_break.tStart = t  # local t and not account for scr refresh
            key_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_break.started')
            # update status
            key_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_break.status == STARTED and not waitOnFlip:
            theseKeys = key_break.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_break_allKeys.extend(theseKeys)
            if len(_key_break_allKeys):
                key_break.keys = _key_break_allKeys[-1].name  # just the last key pressed
                key_break.rt = _key_break_allKeys[-1].rt
                key_break.duration = _key_break_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=block_break,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            block_break.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if block_break.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in block_break.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_break" ---
    for thisComponent in block_break.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for block_break
    block_break.tStop = globalClock.getTime(format='float')
    block_break.tStopRefresh = tThisFlipGlobal
    thisExp.addData('block_break.stopped', block_break.tStop)
    # check responses
    if key_break.keys in ['', [], None]:  # No response was made
        key_break.keys = None
    thisExp.addData('key_break.keys',key_break.keys)
    if key_break.keys != None:  # we had a response
        thisExp.addData('key_break.rt', key_break.rt)
        thisExp.addData('key_break.duration', key_break.duration)
    thisExp.nextEntry()
    # the Routine "block_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    random_block = data.TrialHandler2(
        name='random_block',
        nReps=1, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequence_con.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(random_block)  # add the loop to the experiment
    thisRandom_block = random_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRandom_block.rgb)
    if thisRandom_block != None:
        for paramName in thisRandom_block:
            globals()[paramName] = thisRandom_block[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRandom_block in random_block:
        random_block.status = STARTED
        if hasattr(thisRandom_block, 'status'):
            thisRandom_block.status = STARTED
        currentLoop = random_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRandom_block.rgb)
        if thisRandom_block != None:
            for paramName in thisRandom_block:
                globals()[paramName] = thisRandom_block[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[fixation, line1, line2, line3, line4, probe, key_resp],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        probe.setPos((pos, 60))
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code
        trial_num += 1
        cond = 'sequential' if currentLoop.name == 'sequential_block' else 'random'
        thisExp.addData('condition', cond)
        thisExp.addData('trial_num', trial_num)
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        thisExp.currentRoutine = trial
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisRandom_block, 'status') and thisRandom_block.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *line1* updates
            
            # if line1 is starting this frame...
            if line1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line1.frameNStart = frameN  # exact frame index
                line1.tStart = t  # local t and not account for scr refresh
                line1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line1.started')
                # update status
                line1.status = STARTED
                line1.setAutoDraw(True)
            
            # if line1 is active this frame...
            if line1.status == STARTED:
                # update params
                pass
            
            # *line2* updates
            
            # if line2 is starting this frame...
            if line2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line2.frameNStart = frameN  # exact frame index
                line2.tStart = t  # local t and not account for scr refresh
                line2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line2.started')
                # update status
                line2.status = STARTED
                line2.setAutoDraw(True)
            
            # if line2 is active this frame...
            if line2.status == STARTED:
                # update params
                pass
            
            # *line3* updates
            
            # if line3 is starting this frame...
            if line3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line3.frameNStart = frameN  # exact frame index
                line3.tStart = t  # local t and not account for scr refresh
                line3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line3.started')
                # update status
                line3.status = STARTED
                line3.setAutoDraw(True)
            
            # if line3 is active this frame...
            if line3.status == STARTED:
                # update params
                pass
            
            # *line4* updates
            
            # if line4 is starting this frame...
            if line4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                line4.frameNStart = frameN  # exact frame index
                line4.tStart = t  # local t and not account for scr refresh
                line4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'line4.started')
                # update status
                line4.status = STARTED
                line4.setAutoDraw(True)
            
            # if line4 is active this frame...
            if line4.status == STARTED:
                # update params
                pass
            
            # *probe* updates
            
            # if probe is starting this frame...
            if probe.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                probe.frameNStart = frameN  # exact frame index
                probe.tStart = t  # local t and not account for scr refresh
                probe.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe.started')
                # update status
                probe.status = STARTED
                probe.setAutoDraw(True)
            
            # if probe is active this frame...
            if probe.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['z','x','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(corr_resp)) or (key_resp.keys == corr_resp):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for random_block (TrialHandler)
        random_block.addData('key_resp.keys',key_resp.keys)
        random_block.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            random_block.addData('key_resp.rt', key_resp.rt)
            random_block.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from code
        # autosave every 50 trials so data are never lost if the run is interrupted
        try:
            if trial_num % 50 == 0:
                thisExp.saveAsWideText(thisExp.dataFileName + '_autosave.csv', delim='auto', fileCollisionMethod='overwrite')
        except Exception as err:
            print('autosave skipped:', err)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisRandom_block as finished
        if hasattr(thisRandom_block, 'status'):
            thisRandom_block.status = FINISHED
        # if awaiting a pause, pause now
        if random_block.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            random_block.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'random_block'
    random_block.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if random_block.trialList in ([], [None], None):
        params = []
    else:
        params = random_block.trialList[0].keys()
    # save data for this loop
    random_block.saveAsText(filename + '_random_block.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    # Run 'End Experiment' code from code
    # Build ONE Excel file with all 400 trials ('data' sheet) + an 'analysis' sheet.
    # Wrapped in try/except so a problem here can never stop the normal data saving.
    try:
        import pandas as pd
        thisExp.saveAsWideText(thisExp.dataFileName + '.csv', delim='auto')
        df = pd.read_csv(thisExp.dataFileName + '.csv')
        t = df[df['condition'].notna()].copy()
        t['rt'] = t['key_resp.rt']
        t['accuracy'] = t['key_resp.corr']
        keep = ['trial_num', 'condition', 'pos', 'corr_resp', 'key_resp.keys', 'rt', 'accuracy']
        t = t[[c for c in keep if c in t.columns]].sort_values('trial_num')
        ok = t[t['accuracy'] == 1].copy()          # accurate trials only
    
        # 1) mean RT per condition and the sequential-vs-random difference
        summ = ok.groupby('condition')['rt'].agg(n_correct='count', mean_rt='mean', sd_rt='std', median_rt='median').reset_index()
        acc = t.groupby('condition')['accuracy'].mean().rename('accuracy').reset_index()
        summ = summ.merge(acc, on='condition')
        m = summ.set_index('condition')['mean_rt']
        diff = pd.DataFrame({'measure': ['mean RT random - mean RT sequential (s)'],
                             'value': [m.get('random') - m.get('sequential')]})
    
        # 2) change in RT across trials: mean RT per bin of 20 trials per condition
        ok['trial_bin_20'] = ((ok['trial_num'] - 1) // 20) + 1
        bins = ok.groupby(['condition', 'trial_bin_20'])['rt'].mean().reset_index()
    
        with pd.ExcelWriter(thisExp.dataFileName + '.xlsx', engine='openpyxl') as xw:
            t.to_excel(xw, sheet_name='data', index=False)
            summ.to_excel(xw, sheet_name='analysis', index=False, startrow=1)
            diff.to_excel(xw, sheet_name='analysis', index=False, startrow=6)
            bins.to_excel(xw, sheet_name='analysis', index=False, startrow=10)
            ws = xw.sheets['analysis']
            ws['A1'] = 'Mean RT of accurate trials'
            ws['A6'] = 'Difference'
            ws['A10'] = 'Mean RT (s) per 20-trial bin'
    except Exception as err:
        print('Excel/analysis step skipped:', err)
    # Run 'End Experiment' code from code
    # Build ONE Excel file with all 400 trials ('data' sheet) + an 'analysis' sheet.
    # Wrapped in try/except so a problem here can never stop the normal data saving.
    try:
        import pandas as pd
        thisExp.saveAsWideText(thisExp.dataFileName + '.csv', delim='auto')
        df = pd.read_csv(thisExp.dataFileName + '.csv')
        t = df[df['condition'].notna()].copy()
        t['rt'] = t['key_resp.rt']
        t['accuracy'] = t['key_resp.corr']
        keep = ['trial_num', 'condition', 'pos', 'corr_resp', 'key_resp.keys', 'rt', 'accuracy']
        t = t[[c for c in keep if c in t.columns]].sort_values('trial_num')
        ok = t[t['accuracy'] == 1].copy()          # accurate trials only
    
        # 1) mean RT per condition and the sequential-vs-random difference
        summ = ok.groupby('condition')['rt'].agg(n_correct='count', mean_rt='mean', sd_rt='std', median_rt='median').reset_index()
        acc = t.groupby('condition')['accuracy'].mean().rename('accuracy').reset_index()
        summ = summ.merge(acc, on='condition')
        m = summ.set_index('condition')['mean_rt']
        diff = pd.DataFrame({'measure': ['mean RT random - mean RT sequential (s)'],
                             'value': [m.get('random') - m.get('sequential')]})
    
        # 2) change in RT across trials: mean RT per bin of 20 trials per condition
        ok['trial_bin_20'] = ((ok['trial_num'] - 1) // 20) + 1
        bins = ok.groupby(['condition', 'trial_bin_20'])['rt'].mean().reset_index()
    
        with pd.ExcelWriter(thisExp.dataFileName + '.xlsx', engine='openpyxl') as xw:
            t.to_excel(xw, sheet_name='data', index=False)
            summ.to_excel(xw, sheet_name='analysis', index=False, startrow=1)
            diff.to_excel(xw, sheet_name='analysis', index=False, startrow=6)
            bins.to_excel(xw, sheet_name='analysis', index=False, startrow=10)
            ws = xw.sheets['analysis']
            ws['A1'] = 'Mean RT of accurate trials'
            ws['A6'] = 'Difference'
            ws['A10'] = 'Mean RT (s) per 20-trial bin'
    except Exception as err:
        print('Excel/analysis step skipped:', err)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

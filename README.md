# chord-progression-generator

## Table of contents

* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use](#how-to-use)

## Introduction

The goal of this project is to create a flask server that generates and returns midi chord progressions using RESTful principles. Server returns a midi file that is ready to use in any DAW that is compatible with midi format.

## Technologies

Project is created with:

* Flask version: 2.1.3
* Flask-RESTful version: 0.3.9
* MIDIUtil version: 1.2.1

## Setup

To run this project first install requirements.

```
$ pip install -r 'requirements.txt'
```

Then all you have to do is run **run.py** file.

```
$ python run.py
```

## Examples of use

### How to use

To generate progression you need to send a POST request to running server on [http://127.0.0.1:5000/generate](http://127.0.0.1:5000/generate) with parameters:

* key (one of musicial keys ie. c, c#, d and so on)
* mode (major or minor, since these are the only one supported)

### View already generated progressions

To view already generated progressions visit [http://127.0.0.1:5000](http://127.0.0.1:5000) or send GET request

### Download midi file

To download already generated midi file visit [http://127.0.0.1:5000](http://127.0.0.1:5000)/<midi file name>

# batchwave
Batchwave is a command line abstraction for the NI-RFmx Batch Waveform Creator.
It enables on-the-fly NI 5GNR waveform creation from Python.
Coupled with NI-RFSG, batchwave can be utilized for dynamic 5GNR waveform generation from NI Vector Signal Generators and VSTs.

Visit [rfmx-pythonnet](https://github.com/NISystemsEngineering/rfmx-pythonnet) for examples using NI-RFSG. 

## Video Demos
[Introduction](https://youtu.be/2uwIhHBpVzg)

[Remote with RPyC](https://www.youtube.com/watch?v=MqvvBslT0z8&feature=youtu.be)

## Dependencies
Batchwave requires RFmx NR 20.0 or higher and has only been tested on Python 3.

## Cross Platform Compatibility
The wfmcreator.WaveformCreator class has a dependency on a Windows exe and therefore can only be instantiated on a Windows machine.
All other classes are cross platform.
See the remoting examples to target batchwave from a non-Windows OS.
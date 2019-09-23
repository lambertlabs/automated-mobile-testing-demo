# automated-mobile-testing-demo
This code is for our automated mobile testing tutorial on the Lambert Labs website: https://lambertlabs.com/2019/09/23/writing-tests-for-android-apps-using-python-and-linux/

It contains a short mobile test for the _Chess Free_ Android app, to be run on Ubuntu 16.04+.

To run this project: 
1. Follow the instructions in the _Setting up the environment_ section of the tutorial
2. Clone this repository
3. Replace `android_apps/apk_file_goes_here` with the APK file of the Chess Free app (V3.02): https://apkpure.com/chess-free/uk.co.aifactory.chessfree/versions
4. Start up Appium, and start up the Android Emulator
5. Open a terminal in the top level directory and run `pytest`
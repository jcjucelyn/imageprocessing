## Set-up using MacOS:

Follow the tutorial on GitHub to set up the environment. If an error “ImportError: unable to find shared zbar library” appears:
1.	Open terminal
2.	Run ‘find / -name “libzbar.dylib” 2>/dev/null’
3.	Copy directory the libzbar.dylib is saved to
4.	Run ‘nano ~/.bashrc’
5.	Add ‘export DYLD_LIBRARY_PATH= “[path from step 3]:$DYLD_LIBRARY_PATH’
a.	Path may look like: ‘/System/Volumes/Data/opt/homebrew/lib’
6.	Save file (ctrl X > Y > enter)
7.	Run ‘source ~/.bashrc’
8.	Check path by running ‘echo $DYLD_LIBRARY_PATH’

Run the environment test:
•	pytest .

If all tests are passed, the environment has been set up correctly. 

NB: In Jupyter Notebooks, if the same error arises, copy over the below code into a cell and run it in each notebook prior to the rest of the code:
•	import os
•	os.environ['DYLD_LIBRARY_PATH'] = ‘[path from above step 3]’

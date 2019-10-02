# Functional test assignment

### Installation
Assuming you have an OS X system, which has python 2 and git preinstalled, in order to run the test you need to install the following:

- Clone the project:
```
git clone https://github.com/margaritaumaniuc/presto.git
```


- Install pytest
```
$ pip install -U pytest
```

- Install ChromeDriver

1) Download ChromeDriver for OS X from: https://sites.google.com/a/chromium.org/chromedriver/downloads
2) You might have exception if chromedriver has a different version of Chrome that you use
3) Move the executable to the cloned project's tests/lib directory
```
$ mv chromedriver path_to_project/tests/lib
```

### Running the test:
```
$ cd tests
$ py.test test_sign_up.py
```
from distutils.core import setup
import py2exe

setup(
        console=['podtag.py'],
        options={
               "py2exe":{
                        "optimize": 2,
                        "dist_dir": "D:\\py2exe\\podtag",
                }
        }
)

# To generate binary
# python setup.py py2exe

# http://www.py2exe.org/index.cgi/Tutorial

# Two directories will be created when you run your setup script, build and dist. 
# The build directory is used as working space while your application is being packaged. 
# It is safe to delete the build directory after your setup script has finished running. 
# The files in the dist directory are the ones needed to run your application. 

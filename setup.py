from importlib.metadata import entry_points
from setuptools import setup
import os


setup(
   name="fibonacci",
   version="1.0.0",
   description="a calculator for Fibonacci numbers",   
   long_description="same",
   author="Kristian Rother",
   author_email="kristian.rother@posteo.de",
   packages=["fibonacci"],  # name of Python package folder, important
   url="none",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.10"
      "Programming Language :: Python :: 3.11"
      "Programming Language :: Python :: 3.12"
   ],
   entry_points={
        "console_scripts":["fibo=fibonacci.user_interface:run"]
        #                   ^command=package.module:function
   }
)

from setuptools import setup

args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}

requires = []
entry_points = {"console_scripts": []}


def do_setup(args_dict, requires, entry_points):
    args_dict.update({"install_requires": requires, "entry_points": entry_points})
    setup(**args_dict)


do_setup(args_dict, requires, entry_points)

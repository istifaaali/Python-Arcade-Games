from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ball.py", base=base)]

packages = ["idna","pygame","random","time"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
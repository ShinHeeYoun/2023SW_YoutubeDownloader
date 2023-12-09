# setup.py
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'includes': ['gui', 'downloader'],  # 모듈 추가
    }
}

executables = [Executable("main.py", base=None)]  # base=None은 콘솔 응용 프로그램으로 만들기

setup(
    name="MyProgram",
    version="1.0",
    description="My Description",
    options=options,
    executables=executables
)
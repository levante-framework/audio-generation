from setuptools import setup, find_packages

setup(
    name='Levante Audio Tools',
    version='0.1.0',
    packages=find_packages(include=['your_package_name', 'your_package_name.*']),
    install_requires=[
        # List your project dependencies here
        beautifulsoup4==4.12.3,
        bs4==0.0.2,
        certifi==2024.12.14,
        charset-normalizer==3.4.1,
        ctk==0.1,
        customtkinter==5.2.2,
        darkdetect==0.8.0,
        docopt==0.6.2,
        idna==3.10,
        numpy==2.2.1,
        packaging==24.2,
        pandas==2.2.3,
        pipreqs==0.4.13,
        playsound==1.2.2,
        python-dateutil==2.9.0.post0,
        pytz==2024.2,
        requests==2.32.3,
        setuptools==75.6.0,
        six==1.17.0,
        soupsieve==2.6,
        tzdata==2024.2,
        urllib3==2.3.0,
        wheel==0.45.1,
        yarg==0.1.10

    ],
    description='Scripts to help generate accurate audio',
    author='David Cardinal',
    author_email='david81@stanford.edu',
)
from setuptools import setup, find_packages

setup(
    name='bag_of_tasks_rest',
    version='0.1',
    install_requires=[
        'django==2.0.4',
        'djangorestframework==3.8.2',
        'psycopg2==2.7.4',
    ],
    packages=find_packages(),
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'bag_of_tasks_rest=manage:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Bag of Tasks',
)

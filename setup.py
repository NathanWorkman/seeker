from setuptools import setup, find_packages

setup(
    name='seeker',
    version='0.2.0',
    author=u'Nathan Workman',
    author_email='nathancworkman@gmail.com',
    url='https://github.com/NathanWorkman/seeker.git',
    packages=find_packages(),
    requires=['scrapy (>=1.5.0)', 'django(>=2.0.0)'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Framework :: Django',
        'Framework :: Scrapy',
    ],
    zip_safe=False,
)

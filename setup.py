from setuptools import setup

setup(
    name='PyUpdater-SCP-Plugin',
    version='3.0.5',
    description='SCP plugin for PyUpdater',
    author='JMSwag',
    author_email='johnymoswag@gmail.com',
    url='https://github.com/JMSwag/PyUpdater-SCP-Plugin',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],
    platforms=['Any'],
    provides=['pyupdater.plugins',],
    install_requires=[
        'paramiko',
        'scp',
        ],
    py_modules=['scp_uploader'],
    include_package_data=True,
    entry_points={
        'pyupdater.plugins': [
            'scp = scp_uploader:SCPUploader',
        ],
    },
    zip_safe=False,
)

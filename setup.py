from setuptools import setup

setup(
    name='PyUpdater-SCP-Plugin',
    version='2.2',

    description='SCP Uploader Extension',

    author='JohnyMoSwag',
    author_email='johnymoswag@gmail.com',

    url='https://github.com/JohnyMoSwag/PyUpdater-SCP-Plugin',

    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['pyupdater.plugins',
              ],

    install_requires=[
        'jms-utils >= 0.6.2',
        'paramiko',
        'scp',
        ],

    py_modules=['scp_plugin'],

    include_package_data=True,

    entry_points={
        'pyupdater.plugins.uploaders': [
            'scp = scp_plugin:SCPUploader',
        ],
    },

    zip_safe=False,
)

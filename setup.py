from setuptools import setup

import versioneer


with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='PyUpdater-SCP-Plugin',
    version=versioneer.get_version(),
    description='SCP plugin for PyUpdater',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='JMSwag',
    author_email='johnymoswag@gmail.com',
    url='https://github.com/JMSwag/PyUpdater-SCP-Plugin',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Environment :: Console'
                 ],
    platforms=['Any'],
    install_requires=[
        'paramiko',
        'scp',
        ],
    py_modules=['scp_uploader', '_version'],
    include_package_data=True,
    entry_points={
        'pyupdater.plugins.upload': [
            'scp = scp_uploader:SCPUploader',
        ],
    },
    zip_safe=False,
    cmdclass=versioneer.get_cmdclass(),
)

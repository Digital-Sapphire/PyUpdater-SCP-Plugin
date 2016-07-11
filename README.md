[![PyPI version](https://badge.fury.io/py/PyUpdater-SCP-Plugin.svg)](http://badge.fury.io/py/PyUpdater-SCP-Plugin)

# PyUpdater SCP plugin

PyUpdater upload plugin for scp

## Installing

    $ pip install PyUpdater-SCP-Plugin

## Configuration

Environmental Variables
##### Note that all env vars are optional but will be used as global options if set.

| Variable      | Meaning        |
| ------------- |-------------|
| PYU_SSH_USERNAME | SSH Username |
| PYU_SSH_PASSWORD | Path to SSH keyfile or password |
| PYU_SSH_HOST | IP or URL address or server |
| PYU_SSH_PORT | Port used for ssh |
| PYU_SSH_REMOTE_PATH | Full path to directory on remote machine to store updates |


The above settings can be overwritten, for a repo, using the command below.

    $ pyupdater settings --plugin plugin-name

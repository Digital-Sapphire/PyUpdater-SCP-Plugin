[![PyPI version](https://badge.fury.io/py/PyUpdater-SCP-Plugin.svg)](http://badge.fury.io/py/PyUpdater-SCP-Plugin)

# PyUpdater SCP plugin

PyUpdater upload plugin for scp

## Installing

    $ pip install PyUpdater-SCP-Plugin

## Configuration

Optional - If set will be used globally. Will be overwritten when you add scp settings during pyupdater init

| Variable      | Meaning        |
| ------------- |-------------|
| PYIU_SSH_USERNAME | SSH Username (optional) |
| PYIU_SSH_PASSWORD | Path to SSH keyfile or password |
| PYIU_SSH_IP_URL | ip or url address or server (optional) |
| PYIU_SSH_REMOTE_PATH | Full path to directory on remote machine to store updates (optional) |

## Changes

* v1.1

    - Updated

        Compat with PyUpdater 0.19+
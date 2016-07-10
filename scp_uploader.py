# The MIT License (MIT)
#
# Copyright (c) 2014 JohnyMoSwag <johnymoswag@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os
import sys

import paramiko
from scp import SCPClient

from pyupdater.utils.exceptions import UploaderError
from pyupdater.uploader import BaseUploader

log = logging.getLogger(__name__)


class SCPUploader(BaseUploader):

    name = 'SCP'
    author = 'Digital Sapphire'

    def init_config(self, config):
        # Used to set global configs.
        # Will be overridden with repo specific config
        self.username = os.environ.get(u'PYU_SSH_USERNAME')
        self.password = os.environ.get(u'PYU_SSH_PASSWORD')
        self.host = os.environ.get(u'PYU_SSH_HOST')
        self.port = os.environ.get(u'PYU_SSH_PORT', 22)
        self.remote_dir = os.environ.get(u'PYU_SSH_REMOTE_PATH')

        username = config.get(u'username')
        if username is not None:
            self.username = username
        else:
            if self.username is None:
                raise UploaderError(u'Username is not set')

        password = config.get(u'password')
        if password is not None:
            self.password = password
        else:
            if self.password is None:
                raise UploaderError(u'Key file or password is not set')

        host = config.get(u'host')
        if host is not None:
            self.host = host
        else:
            if self.host is None:
                raise UploaderError(u'Host is not set')

        port = config.get(u'port')
        if port is not None:
            self.port = port

        remote_dir = config.get(u'remote_dir')
        if remote_dir is not None:
            self.remote_dir = remote_dir
        else:
            if self.remote_dir is None:
                raise UploaderError(u'Remote directory is not set')
        self.connect()

    def set_config(self, config):
        username = config.get('username')
        username = self.get_answer('Enter username. Can be left blank to '
                                   'use environmental variable.',
                                   default=username)
        config['username'] = username

        password = config.get('password')
        password = self.get_answer('Enter password or path to keyfile',
                                   default=password)
        config['password'] = password

        host = config.get('host')
        host = self.get_answer('Enter host', default=host)
        config['host'] = host

        port = config.get('port', 22)
        port = self.get_answer('Port number',default=port)
        config['port'] = port

        remote_dir = config.get('remote_dir')
        remote_dir = self.get_answer('Enter remote directory',
                                     default=remote_dir)
        config['remote_dir'] = remote_dir


    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        data = dict(username=self.username, port=int(self.port),
                    timeout=5.0)
        private_key = os.path.expanduser(self.password)
        if os.path.exists(private_key):
            data['key_filename'] = private_key
        else:
            data['password'] = self.password

        self.ssh.connect(self.host, **data)
        self.client = SCPClient(self.ssh.get_transport(),
                                progress=self.ssh_progress)

    def upload_file(self, filename):
        try:
            self.client.put(filename, remote_path=self.remote_dir)
            os.remove(filename)
            return True
        except Exception as err:
            log.error('Failed to upload file')
            log.debug(err, exc_info=True)
            self._connect()
            return False

    def ssh_progress(self, filename, size, sent):
        percent = float(sent) / size * 100
        sys.stdout.write('\r%.1f' % percent)
        sys.stdout.flush()

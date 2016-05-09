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

from paramiko import SSHClient
from scp import SCPClient

from pyupdater.utils.exceptions import UploaderError
from pyupdater.uploader import BaseUploader

log = logging.getLogger(__name__)


class SCPUploader(BaseUploader):

    name = 'SCP'
    author = 'Digital Sapphire'

    def init_config(self, config):
        self.username = os.environ.get(u'PYU_SSH_USERNAME')
        self.password = os.environ.get(u'PYU_SSH_PASSWORD')
        self.host = os.environ.get(u'PYU_SSH_IP_URL')
        self.remote_dir = os.environ.get(u'PYU_SSH_REMOTE_PATH')

        username = config.get(u'ssh_username')
        if username is not None:
            self.username = username
        else:
            if self.username is None:
                raise UploaderError(u'Username is not set')

        if self.password is None:
            raise UploaderError(u'Key file or password is not set')

        host = config.get(u'ssh_host')
        if host is not None:
            self.host = host
        else:
            if self.host is None:
                raise UploaderError(u'Host is not set')

        remote_dir = config.get(u'remote_dir')
        if remote_dir is not None:
            self.remote_dir = remote_dir
        else:
            if self.remote_dir is None:
                raise UploaderError(u'Remote directory is not set')
        self.connect()

    def set_config(self, config):
        username = config.get('username')
        username = self.get_answer('Enter username', default=username)
        config['username'] = username

        host = config.get('host')
        host = self.get_answer('Enter host', default=host)
        config['host'] = host

        remote_dir = config.get('remote_dir')
        remote_dir = self.get_answer('Enter remote directory',
                                     default=remote_dir)
        config['remote_dir'] = remote_dir


    def connect(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.connect(self.host, username=self.username,
                         key_filename=self.password)
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

# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse
from django.conf import settings
import os


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add(request):
    content = ''
    path = os.path.join(settings.BASE_DIR, 'persistent-storage', 'storage.txt')
    with open(path, 'a') as file:
        file.write('\nAdding new line 1')

    with open(path, 'r') as file:
        content = file.read()

    return HttpResponse("Added to storage:" + content)

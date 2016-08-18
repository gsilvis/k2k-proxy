#   Copyright 2016 Massachusetts Open Cloud
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

from mixmatch.services import image
from mixmatch.services import volume


def construct_url(service_provider, service_type,
                  version, action, project_id=None):
    if service_type == 'image':
        return image.construct_url(service_provider, version, action)
    elif service_type in ['volume', 'volumev2']:
        return volume.construct_url(service_provider, version, action,
                                    project_id=project_id)

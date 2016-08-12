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

import json

from mixmatch.ext import base


class ImageAggregator(base.BaseExtension):
    def __init__(self):
        self.aggregator = True

    def aggregate(self, response):
        image_list = []
        for sp, sp_response in response.iteritems():
            images = json.loads(sp_response.text)
            if type(images) == dict:
                image_list += images["images"]

        return json.dumps({ "images": image_list})
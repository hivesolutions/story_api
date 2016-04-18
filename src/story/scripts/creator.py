#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Story API
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Story API.
#
# Hive Story API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Story API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Story API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier
import story

def create(*args, **kwargs):
    api = story.Api()
    return api.create_object(kwargs)

if __name__ == "__main__":
    name = appier.conf("NAME", "untitled")
    path = appier.conf("PATH", None)

    if not path:
        raise appier.OperationalError(message = "No path defined")

    file = open(path, "rb")
    kwargs = dict(name = name, file = file)

    result = create(**kwargs)
    print(result)
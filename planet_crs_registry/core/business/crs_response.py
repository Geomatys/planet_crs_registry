# -*- coding: utf-8 -*-
# Planet CRS Registry - The coordinates reference system registry for solar bodies
# Copyright (C) 2021-2022 - CNES (Jean-Christophe Malapert for PDSSP)
#
# This file is part of Planet CRS Registry.
#
# Planet CRS Registry is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License v3  as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Planet CRS Registry is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License v3  for more details.
#
# You should have received a copy of the GNU Lesser General Public License v3
# along with Planet CRS Registry.  If not, see <https://www.gnu.org/licenses/>.
"""Handles the IAU responses of the IAU web services."""
import os
import subprocess
import tempfile
from typing import Any

from fastapi import Response

from _version import __apache_sis__
from ..models import Identifiers
from planet_crs_registry.config.cfg import IS_PROD  # pylint: disable=C0411


class IdentifiersResponse(Response):
    """Creates the Identifiers response of the IAU web service."""

    media_type = "application/xml"

    def render(self, content: Any) -> bytes:
        result: bytes
        if content is None:
            result = b""
        elif isinstance(content, bytes):
            result = content
        elif isinstance(content, Identifiers):
            result = content.to_xml()
        else:
            result = Identifiers(identifiers=content).to_xml()
        return result


class GmlResponse(Response):
    """Creates the GML response of the IAU web service."""

    media_type = "application/xml"

    def render(self, content: str) -> bytes:
        """Renders the GML response with ApacheSIS CLI.

        Args:
            content (str): IAU identifier

        Returns:
            bytes: the response in GML
        """

        # ApacheSIS CLI needs a file as input
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(content)

        data: bytes
        data = subprocess.check_output(
            [f"/apache-sis-{__apache_sis__}/bin/sis", "crs", temp_file.name,
             "--format", "xml"]
        )

        os.unlink(temp_file.name)

        data_str: str = data.decode("utf-8")
        # data_str = data_str.replace(
        #     "<gml:GeographicCRS",
        #     '<gml:GeographicCRS xmlns:gml="http://www.opengis.net/gml/3.2"\
        #          xmlns:gmd="http://www.isotc211.org/2005/gmd"',
        # )
        # data_str = data_str.replace(
        #     "<gml:ProjectedCRS",
        #     '<gml:ProjectedCRS xmlns:gml="http://www.opengis.net/gml/3.2"\
        #          xmlns:gmd="http://www.isotc211.org/2005/gmd"',
        # )
        # data_str = data_str.replace("\n", "")
        return Response(content=data_str, media_type="application/xml").render(
            data_str
        )

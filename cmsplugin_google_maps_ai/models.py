# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

GOOGLE_MAPS_MAXIMUM_ZOOM_LEVEL = 21


@python_2_unicode_compatible
class GoogleMapsAddressEmbed(CMSPlugin):
    street_address = models.CharField(
        verbose_name=_('street address'),
        max_length=128,
        blank=True,
    )
    postal_code = models.CharField(
        verbose_name=_('postal code'),
        max_length=24,
        blank=True,
    )
    city = models.CharField(
        verbose_name=_('city'),
        max_length=128,
        blank=True,
    )
    country = models.CharField(
        verbose_name=_('country'),
        max_length=128,
        blank=True,
    )
    embed_height = models.PositiveSmallIntegerField(
        verbose_name=_('embed height'),
        default=250,
        help_text=_('Height of the map embed in pixels.'),
        blank=False,
        null=False,
    )
    zoom_level = models.PositiveSmallIntegerField(
        verbose_name=_('zoom level'),
        default=15,
        help_text=_('Map zoom level. Values range from 0 (the whole world) to 21 (individual buildings).'),
        blank=False,
        null=False,
    )

    def __str__(self):
        return 'Google Maps Embed - %s' % self.address

    @property
    def address(self):
        return '{street_address}, {postal_code} {city}, {country}'.format(
            street_address=self.street_address,
            postal_code=self.postal_code,
            city=self.city,
            country=self.country
        )

    @property
    def embed_q(self):
        """
        Returns the `q` GET parameter for Google Maps embed url.
        """
        return '{street_address}+{postal_code}+{city}+{country}'.format(
            street_address=self.street_address,
            postal_code=self.postal_code,
            city=self.city,
            country=self.country
        ).replace(' ', '')

    @property
    def zoom(self):
        """
        Limits zoom level to largest value supported by Google Maps.
        """
        return min(self.zoom_level, GOOGLE_MAPS_MAXIMUM_ZOOM_LEVEL)

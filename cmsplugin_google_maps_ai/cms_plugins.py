from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext as _

from cmsplugin_google_maps_ai.models import GoogleMapsAddressEmbed


class GoogleMapsPlugin(CMSPluginBase):
    model = GoogleMapsAddressEmbed
    name = _('Google Maps address embed')
    fieldsets = (
        ('', {
            'fields': (
                ('street_address', 'postal_code'),
                ('city', 'country'),
            ),
        }),
        (_('Layout'), {
            'fields': ('embed_height', 'zoom_level'),
        }),
    )
    render_template = 'cmsplugin_google_maps_ai/address_embed.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'api_key': getattr(settings, "GOOGLE_MAPS_API_KEY", None),
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(GoogleMapsPlugin)

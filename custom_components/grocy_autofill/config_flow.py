from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY
import voluptuous as vol

from .const import DOMAIN, CONF_GROCY_URL, CONF_POLL_INTERVAL

class GrocyAutofillConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle config flow."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Grocy AutoFill", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_GROCY_URL): str,
            vol.Required(CONF_API_KEY): str,
            vol.Required(CONF_POLL_INTERVAL, default=30): int,
        })
        return self.async_show_form(step_id="user", data_schema=schema)

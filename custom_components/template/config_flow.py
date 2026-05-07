"""Integration config flow"""

import logging
from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class BluettiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle config flow for integration."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle user input."""

        _LOGGER.debug("Handling user input for integration %s", DOMAIN)

        if user_input is not None:
            return self.async_create_entry(
                title="Entry title",
                data={
                    "text": user_input["text"]
                },
            )

        data_schema = vol.Schema(
            {
                vol.Required("text"): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
        )

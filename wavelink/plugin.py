from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.plugin import PluginInfo


class Plugin:
    """
    Represents a Lavalink plugin.

    Parameters
    ----------
    data:
        The data to create the plugin.

    Attributes
    ----------
    name: :class:`str`
        The name of the plugin.
    version: :class:`str`
        The version of the plugin.
    """

    __slots__ = ("name", "version")

    def __init__(self, data: PluginInfo) -> None:
        self.name: str = data["name"]
        self.version: str = data["version"]

    def __repr__(self):
        return f"<Plugin name={self.name} version={self.version}"

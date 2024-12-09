from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_role import NodeRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.peer_info import PeerInfo


T = TypeVar("T", bound="NodeNetwork")


@_attrs_define
class NodeNetwork:
    """
    Attributes:
        node_roles (Union[Unset, NodeRole]): Role of this node. (N.B. Sentry nodes are being deprecated.)
        num_peers (Union[Unset, str]): Number of peers the node is connected to.
        is_syncing (Union[Unset, bool]): Whether or not the node is syncing. `False` indicates that the node is in sync.
        should_have_peers (Union[Unset, bool]): Whether or not the node should be connected to peers. Might be false for
            local chains or when running without discovery.
        local_peer_id (Union[Unset, str]): Local copy of the `PeerId`.
        local_listen_addresses (Union[Unset, list[str]]): Multiaddresses that the local node is listening on. The
            addresses include a trailing `/p2p/` with the local PeerId, and are thus suitable to be passed to
            `system_addReservedPeer` or as a bootnode address for example.
        peers_info (Union[Unset, list['PeerInfo']]):
    """

    node_roles: Union[Unset, NodeRole] = UNSET
    num_peers: Union[Unset, str] = UNSET
    is_syncing: Union[Unset, bool] = UNSET
    should_have_peers: Union[Unset, bool] = UNSET
    local_peer_id: Union[Unset, str] = UNSET
    local_listen_addresses: Union[Unset, list[str]] = UNSET
    peers_info: Union[Unset, list["PeerInfo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_roles: Union[Unset, str] = UNSET
        if not isinstance(self.node_roles, Unset):
            node_roles = self.node_roles.value

        num_peers = self.num_peers

        is_syncing = self.is_syncing

        should_have_peers = self.should_have_peers

        local_peer_id = self.local_peer_id

        local_listen_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.local_listen_addresses, Unset):
            local_listen_addresses = self.local_listen_addresses

        peers_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.peers_info, Unset):
            peers_info = []
            for peers_info_item_data in self.peers_info:
                peers_info_item = peers_info_item_data.to_dict()
                peers_info.append(peers_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_roles is not UNSET:
            field_dict["nodeRoles"] = node_roles
        if num_peers is not UNSET:
            field_dict["numPeers"] = num_peers
        if is_syncing is not UNSET:
            field_dict["isSyncing"] = is_syncing
        if should_have_peers is not UNSET:
            field_dict["shouldHavePeers"] = should_have_peers
        if local_peer_id is not UNSET:
            field_dict["localPeerId"] = local_peer_id
        if local_listen_addresses is not UNSET:
            field_dict["localListenAddresses"] = local_listen_addresses
        if peers_info is not UNSET:
            field_dict["peersInfo"] = peers_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.peer_info import PeerInfo

        d = src_dict.copy()
        _node_roles = d.pop("nodeRoles", UNSET)
        node_roles: Union[Unset, NodeRole]
        if isinstance(_node_roles, Unset):
            node_roles = UNSET
        else:
            node_roles = NodeRole(_node_roles)

        num_peers = d.pop("numPeers", UNSET)

        is_syncing = d.pop("isSyncing", UNSET)

        should_have_peers = d.pop("shouldHavePeers", UNSET)

        local_peer_id = d.pop("localPeerId", UNSET)

        local_listen_addresses = cast(list[str], d.pop("localListenAddresses", UNSET))

        peers_info = []
        _peers_info = d.pop("peersInfo", UNSET)
        for peers_info_item_data in _peers_info or []:
            peers_info_item = PeerInfo.from_dict(peers_info_item_data)

            peers_info.append(peers_info_item)

        node_network = cls(
            node_roles=node_roles,
            num_peers=num_peers,
            is_syncing=is_syncing,
            should_have_peers=should_have_peers,
            local_peer_id=local_peer_id,
            local_listen_addresses=local_listen_addresses,
            peers_info=peers_info,
        )

        node_network.additional_properties = d
        return node_network

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

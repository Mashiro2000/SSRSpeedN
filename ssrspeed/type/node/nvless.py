from ssrspeed.type.node.basis import BasisNode


class NodeVless(BasisNode):
    def __init__(self, config: dict):
        super().__init__(config)
        self._type = "Vless"

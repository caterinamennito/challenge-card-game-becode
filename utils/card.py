from typing import Literal, List


IconType = Literal['♥', '♦', '♣', '♠']
ValueType = Literal['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
class Symbol:

    def __init__(self,  icon:IconType):
        icon_color_dict = {'♥': 'red', '♦': 'red', '♣': 'black', '♠': 'black'}
        self.icon = icon
        self.color = icon_color_dict[icon]
    
    def __str__(self) -> str:
        return f"The card symbol {self.icon} {self.color}"
    
class Card(Symbol):

    def __init__(self, icon: IconType, value: ValueType):
        super().__init__(icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} {self.icon} {self.color} "
import json

class settings:
    class bindings:
        def __init__(self) -> None:
            with open("bindings.json") as f:
                self.bindings = json.load(f)
        
        def getBindings(self) -> dict[str]:
            return self.bindings
        
        def setBindings(self, type: str, binding: str):
            new_bindings = {
                "forward": binding if type == "forward" else self.bindings["forward"],
                "backward": binding if type == "backward" else self.bindings["backward"],
                "left": binding if type == "left" else self.bindings["left"],
                "right": binding if type == "right" else self.bindings["right"]
            }

            with open("bindings.json", "w") as f:
                json.dump(new_bindings, f, indent = 4)
    
    class options:
        def __init__(self) -> None:
            with open("options.json") as f:
                self.options = json.load(f)
        
        def getOptions(self) -> dict[list[int]]:
            return self.options
        
print(settings.options().getOptions())
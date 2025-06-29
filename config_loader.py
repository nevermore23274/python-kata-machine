"""
Configuration loader for Python Kata-Machine
Loads algorithm configuration from kata.config.py
"""

import os
import sys
import importlib.util
from typing import List, Dict, Any
from pathlib import Path


class ConfigLoader:
    """Loads and validates kata configuration"""
    
    def __init__(self, config_path: str = None):
        if config_path is None:
            # Find kata-machine root directory (where kata.config.py exists)
            kata_root = Path(__file__).parent
            while kata_root != kata_root.parent and not (kata_root / "kata.config.py").exists():
                kata_root = kata_root.parent
            config_path = str(kata_root / "kata.config.py")

        self.config_path = Path(config_path)
        
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from kata.config.py"""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create a kata.config.py file in your project root."
            )
        
        # Load the config module
        spec = importlib.util.spec_from_file_location("kata_config", self.config_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load config from {self.config_path}")
            
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        self._config_module = config_module
        
        # Extract configuration
        config = {
            "dsa": self._get_dsa_list(),
            "config_path": str(self.config_path),
            "available_algorithms": self._get_all_available_algorithms()
        }
        
        self._validate_config(config)
        return config
    
    def _get_dsa_list(self) -> List[str]:
        """Get the DSA list from the config module"""
        if hasattr(self._config_module, 'DSA'):
            return self._config_module.DSA
        else:
            raise AttributeError(
                "DSA list not found in kata.config.py\n"
                "Please define a DSA list with your selected algorithms."
            )
    
    def _get_all_available_algorithms(self) -> List[str]:
        """Get all available algorithm configurations from the module"""
        algorithms = set()
        
        for attr_name in dir(self._config_module):
            if attr_name.endswith('_DSA') or attr_name == 'DSA':
                attr_value = getattr(self._config_module, attr_name)
                if isinstance(attr_value, list):
                    algorithms.update(attr_value)
        
        return sorted(list(algorithms))
    
    def _validate_config(self, config: Dict[str, Any]) -> None:
        """Validate the loaded configuration"""
        dsa_list = config["dsa"]
        
        if not isinstance(dsa_list, list):
            raise TypeError("DSA must be a list of algorithm names")
        
        if len(dsa_list) == 0:
            raise ValueError("DSA list cannot be empty")
        
        # Check for duplicates
        if len(dsa_list) != len(set(dsa_list)):
            duplicates = [x for x in dsa_list if dsa_list.count(x) > 1]
            raise ValueError(f"Duplicate algorithms found in DSA list: {set(duplicates)}")
        
        # Validate algorithm names (basic check)
        for algo in dsa_list:
            if not isinstance(algo, str):
                raise TypeError(f"Algorithm name must be a string, got: {type(algo)}")
            if not algo.strip():
                raise ValueError("Algorithm name cannot be empty or whitespace")
    
    def get_algorithm_count(self) -> int:
        """Get the number of algorithms configured"""
        config = self.load_config()
        return len(config["dsa"])
    
    def list_algorithms(self) -> List[str]:
        """Get list of configured algorithms"""
        config = self.load_config()
        return config["dsa"]
    
    def print_config_summary(self) -> None:
        """Print a summary of the current configuration"""
        try:
            config = self.load_config()
            dsa_list = config["dsa"]
            
            print(f"📋 Kata Configuration Summary")
            print(f"   Config file: {config['config_path']}")
            print(f"   Algorithms selected: {len(dsa_list)}")
            print(f"   Total available: {len(config['available_algorithms'])}")
            print()
            print("🔧 Selected Algorithms:")
            for i, algo in enumerate(dsa_list, 1):
                print(f"   {i:2d}. {algo}")
            print()
            
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")


# Convenience function for quick access
def load_kata_config(config_path: str = "kata.config.py") -> Dict[str, Any]:
    """Quick function to load kata configuration"""
    loader = ConfigLoader(config_path)
    return loader.load_config()


if __name__ == "__main__":
    # CLI for testing configuration
    loader = ConfigLoader()
    loader.print_config_summary()

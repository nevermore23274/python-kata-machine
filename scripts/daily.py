#!/usr/bin/env python3
"""
Daily practice generator for Python Kata-Machine
Generates one algorithm per day following course progression
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Add parent directory to path so we can import config_loader
sys.path.append(str(Path(__file__).parent.parent))
from config_loader import ConfigLoader


class DailyPracticeGenerator:
    """Generates daily algorithm practice following course progression"""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path.cwd()
        self.progress_file = self.base_dir / ".kata_progress.json"
        self.config_loader = ConfigLoader()
        
    def load_progress(self) -> Dict:
        """Load progress from local file"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Default progress
        return {
            "current_day": 1,
            "current_algorithm_index": 0,
            "completed_algorithms": [],
            "start_date": datetime.now().isoformat()
        }
    
    def save_progress(self, progress: Dict) -> None:
        """Save progress to local file"""
        with open(self.progress_file, 'w') as f:
            json.dump(progress, f, indent=2)
    
    def get_next_algorithm(self) -> Optional[str]:
        """Get the next algorithm in the progression"""
        try:
            config = self.config_loader.load_config()
            progression = config["dsa"]  # COURSE_PROGRESSION
            
            progress = self.load_progress()
            current_index = progress["current_algorithm_index"]
            
            if current_index < len(progression):
                return progression[current_index]
            else:
                return None  # Course completed
                
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")
            return None
    
    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        result = []
        for i, char in enumerate(name):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)
    
    def _create_algorithm_stub(self, algorithm_name: str, day_num: int) -> str:
        """Create the content for an algorithm stub file"""
        snake_name = self._to_snake_case(algorithm_name)
        
        stub_template = f'''"""
{algorithm_name} Algorithm Implementation
Daily Practice - Day {day_num}

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def {snake_name}(*args, **kwargs):
    """
    {algorithm_name} implementation
    
    TODO: 
    1. Follow the course lesson for {algorithm_name}
    2. Implement the algorithm step by step
    3. Test your implementation with: python kata.py test
    
    Args:
        *args: Replace with actual parameters based on algorithm requirements
        **kwargs: Replace with actual parameters based on algorithm requirements
    
    Returns:
        Replace with actual return type and description
        
    Time Complexity: O(?) - TODO: Analyze after implementation
    Space Complexity: O(?) - TODO: Analyze after implementation
    """
    # TODO: Implement {algorithm_name}
    # Remove this line and add your implementation
    raise NotImplementedError(f"TODO: Implement {algorithm_name}")


# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing {algorithm_name}...")
    
    # Example test cases (replace with actual test cases)
    # result = {snake_name}(test_input)
    # print(f"Result: {{result}}")
    
    print("Run 'python kata.py test' to run the full test suite")
'''
        return stub_template
    
    def generate_daily_practice(self) -> int:
        """Generate today's algorithm practice"""
        progress = self.load_progress()
        algorithm = self.get_next_algorithm()
        
        if algorithm is None:
            print("🎉 Congratulations! You've completed the entire course!")
            print("   You can restart with: python kata.py reset")
            return 0
        
        current_day = progress["current_day"]
        
        print(f"📅 Day {current_day} Practice")
        print(f"🎯 Today's Algorithm: {algorithm}")
        print()
        
        # Create daily directory
        day_dir = self.base_dir / f"day{current_day}"
        day_dir.mkdir(exist_ok=True)
        
        # Create algorithm file
        filename = self._to_snake_case(algorithm) + ".py"
        file_path = day_dir / filename
        
        # Don't overwrite if it already exists
        if file_path.exists():
            print(f"📄 {filename} already exists")
            print(f"📂 Continue working in: {day_dir}")
        else:
            # Generate the stub content
            stub_content = self._create_algorithm_stub(algorithm, current_day)
            
            # Write the file
            with open(file_path, 'w') as f:
                f.write(stub_content)
            
            print(f"📄 Created {filename}")
            print(f"📂 Working directory: {day_dir}")
        
        # Create __init__.py
        init_file = day_dir / "__init__.py"
        if not init_file.exists():
            snake_name = self._to_snake_case(algorithm)
            init_content = f'''"""
Day {current_day} - {algorithm}
Daily Python Kata Practice
"""

from .{snake_name} import {snake_name}

__all__ = ["{snake_name}"]
'''
            with open(init_file, 'w') as f:
                f.write(init_content)
        
        print()
        print("🚀 Ready to code!")
        print(f"   1. cd {day_dir}")
        print(f"   2. Edit {filename}")
        print(f"   3. Run: python kata.py test")
        print()
        print(f"💡 Tip: Watch ThePrimeagen's lesson on {algorithm} first!")
        
        return 0
    
    def mark_complete_and_advance(self) -> int:
        """Mark current algorithm as complete and advance to next"""
        progress = self.load_progress()
        current_algorithm = self.get_next_algorithm()
        
        if current_algorithm:
            # Mark current as completed
            if current_algorithm not in progress["completed_algorithms"]:
                progress["completed_algorithms"].append(current_algorithm)
            
            # Advance to next
            progress["current_algorithm_index"] += 1
            progress["current_day"] += 1
            
            self.save_progress(progress)
            
            next_algorithm = self.get_next_algorithm()
            if next_algorithm:
                print(f"✅ {current_algorithm} marked complete!")
                print(f"📅 Tomorrow's algorithm: {next_algorithm}")
            else:
                print(f"✅ {current_algorithm} marked complete!")
                print("🎉 Course completed! Congratulations!")
        
        return 0
    
    def show_progress(self) -> int:
        """Show current progress through the course"""
        progress = self.load_progress()
        
        try:
            config = self.config_loader.load_config()
            total_algorithms = len(config["dsa"])
            current_index = progress["current_algorithm_index"]
            completed = len(progress["completed_algorithms"])
            
            print(f"📊 Course Progress")
            print(f"   Day: {progress['current_day']}")
            print(f"   Completed: {completed}/{total_algorithms} algorithms")
            print(f"   Progress: {(completed/total_algorithms)*100:.1f}%")
            print()
            
            if completed > 0:
                print("✅ Completed algorithms:")
                for algo in progress["completed_algorithms"][-5:]:  # Show last 5
                    print(f"   • {algo}")
                if len(progress["completed_algorithms"]) > 5:
                    print(f"   ... and {len(progress['completed_algorithms']) - 5} more")
                print()
            
            current_algo = self.get_next_algorithm()
            if current_algo:
                print(f"🎯 Current algorithm: {current_algo}")
            else:
                print("🎉 Course completed!")
                
        except Exception as e:
            print(f"❌ Error loading progress: {e}")
            return 1
        
        return 0
    
    def reset_progress(self) -> int:
        """Reset progress to start over"""
        if self.progress_file.exists():
            self.progress_file.unlink()
        
        print("🔄 Progress reset!")
        print("   Run 'python kata.py daily' to start over")
        return 0


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Daily algorithm practice")
    parser.add_argument("action", choices=["generate", "complete", "progress", "reset"], 
                       default="generate", nargs="?",
                       help="Action to perform")
    
    args = parser.parse_args()
    
    generator = DailyPracticeGenerator()
    
    if args.action == "generate":
        return generator.generate_daily_practice()
    elif args.action == "complete":
        return generator.mark_complete_and_advance()
    elif args.action == "progress":
        return generator.show_progress()
    elif args.action == "reset":
        return generator.reset_progress()


if __name__ == "__main__":
    sys.exit(main())

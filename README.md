# Python Kata-Machine

A Python port of ThePrimeagen's [kata-machine](https://github.com/ThePrimeagen/kata-machine) for practicing algorithms and data structures without TypeScript.

## What This Is

This project recreates the exact same workflow and algorithms from ThePrimeagen's "The Last Algorithms Course You'll Need" but using Python instead of TypeScript. Perfect for developers who want to follow the course but prefer Python over TypeScript.

## Project Status

**✅ COMPLETED:**
- [x] Docker container setup with Python 3.11
- [x] Development environment with pytest, black, mypy
- [x] Volume mounting for persistent local development
- [x] One-command setup for immediate coding
- [x] Configuration system (`kata.config.py` - equivalent to `ligma.config.js`)
- [x] Configuration validation and loading (`config_loader.py`)
- [x] Algorithm stub generation (`scripts/generate.py` - equivalent to `yarn generate`)
- [x] Practice folder management (`scripts/clear.py` - equivalent to `yarn clear`)
- [x] All 25 algorithm templates with proper function stubs

**🚧 IN PROGRESS:**
- [ ] Test framework setup (equivalent to `yarn test`)
- [ ] Algorithm implementations with proper test cases

**📋 TODO:**
- [ ] Complete test suite for all algorithms
- [ ] Algorithm implementations for ThePrimeagen's course:
  - [ ] **Search:** LinearSearch, BinarySearchList, TwoCrystalBalls
  - [ ] **Sorting:** BubbleSort, InsertionSort, MergeSort, QuickSort
  - [ ] **Data Structures:** Queue, Stack, ArrayList, SinglyLinkedList, DoublyLinkedList
  - [ ] **Trees:** BTPreOrder, BTInOrder, BTPostOrder, BTBFS, CompareBinaryTrees, DFSOnBST
  - [ ] **Graphs:** BFSGraphMatrix, DFSGraphList, Dijkstra, PrimsList
  - [ ] **Advanced:** Trie, LRU, Map

## Quick Start

### Prerequisites
- Docker and Docker Compose

### Setup
```bash
# Clone or create project directory
mkdir python-kata-machine
cd python-kata-machine

# Save Dockerfile and docker-compose.yml to this directory

# Start coding immediately
docker-compose run --rm python-kata
```

### Inside the Container
Once you're in, use these Python commands (equivalent to original TypeScript):

**Current Working Commands:**
```bash
python check_config.py           # Validate configuration
python scripts/generate.py       # Create daily practice (equivalent to 'yarn generate')
python scripts/clear.py          # Clear generated folders (equivalent to 'yarn clear')
```

**Coming Soon:**
```bash
pytest                          # Run tests (equivalent to 'yarn test')
```

## How It Works

1. **Configure Algorithms:** Edit `kata.config.py` to choose which algorithms to practice ✅
2. **Generate Daily Practice:** Run `python scripts/generate.py` to create `src/day1/`, `src/day2/`, etc. ✅
3. **Implement Algorithms:** Fill in the function stubs with your implementations ✅ (ready)
4. **Test Your Code:** Run `pytest` to verify correctness 🚧 (in progress)
5. **Repeat Daily:** Build muscle memory through spaced repetition ✅

## Current Workflow

```bash
# 1. Start the container and check configuration
docker-compose run --rm python-kata
python check_config.py

# 2. Generate your first day of practice
python scripts/generate.py

# 3. Navigate to the generated folder and start coding
cd src/day1
ls  # See all 25 algorithm files ready for implementation

# 4. Implement algorithms in the generated .py files
# Edit files like linear_search.py, bubble_sort.py, etc.

# 5. Test your implementations (coming soon)
pytest

# 6. Clear and start fresh when needed
python scripts/clear.py --all
```

## Development Environment

The container includes:
- **Python 3.11** - Latest stable Python
- **pytest** - Testing framework (equivalent to Jest)
- **black** - Code formatter (equivalent to Prettier)
- **mypy** - Type checking (equivalent to TypeScript)
- **rich** - Beautiful console output
- **pyyaml** - Configuration file support

## Project Structure (Current)

```
python-kata-machine/
├── kata.config.py              # Algorithm selection ✅
├── config_loader.py           # Configuration system ✅
├── check_config.py            # Config validation ✅
├── scripts/
│   ├── generate.py            # Generate daily practice folders ✅
│   └── clear.py              # Clear generated folders ✅
├── src/                      # Generated daily practice folders
│   ├── day1/                 # Example: 25 algorithm stubs ✅
│   │   ├── __init__.py
│   │   ├── linear_search.py
│   │   ├── bubble_sort.py
│   │   ├── quick_sort.py
│   │   └── ... (22 more)
│   ├── day2/                 # Generated on next run
│   └── ...
└── tests/                    # Test files (coming soon)
```

## Why Python?

- **Simpler Syntax:** Focus on algorithms, not language complexity
- **Better for Learning:** More readable implementations
- **No Build Step:** Direct execution without compilation
- **Rich Ecosystem:** Excellent testing and development tools
- **Type Hints:** Optional typing for those who want it

## Contributing to This Port

This is a learning project! Feel free to suggest improvements or help implement algorithms.

---

*This project is inspired by and based on [ThePrimeagen's kata-machine](https://github.com/ThePrimeagen/kata-machine). All credit for the original concept and algorithm selection goes to ThePrimeagen.*

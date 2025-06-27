# Python Kata-Machine

A Python port of ThePrimeagen's [kata-machine](https://github.com/ThePrimeagen/kata-machine) for practicing algorithms and data structures without TypeScript.

## What This Is

This project recreates the exact same workflow and algorithms from ThePrimeagen's "The Last Algorithms Course You'll Need" but using Python instead of TypeScript. Perfect for developers who want to follow the course but prefer Python over TypeScript.

## Quick Start

### Prerequisites
- Docker and Docker Compose

### Setup
```bash
# Clone or create project directory
mkdir python-kata-machine
cd python-kata-machine
git clone https://github.com/nevermore23274/python-kata-machine.git

# Start coding immediately
docker-compose run --rm python-kata
```

### Inside the Container
The complete Python kata-machine system with all commands working:

**Main Commands:**
```bash
python kata.py config             # ✅ Validate configuration
python kata.py generate           # ✅ Create daily practice (equivalent to 'yarn generate')
python kata.py test               # ✅ Run tests (equivalent to 'yarn test')
python kata.py clear --all        # ✅ Clear generated folders (equivalent to 'yarn clear')
python kata.py setup-tests        # ✅ Generate test templates for all algorithms
```

**Quick Commands:**
```bash
python kata.py test --day 1              # Test specific day
python kata.py test --algorithm QuickSort # Test specific algorithm
python kata.py clear --day 2             # Clear specific day
```

## How It Works (Complete System!)

1. **Configure Algorithms:** Edit `kata.config.py` to choose which algorithms to practice ✅
2. **Generate Daily Practice:** Run `python kata.py generate` to create `src/day1/`, `src/day2/`, etc. ✅
3. **Implement Algorithms:** Fill in the function stubs with your implementations ✅
4. **Test Your Code:** Run `python kata.py test` to verify correctness ✅
5. **Repeat Daily:** Build muscle memory through spaced repetition ✅

## Complete Workflow Example

```bash
# 1. Start the container and check configuration
docker-compose run --rm python-kata
python kata.py config

# 2. Generate your first day of practice
python kata.py generate

# 3. Navigate to the generated folder and start coding
cd src/day1
ls  # See all 25 algorithm files ready for implementation

# 4. Implement an algorithm (example: linear_search.py)
# Edit the file and replace the NotImplementedError with your code

# 5. Test your implementation
python kata.py test --algorithm LinearSearch

# 6. Test everything
python kata.py test

# 7. Generate next day when ready for more practice
python kata.py generate

# 8. Clear and start fresh when needed
python kata.py clear --all
```

## What You Get When You Test

```bash
python kata.py test
# Shows:
# ✅ Tests PASS for implemented algorithms  
# ❌ Tests FAIL for incorrect implementations
# ⏭️  Tests SKIP for unimplemented algorithms (placeholder tests)
# 📊 Full test report with detailed feedback
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
├── kata.py                    # Main command interface ✅
├── test_runner.py             # Test runner system ✅
├── pytest.ini                # Pytest configuration ✅
├── scripts/
│   ├── generate.py            # Generate daily practice folders ✅
│   ├── clear.py              # Clear generated folders ✅
│   └── generate_tests.py     # Generate test templates ✅
├── tests/                    # Complete test suite ✅
│   ├── conftest.py           # Pytest fixtures and config ✅
│   ├── test_linear_search.py # Example: Complete test cases ✅
│   ├── test_bubble_sort.py   # Example: Complete test cases ✅
│   └── ... (25 test files)   # All algorithms covered ✅
├── src/                      # Generated daily practice folders
│   ├── day1/                 # 25 algorithm stubs ready for coding ✅
│   │   ├── __init__.py       # Python package setup ✅
│   │   ├── linear_search.py  # Ready for implementation ✅
│   │   ├── bubble_sort.py    # Ready for implementation ✅
│   │   ├── quick_sort.py     # Ready for implementation ✅
│   │   └── ... (22 more)     # All 25 algorithms ✅
│   ├── day2/                 # Generated on next run
│   └── ...
└── Dockerfile, docker-compose.yml # Container setup ✅
```

## Why Python Kata-Machine?

- **✅ Complete TypeScript Replacement:** Exact same workflow as the original kata-machine
- **🐍 Simpler Syntax:** Focus on algorithms, not language complexity  
- **📚 Better for Learning:** More readable implementations
- **🚀 No Build Step:** Direct execution without compilation
- **🧪 Excellent Testing:** Comprehensive pytest-based test suite
- **🎯 Type Hints:** Optional typing for those who want it
- **📦 Containerized:** Consistent environment across all systems
- **🔄 Daily Practice:** Same spaced repetition system as original

## Ready to Start!

This is a **complete, working system** - equivalent to the original TypeScript kata-machine but in Python. You can now follow ThePrimeagen's "The Last Algorithms Course You'll Need" using Python instead of TypeScript!

**Next Steps:**
1. Set up the container (5 minutes)
2. Run `python kata.py generate` to create your first practice day
3. Start implementing algorithms as you follow the course
4. Use `python kata.py test` to validate your implementations
5. Build algorithmic thinking through daily practice

Happy coding! 🎉

---

*This project is inspired by and based on [ThePrimeagen's kata-machine](https://github.com/ThePrimeagen/kata-machine). All credit for the original concept and algorithm selection goes to ThePrimeagen.*

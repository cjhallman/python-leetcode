# -----------------------------------------------------------------------------
# CHECK PRE-REQS
# -----------------------------------------------------------------------------
# Check for a python3 executable in the PATH
override PY3_EXECUTABLE_NAME := python3
export PY3_EXECUTABLE_NAME
ifneq ($(shell command -v $(PY3_EXECUTABLE_NAME) >/dev/null 2>&1; echo $$?), 0)
$(error $(PY3_EXECUTABLE_NAME) is not available in the PATH)
endif

# -----------------------------------------------------------------------------
# VARIABLES - PROJECT DIRECTORIES
# -----------------------------------------------------------------------------

override REPOROOT := $(shell git rev-parse --show-toplevel)
override WORKROOT := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# -----------------------------------------------------------------------------
# TARGETS - PRIMARY
# -----------------------------------------------------------------------------
.PHONY: init
init: \
	_python-venv-create \
	_python-pip-install

.PHONY: freeze
freeze: \
	_helper-ensure-pwd-is-reporoot \
	_python-venv-clean \
	_python-venv-create \
	_python-pip-freeze \
	_python-pip-install

.PHONY: fmt
fmt: \
	_helper-ensure-pwd-is-reporoot \
	_fmt-python-isort \
	_fmt-python-black

.PHONY: lint
lint: \
	_helper-ensure-pwd-is-reporoot \
	_lint-python-isort \
	_lint-python-black \
	_lint-python-flake8

# Run pytest
.PHONY: test
test: \
	_helper-ensure-pwd-is-reporoot \
	_run-pytest
	 

# -----------------------------------------------------------------------------
# TARGETS - PYTHON DEPENDENCY MANAGEMENT
# -----------------------------------------------------------------------------
# Virtualenvs
override VENV_DIR := $(REPOROOT)/.venv
override VENV_ACTIVATE := $(VENV_DIR)/bin/activate

# Create Python Venv
.PHONY: _python-venv-create
_python-venv-create:
	@echo INFO $@ is STARTING... 
	@$(PY3_EXECUTABLE_NAME) -m venv $(VENV_DIR) \
		&& source $(VENV_ACTIVATE) \
		&& pip install --quiet --upgrade \
			"setuptools" \
			"wheel" \
			"pip-tools>=6"
	@echo INFO $@ is DONE

# Install Requirements 
.PHONY: _python-pip-install
_python-pip-install:
	@echo INFO $@ is STARTING... 
	@source $(VENV_ACTIVATE) \
		&& pip-sync --quiet $(REPOROOT)/requirements.txt
	@echo INFO $@ is DONE

.PHONY: _python-venv-clean
_python-venv-clean:
	@echo INFO $@ is STARTING... 
	@rm -rf $(VENV_DIR)
	@echo INFO $@ is DONE

.PHONY: _python-pip-freeze
_python-pip-freeze:
	@echo INFO $@ is STARTING... 
	@rm -f ./requirements.txt
	@source $(VENV_ACTIVATE) \
		&& export CUSTOM_COMPILE_COMMAND="make freeze" \
		&& cd $(REPOROOT) \
		&& pip-compile \
			--strip-extras \
			--resolver=backtracking \
			--quiet \
			--rebuild \
			--output-file ./requirements.txt \
			./requirements.in
	@echo INFO $@ is DONE

# -----------------------------------------------------------------------------
# TARGETS - FORMATTING
# -----------------------------------------------------------------------------

.PHONY: _fmt-python-isort
_fmt-python-isort:
	@echo INFO $@ is STARTING...
	@cd $(REPOROOT) \
		&& source $(VENV_ACTIVATE) \
		&& isort -- $(WORKROOT)
	@echo INFO $@ is DONE 

.PHONY: _fmt-python-black
_fmt-python-black:
	@echo INFO $@ is STARTING...
	@cd $(REPOROOT) \
		&& source $(VENV_ACTIVATE) \
		&& black -- $(WORKROOT)
	@echo INFO $@ is DONE 

# -----------------------------------------------------------------------------
# TARGETS - LINTING
# -----------------------------------------------------------------------------

.PHONY: _lint-python-isort
_lint-python-isort:
	@echo INFO $@ is STARTING...
	@cd $(REPOROOT) \
		&& source $(VENV_ACTIVATE) \
		&& isort --check -- $(WORKROOT)
	@echo INFO $@ is DONE 

.PHONY: _lint-python-black
_lint-python-black:
	@echo INFO $@ is STARTING...
	@cd $(REPOROOT) \
		&& source $(VENV_ACTIVATE) \
		&& black --check -- $(WORKROOT)
	@echo INFO $@ is DONE 

.PHONY: _lint-python-flake8
_lint-python-flake8:
	@echo INFO $@ is STARTING...
	@cd $(REPOROOT) \
		&& source $(VENV_ACTIVATE) \
		&& flake8 -- $(WORKROOT)
	@echo INFO $@ is DONE

# -----------------------------------------------------------------------------
# TARGETS - HELPERS
# -----------------------------------------------------------------------------

.PHONY: _helper-ensure-pwd-is-reporoot
_helper-ensure-pwd-is-reporoot:
	@if [[ "$(CURDIR)" != "$(REPOROOT)" ]]; then \
	echo INFO "Current Directory is: $(CURDIR)"; \
	echo INFO "Repository root is: $(REPOROOT)"; \
	echo ERROR "'make $(MAKECMDGOALS)' must be executed from the root of this repository"; \
	exit 1; \
	fi 

# -----------------------------------------------------------------------------
# TARGETS - TESTS
# -----------------------------------------------------------------------------

.PHONY: _run-pytest
_run-pytest:
	@echo INFO $@ is STARTING... 
	@source $(VENV_ACTIVATE) \
	&& pytest -s -vv
	@echo INFO $@ is DONE
install:
	@echo "Installing..."
	@python3 -m venv myenv
	@myenv/bin/pip install -r requirements.txt
	@echo "Done."

test:
	@echo "Running tests..."
	@myenv/bin/pytest
	@echo "Done."

run:
	@echo "Running..."
	@myenv/bin/flask --app lib/app.py run
	@echo "Done."
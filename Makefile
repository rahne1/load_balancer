test:
		docker-compose up -d
		python3 -m pytest --disable-warnings || true
		docker-compose down
		@echo "Done!"
	
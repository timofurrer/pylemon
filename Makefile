install:
	@echo "Installing pylemon python package ..."
	@python setup.py install > /dev/null
	@echo "Installing startup script ..."
	@cp etc/init.d/pylemon /etc/init.d
	@echo "Updating run levels ..."
	@update-rc.d pylemon defaults

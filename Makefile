test:
	coverage run --branch --source=signals_wtf manage.py test signals_wtf
	coverage report --omit=signals_wtf/test*

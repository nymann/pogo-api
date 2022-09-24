run:
	uvicorn ${COMPONENT}.asgi:app --reload --port 8228 --host 0.0.0.0

.PHONY: run

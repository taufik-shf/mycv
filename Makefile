UV := uv run

.PHONY: build pdf serve wserve clean

build:
	$(UV) python build.py

pdf: build
	$(UV) weasyprint index.html cv.pdf

serve:
	python3 -m http.server 8080

wserve:
	@echo "Open in Windows browser: http://$$(hostname -I | awk '{print $$1}'):8080"
	python3 -m http.server 8080 --bind 0.0.0.0

clean:
	rm -f cv.pdf index.html

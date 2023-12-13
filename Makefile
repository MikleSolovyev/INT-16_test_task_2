.DEFAULT_GOAL: run

CONT_NAME=juice-shop
CUR_DIR=$(shell pwd)
ZAP_REPORT_PATH=$(CUR_DIR)/zap_report.json
RESULT_REPORT_PATH=$(CUR_DIR)/res_report.json

run: shop zap convert

shop:
	docker start $(CONT_NAME) || docker run --pull=missing --name=$(CONT_NAME) -d -p 3000:3000 bkimminich/juice-shop

zap:
	zap.sh -cmd -quickurl http://localhost:3000/ -quickout $(ZAP_REPORT_PATH)

convert:
	python3 main.py -i $(ZAP_REPORT_PATH) -o $(RESULT_REPORT_PATH)

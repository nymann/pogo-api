TARGET?=local
COMPONENT?=pogo_api
VERSION:=src/${COMPONENT}/core/version.py

include make/common.mk

include make/install.mk
include make/test.mk
include make/help.mk
include make/clean.mk
include make/lint.mk
include make/ci.mk

.DEFAULT:help

SHELL := /bin/bash
.PHONY: converge

converge:
	molecule converge

destroy:
	molecule destroy

login:
	molecule login

test:
	molecule test

include .env


solver-add:
	python3 solvers.py add $(path) $(name)

exp-init:
	python3 experiments.py init $(exp_name) $(solver_name)

exp-run:
	datasphere project job execute -p ${DS_PROJECT} -c experiments/$(exp_name)/config.yaml


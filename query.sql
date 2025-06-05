CREATE DATABASE Onebeat

CREATE TABLE Transactions (
	id_transacao VARCHAR(100),
	data DATE,
	valor FLOAT,
	descricao VARCHAR(100),
	tipo VARCHAR(100),
	status VARCHAR(100),
	conta_origem VARCHAR(100),
	conta_destino VARCHAR(100)
)
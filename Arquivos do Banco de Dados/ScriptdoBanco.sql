/* Aq é a criação do Banco de Dados*/
create database Cadastro;

/* Aq para ter acesso ao Banco de Dados*/
use Cadastro;

/* Aq para criar uma tabela dentro do Banco */
create table usuario (
id int auto_increment primary key,
nome varchar(50) not null,
sobrenome varchar(50) not null,
senha varchar(50) not null,
email varchar(50) not null unique
);

/* Aq visualização descritiva da Tabela*/
desc usuario;

/* Aq para verificar os dados Salvos*/
select * from usuario;

/* Aq para limpar os dados da tabela. Cuidado!*/
truncate table usuario;

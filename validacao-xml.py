#/usr/bin/python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

try:
	arquivo = ET.parse('vendas.xml')
	root = arquivo.getroot()

	for venda in root.iter('venda'):
		print u'''-------------------- VENDA DE VEÍCULO --------------------\n
		Concessionária: %s 
		Endereço: %s 
		Cidade: %s 
		Estado: %s''' % (venda.attrib['nome_concessionaria'], venda.attrib['endereco_concessionaria'], venda.attrib['cidade_concessionaria'], venda.attrib['estado_concessionaria'])


	print '\nInformações do cliente'
	for informacoes_cliente in root.iter('informacoes_cliente'):
		print u'''
		Nome: %s
		RG: %s
		CNH: %s
		Categoria: %s''' %(informacoes_cliente.find('nome').text, informacoes_cliente.find('rg').text, informacoes_cliente.find('cnh').text, informacoes_cliente.find('categoria_cnh').text)

	for endereco in root.iter('endereco'):
		print u'''
		Rua: %s
		Número: %s
		Bairro: %s
		Cidade: %s
		Estado: %s
		CEP: %s''' %(endereco.find('rua').text, endereco.find('numero').text, endereco.find('bairro').text, endereco.find('cidade').text, endereco.find('estado').text, endereco.find('cep').text)

		print '\n\tContato'

	for contato in root.iter('contato'):
		print u'''
			Telefone: %s
			Celular: %s
			E-mail: %s''' %(contato.find('telefone').text, contato.find('celular').text, contato.find('email').text)

	for informacoes_venda in root.iter('informacoes_venda'):
		print u'''\nInformações da venda\n
		Número do pedido: %s
		Data da venda: %s
		Valor da venda: %s
		Valor da tabela fipe: %s ''' % (informacoes_venda.attrib['numero_venda'], informacoes_venda.find('data_venda').text, informacoes_venda.find('valor_venda').text, informacoes_venda.find('valor_tabela_fipe').text)

	for veiculo in root.iter('veiculo'):
		print u'''\nVeículo\n
		Marca: %s
		Modelo: %s
		Placa: %s
		Município: %s (%s)
		Tipo: %s
		Combustível: %s
		Motor: %s
		Ano: %s
		Quilometragem: %s km
		Observações: %s ''' % (veiculo.find('marca').text, veiculo.find('modelo').text, veiculo.find('placa').text, veiculo.find('municipio').text,veiculo.find('estado').text, veiculo.find('tipo').text, veiculo.find('combustivel').text, veiculo.find('motor').text, veiculo.find('ano').text, veiculo.find('km').text, veiculo.find('observacoes').text)

	for item in root.iter('opcionais'):
		print '\n\tOpcionais\n'
		for i in range(len(item)):
			print '\t\t', item[i].text
	print '\nXML bem formado, sintaxe OK\n'

except ET.ParseError:
	print "Sintaxe incorreta. Verifique o arquivo"

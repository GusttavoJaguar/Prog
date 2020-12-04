//calculadora básica
function acaoBotao(){

	var valor01, valor02, operacao, resultado

	valor01 = prompt("Digite o primeiro valor: ")
	operacao = prompt("Digite a operação que deseja executar: Ex: +, -, *, /")
	valor02 = prompt("Digite o segundo valor: ")

	if (operacao == "+"){
		resultado = parseInt(valor01) + parseInt(valor02)
	}else if(operacao == "-"){
		resultado = parseInt(valor01) - parseInt(valor02)
	}else if(operacao == "*"){
		resultado = parseInt(valor01) * parseInt(valor02)
	}else if(operacao == "/"){
		resultado = parseInt(valor01) / parseInt(valor02)
	}
	document.getElementById("botao").innerText = resultado
}